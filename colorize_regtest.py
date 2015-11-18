#!/usr/bin/python
"""
Expected results are in 'regtest.py'

Run without arguments: check the expected results.

Run with 'rewrite' argument: create the new expected results
"""

import sys
import colorize

def check(input_val, expected_str, expected_cleanup, write_in):
    p = colorize.Parser(input_val)
    parsed         = p.parse()
    result_str     = parsed.str()
    result_cleanup = parsed.cleanup()
    if write_in:
        write_in.write(repr(input_val) + '\n')
        write_in.write(repr(result_str) + '\n')
        write_in.write(repr(result_cleanup) + '\n')
        return
    if result_str != expected_str or result_cleanup != expected_cleanup:
        print 'Input        :', input_val
        if result_str != expected_str:
            print 'Result str       :', result_str
            print 'Expected str     :', expected_str
        if result_cleanup != expected_cleanup:
            print 'Result cleanup   :', result_cleanup
            print 'Expected cleanup :', expected_cleanup
        print parsed.nice()
        i = 0
        for i in range(len(expected_str)):
            if result_str[i] != expected_str[i]:
                break
        print '===>' + result_str[i:]
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
for input_value, expected_value, expected_cleanup in zip(tests[::3],
                                                         tests[1::3],
                                                         tests[2::3]):
    input_value = eval(input_value)
    expected_value = eval(expected_value)
    expected_cleanup = eval(expected_cleanup)
    error = check(input_value, expected_value, expected_cleanup, f) or error

if colorize.Parser(u'cp --recursive').parse().cleanup() != "Line(Pipeline(Command(Argument(Normal(u'cp'))Argument(Normal(u'-r')))))":
    there_is_an_unicode_problem


if f:
    f.close()

if error:
    sys.exit(1)

print "OK"
