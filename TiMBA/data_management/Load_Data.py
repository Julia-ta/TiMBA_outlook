
import os
import shutil
import tempfile
import zipfile
import urllib.request


def load_data(
    user: str,
    repo: str,
    branch: str,
    source_folder: str,
    dest_repo_path: str,
    dest_folder: str,):

    zip_url = f"https://github.com/{user}/{repo}/archive/refs/heads/{branch}.zip"

    with tempfile.TemporaryDirectory() as tmpdir:
        zip_path = os.path.join(tmpdir, f"{repo}.zip")
        print(f" Load {zip_url} ...")
        urllib.request.urlretrieve(zip_url, zip_path)

        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(tmpdir)

        repo_root = os.path.join(tmpdir, f"{repo}-{branch}")
        source_path = os.path.join(repo_root, source_folder)
        if not os.path.exists(source_path):
            raise FileNotFoundError(f"Folder {source_folder} not found in {repo}")

        target_path = os.path.join(dest_repo_path, dest_folder)
        os.makedirs(os.path.dirname(target_path), exist_ok=True)

        if os.path.exists(target_path):
            print(f" {target_path} already exist and will be overwritten")
            shutil.rmtree(target_path)

        shutil.copytree(source_path, target_path)
        print(f"Input data is saved")