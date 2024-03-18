# To be ran by devs, no need for the likes of you to run this, peasant
# This script is just for compiling the build from python to an exe

# How to run this script: python setup.py build
from cx_Freeze import setup, Executable

# List of all the Python files you want to include
files = ['main.py', 'utils.py']

# Executable configuration
executables = [Executable(script='main.py', base=None)]

# Setup configuration
setup(
    name='HaxPomp2024',
    version='1.0',
    description='hand recognition and music generation software',
    executables=executables,
    options={
        'build_exe': {
            'include_files': files,
        }
    }
)
