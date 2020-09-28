import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fair_queuing",
    version="0.0.1",
    author="edern haumont",
    author_email="edern.haumont@gmail.com",
    description="A fair queuing implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Xaxetrov/fair-queuing",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)