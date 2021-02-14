from os import path

from setuptools import setup
from setuptools_rust import RustExtension

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="cumin-py",
    version="0.0.4",
    author="cympfh",
    author_email="cympfh@gmail.com",
    url="https://github.com/cympfh/cumin-py",
    description="Python Binding for cumin",
    classifiers=["License :: OSI Approved :: MIT License"],
    long_description=long_description,
    packages=["cumin"],
    rust_extensions=[RustExtension("cumin.cumin_py", "Cargo.toml", debug=False)],
    include_package_data=True,
    zip_safe=False,
)
