#!/usr/bin/env python3
"""
Setup script for AutoMed Healthcare Chatbot.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="automed-healthcare-chatbot",
    version="0.1.0",
    author="Samuel Nambili",
    author_email="nambili.samuel@example.com",
    description="A multi-agent healthcare chatbot using AutoGen",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nambili-samuel/automed-healthcare-chatbot",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "automed=main:main",
        ],
    },
    include_package_data=True,
    keywords="healthcare, chatbot, autogen, multi-agent, ai",
)