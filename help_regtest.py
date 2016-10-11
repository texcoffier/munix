#!/usr/bin/python3

import sys
import re
import os
import colorize

rewrite = 'rewrite' in sys.argv

def nice_repr(t):
    if isinstance(t, list):
        return '[' + ','.join(nice_repr(i) for i in t) + ']'
    if isinstance(t, str):
        return '\n'.join('\t' + repr(i) for i in re.split("\n+", t)) + '\n'
    return str(t)
    

def help_check(tests):
    output = open("help_regtest.txt.new", "w")
    error = False
    output.write('[')
    for test in tests:
        p = colorize.Parser(test[0]).parse()
        last = '\000'
        computed = [test[0]]
        computed2 = [test[0]]
        for i in range(0, len(test[0])+1):
            t = re.sub("<[^>]*>", "", p.help(i))
            if t != last:
                j = -1
                while t[j] == last[j]:
                    j -= 1
                if j == -1:
                    tt = t
                else:
                    tt = t[:j+1]
                computed.append([i, j, tt])
                computed2.append([i, j, tt.replace("\n", "")])
                last = t
        output.write('['+',\n'.join(nice_repr(i) for i in computed) + '],\n')
        if test != computed2:
            error = True
    output.write(']\n')
    output.close()
    return error

error = False
with open("help_regtest.txt", "r") as h:
    error = help_check(eval(h.read()))


if error and not rewrite:
    os.system("diff -U 20 help_regtest.txt help_regtest.txt.new")
    print("\nTo record the changes, run:  {} rewrite".format(sys.argv[0]))
    sys.exit(1)

if rewrite:
    os.rename("help_regtest.txt.new", "help_regtest.txt")
    print("Changes recorded...")
else:
    os.unlink("help_regtest.txt.new")
    print('REGTEST PYTHON help messages OK')
