''
'Line()'
'a'
"Line(Pipeline(Command(Argument(Normal('a')))))"
'aa'
"Line(Pipeline(Command(Argument(Normal('aa')))))"
'a aa  a'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(Normal('aa')),Separator('  '),Argument(Normal('a')))))"
'a\\ a\\ \\   \\    \\'
"Line(Pipeline(Command(Argument(Normal('a'),Backslash('\\\\'),Normal(' a'),Backslash('\\\\'),Normal(' '),Backslash('\\\\'),Normal(' ')),Separator('  '),Argument(Backslash('\\\\'),Normal(' ')),Separator('   '),Argument(Unterminated('\\\\')))))"
"' ' '  ' '\\' '\\\\' '\\\\\\' '"
'Line(Pipeline(Command(Argument(Quote("\'"),Normal(\' \'),Quote("\'")),Separator(\' \'),Argument(Quote("\'"),Normal(\'  \'),Quote("\'")),Separator(\' \'),Argument(Quote("\'"),Normal(\'\\\\\'),Quote("\'")),Separator(\' \'),Argument(Quote("\'"),Normal(\'\\\\\\\\\'),Quote("\'")),Separator(\' \'),Argument(Quote("\'"),Normal(\'\\\\\\\\\\\\\'),Quote("\'")),Separator(\' \'),Argument(Unterminated("\'")))))'
"a'b"
'Line(Pipeline(Command(Argument(Normal(\'a\'),Unterminated("\'"),Normal(\'b\')))))'
"$A '$B' \\$B $/ $B1/ $"
'Line(Pipeline(Command(Argument(Variable(\'$A\')),Separator(\' \'),Argument(Quote("\'"),Normal(\'$B\'),Quote("\'")),Separator(\' \'),Argument(Backslash(\'\\\\\'),Normal(\'$B\')),Separator(\' \'),Argument(Normal(\'$/\')),Separator(\' \'),Argument(Variable(\'$B1\'),Normal(\'/\')),Separator(\' \'),Argument(Normal(\'$\')))))'
'$A$B'
"Line(Pipeline(Command(Argument(Variable('$A'),Variable('$B')))))"
'"A $B \\$C \\"" "'
'Line(Pipeline(Command(Argument(Guillemet(\'"\'),Normal(\'A \'),Variable(\'$B\'),Normal(\' \'),Backslash(\'\\\\\'),Normal(\'$C \'),Backslash(\'\\\\\'),Normal(\'"\'),Guillemet(\'"\')),Separator(\' \'),Argument(Unterminated(\'"\')))))'
'"$" "a'
'Line(Pipeline(Command(Argument(Guillemet(\'"\'),Normal(\'$\'),Guillemet(\'"\')),Separator(\' \'),Argument(Unterminated(\'"\'),Normal(\'a\')))))'
'a>b'
"Line(Pipeline(Command(Argument(Normal('a')),Redirection(Fildes(''),Direction('>'),File(Normal('b'))))))"
'a >$C >>\\$ <" $A"'
'Line(Pipeline(Command(Argument(Normal(\'a\')),Separator(\' \'),Redirection(Fildes(\'\'),Direction(\'>\'),File(Variable(\'$C\'))),Separator(\' \'),Redirection(Fildes(\'\'),Direction(\'>>\'),File(Backslash(\'\\\\\'),Normal(\'$\'))),Separator(\' \'),Redirection(Fildes(\'\'),Direction(\'<\'),File(Guillemet(\'"\'),Normal(\' \'),Variable(\'$A\'),Guillemet(\'"\'))))))'
'22>A B'
"Line(Pipeline(Command(Redirection(Fildes('22'),Direction('>'),File(Normal('A'))),Separator(' '),Argument(Normal('B')))))"
'a >&23'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Redirection(Fildes(''),Direction('>'),Fildes('&23')))))"
'a | b'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' ')),Pipe('| '),Command(Argument(Normal('b')))))"
'a|b'
"Line(Pipeline(Command(Argument(Normal('a'))),Pipe('|'),Command(Argument(Normal('b')))))"
'a | b c | d e f'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' ')),Pipe('| '),Command(Argument(Normal('b')),Separator(' '),Argument(Normal('c')),Separator(' ')),Pipe('| '),Command(Argument(Normal('d')),Separator(' '),Argument(Normal('e')),Separator(' '),Argument(Normal('f')))))"
'|a'
"Line(Pipeline(Unterminated('|'),Command(Argument(Normal('a')))))"
'a | '
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' ')),Unterminated('| ')))"
'a;b ; c'
"Line(Pipeline(Command(Argument(Normal('a')))),DotComa(';'),Pipeline(Command(Argument(Normal('b')),Separator(' '))),DotComa('; '),Pipeline(Command(Argument(Normal('c')))))"
';a;'
"Line(Unterminated(';'),Pipeline(Command(Argument(Normal('a')))),Unterminated(';'))"
'a | b ; c | d'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' ')),Pipe('| '),Command(Argument(Normal('b')),Separator(' '))),DotComa('; '),Pipeline(Command(Argument(Normal('c')),Separator(' ')),Pipe('| '),Command(Argument(Normal('d')))))"
'a#b'
"Line(Pipeline(Command(Argument(Normal('a#b')))))"
'a #b'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '))),Comment('#b'))"
'a | ;'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' ')),Unterminated('| ')),Unterminated(';'))"
'a | # b'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' ')),Unterminated('| ')),Comment('# b'))"
'a ; # b'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '))),Unterminated('; '),Comment('# b'))"
'a [ab]'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(SquareBracket(SquareBracketStart('['),SquareBracketChar('a'),SquareBracketChar('b'),SquareBracketStop(']'))))))"
'a ['
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(Unterminated('[')))))"
'a [a-bcd-e]'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(SquareBracket(SquareBracketStart('['),SquareBracketInterval('a-b'),SquareBracketChar('c'),SquareBracketInterval('d-e'),SquareBracketStop(']'))))))"
'a []a-c-d]'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(SquareBracket(SquareBracketStart('['),SquareBracketChar(']'),SquareBracketInterval('a-c'),SquareBracketChar('-'),SquareBracketChar('d'),SquareBracketStop(']'))))))"
'a [!a-]]'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(SquareBracket(SquareBracketStart('['),SquareBracketNegate('!'),SquareBracketChar('a'),SquareBracketChar('-'),SquareBracketStop(']')),Normal(']')))))"
'a [1*'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(Unterminated('['),Normal('1'),Star('*')))))"
'(a)'
"Line(Pipeline(Group(GroupStart('('),Line(Pipeline(Command(Argument(Normal('a'))))),GroupStop(')'))))"
'(a'
"Line(Pipeline(Group(Unterminated('('),Line(Pipeline(Command(Argument(Normal('a'))))))))"
'a ('
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Unexpected('('))))"
'( d ; e )'
"Line(Pipeline(Group(GroupStart('('),Line(Pipeline(Command(Separator(' '),Argument(Normal('d')),Separator(' '))),DotComa('; '),Pipeline(Command(Argument(Normal('e')),Separator(' ')))),GroupStop(')'))))"
'a ; ( b ) ; c'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '))),DotComa('; '),Pipeline(Group(GroupStart('('),Line(Pipeline(Command(Separator(' '),Argument(Normal('b')),Separator(' ')))),GroupStop(') '))),DotComa('; '),Pipeline(Command(Argument(Normal('c')))))"
'( a ; b ) | ( c ; d )'
"Line(Pipeline(Group(GroupStart('('),Line(Pipeline(Command(Separator(' '),Argument(Normal('a')),Separator(' '))),DotComa('; '),Pipeline(Command(Argument(Normal('b')),Separator(' ')))),GroupStop(') ')),Pipe('| '),Group(GroupStart('('),Line(Pipeline(Command(Separator(' '),Argument(Normal('c')),Separator(' '))),DotComa('; '),Pipeline(Command(Argument(Normal('d')),Separator(' ')))),GroupStop(')'))))"
'( a ) >b'
"Line(Pipeline(Group(GroupStart('('),Line(Pipeline(Command(Separator(' '),Argument(Normal('a')),Separator(' ')))),GroupStop(') '),Redirection(Fildes(''),Direction('>'),File(Normal('b'))))))"
'A=B'
"Line(Pipeline(Command(Affectation(Normal('A'),Equal('='),Normal('B')))))"
'A=B b c'
"Line(Pipeline(Command(Affectation(Normal('A'),Equal('='),Normal('B')),Separator(' '),Argument(Normal('b')),Separator(' '),Argument(Normal('c')))))"
'a $(c) b'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(Replacement(GroupStart('$('),Line(Pipeline(Command(Argument(Normal('c'))))),GroupStop(')'))),Separator(' '),Argument(Normal('b')))))"
'a & b &'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '))),Background('& '),Pipeline(Command(Argument(Normal('b')),Separator(' '))),Background('&'))"
'a; ;b'
"Line(Pipeline(Command(Argument(Normal('a')))),Unterminated('; '),DotComa(';'),Pipeline(Command(Argument(Normal('b')))))"
'a | ; && #'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' ')),Unterminated('| ')),Unterminated('; '),Unterminated('&& '),Comment('#'))"
'[]a]'
"Line(Pipeline(Command(Argument(SquareBracket(SquareBracketStart('['),SquareBracketChar(']'),SquareBracketChar('a'),SquareBracketStop(']'))))))"
'[!]]'
"Line(Pipeline(Command(Argument(SquareBracket(SquareBracketStart('['),SquareBracketNegate('!'),SquareBracketChar(']'),SquareBracketStop(']'))))))"
' |a'
"Line(Pipeline(Separator(' '),Unterminated('|'),Command(Argument(Normal('a')))))"
