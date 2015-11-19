''
'Line()'
'Line()'
'a'
"Line(Pipeline(Command(Argument(Normal('a')))))"
"Line(Pipeline(Command(Argument(Normal('a')))))"
'aa'
"Line(Pipeline(Command(Argument(Normal('aa')))))"
"Line(Pipeline(Command(Argument(Normal('aa')))))"
'a aa  a'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(Normal('aa')),Separator('  '),Argument(Normal('a')))))"
"Line(Pipeline(Command(Argument(Normal('a'))Argument(Normal('aa'))Argument(Normal('a')))))"
'a b '
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(Normal('b')),Separator(' '))))"
"Line(Pipeline(Command(Argument(Normal('a'))Argument(Normal('b')))))"
'a\\ a\\ \\   \\    \\'
"Line(Pipeline(Command(Argument(Normal('a'),Backslash('\\\\'),Normal(' a'),Backslash('\\\\'),Normal(' '),Backslash('\\\\'),Normal(' ')),Separator('  '),Argument(Backslash('\\\\'),Normal(' ')),Separator('   '),Argument(Unterminated('\\\\')))))"
"Line(Pipeline(Command(Argument(Normal('a a  '))Argument(Normal(' '))Argument(Unterminated('\\\\')))))"
"' ' '  ' '\\' '\\\\' '\\\\\\' '"
'Line(Pipeline(Command(Argument(Quote("\'"),Normal(\' \'),Quote("\'")),Separator(\' \'),Argument(Quote("\'"),Normal(\'  \'),Quote("\'")),Separator(\' \'),Argument(Quote("\'"),Normal(\'\\\\\'),Quote("\'")),Separator(\' \'),Argument(Quote("\'"),Normal(\'\\\\\\\\\'),Quote("\'")),Separator(\' \'),Argument(Quote("\'"),Normal(\'\\\\\\\\\\\\\'),Quote("\'")),Separator(\' \'),Argument(Unterminated("\'")))))'
'Line(Pipeline(Command(Argument(Normal(\' \'))Argument(Normal(\'  \'))Argument(Normal(\'\\\\\'))Argument(Normal(\'\\\\\\\\\'))Argument(Normal(\'\\\\\\\\\\\\\'))Argument(Unterminated("\'")))))'
"a'b"
'Line(Pipeline(Command(Argument(Normal(\'a\'),Unterminated("\'"),Normal(\'b\')))))'
'Line(Pipeline(Command(Argument(Normal(\'a\')Unterminated("\'")Normal(\'b\')))))'
"$A '$B' \\$B $/ $B1/ $"
'Line(Pipeline(Command(Argument(Variable(\'$A\')),Separator(\' \'),Argument(Quote("\'"),Normal(\'$B\'),Quote("\'")),Separator(\' \'),Argument(Backslash(\'\\\\\'),Normal(\'$B\')),Separator(\' \'),Argument(Normal(\'$/\')),Separator(\' \'),Argument(Variable(\'$B1\'),Normal(\'/\')),Separator(\' \'),Argument(Normal(\'$\')))))'
"Line(Pipeline(Command(Argument(Variable('$A'))Argument(Normal('$B'))Argument(Normal('$B'))Argument(Normal('$/'))Argument(Variable('$B1')Normal('/'))Argument(Normal('$')))))"
'$A$B'
"Line(Pipeline(Command(Argument(Variable('$A'),Variable('$B')))))"
"Line(Pipeline(Command(Argument(Variable('$A')Variable('$B')))))"
'"A $B \\$C \\"" "'
'Line(Pipeline(Command(Argument(Guillemet(\'"\'),Normal(\'A \'),Variable(\'$B\'),Normal(\' \'),Backslash(\'\\\\\'),Normal(\'$C \'),Backslash(\'\\\\\'),Normal(\'"\'),Guillemet(\'"\')),Separator(\' \'),Argument(Unterminated(\'"\')))))'
'Line(Pipeline(Command(Argument(Normal(\'A \')VariableProtected(\'$B\')Normal(\' $C "\'))Argument(Unterminated(\'"\')))))'
'"$" "a'
'Line(Pipeline(Command(Argument(Guillemet(\'"\'),Normal(\'$\'),Guillemet(\'"\')),Separator(\' \'),Argument(Unterminated(\'"\'),Normal(\'a\')))))'
'Line(Pipeline(Command(Argument(Normal(\'$\'))Argument(Unterminated(\'"\')Normal(\'a\')))))'
'a>b'
"Line(Pipeline(Command(Argument(Normal('a')),Redirection(Fildes(''),Direction('>'),File(Normal('b'))))))"
"Line(Pipeline(Command(Argument(Normal('a'))Redirection(Fildes('')Direction('>')File(Normal('b'))))))"
'a >$C >>\\$ <" $A"'
'Line(Pipeline(Command(Argument(Normal(\'a\')),Separator(\' \'),Redirection(Fildes(\'\'),Direction(\'>\'),File(Variable(\'$C\'))),Separator(\' \'),Redirection(Fildes(\'\'),Direction(\'>>\'),File(Backslash(\'\\\\\'),Normal(\'$\'))),Separator(\' \'),Redirection(Fildes(\'\'),Direction(\'<\'),File(Guillemet(\'"\'),Normal(\' \'),Variable(\'$A\'),Guillemet(\'"\'))))))'
"Line(Pipeline(Command(Argument(Normal('a'))Redirection(Fildes('')Direction('>')File(Variable('$C')))Redirection(Fildes('')Direction('>>')File(Normal('$')))Redirection(Fildes('')Direction('<')File(Normal(' ')VariableProtected('$A'))))))"
'22>A B'
"Line(Pipeline(Command(Redirection(Fildes('22'),Direction('>'),File(Normal('A'))),Separator(' '),Argument(Normal('B')))))"
"Line(Pipeline(Command(Redirection(Fildes('22')Direction('>')File(Normal('A')))Argument(Normal('B')))))"
'a >&23'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Redirection(Fildes(''),Direction('>'),Fildes('&23')))))"
"Line(Pipeline(Command(Argument(Normal('a'))Redirection(Fildes('')Direction('>')Fildes('&23')))))"
'a | b'
"Line(Pipeline(Command(Argument(Normal('a'))),Pipe(' | '),Command(Argument(Normal('b')))))"
"Line(Pipeline(Command(Argument(Normal('a')))Command(Argument(Normal('b')))))"
'a|b'
"Line(Pipeline(Command(Argument(Normal('a'))),Pipe('|'),Command(Argument(Normal('b')))))"
"Line(Pipeline(Command(Argument(Normal('a')))Command(Argument(Normal('b')))))"
'a | b c | d e f'
"Line(Pipeline(Command(Argument(Normal('a'))),Pipe(' | '),Command(Argument(Normal('b')),Separator(' '),Argument(Normal('c'))),Pipe(' | '),Command(Argument(Normal('d')),Separator(' '),Argument(Normal('e')),Separator(' '),Argument(Normal('f')))))"
"Line(Pipeline(Command(Argument(Normal('a')))Command(Argument(Normal('b'))Argument(Normal('c')))Command(Argument(Normal('d'))Argument(Normal('e'))Argument(Normal('f')))))"
'|a'
"Line(Pipeline(Unterminated('|'),Command(Argument(Normal('a')))))"
"Line(Pipeline(Unterminated('|')Command(Argument(Normal('a')))))"
'a | '
"Line(Pipeline(Command(Argument(Normal('a'))),Separator(' '),Unterminated('| ')))"
"Line(Pipeline(Command(Argument(Normal('a')))Unterminated('| ')))"
'a;b ; c'
"Line(Pipeline(Command(Argument(Normal('a')))),DotComa(';'),Pipeline(Command(Argument(Normal('b')))),DotComa(' ; '),Pipeline(Command(Argument(Normal('c')))))"
"Line(Pipeline(Command(Argument(Normal('a'))))Pipeline(Command(Argument(Normal('b'))))Pipeline(Command(Argument(Normal('c')))))"
';a;'
"Line(Unterminated(';'),Pipeline(Command(Argument(Normal('a')))),Unterminated(';'))"
"Line(Unterminated(';')Pipeline(Command(Argument(Normal('a'))))Unterminated(';'))"
'a | b ; c | d'
"Line(Pipeline(Command(Argument(Normal('a'))),Pipe(' | '),Command(Argument(Normal('b')))),DotComa(' ; '),Pipeline(Command(Argument(Normal('c'))),Pipe(' | '),Command(Argument(Normal('d')))))"
"Line(Pipeline(Command(Argument(Normal('a')))Command(Argument(Normal('b'))))Pipeline(Command(Argument(Normal('c')))Command(Argument(Normal('d')))))"
'a#b'
"Line(Pipeline(Command(Argument(Normal('a#b')))))"
"Line(Pipeline(Command(Argument(Normal('a#b')))))"
'a #b'
"Line(Pipeline(Command(Argument(Normal('a')))),Separator(' '),Comment('#b'))"
"Line(Pipeline(Command(Argument(Normal('a'))))Comment('#b'))"
'a | ;'
"Line(Pipeline(Command(Argument(Normal('a'))),Separator(' '),Unterminated('| ')),Unterminated(';'))"
"Line(Pipeline(Command(Argument(Normal('a')))Unterminated('| '))Unterminated(';'))"
'a | # b'
"Line(Pipeline(Command(Argument(Normal('a'))),Separator(' '),Unterminated('| ')),Comment('# b'))"
"Line(Pipeline(Command(Argument(Normal('a')))Unterminated('| '))Comment('# b'))"
'a ; # b'
"Line(Pipeline(Command(Argument(Normal('a')))),Separator(' '),Unterminated('; '),Comment('# b'))"
"Line(Pipeline(Command(Argument(Normal('a'))))Unterminated('; ')Comment('# b'))"
'a [ab]'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(SquareBracket(SquareBracketStart('['),SquareBracketChar('a'),SquareBracketChar('b'),SquareBracketStop(']'))))))"
"Line(Pipeline(Command(Argument(Normal('a'))Argument(SquareBracket(SquareBracketStart('[')SquareBracketChar('a')SquareBracketChar('b')SquareBracketStop(']'))))))"
'a ['
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(Normal('[')))))"
"Line(Pipeline(Command(Argument(Normal('a'))Argument(Normal('[')))))"
'a [a-bcd-e]'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(SquareBracket(SquareBracketStart('['),SquareBracketInterval('a-b'),SquareBracketChar('c'),SquareBracketInterval('d-e'),SquareBracketStop(']'))))))"
"Line(Pipeline(Command(Argument(Normal('a'))Argument(SquareBracket(SquareBracketStart('[')SquareBracketInterval('a-b')SquareBracketChar('c')SquareBracketInterval('d-e')SquareBracketStop(']'))))))"
'a []a-c-d]'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(SquareBracket(SquareBracketStart('['),SquareBracketChar(']'),SquareBracketInterval('a-c'),SquareBracketChar('-'),SquareBracketChar('d'),SquareBracketStop(']'))))))"
"Line(Pipeline(Command(Argument(Normal('a'))Argument(SquareBracket(SquareBracketStart('[')SquareBracketChar(']')SquareBracketInterval('a-c')SquareBracketChar('-')SquareBracketChar('d')SquareBracketStop(']'))))))"
'a [!a-]]'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(SquareBracket(SquareBracketStart('['),SquareBracketNegate('!'),SquareBracketChar('a'),SquareBracketChar('-'),SquareBracketStop(']')),Normal(']')))))"
"Line(Pipeline(Command(Argument(Normal('a'))Argument(SquareBracket(SquareBracketStart('[')SquareBracketNegate('!')SquareBracketChar('a')SquareBracketChar('-')SquareBracketStop(']'))Normal(']')))))"
'a [1*'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(Normal('[1'),Star('*')))))"
"Line(Pipeline(Command(Argument(Normal('a'))Argument(Normal('[1')Star('*')))))"
'(a)'
"Line(Pipeline(Group(GroupStart('('),Line(Pipeline(Command(Argument(Normal('a'))))),GroupStop(')'))))"
"Line(Pipeline(Group(GroupStart Line(Pipeline(Command(Argument(Normal('a')))))GroupStop )))"
'(a'
"Line(Pipeline(Group(Unterminated('('),Line(Pipeline(Command(Argument(Normal('a'))))))))"
"Line(Pipeline(Group(Unterminated('(')Line(Pipeline(Command(Argument(Normal('a'))))))))"
'a ('
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Unexpected('('))))"
"Line(Pipeline(Command(Argument(Normal('a'))Unexpected('('))))"
'( d ; e )'
"Line(Pipeline(Group(GroupStart('('),Line(Pipeline(Command(Separator(' '),Argument(Normal('d')))),DotComa(' ; '),Pipeline(Command(Argument(Normal('e'))))),GroupStop(' )'))))"
"Line(Pipeline(Group(GroupStart Line(Pipeline(Command(Argument(Normal('d'))))Pipeline(Command(Argument(Normal('e')))))GroupStop )))"
'a ; ( b ) ; c'
"Line(Pipeline(Command(Argument(Normal('a')))),DotComa(' ; '),Pipeline(Group(GroupStart('('),Line(Pipeline(Command(Separator(' '),Argument(Normal('b'))))),GroupStop(' ) '))),DotComa('; '),Pipeline(Command(Argument(Normal('c')))))"
"Line(Pipeline(Command(Argument(Normal('a'))))Pipeline(Group(GroupStart Line(Pipeline(Command(Argument(Normal('b')))))GroupStop ))Pipeline(Command(Argument(Normal('c')))))"
'( a ; b ) | ( c ; d )'
"Line(Pipeline(Group(GroupStart('('),Line(Pipeline(Command(Separator(' '),Argument(Normal('a')))),DotComa(' ; '),Pipeline(Command(Argument(Normal('b'))))),GroupStop(' ) ')),Pipe('| '),Group(GroupStart('('),Line(Pipeline(Command(Separator(' '),Argument(Normal('c')))),DotComa(' ; '),Pipeline(Command(Argument(Normal('d'))))),GroupStop(' )'))))"
"Line(Pipeline(Group(GroupStart Line(Pipeline(Command(Argument(Normal('a'))))Pipeline(Command(Argument(Normal('b')))))GroupStop )Group(GroupStart Line(Pipeline(Command(Argument(Normal('c'))))Pipeline(Command(Argument(Normal('d')))))GroupStop )))"
'( a ) >b'
"Line(Pipeline(Group(GroupStart('('),Line(Pipeline(Command(Separator(' '),Argument(Normal('a'))))),GroupStop(' ) '),Redirection(Fildes(''),Direction('>'),File(Normal('b'))))))"
"Line(Pipeline(Group(GroupStart Line(Pipeline(Command(Argument(Normal('a')))))GroupStop Redirection(Fildes('')Direction('>')File(Normal('b'))))))"
'A=B'
"Line(Pipeline(Command(Affectation(Normal('A'),Equal('='),Normal('B')))))"
"Line(Pipeline(Command(Affectation(Normal('A')Equal('=')Normal('B')))))"
'A=B b c'
"Line(Pipeline(Command(Affectation(Normal('A'),Equal('='),Normal('B')),Separator(' '),Argument(Normal('b')),Separator(' '),Argument(Normal('c')))))"
"Line(Pipeline(Command(Affectation(Normal('A')Equal('=')Normal('B'))Argument(Normal('b'))Argument(Normal('c')))))"
'a $(c) b'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(Replacement(GroupStart('$('),Line(Pipeline(Command(Argument(Normal('c'))))),GroupStop(')'))),Separator(' '),Argument(Normal('b')))))"
"Line(Pipeline(Command(Argument(Normal('a'))Argument(Replacement(GroupStart Line(Pipeline(Command(Argument(Normal('c')))))GroupStop ))Argument(Normal('b')))))"
'a & b &'
"Line(Backgrounded(Pipeline(Command(Argument(Normal('a'))))),Background(' & '),Backgrounded(Pipeline(Command(Argument(Normal('b')))),Background(' &')))"
"Line(Backgrounded(Pipeline(Command(Argument(Normal('a')))))Backgrounded(Pipeline(Command(Argument(Normal('b'))))))"
'a; ;b'
"Line(Pipeline(Command(Argument(Normal('a')))),Unterminated('; '),DotComa(';'),Pipeline(Command(Argument(Normal('b')))))"
"Line(Pipeline(Command(Argument(Normal('a'))))Unterminated('; ')Pipeline(Command(Argument(Normal('b')))))"
'a | ; && #'
"Line(Pipeline(Command(Argument(Normal('a'))),Separator(' '),Unterminated('| ')),Conditionnal(Unterminated('; '),Unterminated('&& ')),Comment('#'))"
"Line(Pipeline(Command(Argument(Normal('a')))Unterminated('| '))Conditionnal(Unterminated('; ')Unterminated('&& '))Comment('#'))"
'[]a]'
"Line(Pipeline(Command(Argument(SquareBracket(SquareBracketStart('['),SquareBracketChar(']'),SquareBracketChar('a'),SquareBracketStop(']'))))))"
"Line(Pipeline(Command(Argument(SquareBracket(SquareBracketStart('[')SquareBracketChar(']')SquareBracketChar('a')SquareBracketStop(']'))))))"
'[!]]'
"Line(Pipeline(Command(Argument(SquareBracket(SquareBracketStart('['),SquareBracketNegate('!'),SquareBracketChar(']'),SquareBracketStop(']'))))))"
"Line(Pipeline(Command(Argument(SquareBracket(SquareBracketStart('[')SquareBracketNegate('!')SquareBracketChar(']')SquareBracketStop(']'))))))"
' |a'
"Line(Pipeline(Separator(' '),Unterminated('|'),Command(Argument(Normal('a')))))"
"Line(Pipeline(Unterminated('|')Command(Argument(Normal('a')))))"
'[$a\'$a\'"$a"\\"\\\']'
'Line(Pipeline(Command(Argument(SquareBracket(SquareBracketStart(\'[\'),Variable(\'$a\'),Quote("\'"),Normal(\'$\'),Normal(\'a\'),Quote("\'"),Guillemet(\'"\'),Variable(\'$a\'),Guillemet(\'"\'),Backslash(\'\\\\\'),Normal(\'"\'),Backslash(\'\\\\\'),Normal("\'"),SquareBracketStop(\']\'))))))'
'Line(Pipeline(Command(Argument(SquareBracket(SquareBracketStart(\'[\')Variable(\'$a\')Normal(\'$a\')VariableProtected(\'$a\')Normal(\'"\\\'\')SquareBracketStop(\']\'))))))'
'[a\\]]'
"Line(Pipeline(Command(Argument(SquareBracket(SquareBracketStart('['),SquareBracketChar('a'),Backslash('\\\\'),Normal(']'),SquareBracketStop(']'))))))"
"Line(Pipeline(Command(Argument(SquareBracket(SquareBracketStart('[')SquareBracketChar('a')Normal(']')SquareBracketStop(']'))))))"
'[a b]'
"Line(Pipeline(Command(Argument(Normal('[a')),Separator(' '),Argument(Normal('b]')))))"
"Line(Pipeline(Command(Argument(Normal('[a'))Argument(Normal('b]')))))"
'a&&b&'
"Line(Backgrounded(Conditionnal(Pipeline(Command(Argument(Normal('a')))),And('&&'),Pipeline(Command(Argument(Normal('b'))))),Background('&')))"
"Line(Backgrounded(Conditionnal(Pipeline(Command(Argument(Normal('a'))))&&Pipeline(Command(Argument(Normal('b')))))))"
'a&b&&c&'
"Line(Backgrounded(Pipeline(Command(Argument(Normal('a'))))),Background('&'),Backgrounded(Conditionnal(Pipeline(Command(Argument(Normal('b')))),And('&&'),Pipeline(Command(Argument(Normal('c'))))),Background('&')))"
"Line(Backgrounded(Pipeline(Command(Argument(Normal('a')))))Backgrounded(Conditionnal(Pipeline(Command(Argument(Normal('b'))))&&Pipeline(Command(Argument(Normal('c')))))))"
'for'
"Line(Pipeline(Command(ForLoop(Unterminated('for')))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for')))))"
'for '
"Line(Pipeline(Command(ForLoop(Unterminated('for ')))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')))))"
'for I'
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable(Argument(Normal('I')))))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable(Argument(Normal('I')))))))"
'for $I$J'
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable(Argument(Variable('$I'),Variable('$J')))))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable(Argument(Variable('$I')Variable('$J')))))))"
'for I ni'
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable(Argument(Normal('I'))),Separator(' '),Unexpected('ni')))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable(Argument(Normal('I')))Unexpected('ni')))))"
'for I in'
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable(Argument(Normal('I'))),In(' in')))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable(Argument(Normal('I')))))))"
'for I in '
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable(Argument(Normal('I'))),In(' in ')))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable(Argument(Normal('I')))))))"
'for I in a'
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable(Argument(Normal('I'))),In(' in '),ForValues(Argument(Normal('a')))))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable(Argument(Normal('I')))ForValues(Argument(Normal('a')))))))"
'for I in a '
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable(Argument(Normal('I'))),In(' in '),ForValues(Argument(Normal('a')),Unterminated(' '))))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable(Argument(Normal('I')))ForValues(Argument(Normal('a'))Unterminated(' '))))))"
'for I in a ;'
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable(Argument(Normal('I'))),In(' in '),ForValues(Argument(Normal('a'))),EndOfValues(' ;')))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable(Argument(Normal('I')))ForValues(Argument(Normal('a')))))))"
'for I in a ; '
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable(Argument(Normal('I'))),In(' in '),ForValues(Argument(Normal('a'))),EndOfValues(' ; ')))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable(Argument(Normal('I')))ForValues(Argument(Normal('a')))))))"
'for I in a $a * ; b'
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable(Argument(Normal('I'))),In(' in '),ForValues(Argument(Normal('a')),Separator(' '),Argument(Variable('$a')),Separator(' '),Argument(Star('*'))),EndOfValues(' ; '),Unexpected('b')))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable(Argument(Normal('I')))ForValues(Argument(Normal('a'))Argument(Variable('$a'))Argument(Star('*')))Unexpected('b')))))"
'for I in a b ; do a ; done'
"Line(Pipeline(Command(ForLoop(For('for '),LoopVariable(Argument(Normal('I'))),In(' in '),ForValues(Argument(Normal('a')),Separator(' '),Argument(Normal('b'))),EndOfValues(' ; '),Body(Do('do '),Pipeline(Command(Argument(Normal('a')))),DotComa(' ; '),Done('done'))))))"
"Line(Pipeline(Command(ForLoop(LoopVariable(Argument(Normal('I')))ForValues(Argument(Normal('a'))Argument(Normal('b')))Body(Pipeline(Command(Argument(Normal('a')))))))))"
'for I in a >'
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable(Argument(Normal('I'))),In(' in '),ForValues(Argument(Normal('a'))),Separator(' '),Unexpected('>')))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable(Argument(Normal('I')))ForValues(Argument(Normal('a')))Unexpected('>')))))"
'while'
"Line(Pipeline(Command(WhileLoop(Unterminated('while')))))"
"Line(Pipeline(Command(WhileLoop(Unterminated('while')))))"
'while a'
"Line(Pipeline(Command(WhileLoop(Unterminated('while '),Command(Argument(Normal('a')))))))"
"Line(Pipeline(Command(WhileLoop(Unterminated('while ')Command(Argument(Normal('a')))))))"
'for I in a;'
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable(Argument(Normal('I'))),In(' in '),ForValues(Argument(Normal('a'))),EndOfValues(';')))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable(Argument(Normal('I')))ForValues(Argument(Normal('a')))))))"
'while a ;'
"Line(Pipeline(Command(WhileLoop(Unterminated('while '),Command(Argument(Normal('a'))),EndOfValues(' ;')))))"
"Line(Pipeline(Command(WhileLoop(Unterminated('while ')Command(Argument(Normal('a')))))))"
'while a ; do'
"Line(Pipeline(Command(WhileLoop(Unterminated('while '),Command(Argument(Normal('a'))),EndOfValues(' ; '),Do('do')))))"
"Line(Pipeline(Command(WhileLoop(Unterminated('while ')Command(Argument(Normal('a')))))))"
'while a ; do a'
"Line(Pipeline(Command(WhileLoop(Unterminated('while '),Command(Argument(Normal('a'))),EndOfValues(' ; '),Body(Do('do '),Pipeline(Command(Argument(Normal('a')))))))))"
"Line(Pipeline(Command(WhileLoop(Unterminated('while ')Command(Argument(Normal('a')))Body(Pipeline(Command(Argument(Normal('a')))))))))"
'while a ; do a ; done'
"Line(Pipeline(Command(WhileLoop(While('while '),Command(Argument(Normal('a'))),EndOfValues(' ; '),Body(Do('do '),Pipeline(Command(Argument(Normal('a')))),DotComa(' ; '),Done('done'))))))"
"Line(Pipeline(Command(WhileLoop(Command(Argument(Normal('a')))Body(Pipeline(Command(Argument(Normal('a')))))))))"
'while a ; '
"Line(Pipeline(Command(WhileLoop(Unterminated('while '),Command(Argument(Normal('a'))),EndOfValues(' ; ')))))"
"Line(Pipeline(Command(WhileLoop(Unterminated('while ')Command(Argument(Normal('a')))))))"
'while a '
"Line(Pipeline(Command(WhileLoop(Unterminated('while '),Command(Argument(Normal('a')),Unterminated(' '))))))"
"Line(Pipeline(Command(WhileLoop(Unterminated('while ')Command(Argument(Normal('a'))Unterminated(' '))))))"
'$10$$$#$?'
"Line(Pipeline(Command(Argument(Variable('$1'),Normal('0'),Variable('$$'),Variable('$#'),Variable('$?')))))"
"Line(Pipeline(Command(Argument(Variable('$1')Normal('0')Variable('$$')Variable('$#')Variable('$?')))))"
'${toto}'
"Line(Pipeline(Command(Argument(Variable('${toto}')))))"
"Line(Pipeline(Command(Argument(Variable('${toto}')))))"
'${toto'
"Line(Pipeline(Command(Argument(Unterminated('${toto')))))"
"Line(Pipeline(Command(Argument(Unterminated('${toto')))))"
'a >'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Unterminated('>'))))"
"Line(Pipeline(Command(Argument(Normal('a'))Unterminated('>'))))"
'a > b'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Redirection(Fildes(''),Direction('> '),File(Normal('b'))))))"
"Line(Pipeline(Command(Argument(Normal('a'))Redirection(Fildes('')Direction('>')File(Normal('b'))))))"
'a > '
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Unterminated('> '))))"
"Line(Pipeline(Command(Argument(Normal('a'))Unterminated('> '))))"
')'
"Line(Unexpected(')'))"
"Line(Unexpected(')'))"
'a >)'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Unterminated('>'))),Unexpected(')'))"
"Line(Pipeline(Command(Argument(Normal('a'))Unterminated('>')))Unexpected(')'))"
'a >#'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Unterminated('>#'))))"
"Line(Pipeline(Command(Argument(Normal('a'))Unterminated('>#'))))"
'>('
"Line(Pipeline(Command(Unterminated('>'),Unexpected('('))))"
"Line(Pipeline(Command(Unterminated('>')Unexpected('('))))"
' a;b '
"Line(Pipeline(Command(Separator(' '),Argument(Normal('a')))),DotComa(';'),Pipeline(Command(Argument(Normal('b')),Separator(' '))))"
"Line(Pipeline(Command(Argument(Normal('a'))))Pipeline(Command(Argument(Normal('b')))))"
'A=5 for'
"Line(Pipeline(Command(Affectation(Normal('A'),Equal('='),Normal('5')),Separator(' '),ForLoop(Unterminated('for')))))"
"Line(Pipeline(Command(Affectation(Normal('A')Equal('=')Normal('5'))ForLoop(Unterminated('for')))))"
' while'
"Line(Pipeline(Command(Separator(' '),WhileLoop(Unterminated('while')))))"
"Line(Pipeline(Command(WhileLoop(Unterminated('while')))))"
' for'
"Line(Pipeline(Command(Separator(' '),ForLoop(Unterminated('for')))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for')))))"
'for I in ; do ; done'
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable(Argument(Normal('I'))),In(' in '),EndOfValues('; '),Body(Do('do '),DotComa('; '),Pipeline(Unexpected('done')))))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable(Argument(Normal('I')))Body(Pipeline(Unexpected('done')))))))"
'if'
"Line(Pipeline(Command(IfThenElse(Unterminated('if')))))"
"Line(Pipeline(Command(IfThenElse(Unterminated('if')))))"
'if '
"Line(Pipeline(Command(IfThenElse(Unterminated('if ')))))"
"Line(Pipeline(Command(IfThenElse(Unterminated('if ')))))"
'if a'
"Line(Pipeline(Command(IfThenElse(Unterminated('if '),Command(Argument(Normal('a')))))))"
"Line(Pipeline(Command(IfThenElse(Unterminated('if ')Command(Argument(Normal('a')))))))"
'if a '
"Line(Pipeline(Command(IfThenElse(Unterminated('if '),Command(Argument(Normal('a')),Unterminated(' '))))))"
"Line(Pipeline(Command(IfThenElse(Unterminated('if ')Command(Argument(Normal('a'))Unterminated(' '))))))"
'if a ;'
"Line(Pipeline(Command(IfThenElse(Unterminated('if '),Command(Argument(Normal('a'))),EndOfValues(' ;')))))"
"Line(Pipeline(Command(IfThenElse(Unterminated('if ')Command(Argument(Normal('a')))))))"
'if a;'
"Line(Pipeline(Command(IfThenElse(Unterminated('if '),Command(Argument(Normal('a'))),EndOfValues(';')))))"
"Line(Pipeline(Command(IfThenElse(Unterminated('if ')Command(Argument(Normal('a')))))))"
'if a; x'
"Line(Pipeline(Command(IfThenElse(Unterminated('if '),Command(Argument(Normal('a'))),EndOfValues('; '),Unexpected('x')))))"
"Line(Pipeline(Command(IfThenElse(Unterminated('if ')Command(Argument(Normal('a')))Unexpected('x')))))"
'if a; then'
"Line(Pipeline(Command(IfThenElse(Unterminated('if '),Command(Argument(Normal('a'))),EndOfValues('; '),ThenBloc(Then('then'))))))"
"Line(Pipeline(Command(IfThenElse(Unterminated('if ')Command(Argument(Normal('a')))ThenBloc()))))"
'if a; then b'
"Line(Pipeline(Command(IfThenElse(Unterminated('if '),Command(Argument(Normal('a'))),EndOfValues('; '),ThenBloc(Then('then '),Pipeline(Command(Argument(Normal('b')))))))))"
"Line(Pipeline(Command(IfThenElse(Unterminated('if ')Command(Argument(Normal('a')))ThenBloc(Pipeline(Command(Argument(Normal('b')))))))))"
'if a; then b c'
"Line(Pipeline(Command(IfThenElse(Unterminated('if '),Command(Argument(Normal('a'))),EndOfValues('; '),ThenBloc(Then('then '),Pipeline(Command(Argument(Normal('b')),Separator(' '),Argument(Normal('c')))))))))"
"Line(Pipeline(Command(IfThenElse(Unterminated('if ')Command(Argument(Normal('a')))ThenBloc(Pipeline(Command(Argument(Normal('b'))Argument(Normal('c')))))))))"
'if a; then b ;'
"Line(Pipeline(Command(IfThenElse(Unterminated('if '),Command(Argument(Normal('a'))),EndOfValues('; '),ThenBloc(Then('then '),Pipeline(Command(Argument(Normal('b')))),DotComa(' ;'))))))"
"Line(Pipeline(Command(IfThenElse(Unterminated('if ')Command(Argument(Normal('a')))ThenBloc(Pipeline(Command(Argument(Normal('b')))))))))"
'if a; then b ; '
"Line(Pipeline(Command(IfThenElse(Unterminated('if '),Command(Argument(Normal('a'))),EndOfValues('; '),ThenBloc(Then('then '),Pipeline(Command(Argument(Normal('b')))),DotComa(' ; '))))))"
"Line(Pipeline(Command(IfThenElse(Unterminated('if ')Command(Argument(Normal('a')))ThenBloc(Pipeline(Command(Argument(Normal('b')))))))))"
'if a; then b ; fi'
"Line(Pipeline(Command(IfThenElse(If('if '),Command(Argument(Normal('a'))),EndOfValues('; '),ThenBloc(Then('then '),Pipeline(Command(Argument(Normal('b')))),DotComa(' ; ')),Fi('fi')))))"
"Line(Pipeline(Command(IfThenElse(Command(Argument(Normal('a')))ThenBloc(Pipeline(Command(Argument(Normal('b')))))))))"
'if a; then fi'
"Line(Pipeline(Command(IfThenElse(Unterminated('if '),Command(Argument(Normal('a'))),EndOfValues('; '),ThenBloc(Then('then '),Pipeline(Unexpected('fi')))))))"
"Line(Pipeline(Command(IfThenElse(Unterminated('if ')Command(Argument(Normal('a')))ThenBloc(Pipeline(Unexpected('fi')))))))"
'if a; then ; fi'
"Line(Pipeline(Command(IfThenElse(Unterminated('if '),Command(Argument(Normal('a'))),EndOfValues('; '),ThenBloc(Then('then '),DotComa('; '),Pipeline(Unexpected('fi')))))))"
"Line(Pipeline(Command(IfThenElse(Unterminated('if ')Command(Argument(Normal('a')))ThenBloc(Pipeline(Unexpected('fi')))))))"
'if a; then ; a ; fi'
"Line(Pipeline(Command(IfThenElse(Unterminated('if '),Command(Argument(Normal('a'))),EndOfValues('; '),ThenBloc(Then('then '),DotComa('; '),Pipeline(Command(Argument(Normal('a')))),DotComa(' ; '),Pipeline(Unexpected('fi')))))))"
"Line(Pipeline(Command(IfThenElse(Unterminated('if ')Command(Argument(Normal('a')))ThenBloc(Pipeline(Command(Argument(Normal('a'))))Pipeline(Unexpected('fi')))))))"
'if a; then b ; else c ; fi'
"Line(Pipeline(Command(IfThenElse(If('if '),Command(Argument(Normal('a'))),EndOfValues('; '),ThenBloc(Then('then '),Pipeline(Command(Argument(Normal('b')))),DotComa(' ; ')),ElseBloc(Else('else'),Pipeline(Command(Separator(' '),Argument(Normal('c')))),DotComa(' ; ')),Fi('fi')))))"
"Line(Pipeline(Command(IfThenElse(Command(Argument(Normal('a')))ThenBloc(Pipeline(Command(Argument(Normal('b')))))ElseBloc(Pipeline(Command(Argument(Normal('c')))))))))"
'if a; then b | ; fi'
"Line(Pipeline(Command(IfThenElse(If('if '),Command(Argument(Normal('a'))),EndOfValues('; '),ThenBloc(Then('then '),Pipeline(Command(Argument(Normal('b'))),Separator(' '),Unterminated('| ')),DotComa('; ')),Fi('fi')))))"
"Line(Pipeline(Command(IfThenElse(Command(Argument(Normal('a')))ThenBloc(Pipeline(Command(Argument(Normal('b')))Unterminated('| ')))))))"
'for i in a ; do a & done'
"Line(Pipeline(Command(ForLoop(For('for '),LoopVariable(Argument(Normal('i'))),In(' in '),ForValues(Argument(Normal('a'))),EndOfValues(' ; '),Body(Do('do '),Backgrounded(Pipeline(Command(Argument(Normal('a'))))),Background(' & '),Done('done'))))))"
"Line(Pipeline(Command(ForLoop(LoopVariable(Argument(Normal('i')))ForValues(Argument(Normal('a')))Body(Backgrounded(Pipeline(Command(Argument(Normal('a'))))))))))"
'for i in a ; do a & b & done'
"Line(Pipeline(Command(ForLoop(For('for '),LoopVariable(Argument(Normal('i'))),In(' in '),ForValues(Argument(Normal('a'))),EndOfValues(' ; '),Body(Do('do '),Backgrounded(Pipeline(Command(Argument(Normal('a'))))),Background(' & '),Backgrounded(Pipeline(Command(Argument(Normal('b'))))),Background(' & '),Done('done'))))))"
"Line(Pipeline(Command(ForLoop(LoopVariable(Argument(Normal('i')))ForValues(Argument(Normal('a')))Body(Backgrounded(Pipeline(Command(Argument(Normal('a')))))Backgrounded(Pipeline(Command(Argument(Normal('b'))))))))))"
'for i in a ; do & done'
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable(Argument(Normal('i'))),In(' in '),ForValues(Argument(Normal('a'))),EndOfValues(' ; '),Body(Do('do '),Backgrounded(),Background('& '),Pipeline(Unexpected('done')))))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable(Argument(Normal('i')))ForValues(Argument(Normal('a')))Body(Backgrounded()Pipeline(Unexpected('done')))))))"
'for i in a ; do a&done'
"Line(Pipeline(Command(ForLoop(For('for '),LoopVariable(Argument(Normal('i'))),In(' in '),ForValues(Argument(Normal('a'))),EndOfValues(' ; '),Body(Do('do '),Backgrounded(Pipeline(Command(Argument(Normal('a'))))),Background('&'),Done('done'))))))"
"Line(Pipeline(Command(ForLoop(LoopVariable(Argument(Normal('i')))ForValues(Argument(Normal('a')))Body(Backgrounded(Pipeline(Command(Argument(Normal('a'))))))))))"
'while a; do b & done'
"Line(Pipeline(Command(WhileLoop(While('while '),Command(Argument(Normal('a'))),EndOfValues('; '),Body(Do('do '),Backgrounded(Pipeline(Command(Argument(Normal('b'))))),Background(' & '),Done('done'))))))"
"Line(Pipeline(Command(WhileLoop(Command(Argument(Normal('a')))Body(Backgrounded(Pipeline(Command(Argument(Normal('b'))))))))))"
'a &; b'
"Line(Backgrounded(Pipeline(Command(Argument(Normal('a'))))),Background(' &'),Unexpected('; '),Pipeline(Command(Argument(Normal('b')))))"
"Line(Backgrounded(Pipeline(Command(Argument(Normal('a')))))Unexpected('; ')Pipeline(Command(Argument(Normal('b')))))"
'while a; do b & ; done'
"Line(Pipeline(Command(WhileLoop(While('while '),Command(Argument(Normal('a'))),EndOfValues('; '),Body(Do('do '),Backgrounded(Pipeline(Command(Argument(Normal('b'))))),Background(' & '),Unexpected('; '),Done('done'))))))"
"Line(Pipeline(Command(WhileLoop(Command(Argument(Normal('a')))Body(Backgrounded(Pipeline(Command(Argument(Normal('b')))))Unexpected('; '))))))"
'$(a)'
"Line(Pipeline(Command(Argument(Replacement(GroupStart('$('),Line(Pipeline(Command(Argument(Normal('a'))))),GroupStop(')'))))))"
"Line(Pipeline(Command(Argument(Replacement(GroupStart Line(Pipeline(Command(Argument(Normal('a')))))GroupStop )))))"
'$('
"Line(Pipeline(Command(Argument(Replacement(Unterminated('$('),Line())))))"
"Line(Pipeline(Command(Argument(Replacement(Unterminated('$(')Line())))))"
'$(a)='
"Line(Pipeline(Command(Argument(Replacement(GroupStart('$('),Line(Pipeline(Command(Argument(Normal('a'))))),GroupStop(')')),Normal('=')))))"
"Line(Pipeline(Command(Argument(Replacement(GroupStart Line(Pipeline(Command(Argument(Normal('a')))))GroupStop )Normal('=')))))"
'$(a'
"Line(Pipeline(Command(Argument(Replacement(Unterminated('$('),Line(Pipeline(Command(Argument(Normal('a'))))))))))"
"Line(Pipeline(Command(Argument(Replacement(Unterminated('$(')Line(Pipeline(Command(Argument(Normal('a'))))))))))"
'$(a='
"Line(Pipeline(Command(Argument(Replacement(Unterminated('$('),Line(Pipeline(Command(Affectation(Normal('a'),Equal('='))))))))))"
"Line(Pipeline(Command(Argument(Replacement(Unterminated('$(')Line(Pipeline(Command(Affectation(Normal('a')Equal('='))))))))))"
'`'
"Line(Pipeline(Command(Argument(Unterminated('`')))))"
"Line(Pipeline(Command(Argument(Unterminated('`')))))"
'`a'
"Line(Pipeline(Command(Argument(Replacement(Unterminated('`'),Pipeline(Command(Argument(Normal('a')))))))))"
"Line(Pipeline(Command(Argument(Replacement(Unterminated('`')Pipeline(Command(Argument(Normal('a')))))))))"
'`a`'
"Line(Pipeline(Command(Argument(Replacement(GroupStart('`'),Pipeline(Command(Argument(Normal('a')))),GroupStop('`'))))))"
"Line(Pipeline(Command(Argument(Replacement(GroupStart Pipeline(Command(Argument(Normal('a'))))GroupStop )))))"
"`a'`"
'Line(Pipeline(Command(Argument(Replacement(Unterminated(\'`\'),Pipeline(Command(Argument(Normal(\'a\'),Unterminated("\'"),Normal(\'`\')))))))))'
'Line(Pipeline(Command(Argument(Replacement(Unterminated(\'`\')Pipeline(Command(Argument(Normal(\'a\')Unterminated("\'")Normal(\'`\')))))))))'
'`a"`'
'Line(Pipeline(Command(Argument(Replacement(Unterminated(\'`\'),Pipeline(Command(Argument(Normal(\'a\'),Unterminated(\'"\'),Unterminated(\'`\')))))))))'
'Line(Pipeline(Command(Argument(Replacement(Unterminated(\'`\')Pipeline(Command(Argument(Normal(\'a\')Unterminated(\'"\')Unterminated(\'`\')))))))))'
'` a `'
"Line(Pipeline(Command(Argument(Replacement(GroupStart('` '),Pipeline(Command(Argument(Normal('a')))),GroupStop(' `'))))))"
"Line(Pipeline(Command(Argument(Replacement(GroupStart Pipeline(Command(Argument(Normal('a'))))GroupStop )))))"
'a&&b&&c'
"Line(Conditionnal(Pipeline(Command(Argument(Normal('a')))),And('&&'),Pipeline(Command(Argument(Normal('b')))),And('&&'),Pipeline(Command(Argument(Normal('c'))))))"
"Line(Conditionnal(Pipeline(Command(Argument(Normal('a'))))&&Pipeline(Command(Argument(Normal('b'))))&&Pipeline(Command(Argument(Normal('c'))))))"
'a&&b||c&&d'
"Line(Conditionnal(Pipeline(Command(Argument(Normal('a')))),And('&&'),Pipeline(Command(Argument(Normal('b')))),Or('||'),Pipeline(Command(Argument(Normal('c')))),And('&&'),Pipeline(Command(Argument(Normal('d'))))))"
"Line(Conditionnal(Pipeline(Command(Argument(Normal('a'))))&&Pipeline(Command(Argument(Normal('b'))))||Pipeline(Command(Argument(Normal('c'))))&&Pipeline(Command(Argument(Normal('d'))))))"
'for I in ; do A ; done >B'
"Line(Pipeline(Command(ForLoop(For('for '),LoopVariable(Argument(Normal('I'))),In(' in '),EndOfValues('; '),Body(Do('do '),Pipeline(Command(Argument(Normal('A')))),DotComa(' ; '),Done('done')),Separator(' '),Redirection(Fildes(''),Direction('>'),File(Normal('B')))))))"
"Line(Pipeline(Command(ForLoop(LoopVariable(Argument(Normal('I')))Body(Pipeline(Command(Argument(Normal('A')))))Redirection(Fildes('')Direction('>')File(Normal('B')))))))"
'for I in ; do A ; done # D'
"Line(Pipeline(Command(ForLoop(For('for '),LoopVariable(Argument(Normal('I'))),In(' in '),EndOfValues('; '),Body(Do('do '),Pipeline(Command(Argument(Normal('A')))),DotComa(' ; '),Done('done'))))),Separator(' '),Comment('# D'))"
"Line(Pipeline(Command(ForLoop(LoopVariable(Argument(Normal('I')))Body(Pipeline(Command(Argument(Normal('A'))))))))Comment('# D'))"
'for I in ; do A ; done BC ; D'
"Line(Pipeline(Command(ForLoop(For('for '),LoopVariable(Argument(Normal('I'))),In(' in '),EndOfValues('; '),Body(Do('do '),Pipeline(Command(Argument(Normal('A')))),DotComa(' ; '),Done('done')),Separator(' '),Unexpected('BC ')))),DotComa('; '),Pipeline(Command(Argument(Normal('D')))))"
"Line(Pipeline(Command(ForLoop(LoopVariable(Argument(Normal('I')))Body(Pipeline(Command(Argument(Normal('A')))))Unexpected('BC '))))Pipeline(Command(Argument(Normal('D')))))"
'if a ; then b ; fi >x m'
"Line(Pipeline(Command(IfThenElse(If('if '),Command(Argument(Normal('a'))),EndOfValues(' ; '),ThenBloc(Then('then '),Pipeline(Command(Argument(Normal('b')))),DotComa(' ; ')),Fi('fi'),Separator(' '),Redirection(Fildes(''),Direction('>'),File(Normal('x'))),Separator(' '),Unexpected('m')))))"
"Line(Pipeline(Command(IfThenElse(Command(Argument(Normal('a')))ThenBloc(Pipeline(Command(Argument(Normal('b')))))Redirection(Fildes('')Direction('>')File(Normal('x')))Unexpected('m')))))"
'fi;done;else;do'
"Line(Pipeline(Unexpected('fi')))"
"Line(Pipeline(Unexpected('fi')))"
'\'do\';"done"'
'Line(Pipeline(Command(Argument(Quote("\'"),Normal(\'do\'),Quote("\'")))),DotComa(\';\'),Pipeline(Command(Argument(Guillemet(\'"\'),Normal(\'done\'),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Argument(Normal('do'))))Pipeline(Command(Argument(Normal('done')))))"
'for I in ; do a ; fi'
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable(Argument(Normal('I'))),In(' in '),EndOfValues('; '),Body(Do('do '),Pipeline(Command(Argument(Normal('a')))),DotComa(' ; '),Pipeline(Unexpected('fi')))))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable(Argument(Normal('I')))Body(Pipeline(Command(Argument(Normal('a'))))Pipeline(Unexpected('fi')))))))"
'  done'
"Line(Pipeline(Unexpected('  done')))"
"Line(Pipeline(Unexpected('  done')))"
'cp --recursive'
"Line(Pipeline(Command(Argument(Normal('cp')),Separator(' '),Argument(Normal('--recursive')))))"
"Line(Pipeline(Command(Argument(Normal('cp'))Argument(Normal('-r')))))"
'cd --recursive'
"Line(Pipeline(Command(Argument(Normal('cd')),Separator(' '),Argument(Normal('--recursive')))))"
"Line(Pipeline(Command(Argument(Normal('cd'))Argument(Normal('--recursive')))))"
'$A'
"Line(Pipeline(Command(Argument(Variable('$A')))))"
"Line(Pipeline(Command(Argument(Variable('$A')))))"
'"$A"'
'Line(Pipeline(Command(Argument(Guillemet(\'"\'),Variable(\'$A\'),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Argument(VariableProtected('$A')))))"
'$($A "$B") "$($C "$D")"'
'Line(Pipeline(Command(Argument(Replacement(GroupStart(\'$(\'),Line(Pipeline(Command(Argument(Variable(\'$A\')),Separator(\' \'),Argument(Guillemet(\'"\'),Variable(\'$B\'),Guillemet(\'"\'))))),GroupStop(\')\'))),Separator(\' \'),Argument(Guillemet(\'"\'),Replacement(GroupStart(\'$(\'),Line(Pipeline(Command(Argument(Variable(\'$C\')),Separator(\' \'),Argument(Guillemet(\'"\'),Variable(\'$D\'),Guillemet(\'"\'))))),GroupStop(\')\')),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Argument(Replacement(GroupStart Line(Pipeline(Command(Argument(Variable('$A'))Argument(VariableProtected('$B')))))GroupStop ))Argument(ReplacementProtected(GroupStart Line(Pipeline(Command(Argument(Variable('$C'))Argument(VariableProtected('$D')))))GroupStop )))))"
'"$(a")'
'Line(Pipeline(Command(Argument(Unterminated(\'"\'),Replacement(Unterminated(\'$(\'),Line(Pipeline(Command(Argument(Normal(\'a\'),Unterminated(\'"\'),Normal(\')\'))))))))))'
'Line(Pipeline(Command(Argument(Unterminated(\'"\')Replacement(Unterminated(\'$(\')Line(Pipeline(Command(Argument(Normal(\'a\')Unterminated(\'"\')Normal(\')\'))))))))))'
