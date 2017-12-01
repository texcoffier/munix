#!/usr/bin/python3
"""
Parse the lines on the standard input
"""

import sys
import colorize

for line in sys.stdin:
    print(line, "===>")
    print(colorize.Parser(line).parse().str())

print("OK")
