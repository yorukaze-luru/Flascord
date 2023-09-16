from setuptools import setup, Extension, find_packages
import os

VERSION = '0.1.1'

def load_requires_from_file():
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
    return requirements

def load_readme_from_file():
    with open('README.md', 'r', encoding='utf-8') as fp:
        readme = fp.read()
    return readme

setup(
    name='Flascord',
    author='Yorukaze LURU',
    license='MIT',
    url="https://github.com/yorukaze-luru/Flascord",
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    KEYWORDS = 'flask discord oauth2',
    long_description=load_readme_from_file(),
    long_description_content_type='text/markdown',
    CLASSIFIERS=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires=load_requires_from_file(),
)
