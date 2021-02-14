from setuptools import setup
from setuptools_rust import RustExtension


setup(
    name="cumin",
    version="0.0.1",
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
    packages=["cumin"],
    rust_extensions=[RustExtension("cumin.cumin_py", "Cargo.toml", debug=False)],
    include_package_data=True,
    zip_safe=False,
)
