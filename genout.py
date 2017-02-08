#!/usr/bin/python3


"""
    "genout.py", by Sean Soderman
    Generates output from executables within student directories.
    Can deal with arbitrarily nested directories.
"""
import sys
import subprocess
import os
import argparse
from subprocess import STDOUT, DEVNULL

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=('Runs executables within nested'
                                                  'directories'))
    parser.add_argument('-r', '--root', type=str,
                        help='Root of directory tree containing student programs.',
                        required=True)
    parser.add_argument('-n', '--name', type=str, default='run',
                        help='The name of the executable to run.')
    parser.add_argument('-o', '--out', type=str, default='myout',
                        help='The name of the file to direct output to.')
    parser.add_argument('-i', '--input', type=str, help='The input file being used (if any)',
                        required=False, default=DEVNULL)
    
    args = parser.parse_args()
    root = args.root
    #Basically the input file handle to use.
    inpath = ''
    executable = args.name
    output = args.out
    for dirpath, dirnames, filenames in os.walk(root):
        #Found the directory with the executable, run it & save output.
        if executable in filenames:
            #Have to reopen file handle for every execution.
            try:
                inpath = open(args.input, 'r')
            except FileNotFoundError as f:
                print(f)
            try:
                cmd = "{}".format(os.path.join(dirpath, executable))
                outed = subprocess.check_output(cmd.split(), stderr=STDOUT,
                                                stdin=inpath)
                with open(os.path.join(dirpath, output), 'w') as outfile:
                    outfile.write(str(outed, encoding='UTF-8'))
            except subprocess.CalledProcessError as cpe:
                with open(os.path.join(dirpath, "runtime_error"), "w") as errfile:
                    errfile.write(str(cpe.output, encoding='UTF-8'))
