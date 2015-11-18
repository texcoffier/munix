#!/usr/bin/python
"""
Expected results are in 'regtest.py'

Run without arguments: check the expected results.

Run with 'rewrite' argument: create the new expected results
"""

import sys
import colorize

def check(input_val, expected, write_in):
    p = colorize.Parser(input_val)
    parsed = p.parse()
    result = parsed.str()
    if write_in:
        write_in.write(repr(input_val) + '\n')
        write_in.write(repr(result) + '\n')
        return
    if result != expected:
        print 'Input   :', input_val
        print 'Result  :', result
        print 'Expected:', expected
        print parsed.nice()
        i = 0
        for i in range(len(expected)):
            if result[i] != expected[i]:
                break
        print '===>' + result[i:]
        return True
    for i in range(len(input_val)):
        parsed.html(i)
        parsed.help(i)

f = open("regtest.py", "r")
tests = f.readlines()
f.close()

if 'rewrite' in sys.argv:
    f = open("regtest.py", "w")
else:
    f = None

error = False
for input_value, expected_value in zip(tests[::2], tests[1::2]):
    input_value = eval(input_value)
    expected_value = eval(expected_value)
    error = check(input_value, expected_value, f) or error

if colorize.Parser(u'cp --recursive').parse().str() != "Line(Pipeline(Command(Argument(Normal(u'cp')),Separator(u' '),Argument(Normal(u'-r')))))":
    there_is_an_unicode_problem


if f:
    f.close()

if error:
    sys.exit(1)

print "OK"
