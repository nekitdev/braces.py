from pathlib import Path
import re
import site

from setuptools import setup  # type: ignore  # no stubs or types

for site_packages_path in reversed(site.getsitepackages()):
    site_packages = Path(site_packages_path)

    if site_packages.exists():
        break

else:
    site_packages = Path(site.USER_SITE)

try:
    (site_packages / "braces.pth").touch()  # attempt to create the path file

except OSError:
    site_packages = Path(site.USER_SITE)

root = Path(__file__).parent

requirements = (root / "requirements.txt").read_text("utf-8").splitlines()

init = (root / "braces" / "__init__.py").read_text("utf-8")

result = re.search(
    r"^__version__\s*=\s*[\"']([^\"']*)[\"']", init, re.MULTILINE
)

if result is None:
    raise RuntimeError("Failed to find version.")

version = result.group(1)

long_description = (root / "README.rst").read_text("utf-8")

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
    long_description=long_description,
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
