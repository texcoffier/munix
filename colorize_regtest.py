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
check("$A '$B' \\$B $/ $B1/ $", """Line(Pipeline(Command(Argument(Variable('$A')),Separator(' '),Argument(Quote("'"),Normal('$B'),Quote("'")),Separator(' '),Argument(Backslash('\\\\'),Normal('$B')),Separator(' '),Argument(Normal('$/')),Separator(' '),Argument(Variable('$B1'),Normal('/')),Separator(' '),Argument(Normal('$')))))""")
check("$A$B", "Line(Pipeline(Command(Argument(Variable('$A'),Variable('$B')))))")
check('"A $B \\$C \\"" "', """Line(Pipeline(Command(Argument(Guillemet('"'),Normal('A '),Variable('$B'),Normal(' '),Backslash('\\\\'),Normal('$C '),Backslash('\\\\'),Normal('"'),Guillemet('"')),Separator(' '),Argument(Unterminated('"')))))""")
check('"$" "a', """Line(Pipeline(Command(Argument(Guillemet('"'),Normal('$'),Guillemet('"')),Separator(' '),Argument(Unterminated('"'),Normal('a')))))""")
check('a>b', "Line(Pipeline(Command(Argument(Normal('a')),Redirection(Fildes(''),Direction('>'),File(Normal('b'))))))")
check('a >$C >>\\$ <" $A"', """Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Redirection(Fildes(''),Direction('>'),File(Variable('$C'))),Separator(' '),Redirection(Fildes(''),Direction('>>'),File(Backslash('\\\\'),Normal('$'))),Separator(' '),Redirection(Fildes(''),Direction('<'),File(Guillemet('"'),Normal(' '),Variable('$A'),Guillemet('"'))))))""")
check("22>A B", "Line(Pipeline(Command(Redirection(Fildes('22'),Direction('>'),File(Normal('A'))),Separator(' '),Argument(Normal('B')))))")
check("a >&23", "Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Redirection(Fildes(''),Direction('>'),Fildes('&23')))))")
check("a | b", "Line(Pipeline(Command(Argument(Normal('a'))),Pipe(' | '),Command(Argument(Normal('b')))))")
check("a|b", "Line(Pipeline(Command(Argument(Normal('a'))),Pipe('|'),Command(Argument(Normal('b')))))")
check("a | b c | d e f", "Line(Pipeline(Command(Argument(Normal('a'))),Pipe(' | '),Command(Argument(Normal('b')),Separator(' '),Argument(Normal('c'))),Pipe(' | '),Command(Argument(Normal('d')),Separator(' '),Argument(Normal('e')),Separator(' '),Argument(Normal('f')))))")
check("|a", "Line(Pipeline(Unterminated('|'),Command(Argument(Normal('a')))))")
check("a | ", "Line(Pipeline(Command(Argument(Normal('a'))),Unterminated(' | ')))")
check("a;b ; c", "Line(Pipeline(Command(Argument(Normal('a')))),DotComa(';'),Pipeline(Command(Argument(Normal('b')))),DotComa(' ; '),Pipeline(Command(Argument(Normal('c')))))")
check(";a;", "Line(Unterminated(';'),Pipeline(Command(Argument(Normal('a')))),Unterminated(';'))")
check("a | b ; c | d", "Line(Pipeline(Command(Argument(Normal('a'))),Pipe(' | '),Command(Argument(Normal('b')))),DotComa(' ; '),Pipeline(Command(Argument(Normal('c'))),Pipe(' | '),Command(Argument(Normal('d')))))")
check("a#b", "Line(Pipeline(Command(Argument(Normal('a#b')))))")
check("a #b", "Line(Pipeline(Command(Argument(Normal('a')))),Separator(' '),Comment('#b'))")
check("a | ;", "Line(Pipeline(Command(Argument(Normal('a'))),Unterminated(' | ')),Unterminated(';'))")
check("a | # b", "Line(Pipeline(Command(Argument(Normal('a'))),Unterminated(' | ')),Comment('# b'))")
check("a ; # b", "Line(Pipeline(Command(Argument(Normal('a')))),Unterminated(' ; '),Comment('# b'))")

check("a [ab]", "Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(SquareBracket(SquareBracketStart('['),SquareBracketChar('a'),SquareBracketChar('b'),SquareBracketStop(']'))))))")
check("a [", "Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(Unterminated('[')))))")
check("a [a-bcd-e]", "Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(SquareBracket(SquareBracketStart('['),SquareBracketInterval('a-b'),SquareBracketChar('c'),SquareBracketInterval('d-e'),SquareBracketStop(']'))))))")
check("a []a-c-d]", "Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(SquareBracket(SquareBracketStart('['),SquareBracketStop(']')),Normal('a-c-d]')))))")
check("a [!a-]]", "Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(SquareBracket(SquareBracketStart('['),SquareBracketChar('!'),SquareBracketChar('a'),SquareBracketChar('-'),SquareBracketStop(']')),Normal(']')))))")
check("a [1*", "Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(Unterminated('['),Normal('1'),Star('*')))))")

check("(a)", "Line(Pipeline(Group(GroupStart('('),Line(Pipeline(Command(Argument(Normal('a'))))),GroupStop(')'))))")
check("(a", "Line(Pipeline(Group(Unterminated('('),Line(Pipeline(Command(Argument(Normal('a'))))))))")
check("a (", "Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Unexpected('('))))")
check("( d ; e )", "Line(Pipeline(Group(GroupStart('( '),Line(Pipeline(Command(Argument(Normal('d')))),DotComa(' ; '),Pipeline(Command(Argument(Normal('e'))))),GroupStop(' )'))))")
check("a ; ( b ) ; c", "Line(Pipeline(Command(Argument(Normal('a')))),DotComa(' ; '),Pipeline(Group(GroupStart('( '),Line(Pipeline(Command(Argument(Normal('b'))))),GroupStop(' ) '))),DotComa('; '),Pipeline(Command(Argument(Normal('c')))))")
check("( a ; b ) | ( c ; d )", "Line(Pipeline(Group(GroupStart('( '),Line(Pipeline(Command(Argument(Normal('a')))),DotComa(' ; '),Pipeline(Command(Argument(Normal('b'))))),GroupStop(' ) ')),Pipe('| '),Group(GroupStart('( '),Line(Pipeline(Command(Argument(Normal('c')))),DotComa(' ; '),Pipeline(Command(Argument(Normal('d'))))),GroupStop(' )'))))")

check("( a ) >b",  "Line(Pipeline(Group(GroupStart('( '),Line(Pipeline(Command(Argument(Normal('a'))))),GroupStop(' ) '),Redirection(Fildes(''),Direction('>'),File(Normal('b'))))))")
      
print "OK"
