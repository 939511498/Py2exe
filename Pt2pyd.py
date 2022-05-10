from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize(['tar1.py','tar2.py']))#Support muti .py trans to .pyd

#Run at terminal -> python setup.py build_ext --inplace
