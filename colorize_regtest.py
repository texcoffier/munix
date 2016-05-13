#!/usr/bin/python3
"""
Expected results are in 'regtest.py'

Run without arguments: check the expected results.

Run with 'rewrite' argument: create the new expected results
"""

import sys
import json
import os
import colorize

def check(input_val, expected_str, expected_cleanup, write_in):
    p = colorize.Parser(input_val)
    parsed         = p.parse()
    result_str     = parsed.str()
    result_cleanup = parsed.cleanup(True)
    if write_in:
        write_in.write(repr(input_val) + '\n')
        write_in.write(repr(result_str) + '\n')
        write_in.write(repr(result_cleanup) + '\n')
        return
    if result_str != expected_str or result_cleanup != expected_cleanup:
        print(('Input        :', input_val))
        if result_str != expected_str:
            print(('Result str       :', result_str))
            print(('Expected str     :', expected_str))
        if result_cleanup != expected_cleanup:
            print(('Result cleanup   :', result_cleanup))
            print(('Expected cleanup :', expected_cleanup))
        print((parsed.nice()))
        i = 0
        for i in range(len(expected_str)):
            if result_str[i] != expected_str[i]:
                break
        print(('===>' + result_str[i:]))
        return True
    for i in range(len(input_val)):
        parsed.html(i)
        parsed.help(i)

def get_tests():
    f = open("regtest.py", "r")
    tests = f.readlines()
    f.close()
    for input, expect, expect_clean in zip(tests[::3],
                                           tests[1::3]+['""'],
                                           tests[2::3]+['""']):
        yield eval(input), eval(expect), eval(expect_clean)

def regtest_js():
    f = open("xxx.js", "w")
    g = open("colorize.js", "r")
    f.write(g.read())
    g.close()
    f.write("""
function check(input, expect, cleanup)
{
    try {
          a = new Parser(input).parse();
        }
    catch(e)
        {
          console.log(input) ;
          console.log(e) ;
          return ;
        }
    if ( a.str() != expect)
        {
          console.log(input) ;
          console.log("STR()   : " + a.str()) ;
          console.log("EXPECTED: " + expect) ;
          return ;
        }
    if ( a.cleanup(true) != cleanup)
        {
          console.log(input) ;
          console.log("CLEANUP(): " + a.cleanup(true)) ;
          console.log("EXPECTED:  " + cleanup) ;
          return ;
        }
}
    """)
    for input_value, expected_value, expected_cleanup in get_tests():
        f.write("check({},{},{});\n".format(json.dumps(input_value),
                                            json.dumps(expected_value),
                                            json.dumps(expected_cleanup),
                                        ))
    f.close()
    f = os.popen("node xxx.js || nodejs xxx.js", "r")
    c = f.read()
    f.close()
    if c.strip() != "":
        print(c)
        sys.exit(1)
    print("REGTEST JS OK")

def regtest_py():
    if 'rewrite' in sys.argv:
        f = open("regtest.py.new", "w")
    else:
        f = None

    error = False
    for input_value, expected_value, expected_cleanup in get_tests():
        error = check(input_value, expected_value, expected_cleanup, f) or error

    if (colorize.Parser('cp --recursive').parse().cleanup(True)
        !=
        "Line(Pipeline(Command(Argument(Normal('cp'))Argument(Normal('-r')))))"
        ):
        there_is_an_unicode_problem

    if f:
        f.close()
        os.rename("regtest.py.new", "regtest.py")

    if error:
        print("To rewrite regtest results if these errors are not real, run:")
        print("    %s rewrite" % sys.argv[0])
        sys.exit(1)
    print("REGTEST PYTHON OK")

regtest_py()
regtest_js()

