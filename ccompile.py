#!/usr/bin/python

"""
    'ccompile.py', by Sean Soderman.
    Iterates through a directory listing, compiling
    C code with the command line from Clark's makefile.
    Must be run from the directory **above** the directories containing
    student code.
"""
import sys
import os
import subprocess
from subprocess import STDOUT
if len(sys.argv) < 2:
    sys.stderr.write("Usage: {} <root>\n".format(sys.argv[0]))

theDir = sys.argv[1]
#Command line allowing for easy compilation of a student's
#code. The {} bit requires a full path to their program.
cmdline = ("g++ -std=c++11 -g -o {}/p1"
          " compile/cs3723p1Driver.o  compile/hashApi.o  compile/hexDump64.o {}"
          )
#Full pathname to the required header file. Necessary for creating
#a symbolic link to it within the student's source code directory.
header = "/home/sean/classes/recitation/prgms/assign1/cs3723p1.h"
for dirpath, dirnames, filenames in os.walk(theDir):
    for i in filenames:
        if i == "cs3723p1.c":
            if "cs3723p1.h" not in filenames:
                os.link(header, os.path.join(dirpath, "cs3723p1.h"))
            error = ""
            try:
                error = subprocess.check_output((cmdline.format(dirpath, 
                                         os.path.join(dirpath, i)).split()), stderr=STDOUT)
            except subprocess.CalledProcessError as cpe:
                with open(os.path.join(dirpath, "error"), "w") as errfile:
                    errfile.write(cpe.output)
