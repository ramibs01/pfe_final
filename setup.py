import sys
import os
from cx_Freeze import setup, Executable

files = ["Mon projet.ico", "Icons_home"]

target = Executable(
    script="main_window_Jenkins.py",
    base="Win32GUI",
    icon="Mon projet.ico"
)

setup(
    name="CodeGenerator",
    version="1.0.0",
    description="Code generator, jenkinsfile, dockerfile et gitlab CI",
    options={"build_exe": {'include_files': files}},
    executables=[target]
)
