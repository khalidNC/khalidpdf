import setuptools
from pathlib import Path

setuptools.setup(
  name="khalidpdf",
  version=1.2,
  long_description=Path("README.md").read_text(),
  packages=setuptools.find_packages(exclude=['tests', 'data'])
)
