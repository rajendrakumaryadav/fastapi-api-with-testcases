# Setup it as package
from setuptools import setup

name = "api-project"
version = "0.1.0"
description = "FastAPI"
author = "FastAPI"
author_email = "demo@demo.com"
url = "https://fastapi.tiangolo.com/"
license = "MIT"
packages = ["api_project"]
install_requires = []
install_dev_requires = []
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Build Tools",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.8",
]
keywords = [
    "fastapi",
    "api",
    "rest",
    "asyncio",
    "uvicorn"]
entry_points = {
    "console_scripts": [
        "api-project = api_project.main:main"
    ]
}

setup(
    name=name,
    version=version,
    description=description,
    author=author,
    author_email=author_email,
    url=url,
    license=license,
    packages=packages,
    install_requires=install_requires,
    extras_require={
        "dev": install_dev_requires
    },
    classifiers=classifiers,
    keywords=keywords,
    entry_points=entry_points
)
