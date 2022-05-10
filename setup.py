from distutils.core import setup
from Cython.Build import cythonize

# build_dir = 'build'
# build_temp_dir = 'build/temp'
#
# setup(
#     name = 'main_pics',
#     ext_modules = cythonize(['main.py']),
#     script_args=["install"]
# )
setup(ext_modules = cythonize(['main.py']))
#python setup.py build_ext --inplace