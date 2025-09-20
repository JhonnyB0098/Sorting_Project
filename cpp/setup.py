from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        "cpp_sorts",
        ["cpp_sorts.cpp"],
        include_dirs=[pybind11.get_include()],
        language="c++"
    ),
]

setup(
    name="cpp_sorts",
    version="0.1",
    ext_modules=ext_modules,
)
