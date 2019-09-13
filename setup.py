import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="apriopy",
    version="0.0.1",
    author="Gökhan Gerdan",
    author_email="gokhang1327@gmail.com",
    description="Apriori algorithm.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gokhangerdan/Apriopy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)