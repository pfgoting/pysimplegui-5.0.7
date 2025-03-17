from setuptools import setup, find_packages

setup(
    name="PySimpleGUI",
    version="5.0.7",
    packages=find_packages(),
    install_requires=[
        "rsa>=4.9",
    ],
    author="Prince Goting",
    description="A rebuilt version of PySimpleGUI",
    url="https://github.com/yourusername/PySimpleGUI",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

