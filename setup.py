from distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(
    name="parallel_sort_implementation",
    ext_modules=cythonize(
        "parallel_sort_implementation/quicksort.pyx",
    ),
    include_dirs=[numpy.get_include(), "./parallel_sort_implementation/"],
    version="0.0.1",
)
