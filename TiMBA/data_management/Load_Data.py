
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

        #print("drp: ",dest_repo_path)
        print("drf: ",dest_folder)
        os.makedirs(os.path.dirname(dest_folder), exist_ok=True)

        if os.path.exists(dest_folder):
            print(f" {dest_folder} already exist and will be overwritten")
            shutil.rmtree(dest_folder)

        shutil.copytree(source_path, dest_folder)
        print(f"Input data is saved")