import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="webscrapper",
    version="1.0.0",
    author="Craig Opie",
    author_email="craigopie@gmail.com",
    description="A simple web scrapper used to retrieve updated stock values.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CraigOpie/webscrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
