#!/usr/bin/python3

"""
    'ccompile.py', by Sean Soderman.
    Iterates through a directory listing, compiling
    C code with the command line specified.
    Must be run from the directory **above** the directories containing
    student code.
"""
import sys
import os
import subprocess
import argparse
from subprocess import STDOUT

"""
    The main idea: iterate through directory tree recursively until I find a
    directory with c programs inside. If there exist no header files in this
    directory, link the required ones (specified on the command line) to
    this directory so the compilation will work out. If there also exist
    c source code files not contained within the directory, include them
    in the compilation command (either specified on the command line or spec'd
    as a directory on the command line). Output the executable (named "run" by default)
    into the directory with the source code.
"""
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=('Compiles C programs'
                                                  'within nested directories'))

    parser.add_argument('-r', '--root', type=str,
                        help='Root of directory tree containing student programs')


    parser.add_argument('-n', '--name', type=str, default='run',
                        help='The name of the output executable.')
    """
    #TODO: Add option for "make", unecessary for now.
    compile_group = parser.add_mutually_exclusive_group(required=True)

    #FIXME: Probably unnecessary. I think I can just use my own little
    #command for compiling c programs...
    compile_group.add_argument('-c', '--command', type=str,
                        help=('The portion of the compilation command that'
                              ' is general to all student files.'
                             ), required=True)
    """
    parser.add_argument('-h', '--headers', type=str, nargs='*',
                        help='The header files required for compilation.',
                        required=False)
    parser.add_argument('-o', 'other_files', type=str, nargs='*',
                        help=('A list of c program files that are required for'
                              ' compilation (i.e., driver program files.'),
                        required=False)

    #Command line allowing for easy compilation of a student's
    #code. The {} bit requires a full path to their program.
    """
    cmdline = ("g++ -std=c++11 -g -o {}/p1"
              " compile/cs3723p1Driver.o  compile/hashApi.o  compile/hexDump64.o {}"
              )
    """
    parser.parse_args()

    cmdline = ('gcc -o {outdir}/{name} {other_files}')
    #Full pathname to the required header file. Necessary for creating
    #a symbolic link to it within the student's source code directory.
    #header = "/home/sean/classes/recitation/prgms/assign1/cs3723p1.h"
    #headers = ' '.join(parser.headers)
    for dirpath, dirnames, filenames in os.walk(parser.root):
        code_dir = any(map(lambda x: x.endswith('.c'), filenames))
        headers = [x for x in filenames if x.endswith('.h')]
        #no_header = any(map(lambda x: x.endswith('.h'), filenames))
        #Is there source code within this directory?
        if code_dir:
            #Link appropriate header files spec'd on cmdline to compilation
            #directory.
            if len(headers) == 0:
                map(lambda x: os.link(x, os.path.join(dirpath, x), parser.headers)
            #TODO: Even needed?
            error = ""
            cmd_cpy = cmdline.format(outdir=dirpath, name=parser.name, 
                                     other_files=parser.other_files)
            try:
                error = subprocess.check_output(cmd_cpy.split(), stderr=STDOUT)
            except subprocess.CalledProcessError as cpe:
                with open(os.path.join(dirpath, "error"), "w") as errfile:
                    errfile.write(cpe.output)