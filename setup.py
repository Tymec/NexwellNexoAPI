import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NexoAPI",
    version="0.0.3",
    author="Tymec",
    author_email="tymek11rt.yt@gmail.com",
    description="Unofficial Nexovision API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tymec/NexoAPI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)