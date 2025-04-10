import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "weather-image-recognition-using-CNN"
AUTHOR_USER_NAME = "shivani983"
SRC_REPO = "ComputerVisionProject"
AUTHOR_EMAIL = "shivani_2312res617@iitp.ac.in"


setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,

    description = " A project for weather classifiaction using CNN",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages = setuptools.find_packages(where = "src")

)