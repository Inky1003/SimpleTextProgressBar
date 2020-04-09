import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="simpletextprogressbar", # Replace with your own username
    version="1.1.0",
    author="Inky",
    author_email="inky1003@gmail.com",
    description="A simple progress bar for simple projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Inky1003/SimpleTextProgressBar/issues",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3.0-only",
        "Operating System :: OS Independent",
    ],
    keywords='progress bar command line console text window simple lightweight',
    python_requires='>=3.5',
    project_urls={
        'Bug Reports': 'https://github.com/Inky1003/SimpleTextProgressBar/issues',
        'Source': 'https://github.com/Inky1003/SimpleTextProgressBar/',
    },
)