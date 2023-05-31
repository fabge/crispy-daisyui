import os
import sys

from setuptools import find_packages, setup

import crispy_daisyui

if sys.argv[-1] == "publish":
    if os.system("pip freeze | grep wheel"):
        print("wheel not installed.\nUse `pip install wheel`.\nExiting.")
        sys.exit()
    if os.system("pip freeze | grep twine"):
        print("twine not installed.\nUse `pip install twine`.\nExiting.")
        sys.exit()
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    print("You probably want to also tag the version now:")
    print("  git tag -a {} -m 'version {}'".format(crispy_daisyui.__version__, crispy_daisyui.__version__))
    print("  git push --tags")
    sys.exit()

setup(
    name="crispy-daisyui",
    version=crispy_daisyui.__version__,
    description="A DaisyUI package for Django Crispy Forms",
    long_description=open("README.rst").read(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=["forms", "django", "crispy", "tailwind", "daisyui"],
    author="Fabian Geiger",
    author_email="geiger.fabian@outlook.com",
    url="https://github.com/fabge/crispy-daisyui",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=["django-crispy-forms>=1.11.2", "django>=3.2"],
    zip_safe=False,
)
