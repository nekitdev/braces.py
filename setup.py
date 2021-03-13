from distutils.sysconfig import get_python_lib
from pathlib import Path
import re

from setuptools import setup  # type: ignore  # no stubs/types

SITE_PACKAGES = get_python_lib()

root = Path(__file__).parent

requirements = (root / "requirements.txt").read_text("utf-8").splitlines()

init = (root / "braces" / "__init__.py").read_text("utf-8")

result = re.search(
    r"^__version__\s*=\s*[\"']([^\"']*)[\"']", init, re.MULTILINE
)

if result is None:
    raise RuntimeError("Failed to find version.")

version = result.group(1)

readme = (root / "README.rst").read_text("utf-8")


setup(
    name="braces.py",
    author="nekitdev",
    author_email="nekitdevofficial@gmail.com",
    url="https://github.com/nekitdev/braces.py",
    project_urls={
        "Issue tracker": "https://github.com/nekitdev/braces.py/issues"
    },
    version=version,
    packages=["braces"],
    license="MIT",
    description="Braces for Python Programming Language.",
    long_description=readme,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ],
    data_files=[(SITE_PACKAGES, ["braces.pth"])],
)
