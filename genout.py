#!/usr/bin/python


"""
    "genout.py", by Sean Soderman
    Generates output from executables within student directories.
"""
import sys
import subprocess
from subprocess import STDOUT
import os

if len(sys.argv) < 3:
    sys.stderr.write("Usage: {} <root> <pathtoinput>\n".format(sys.argv[0]))
    sys.exit(1)

root = sys.argv[1]
inpath = sys.argv[2]
for dirpath, dirnames, filenames in os.walk(sys.argv[1]):
    if "p1" in filenames:
        try:
            print(subprocess.check_output("{}/p1 < {} > {}/myout".format(dirpath,inpath, 
                                          dirpath), shell=True, stderr=STDOUT))
        except subprocess.CalledProcessError as cpe:
            with open(os.path.join(dirpath, "error"), "w") as errfile:
                errfile.write(cpe.output)
        try:
            print(subprocess.check_output("dos2unix {}/myout".format(dirpath), shell=True))
        except subprocess.CalledProcessError as cpe:
            with open(os.path.join(dirpath, "dos2unixerror"), "w") as errfile:
                errfile.write(cpe.output)
