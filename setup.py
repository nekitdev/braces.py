from distutils.sysconfig import get_python_lib
from pathlib import Path
import re
import site

from setuptools import setup  # type: ignore  # no stubs or types

site_packages = Path(next(reversed(site.getsitepackages())))  # use last site packages path

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

# copy braces path file from the root directory into site packages
(site_packages / "braces.pth").write_text((root / "braces.pth").read_text("utf-8"), "utf-8")

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
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Typing :: Typed",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ],
)
