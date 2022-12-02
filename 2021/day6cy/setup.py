from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("day6cy.pyx")
)

