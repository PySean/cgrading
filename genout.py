#!/usr/bin/python


"""
    "genout.py", by Sean Soderman
    Generates output from executables within student directories.
"""
import sys
import subprocess
import os
import argparse
from subprocess import STDOUT

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
                        required=False, default='')
    
    """
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: {} <root> <pathtoinput>\n".format(sys.argv[0]))
        sys.exit(1)

    root = sys.argv[1]
    inpath = sys.argv[2]
    """
    args = parser.parse_args()
    root = args.root;
    inpath = args.input
    #Don't want input redirection happening by default.
    inpath =  '< ' + inpath if inpath != '' else inpath
    executable = args.name
    output = args.out
    for dirpath, dirnames, filenames in os.walk(root):
        if executable in filenames:
            try:
                cmd = "{}/{} {}".format(dirpath, executable, inpath)
                outed = subprocess.check_output(cmd.split(), shell=True, stderr=STDOUT)
                with open(os.path.join(dirpath, output), 'w') as outfile:
                    outfile.write(outed)
            except subprocess.CalledProcessError as cpe:
                with open(os.path.join(dirpath, "error"), "w") as errfile:
                    errfile.write(cpe.output)
            #TODO: Probably don't need to do this.
            """
            try:
                print(subprocess.check_output("dos2unix {}/myout".format(dirpath), shell=True))
            except subprocess.CalledProcessError as cpe:
                with open(os.path.join(dirpath, "dos2unixerror"), "w") as errfile:
                    errfile.write(cpe.output)
            """
