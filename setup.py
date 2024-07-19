from setuptools import setup

import ratelimit


def readme() -> str:
    """Read README file"""
    with open("README.md") as infile:
        return infile.read()


setup(
    name="ratelimit-extended",
    version=ratelimit.__version__,
    description="API rate limit decorator",
    long_description=readme().strip(),
    author="Ömer Faruk Yığın",
    author_email="omert1122@gmail.com",
    url="https://github.com/omert11/ratelimit",
    license="MIT",
    packages=["ratelimit"],
    install_requires=[],
    keywords=["ratelimit", "api", "decorator"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Topic :: Software Development",
    ],
    include_package_data=True,
    zip_safe=False,
)
