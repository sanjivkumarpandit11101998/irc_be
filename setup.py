from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in irc_be/__init__.py
from irc_be import __version__ as version

setup(
	name="irc_be",
	version=version,
	description="customisation",
	author="IRC Business Essentials",
	author_email="ircengg@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
