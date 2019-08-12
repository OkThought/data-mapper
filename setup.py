import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="data-mapper",
    version="0.0.2",
    author="OkThought",
    author_email="bogush.vano@gmail.com",
    description="A declarative data mapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OkThought/data-mapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
