
# Pre-requisites

- Windows / Windows + WSL(Ubuntu)
- [Python 3.7+](https://www.python.org/downloads/windows/)
- [Git](https://git-scm.com/downloads)
- Enabled `INFO` logs on your chia farmer


## Run `main.py`
> python3 main.py --config config.yaml


# How to Package `.exe` file 
> 1: Enter the project root path <br>
> 2: Run with: `pyinstaller -F main.spec`
 


# Notes
If throw some errors，such as not found APScheduler, Please download from the Internet
> pkg_resources.DistributionNotFound: The 'APScheduler' distribution was not found and is required by the application


# PYinstaller package：
> ModuleNotFoundError: No module named 'requests' <br>
> Failed to execute script chiadoge
> 
> How to solve：<br>
> create a python file，add "import requests" in the top ，then install them<br>
> after that, the package will download to your local libraay
> last remove the python file 


