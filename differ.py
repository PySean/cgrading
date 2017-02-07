#!/usr/bin/python3
"""
    "differ.py", by Sean Soderman
    Essentially jumps through a directory tree, diffing generated
    program outputs with the correct output and sending it to an output
    file.
"""

import sys
import subprocess
import argparse
import os
from subprocess import STDOUT

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=('Diffs output of programs'
                                               ' within static directories with'
                                                ' correct output.'))
    parser.add_argument('-r', '--root', type=str,
                         help='Root of directory to seek output files in.',
                         required=True)
    parser.add_argument('-a', '--answerfile', type=str,
                        help=('The name of the output file we are checking student output'
                        ' against.'),
                        required=True)
    parser.add_argument('-n', '--name', type=str, default='myout',
                        help='Name of student output file')
    args = parser.parse_args()
    studentout = args.name
    answerout = args.answerfile
    command = 'diff {} {}'
    for dirpath, dirnames, filenames in os.walk(args.root):
        if studentout in filenames:
            try:
                realcommand = command.format(answerout, os.path.join(dirpath, studentout))
                subprocess.check_output(realcommand.split(), stderr=STDOUT)
            #Diff returns an error code of 1 if there is any difference.
            #So only generate a file when an "error" is caught.
            except subprocess.CalledProcessError as cpe:
                with open(os.path.join(dirpath, 'check.diff'), 'w') as errfile:
                    errfile.write(str(cpe.output, encoding='ASCII'))
