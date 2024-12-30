from setuptools import setup

setup(
    name="vcpkg_precommit",
    version="0.1.0",
    packages=["vcpkg_precommit"],
    entry_points={
        "console_scripts": ["vcpkg-format-manifest=vcpkg_precommit:main"],
    },
)
