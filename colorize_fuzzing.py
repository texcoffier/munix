#!/usr/bin/python3
"""
Try to parse every permutation of the special characters
"""

import math
import itertools
import time
from . import colorize

print("Start very long test")

chars = set((colorize.list_stopper
            + colorize.redirection_stopper
            + colorize.argument_stopper
             + "`").replace("\t", "a1'\""))

nb = 0
last = 0
def check(txt, depth):
    if depth == 0:
        try:
            colorize.Parser(txt).parse()
        except KeyboardInterrupt:
            raise
        except:
            print(("BUG for:", txt))
        return
    depth -= 1
    for char in chars:
        check(txt + char, depth)
for i in range(1, len(chars)):
    print((time.ctime(), "check length:", i))
    check("", i)

print("OK")
