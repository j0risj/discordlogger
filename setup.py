import setuptools

# with open("README.md", "r", encoding="utf-8") as fh:
#    long_description = fh.read()
long_description = "broken"

setuptools.setup(
    name="discordlogger-j0risj",
    version="0.0.2",
    author="j0risj",
    author_email="j0risj@outlook.de",
    description="A logging handler for Discord",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/j0risj/discordlogger",
    packages=setuptools.find_packages(),
    license="LICENSE.md",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "requests"
    ]
)
