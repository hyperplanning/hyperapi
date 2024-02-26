from setuptools import setup, find_packages

setup(
    name="HyperClient",
    version="0.0.0",
    author="JBK",
    author_email="jb@hyperplan.fr",
    description="A simple API client library & Documentation for interacting with Hyperplan API.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/hyperplanning/hyperapi",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pandas",
        "geopandas",
        "pyyaml",
        "responses",
        "pytest"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
