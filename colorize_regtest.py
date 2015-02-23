#!/usr/bin/python

import colorize

def check(input, output):
    p = colorize.Parser(input)
    result = p.parse().str()
    if result != output:
        print 'Input   :', input
        print 'Output  :', result
        print 'Expected:', output
        print p.parse().nice()
        for i in range(len(output)):
            if result[i] != output[i]:
                break
        print '===>' + result[i:]
        bug

check("", "Line()")
check("a", "Line(Pipeline(Command(Argument(Normal('a')))))")
check("aa", "Line(Pipeline(Command(Argument(Normal('aa')))))")
check("a aa  a", "Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(Normal('aa')),Separator('  '),Argument(Normal('a')))))")
check("a\\ a\\ \\   \\    \\", "Line(Pipeline(Command(Argument(Normal('a'),Backslash('\\\\'),Normal(' a'),Backslash('\\\\'),Normal(' '),Backslash('\\\\'),Normal(' ')),Separator('  '),Argument(Backslash('\\\\'),Normal(' ')),Separator('   '),Argument(Unterminated('\\\\')))))")
check("' ' '  ' '\\' '\\\\' '\\\\\\' '", """Line(Pipeline(Command(Argument(Quote("'"),Normal(' '),Quote("'")),Separator(' '),Argument(Quote("'"),Normal('  '),Quote("'")),Separator(' '),Argument(Quote("'"),Normal('\\\\'),Quote("'")),Separator(' '),Argument(Quote("'"),Normal('\\\\\\\\'),Quote("'")),Separator(' '),Argument(Quote("'"),Normal('\\\\\\\\\\\\'),Quote("'")),Separator(' '),Argument(Unterminated("'")))))""")
check("a'b", """Line(Pipeline(Command(Argument(Normal('a'),Unterminated("'"),Normal('b')))))""")
check("$A '$B' \\$B $/ $B1/ $", """Line(Pipeline(Command(Argument(Dollar('$'),Variable('A')),Separator(' '),Argument(Quote("'"),Normal('$B'),Quote("'")),Separator(' '),Argument(Backslash('\\\\'),Normal('$B')),Separator(' '),Argument(Normal('$/')),Separator(' '),Argument(Dollar('$'),Variable('B1'),Normal('/')),Separator(' '),Argument(Normal('$')))))""")
check("$A$B", "Line(Pipeline(Command(Argument(Dollar('$'),Variable('A'),Dollar('$'),Variable('B')))))")
check('"A $B \\$C \\"" "', """Line(Pipeline(Command(Argument(Guillemet('"'),Normal('A '),Dollar('$'),Variable('B'),Normal(' '),Backslash('\\\\'),Normal('$C '),Backslash('\\\\'),Normal('"'),Guillemet('"')),Separator(' '),Argument(Unterminated('"')))))""")
check('"$" "a', """Line(Pipeline(Command(Argument(Guillemet('"'),Normal('$'),Guillemet('"')),Separator(' '),Argument(Unterminated("'"),Normal('a')))))""")
check('a>b', "Line(Pipeline(Command(Argument(Normal('a')),Redirection(Fildes(''),Direction('>'),File(Normal('b'))))))")
check('a >$C >>\\$ <" $A"', """Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Redirection(Fildes(''),Direction('>'),File(Dollar('$'),Variable('C'))),Separator(' '),Redirection(Fildes(''),Direction('>>'),File(Backslash('\\\\'),Normal('$'))),Separator(' '),Redirection(Fildes(''),Direction('<'),File(Guillemet('"'),Normal(' '),Dollar('$'),Variable('A'),Guillemet('"'))))))""")
check("22>A B", "Line(Pipeline(Command(Redirection(Fildes('22'),Direction('>'),File(Normal('A'))),Separator(' '),Argument(Normal('B')))))")
check("a >&23", "Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Redirection(Fildes(''),Direction('>'),Fildes('&23')))))")
check("a | b", "Line(Pipeline(Command(Argument(Normal('a'))),Pipe(' | '),Command(Argument(Normal('b')))))")
check("a|b", "Line(Pipeline(Command(Argument(Normal('a'))),Pipe('|'),Command(Argument(Normal('b')))))")
check("a | b c | d e f", "Line(Pipeline(Command(Argument(Normal('a'))),Pipe(' | '),Command(Argument(Normal('b')),Separator(' '),Argument(Normal('c'))),Pipe(' | '),Command(Argument(Normal('d')),Separator(' '),Argument(Normal('e')),Separator(' '),Argument(Normal('f')))))")
check("|a", "Line(Pipeline(Command(),Unterminated('|'),Command(Argument(Normal('a')))))")
check("a | ", "Line(Pipeline(Command(Argument(Normal('a'))),Unterminated(' |')))")
check("a;b ; c", "Line(Pipeline(Command(Argument(Normal('a')))),DotComa(';'),Pipeline(Command(Argument(Normal('b')))),DotComa(' ; '),Pipeline(Command(Argument(Normal('c')))))")
check(";a;", "Line(Pipeline(Command()),Unterminated(';'),Pipeline(Command(Argument(Normal('a')))),Unterminated(';'))")
check("a | b ; c | d", "Line(Pipeline(Command(Argument(Normal('a'))),Pipe(' | '),Command(Argument(Normal('b')))),DotComa(' ; '),Pipeline(Command(Argument(Normal('c'))),Pipe(' | '),Command(Argument(Normal('d')))))")
check("a#b", "Line(Pipeline(Command(Argument(Normal('a#b')))))")
check("a #b", "Line(Pipeline(Command(Argument(Normal('a')),Separator(' #b'))))")

if colorize.Parser("'a>'>b").parse().html() != """<div class="Parsed Line"><div class="Parsed Pipeline"><div class="Parsed Command"><div class="Parsed Argument"><div class="Parsed Quote">'</div><div class="Parsed Normal">a&gt;</div><div class="Parsed Quote">'</div></div><div class="Parsed Redirection"><div class="Parsed Fildes"></div><div class="Parsed Direction">&gt;</div><div class="Parsed File"><div class="Parsed Normal">b</div></div></div></div></div></div>""":
    print colorize.Parser("'a>'>b").parse().html()
    bug

print "OK"
