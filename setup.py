from setuptools import setup, Extension, find_packages
import os

VERSION = '0.0.7'

def load_requires_from_file(fname):
    if not os.path.exists(fname):
        raise IOError(fname)
    return [pkg.strip() for pkg in open(fname, 'r')]

setup(
    name='Flascord',
    author='Yorukaze LURU',
    license='MIT'
    url="https://github.com/yorukaze-luru/Flascord",
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    install_requires=load_requires_from_file('requirements.txt'),
)
