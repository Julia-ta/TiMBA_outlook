# Changelog


## [v1.2.0] - 2025-11-18

### Added
- **Carbon Module implementation**
  - Import and integration of the [Carbon Module](https://github.com/TI-Forest-Sector-Modelling/C-Module) into TiMBA
  - Setup structure for further model extensions

## [v1.1.0] - 2025-10-20

### Added
- Add paper for peer-reviewed JOSS publication
- Add workflow dispatch to enable manual activation of the GitHub Actions

### Changed
- Changed compatibility to Python <= 3.11
- Update default scenario input and default results for test suite
- Revisions of README to comply with JOSS reviews (add section for know issues and installation process)

## [v1.0.3] - 2025-04-09

### Added
- **Forest Model:**  
  - Implementation of an upper bound for forest stand density based on forest resources assessment data.
  - Added option to handle scenario_input with and without forest stand density restriction.
- **Documentation**  
  - Added the TiMBA documentation as a PDF file (DOI: 10.3220/253-2025-16).

### Changed
- **scenario input:**
  - Default `scenario_input.xlsx` has been updated with newest data (FAOSTAT, FRA, WTO, and SSP2).   
- **GitHub Actions:**  
  - Updated `setup-python` in `sonarscan.yml`.  
  - Upgraded `upload-artifact` and `setup-python` in `actions.yml`.
- **Coverage Report:**  
  - Included OS and Python version name.  
- **Package upgrades and dependencies**
  - Upgrade cvxpy solver environment to 1.6.4.
  - Fix osqp solver to 0.6.7.post3 to ensure package compatibility.

## [v1.0.2] - 2025-01-29

### Added
- **Python 3.12 compatibility**:
  - TiMBA is upgraded to run with Python 3.12.6.
  - Successfully tested for Python 3.9, 3.10, 3.11. 
- **GitHub Actions**: 
  - Set up GitHub Actions for TiMBA to integrate automated functionality and quality checks.
  - Added compatibility checks with multiple Python versions (Python 3.9, 3.10, 3.11, 3.12) and operating systems
(Windows and Ubuntu).
- **SonarCloud Integration**: Implemented and optimized code coverage and scans to ensure higher code quality.  
  - Integrated SonarCloud into the GitHub Actions pipeline.  
  - Added a SonarCloud quality status badge to `README.md`.   
- **Badges**: Added project badges like release status, coverage, and Zenodo-DOI.

### Changed
- **Package Upgrades**: All packages are upgraded to a version compatible with Python 3.12.
- **Readme & Compatibility**: Updated compatible Python versions and supported operating systems.
- **Scenario input file**: Changed scenario file for more consistent results.
- **Zipped pkl-files**: pkl-files for TiMBA output are zipped now to save storage space.
- **pkl-files with time stamps**: pkl-files for TiMBA output are now saved with a time stamp to allow unambiguous
identification.

### Fixed
- **GitHub Actions Bugs**:  
  - Various adaptations to fix bugs in the GitHub Actions 
- **Fixes to ensure compatibility with Python 3.12**
  - Resolved an issue with `np.isclose` for compatibility between Python 3.12 and Pandas.  
  - Replaced `iteritems` with `items` for compatibility with Python 3.12.
- **Gitignore Improvements**: Extended `.gitignore` to include additional folders like `timba\data\input`.

### Removed
- **Unnecessary Folders**: Removed virtual environment (`venv`) from the repository.  
- **Unsupported Python Versions**: Removed outdated versions from the test matrix.
