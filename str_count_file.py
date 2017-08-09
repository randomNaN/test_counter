# -*- coding: utf-8 -*-
import sys

try:
    with open(sys.argv[1], 'r') as f:
        print("Number of lines: {}".format(len(list(f))))
except FileNotFoundError:
    print("No such file or directory")
except UnicodeDecodeError:
    print("Can't count amount of lines")

    