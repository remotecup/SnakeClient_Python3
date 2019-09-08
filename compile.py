from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("YourClient", ["src/YourClient.py"])
]

setup(
    name='My Snake',  # Inser Your Team Name
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules
)
