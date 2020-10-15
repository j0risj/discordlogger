import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="discordlogger-j0risj", # Replace with your own username
    version="0.0.1",
    author="j0risj",
    author_email="j0risj@outlook.de",
    description="A logging handler for Discord",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/j0risj/discordlogger",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)