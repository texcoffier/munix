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
"Line(Pipeline(Command(Argument(Quote('\\''),Normal(' '),Quote('\\'')),Separator(' '),Argument(Quote('\\''),Normal('  '),Quote('\\'')),Separator(' '),Argument(Quote('\\''),Normal('\\\\'),Quote('\\'')),Separator(' '),Argument(Quote('\\''),Normal('\\\\\\\\'),Quote('\\'')),Separator(' '),Argument(Quote('\\''),Normal('\\\\\\\\\\\\'),Quote('\\'')),Separator(' '),Argument(Unterminated('\\'')))))"
"Line(Pipeline(Command(Argument(Normal(' '))Argument(Normal('  '))Argument(Normal('\\\\'))Argument(Normal('\\\\\\\\'))Argument(Normal('\\\\\\\\\\\\'))Argument(Unterminated('\\'')))))"
"a'b"
"Line(Pipeline(Command(Argument(Normal('a'),Unterminated('\\''),Normal('b')))))"
"Line(Pipeline(Command(Argument(Normal('a')Unterminated('\\'')Normal('b')))))"
"$A '$B' \\$B $/ $B1/ $"
"Line(Pipeline(Command(Argument(Variable('$A')),Separator(' '),Argument(Quote('\\''),Normal('$B'),Quote('\\'')),Separator(' '),Argument(Backslash('\\\\'),Normal('$B')),Separator(' '),Argument(Normal('$/')),Separator(' '),Argument(Variable('$B1'),Normal('/')),Separator(' '),Argument(Normal('$')))))"
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
"Line(Pipeline(Command(Argument(Normal('a'))Argument(SquareBracket(SquareBracketChar('a')SquareBracketChar('b')SquareBracketStart('[')SquareBracketStop(']'))))))"
'a ['
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(Normal('[')))))"
"Line(Pipeline(Command(Argument(Normal('a'))Argument(Normal('[')))))"
'a [a-bcd-e]'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(SquareBracket(SquareBracketStart('['),SquareBracketInterval('a-b'),SquareBracketChar('c'),SquareBracketInterval('d-e'),SquareBracketStop(']'))))))"
"Line(Pipeline(Command(Argument(Normal('a'))Argument(SquareBracket(SquareBracketChar('c')SquareBracketInterval('a-b')SquareBracketInterval('d-e')SquareBracketStart('[')SquareBracketStop(']'))))))"
'a []a-c-d]'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(SquareBracket(SquareBracketStart('['),SquareBracketChar(']'),SquareBracketInterval('a-c'),SquareBracketChar('-'),SquareBracketChar('d'),SquareBracketStop(']'))))))"
"Line(Pipeline(Command(Argument(Normal('a'))Argument(SquareBracket(SquareBracketChar('-')SquareBracketChar(']')SquareBracketChar('d')SquareBracketInterval('a-c')SquareBracketStart('[')SquareBracketStop(']'))))))"
'a [!a-]]'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(SquareBracket(SquareBracketStart('['),SquareBracketNegate('!'),SquareBracketChar('a'),SquareBracketChar('-'),SquareBracketStop(']')),Normal(']')))))"
"Line(Pipeline(Command(Argument(Normal('a'))Argument(SquareBracket(SquareBracketChar('-')SquareBracketChar('a')SquareBracketNegate('!')SquareBracketStart('[')SquareBracketStop(']'))Normal(']')))))"
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
"Line(Pipeline(Command(Affectation(VariableName('A'),Equal('='),Normal('B')))))"
"Line(Pipeline(Command(Affectation(VariableName('A')Equal('=')Normal('B')))))"
'A=B b c'
"Line(Pipeline(Command(Affectation(VariableName('A'),Equal('='),Normal('B')),Separator(' '),Argument(Normal('b')),Separator(' '),Argument(Normal('c')))))"
"Line(Pipeline(Command(Affectation(VariableName('A')Equal('=')Normal('B'))Argument(Normal('b'))Argument(Normal('c')))))"
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
"Line(Pipeline(Command(Argument(SquareBracket(SquareBracketChar(']')SquareBracketChar('a')SquareBracketStart('[')SquareBracketStop(']'))))))"
'[!]]'
"Line(Pipeline(Command(Argument(SquareBracket(SquareBracketStart('['),SquareBracketNegate('!'),SquareBracketChar(']'),SquareBracketStop(']'))))))"
"Line(Pipeline(Command(Argument(SquareBracket(SquareBracketChar(']')SquareBracketNegate('!')SquareBracketStart('[')SquareBracketStop(']'))))))"
' |a'
"Line(Pipeline(Separator(' '),Unterminated('|'),Command(Argument(Normal('a')))))"
"Line(Pipeline(Unterminated('|')Command(Argument(Normal('a')))))"
'[$a\'$a\'"$a"\\"\\\']'
'Line(Pipeline(Command(Argument(SquareBracket(SquareBracketStart(\'[\'),Variable(\'$a\'),Quote(\'\\\'\'),Normal(\'$\'),Normal(\'a\'),Quote(\'\\\'\'),Guillemet(\'"\'),Variable(\'$a\'),Guillemet(\'"\'),Backslash(\'\\\\\'),SquareBracketChar(\'"\'),Backslash(\'\\\\\'),SquareBracketChar(\'\\\'\'),SquareBracketStop(\']\'))))))'
'Line(Pipeline(Command(Argument(SquareBracket(Normal(\'$a\')SquareBracketChar(\'"\')SquareBracketChar(\'\\\'\')SquareBracketStart(\'[\')SquareBracketStop(\']\')Variable(\'$a\')VariableProtected(\'$a\'))))))'
'[a\\]]'
"Line(Pipeline(Command(Argument(SquareBracket(SquareBracketStart('['),SquareBracketChar('a'),Backslash('\\\\'),SquareBracketChar(']'),SquareBracketStop(']'))))))"
"Line(Pipeline(Command(Argument(SquareBracket(SquareBracketChar(']')SquareBracketChar('a')SquareBracketStart('[')SquareBracketStop(']'))))))"
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
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable('I')))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable('I')))))"
'for $I$J'
"Line(Pipeline(Command(ForLoop(Unterminated('for '),Unterminated('$I$J')))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')Unterminated('$I$J')))))"
'for I ni'
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable('I'),Separator(' '),Unexpected('ni')))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable('I')Unexpected('ni')))))"
'for I in'
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable('I'),In(' in')))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable('I')))))"
'for I in '
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable('I'),In(' in ')))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable('I')))))"
'for I in a'
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable('I'),In(' in '),ForValues(Argument(Normal('a')))))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable('I')ForValues(Argument(Normal('a')))))))"
'for I in a '
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable('I'),In(' in '),ForValues(Argument(Normal('a')),Unterminated(' '))))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable('I')ForValues(Argument(Normal('a'))Unterminated(' '))))))"
'for I in a ;'
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable('I'),In(' in '),ForValues(Argument(Normal('a'))),EndOfValues(' ;')))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable('I')ForValues(Argument(Normal('a')))))))"
'for I in a ; '
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable('I'),In(' in '),ForValues(Argument(Normal('a'))),EndOfValues(' ; ')))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable('I')ForValues(Argument(Normal('a')))))))"
'for I in a $a * ; b'
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable('I'),In(' in '),ForValues(Argument(Normal('a')),Separator(' '),Argument(Variable('$a')),Separator(' '),Argument(Star('*'))),EndOfValues(' ; '),Unexpected('b')))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable('I')ForValues(Argument(Normal('a'))Argument(Variable('$a'))Argument(Star('*')))Unexpected('b')))))"
'for I in a b ; do a ; done'
"Line(Pipeline(Command(ForLoop(For('for '),LoopVariable('I'),In(' in '),ForValues(Argument(Normal('a')),Separator(' '),Argument(Normal('b'))),EndOfValues(' ; '),Body(Do('do '),Pipeline(Command(Argument(Normal('a')))),DotComa(' ; '),Done('done'))))))"
"Line(Pipeline(Command(ForLoop(LoopVariable('I')ForValues(Argument(Normal('a'))Argument(Normal('b')))Body(Pipeline(Command(Argument(Normal('a')))))))))"
'for I in a >'
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable('I'),In(' in '),ForValues(Argument(Normal('a'))),Separator(' '),Unexpected('>')))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable('I')ForValues(Argument(Normal('a')))Unexpected('>')))))"
'while'
"Line(Pipeline(Command(WhileLoop(Unterminated('while')))))"
"Line(Pipeline(Command(WhileLoop(Unterminated('while')))))"
'while a'
"Line(Pipeline(Command(WhileLoop(Unterminated('while '),Command(Argument(Normal('a')))))))"
"Line(Pipeline(Command(WhileLoop(Unterminated('while ')Command(Argument(Normal('a')))))))"
'for I in a;'
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable('I'),In(' in '),ForValues(Argument(Normal('a'))),EndOfValues(';')))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable('I')ForValues(Argument(Normal('a')))))))"
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
"Line(Pipeline(Command(Affectation(VariableName('A'),Equal('='),Normal('5')),Separator(' '),Argument(Normal('for')))))"
"Line(Pipeline(Command(Affectation(VariableName('A')Equal('=')Normal('5'))Argument(Normal('for')))))"
' while'
"Line(Pipeline(Command(Separator(' '),WhileLoop(Unterminated('while')))))"
"Line(Pipeline(Command(WhileLoop(Unterminated('while')))))"
' for'
"Line(Pipeline(Command(Separator(' '),ForLoop(Unterminated('for')))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for')))))"
'for I in ; do ; done'
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable('I'),In(' in '),EndOfValues('; '),Body(Do('do '),DotComa('; '),Pipeline(Unexpected('done')))))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable('I')Body(Pipeline(Unexpected('done')))))))"
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
"Line(Pipeline(Command(IfThenElse(If('if '),Command(Argument(Normal('a'))),EndOfValues('; '),ThenBloc(Then('then '),Pipeline(Command(Argument(Normal('b')))),DotComa(' ; ')),ElseBloc(Else('else '),Pipeline(Command(Argument(Normal('c')))),DotComa(' ; ')),Fi('fi')))))"
"Line(Pipeline(Command(IfThenElse(Command(Argument(Normal('a')))ThenBloc(Pipeline(Command(Argument(Normal('b')))))ElseBloc(Pipeline(Command(Argument(Normal('c')))))))))"
'if a; then b | ; fi'
"Line(Pipeline(Command(IfThenElse(If('if '),Command(Argument(Normal('a'))),EndOfValues('; '),ThenBloc(Then('then '),Pipeline(Command(Argument(Normal('b'))),Separator(' '),Unterminated('| ')),DotComa('; ')),Fi('fi')))))"
"Line(Pipeline(Command(IfThenElse(Command(Argument(Normal('a')))ThenBloc(Pipeline(Command(Argument(Normal('b')))Unterminated('| ')))))))"
'for i in a ; do a & done'
"Line(Pipeline(Command(ForLoop(For('for '),LoopVariable('i'),In(' in '),ForValues(Argument(Normal('a'))),EndOfValues(' ; '),Body(Do('do '),Backgrounded(Pipeline(Command(Argument(Normal('a'))))),Background(' & '),Done('done'))))))"
"Line(Pipeline(Command(ForLoop(LoopVariable('i')ForValues(Argument(Normal('a')))Body(Backgrounded(Pipeline(Command(Argument(Normal('a'))))))))))"
'for i in a ; do a & b & done'
"Line(Pipeline(Command(ForLoop(For('for '),LoopVariable('i'),In(' in '),ForValues(Argument(Normal('a'))),EndOfValues(' ; '),Body(Do('do '),Backgrounded(Pipeline(Command(Argument(Normal('a'))))),Background(' & '),Backgrounded(Pipeline(Command(Argument(Normal('b'))))),Background(' & '),Done('done'))))))"
"Line(Pipeline(Command(ForLoop(LoopVariable('i')ForValues(Argument(Normal('a')))Body(Backgrounded(Pipeline(Command(Argument(Normal('a')))))Backgrounded(Pipeline(Command(Argument(Normal('b'))))))))))"
'for i in a ; do & done'
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable('i'),In(' in '),ForValues(Argument(Normal('a'))),EndOfValues(' ; '),Body(Do('do '),Backgrounded(),Background('& '),Pipeline(Unexpected('done')))))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable('i')ForValues(Argument(Normal('a')))Body(Backgrounded()Pipeline(Unexpected('done')))))))"
'for i in a ; do a&done'
"Line(Pipeline(Command(ForLoop(For('for '),LoopVariable('i'),In(' in '),ForValues(Argument(Normal('a'))),EndOfValues(' ; '),Body(Do('do '),Backgrounded(Pipeline(Command(Argument(Normal('a'))))),Background('&'),Done('done'))))))"
"Line(Pipeline(Command(ForLoop(LoopVariable('i')ForValues(Argument(Normal('a')))Body(Backgrounded(Pipeline(Command(Argument(Normal('a'))))))))))"
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
"Line(Pipeline(Command(Argument(Replacement(Unterminated('$('),Line(Pipeline(Command(Affectation(VariableName('a'),Equal('='))))))))))"
"Line(Pipeline(Command(Argument(Replacement(Unterminated('$(')Line(Pipeline(Command(Affectation(VariableName('a')Equal('='))))))))))"
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
"Line(Pipeline(Command(Argument(Replacement(Unterminated('`'),Pipeline(Command(Argument(Normal('a'),Unterminated('\\''),Normal('`')))))))))"
"Line(Pipeline(Command(Argument(Replacement(Unterminated('`')Pipeline(Command(Argument(Normal('a')Unterminated('\\'')Normal('`')))))))))"
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
"Line(Pipeline(Command(ForLoop(For('for '),LoopVariable('I'),In(' in '),EndOfValues('; '),Body(Do('do '),Pipeline(Command(Argument(Normal('A')))),DotComa(' ; '),Done('done')),Separator(' '),Redirection(Fildes(''),Direction('>'),File(Normal('B')))))))"
"Line(Pipeline(Command(ForLoop(LoopVariable('I')Body(Pipeline(Command(Argument(Normal('A')))))Redirection(Fildes('')Direction('>')File(Normal('B')))))))"
'for I in ; do A ; done # D'
"Line(Pipeline(Command(ForLoop(For('for '),LoopVariable('I'),In(' in '),EndOfValues('; '),Body(Do('do '),Pipeline(Command(Argument(Normal('A')))),DotComa(' ; '),Done('done'))))),Separator(' '),Comment('# D'))"
"Line(Pipeline(Command(ForLoop(LoopVariable('I')Body(Pipeline(Command(Argument(Normal('A'))))))))Comment('# D'))"
'for I in ; do A ; done BC ; D'
"Line(Pipeline(Command(ForLoop(For('for '),LoopVariable('I'),In(' in '),EndOfValues('; '),Body(Do('do '),Pipeline(Command(Argument(Normal('A')))),DotComa(' ; '),Done('done')),Separator(' '),Unexpected('BC ')))),DotComa('; '),Pipeline(Command(Argument(Normal('D')))))"
"Line(Pipeline(Command(ForLoop(LoopVariable('I')Body(Pipeline(Command(Argument(Normal('A')))))Unexpected('BC '))))Pipeline(Command(Argument(Normal('D')))))"
'if a ; then b ; fi >x m'
"Line(Pipeline(Command(IfThenElse(If('if '),Command(Argument(Normal('a'))),EndOfValues(' ; '),ThenBloc(Then('then '),Pipeline(Command(Argument(Normal('b')))),DotComa(' ; ')),Fi('fi'),Separator(' '),Redirection(Fildes(''),Direction('>'),File(Normal('x'))),Separator(' '),Unexpected('m')))))"
"Line(Pipeline(Command(IfThenElse(Command(Argument(Normal('a')))ThenBloc(Pipeline(Command(Argument(Normal('b')))))Redirection(Fildes('')Direction('>')File(Normal('x')))Unexpected('m')))))"
'fi;done;else;do'
"Line(Pipeline(Unexpected('fi')))"
"Line(Pipeline(Unexpected('fi')))"
'\'do\';"done"'
'Line(Pipeline(Command(Argument(Quote(\'\\\'\'),Normal(\'do\'),Quote(\'\\\'\')))),DotComa(\';\'),Pipeline(Command(Argument(Guillemet(\'"\'),Normal(\'done\'),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Argument(Normal('do'))))Pipeline(Command(Argument(Normal('done')))))"
'for I in ; do a ; fi'
"Line(Pipeline(Command(ForLoop(Unterminated('for '),LoopVariable('I'),In(' in '),EndOfValues('; '),Body(Do('do '),Pipeline(Command(Argument(Normal('a')))),DotComa(' ; '),Pipeline(Unexpected('fi')))))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')LoopVariable('I')Body(Pipeline(Command(Argument(Normal('a'))))Pipeline(Unexpected('fi')))))))"
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
'a ~'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(Home('~')))))"
"Line(Pipeline(Command(Argument(Normal('a'))Argument(Home('~')))))"
'a "~"'
'Line(Pipeline(Command(Argument(Normal(\'a\')),Separator(\' \'),Argument(Guillemet(\'"\'),Normal(\'~\'),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Argument(Normal('a'))Argument(Normal('~')))))"
'a ~b'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(Home('~b')))))"
"Line(Pipeline(Command(Argument(Normal('a'))Argument(Home('~b')))))"
'a ~b/c'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(Home('~b'),Normal('/c')))))"
"Line(Pipeline(Command(Argument(Normal('a'))Argument(Home('~b')Normal('/c')))))"
'a ~/b'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(Home('~'),Normal('/b')))))"
"Line(Pipeline(Command(Argument(Normal('a'))Argument(Home('~')Normal('/b')))))"
'a ~b*'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(Unterminated('~b'),Star('*')))))"
"Line(Pipeline(Command(Argument(Normal('a'))Argument(Unterminated('~b')Star('*')))))"
'a b~c'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(Normal('b~c')))))"
"Line(Pipeline(Command(Argument(Normal('a'))Argument(Normal('b~c')))))"
"u'a'"
"Line(Pipeline(Command(Argument(Normal('u'),Quote('\\''),Normal('a'),Quote('\\'')))))"
"Line(Pipeline(Command(Argument(Normal('ua')))))"
'more a'
"Line(Pipeline(Command(Argument(Normal('more')),Separator(' '),Argument(Normal('a')))))"
"Line(Pipeline(Command(Argument(Normal('less'))Argument(Normal('a')))))"
'man -k l'
"Line(Pipeline(Command(Argument(Normal('man')),Separator(' '),Argument(Normal('-k')),Separator(' '),Argument(Normal('l')))))"
"Line(Pipeline(Command(Argument(Normal('man'))Argument(Normal('-kl')))))"
'man ""-k ls'
'Line(Pipeline(Command(Argument(Normal(\'man\')),Separator(\' \'),Argument(Guillemet(\'"\'),Guillemet(\'"\'),Normal(\'-k\')),Separator(\' \'),Argument(Normal(\'ls\')))))'
"Line(Pipeline(Command(Argument(Normal('man'))Argument(Normal('-kls')))))"
'man "-k" ls'
'Line(Pipeline(Command(Argument(Normal(\'man\')),Separator(\' \'),Argument(Guillemet(\'"\'),Normal(\'-k\'),Guillemet(\'"\')),Separator(\' \'),Argument(Normal(\'ls\')))))'
"Line(Pipeline(Command(Argument(Normal('man'))Argument(Normal('-kls')))))"
'man "-" ls'
'Line(Pipeline(Command(Argument(Normal(\'man\')),Separator(\' \'),Argument(Guillemet(\'"\'),Normal(\'-\'),Guillemet(\'"\')),Separator(\' \'),Argument(Normal(\'ls\')))))'
"Line(Pipeline(Command(Argument(Normal('man'))Argument(Normal('-'))Argument(Normal('ls')))))"
'man "-"k ls'
'Line(Pipeline(Command(Argument(Normal(\'man\')),Separator(\' \'),Argument(Guillemet(\'"\'),Normal(\'-\'),Guillemet(\'"\'),Normal(\'k\')),Separator(\' \'),Argument(Normal(\'ls\')))))'
"Line(Pipeline(Command(Argument(Normal('man'))Argument(Normal('-kls')))))"
'rm -ri'
"Line(Pipeline(Command(Argument(Normal('rm')),Separator(' '),Argument(Normal('-ri')))))"
"Line(Pipeline(Command(Argument(Normal('rm'))Argument(Normal('-ir')))))"
'rm -r -i'
"Line(Pipeline(Command(Argument(Normal('rm')),Separator(' '),Argument(Normal('-r')),Separator(' '),Argument(Normal('-i')))))"
"Line(Pipeline(Command(Argument(Normal('rm'))Argument(Normal('-ir')))))"
'rm -i -r'
"Line(Pipeline(Command(Argument(Normal('rm')),Separator(' '),Argument(Normal('-i')),Separator(' '),Argument(Normal('-r')))))"
"Line(Pipeline(Command(Argument(Normal('rm'))Argument(Normal('-ir')))))"
'rm --recursive --interactive'
"Line(Pipeline(Command(Argument(Normal('rm')),Separator(' '),Argument(Normal('--recursive')),Separator(' '),Argument(Normal('--interactive')))))"
"Line(Pipeline(Command(Argument(Normal('rm'))Argument(Normal('-ir')))))"
'rm -r --interactive'
"Line(Pipeline(Command(Argument(Normal('rm')),Separator(' '),Argument(Normal('-r')),Separator(' '),Argument(Normal('--interactive')))))"
"Line(Pipeline(Command(Argument(Normal('rm'))Argument(Normal('-ir')))))"
'rm --recursive -i'
"Line(Pipeline(Command(Argument(Normal('rm')),Separator(' '),Argument(Normal('--recursive')),Separator(' '),Argument(Normal('-i')))))"
"Line(Pipeline(Command(Argument(Normal('rm'))Argument(Normal('-ir')))))"
'a b=c'
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(Normal('b=c')))))"
"Line(Pipeline(Command(Argument(Normal('a'))Argument(Normal('b=c')))))"
'tail --lines 5'
"Line(Pipeline(Command(Argument(Normal('tail')),Separator(' '),Argument(Normal('--lines')),Separator(' '),Argument(Normal('5')))))"
"Line(Pipeline(Command(Argument(Normal('tail'))Argument(Normal('-n5')))))"
'tail --lines=5'
"Line(Pipeline(Command(Argument(Normal('tail')),Separator(' '),Argument(Normal('--lines=5')))))"
"Line(Pipeline(Command(Argument(Normal('tail'))Argument(Normal('-n5')))))"
'tail -n 5'
"Line(Pipeline(Command(Argument(Normal('tail')),Separator(' '),Argument(Normal('-n')),Separator(' '),Argument(Normal('5')))))"
"Line(Pipeline(Command(Argument(Normal('tail'))Argument(Normal('-n5')))))"
'[ ]'
"Line(Pipeline(Command(Argument(Normal('[')),Separator(' '),Argument(Normal(']')))))"
"Line(Pipeline(Command(Argument(Normal('['))Argument(Normal(']')))))"
'[|]'
"Line(Pipeline(Command(Argument(Normal('['))),Pipe('|'),Command(Argument(Normal(']')))))"
"Line(Pipeline(Command(Argument(Normal('[')))Command(Argument(Normal(']')))))"
'[\\|]'
"Line(Pipeline(Command(Argument(SquareBracket(SquareBracketStart('['),Backslash('\\\\'),SquareBracketChar('|'),SquareBracketStop(']'))))))"
"Line(Pipeline(Command(Argument(SquareBracket(SquareBracketChar('|')SquareBracketStart('[')SquareBracketStop(']'))))))"
'tar -c -v'
"Line(Pipeline(Command(Argument(Normal('tar')),Separator(' '),Argument(Normal('-c')),Separator(' '),Argument(Normal('-v')))))"
"Line(Pipeline(Command(Argument(Normal('tar'))Argument(Normal('-c')))))"
'tar -v -c'
"Line(Pipeline(Command(Argument(Normal('tar')),Separator(' '),Argument(Normal('-v')),Separator(' '),Argument(Normal('-c')))))"
"Line(Pipeline(Command(Argument(Normal('tar'))Argument(Normal('-c')))))"
'tar -vc'
"Line(Pipeline(Command(Argument(Normal('tar')),Separator(' '),Argument(Normal('-vc')))))"
"Line(Pipeline(Command(Argument(Normal('tar'))Argument(Normal('-c')))))"
'tar -cv'
"Line(Pipeline(Command(Argument(Normal('tar')),Separator(' '),Argument(Normal('-cv')))))"
"Line(Pipeline(Command(Argument(Normal('tar'))Argument(Normal('-c')))))"
'tar -v'
"Line(Pipeline(Command(Argument(Normal('tar')),Separator(' '),Argument(Normal('-v')))))"
"Line(Pipeline(Command(Argument(Normal('tar')))))"
'echo [A][B]'
"Line(Pipeline(Command(Argument(Normal('echo')),Separator(' '),Argument(SquareBracket(SquareBracketStart('['),SquareBracketChar('A'),SquareBracketStop(']')),SquareBracket(SquareBracketStart('['),SquareBracketChar('B'),SquareBracketStop(']'))))))"
"Line(Pipeline(Command(Argument(Normal('echo'))Argument(SquareBracket(SquareBracketChar('A')SquareBracketStart('[')SquareBracketStop(']'))SquareBracket(SquareBracketChar('B')SquareBracketStart('[')SquareBracketStop(']'))))))"
'echo [A;B]'
"Line(Pipeline(Command(Argument(Normal('echo')),Separator(' '),Argument(Normal('[A')))),DotComa(';'),Pipeline(Command(Argument(Normal('B]')))))"
"Line(Pipeline(Command(Argument(Normal('echo'))Argument(Normal('[A'))))Pipeline(Command(Argument(Normal('B]')))))"
'echo [A&B]'
"Line(Backgrounded(Pipeline(Command(Argument(Normal('echo')),Separator(' '),Argument(Normal('[A'))))),Background('&'),Pipeline(Command(Argument(Normal('B]')))))"
"Line(Backgrounded(Pipeline(Command(Argument(Normal('echo'))Argument(Normal('[A')))))Pipeline(Command(Argument(Normal('B]')))))"
'A=*$B*'
"Line(Pipeline(Command(Affectation(VariableName('A'),Equal('='),Normal('*'),Variable('$B'),Normal('*')))))"
"Line(Pipeline(Command(Affectation(VariableName('A')Equal('=')Normal('*')VariableProtected('$B')Normal('*')))))"
'A=B=C'
"Line(Pipeline(Command(Affectation(VariableName('A'),Equal('='),Normal('B=C')))))"
"Line(Pipeline(Command(Affectation(VariableName('A')Equal('=')Normal('B=C')))))"
'A=A$B'
"Line(Pipeline(Command(Affectation(VariableName('A'),Equal('='),Normal('A'),Variable('$B')))))"
"Line(Pipeline(Command(Affectation(VariableName('A')Equal('=')Normal('A')VariableProtected('$B')))))"
'A="A$B"'
'Line(Pipeline(Command(Affectation(VariableName(\'A\'),Equal(\'=\'),Guillemet(\'"\'),Normal(\'A\'),Variable(\'$B\'),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Affectation(VariableName('A')Equal('=')Normal('A')VariableProtected('$B')))))"
'A=A"$B"'
'Line(Pipeline(Command(Affectation(VariableName(\'A\'),Equal(\'=\'),Normal(\'A\'),Guillemet(\'"\'),Variable(\'$B\'),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Affectation(VariableName('A')Equal('=')Normal('A')VariableProtected('$B')))))"
'A-B=5'
"Line(Pipeline(Command(Argument(Normal('A-B=5')))))"
"Line(Pipeline(Command(Argument(Normal('A-B=5')))))"
'for A-B in q ; do x ; done'
"Line(Pipeline(Command(ForLoop(For('for '),Unterminated('A-B'),In(' in '),ForValues(Argument(Normal('q'))),EndOfValues(' ; '),Body(Do('do '),Pipeline(Command(Argument(Normal('x')))),DotComa(' ; '),Done('done'))))))"
"Line(Pipeline(Command(ForLoop(Unterminated('A-B')ForValues(Argument(Normal('q')))Body(Pipeline(Command(Argument(Normal('x')))))))))"
'for A-B in'
"Line(Pipeline(Command(ForLoop(Unterminated('for '),Unterminated('A-B'),In(' in')))))"
"Line(Pipeline(Command(ForLoop(Unterminated('for ')Unterminated('A-B')))))"
'sleep 1m'
"Line(Pipeline(Command(Argument(Normal('sleep')),Separator(' '),Argument(Normal('1m')))))"
"Line(Pipeline(Command(Argument(Normal('sleep'))Argument(Normal('60')))))"
'N=$(a)done'
"Line(Pipeline(Command(Affectation(VariableName('N'),Equal('='),Replacement(GroupStart('$('),Line(Pipeline(Command(Argument(Normal('a'))))),GroupStop(')')),Normal('done')))))"
"Line(Pipeline(Command(Affectation(VariableName('N')Equal('=')ReplacementProtected(GroupStart Line(Pipeline(Command(Argument(Normal('a')))))GroupStop )Normal('done')))))"
'N=done'
"Line(Pipeline(Command(Affectation(VariableName('N'),Equal('='),Normal('done')))))"
"Line(Pipeline(Command(Affectation(VariableName('N')Equal('=')Normal('done')))))"
'A= done'
"Line(Pipeline(Command(Affectation(VariableName('A'),Equal('=')),Separator(' '),Argument(Normal('done')))))"
"Line(Pipeline(Command(Affectation(VariableName('A')Equal('='))Argument(Normal('done')))))"
'a\nb'
"Line(Pipeline(Command(Argument(Normal('a')))),NewLine('\n'),Pipeline(Command(Argument(Normal('b')))))"
"Line(Pipeline(Command(Argument(Normal('a'))))Pipeline(Command(Argument(Normal('b')))))"
'a ;\nb'
"Line(Pipeline(Command(Argument(Normal('a')))),DotComa(' ;'),NewLine('\n'),Pipeline(Command(Argument(Normal('b')))))"
"Line(Pipeline(Command(Argument(Normal('a'))))Pipeline(Command(Argument(Normal('b')))))"
'(a\nb)'
"Line(Pipeline(Group(GroupStart('('),Line(Pipeline(Command(Argument(Normal('a')))),NewLine('\n'),Pipeline(Command(Argument(Normal('b'))))),GroupStop(')'))))"
"Line(Pipeline(Group(GroupStart Line(Pipeline(Command(Argument(Normal('a'))))Pipeline(Command(Argument(Normal('b')))))GroupStop )))"
'A="a\nb"'
'Line(Pipeline(Command(Affectation(VariableName(\'A\'),Equal(\'=\'),Guillemet(\'"\'),Normal(\'a\nb\'),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Affectation(VariableName('A')Equal('=')Normal('a\nb')))))"
'A=a\nb'
"Line(Pipeline(Command(Affectation(VariableName('A'),Equal('='),Normal('a')))),NewLine('\n'),Pipeline(Command(Argument(Normal('b')))))"
"Line(Pipeline(Command(Affectation(VariableName('A')Equal('=')Normal('a'))))Pipeline(Command(Argument(Normal('b')))))"
'for a in *\ndo b ; done'
"Line(Pipeline(Command(ForLoop(For('for '),LoopVariable('a'),In(' in '),ForValues(Argument(Star('*'))),EndOfValues('\n'),Body(Do('do '),Pipeline(Command(Argument(Normal('b')))),DotComa(' ; '),Done('done'))))))"
"Line(Pipeline(Command(ForLoop(LoopVariable('a')ForValues(Argument(Star('*')))Body(Pipeline(Command(Argument(Normal('b')))))))))"
'for a in *\ndo b\ndone'
"Line(Pipeline(Command(ForLoop(For('for '),LoopVariable('a'),In(' in '),ForValues(Argument(Star('*'))),EndOfValues('\n'),Body(Do('do '),Pipeline(Command(Argument(Normal('b')))),NewLine('\n'),Done('done'))))))"
"Line(Pipeline(Command(ForLoop(LoopVariable('a')ForValues(Argument(Star('*')))Body(Pipeline(Command(Argument(Normal('b')))))))))"
'while a\ndo b\ndone'
"Line(Pipeline(Command(WhileLoop(While('while '),Command(Argument(Normal('a'))),EndOfValues('\n'),Body(Do('do '),Pipeline(Command(Argument(Normal('b')))),NewLine('\n'),Done('done'))))))"
"Line(Pipeline(Command(WhileLoop(Command(Argument(Normal('a')))Body(Pipeline(Command(Argument(Normal('b')))))))))"
'a\\\nb'
"Line(Pipeline(Command(Argument(Normal('a'),Backslash('\\\\'),Normal('\nb')))))"
"Line(Pipeline(Command(Argument(Normal('a\nb')))))"
'a&\nb'
"Line(Backgrounded(Pipeline(Command(Argument(Normal('a'))))),Background('&'),NewLine('\n'),Pipeline(Command(Argument(Normal('b')))))"
"Line(Backgrounded(Pipeline(Command(Argument(Normal('a')))))Pipeline(Command(Argument(Normal('b')))))"
'if a\nthen\nb\nfi'
"Line(Pipeline(Command(IfThenElse(If('if '),Command(Argument(Normal('a'))),EndOfValues('\n'),ThenBloc(Then('then\n'),Pipeline(Command(Argument(Normal('b')))),NewLine('\n')),Fi('fi')))))"
"Line(Pipeline(Command(IfThenElse(Command(Argument(Normal('a')))ThenBloc(Pipeline(Command(Argument(Normal('b')))))))))"
'if a\nthen\nb\nelse\nc\nfi'
"Line(Pipeline(Command(IfThenElse(If('if '),Command(Argument(Normal('a'))),EndOfValues('\n'),ThenBloc(Then('then\n'),Pipeline(Command(Argument(Normal('b')))),NewLine('\n')),ElseBloc(Else('else\n'),Pipeline(Command(Argument(Normal('c')))),NewLine('\n')),Fi('fi')))))"
"Line(Pipeline(Command(IfThenElse(Command(Argument(Normal('a')))ThenBloc(Pipeline(Command(Argument(Normal('b')))))ElseBloc(Pipeline(Command(Argument(Normal('c')))))))))"
'if\na\nthen\nb\nfi'
"Line(Pipeline(Command(IfThenElse(If('if\n'),Command(Argument(Normal('a'))),EndOfValues('\n'),ThenBloc(Then('then\n'),Pipeline(Command(Argument(Normal('b')))),NewLine('\n')),Fi('fi')))))"
"Line(Pipeline(Command(IfThenElse(Command(Argument(Normal('a')))ThenBloc(Pipeline(Command(Argument(Normal('b')))))))))"
'if\na\nthen\nb\nc\nfi'
"Line(Pipeline(Command(IfThenElse(If('if\n'),Command(Argument(Normal('a'))),EndOfValues('\n'),ThenBloc(Then('then\n'),Pipeline(Command(Argument(Normal('b')))),NewLine('\n'),Pipeline(Command(Argument(Normal('c')))),NewLine('\n')),Fi('fi')))))"
"Line(Pipeline(Command(IfThenElse(Command(Argument(Normal('a')))ThenBloc(Pipeline(Command(Argument(Normal('b'))))Pipeline(Command(Argument(Normal('c')))))))))"
'if\na\nthen\nb\nfi\nif\na\nthen\nb\nfi'
"Line(Pipeline(Command(IfThenElse(If('if\n'),Command(Argument(Normal('a'))),EndOfValues('\n'),ThenBloc(Then('then\n'),Pipeline(Command(Argument(Normal('b')))),NewLine('\n')),Fi('fi')))),NewLine('\n'),Pipeline(Command(IfThenElse(If('if\n'),Command(Argument(Normal('a'))),EndOfValues('\n'),ThenBloc(Then('then\n'),Pipeline(Command(Argument(Normal('b')))),NewLine('\n')),Fi('fi')))))"
"Line(Pipeline(Command(IfThenElse(Command(Argument(Normal('a')))ThenBloc(Pipeline(Command(Argument(Normal('b'))))))))Pipeline(Command(IfThenElse(Command(Argument(Normal('a')))ThenBloc(Pipeline(Command(Argument(Normal('b')))))))))"
'test a = b'
"Line(Pipeline(Command(Argument(Normal('test')),Separator(' '),ArgumentGroup(Argument(Normal('a')),Separator(' '),Argument(Normal('=')),Separator(' '),Argument(Normal('b'))))))"
"Line(Pipeline(Command(Argument(Normal('test'))ArgumentGroup(Argument(Normal('a'))Argument(Normal('='))Argument(Normal('b'))))))"
'[ -d a ]'
"Line(Pipeline(Command(Argument(Normal('[')),Separator(' '),ArgumentGroup(Argument(Normal('-d')),Separator(' '),Argument(Normal('a'))),Separator(' '),Argument(Normal(']')))))"
"Line(Pipeline(Command(Argument(Normal('['))ArgumentGroup(Argument(Normal('-d'))Argument(Normal('a')))Argument(Normal(']')))))"
'[ a = b -o c -eq d ]'
"Line(Pipeline(Command(Argument(Normal('[')),Separator(' '),ArgumentGroup(ArgumentGroup(Argument(Normal('a')),Separator(' '),Argument(Normal('=')),Separator(' '),Argument(Normal('b'))),Separator(' '),Argument(Normal('-o')),Separator(' '),ArgumentGroup(Argument(Normal('c')),Separator(' '),Argument(Normal('-eq')),Separator(' '),Argument(Normal('d'))),Separator(' ')),Argument(Normal(']')))))"
"Line(Pipeline(Command(Argument(Normal('['))ArgumentGroup(ArgumentGroup(Argument(Normal('a'))Argument(Normal('='))Argument(Normal('b')))Argument(Normal('-o'))ArgumentGroup(Argument(Normal('c'))Argument(Normal('-eq'))Argument(Normal('d'))))Argument(Normal(']')))))"
'grep "a*"'
'Line(Pipeline(Command(Argument(Normal(\'grep\')),Separator(\' \'),RegExpTree(Guillemet(\'"\'),RegExpMultiply(Normal(\'a\'),RegExpStar(\'*\')),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Argument(Normal('grep'))RegExpTree(RegExpMultiply(Normal('a')RegExpStar('*'))))))"
'grep "ab*"'
'Line(Pipeline(Command(Argument(Normal(\'grep\')),Separator(\' \'),RegExpTree(Guillemet(\'"\'),Normal(\'a\'),RegExpMultiply(Normal(\'b\'),RegExpStar(\'*\')),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Argument(Normal('grep'))RegExpTree(Normal('a')RegExpMultiply(Normal('b')RegExpStar('*'))))))"
'grep "*"'
'Line(Pipeline(Command(Argument(Normal(\'grep\')),Separator(\' \'),RegExpTree(Guillemet(\'"\'),Normal(\'*\'),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Argument(Normal('grep'))RegExpTree(Normal('*')))))"
'grep "a""*"'
'Line(Pipeline(Command(Argument(Normal(\'grep\')),Separator(\' \'),RegExpTree(Guillemet(\'"\'),RegExpMultiply(RegExpBloc(Normal(\'a\'),Guillemet(\'"\'),Guillemet(\'"\')),RegExpStar(\'*\')),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Argument(Normal('grep'))RegExpTree(RegExpMultiply(RegExpBloc(Normal('a'))RegExpStar('*'))))))"
'grep "ab""*"'
'Line(Pipeline(Command(Argument(Normal(\'grep\')),Separator(\' \'),RegExpTree(Guillemet(\'"\'),Normal(\'a\'),RegExpMultiply(RegExpBloc(Normal(\'b\'),Guillemet(\'"\'),Guillemet(\'"\')),RegExpStar(\'*\')),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Argument(Normal('grep'))RegExpTree(Normal('a')RegExpMultiply(RegExpBloc(Normal('b'))RegExpStar('*'))))))"
'grep "ab""*c"'
'Line(Pipeline(Command(Argument(Normal(\'grep\')),Separator(\' \'),RegExpTree(Guillemet(\'"\'),Normal(\'a\'),RegExpMultiply(RegExpBloc(Normal(\'b\'),Guillemet(\'"\'),Guillemet(\'"\')),RegExpStar(\'*\')),Normal(\'c\'),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Argument(Normal('grep'))RegExpTree(Normal('a')RegExpMultiply(RegExpBloc(Normal('b'))RegExpStar('*'))Normal('c')))))"
'grep "a*b*"'
'Line(Pipeline(Command(Argument(Normal(\'grep\')),Separator(\' \'),RegExpTree(Guillemet(\'"\'),RegExpMultiply(Normal(\'a\'),RegExpStar(\'*\')),RegExpMultiply(Normal(\'b\'),RegExpStar(\'*\')),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Argument(Normal('grep'))RegExpTree(RegExpMultiply(Normal('a')RegExpStar('*'))RegExpMultiply(Normal('b')RegExpStar('*'))))))"
'grep "a**"'
'Line(Pipeline(Command(Argument(Normal(\'grep\')),Separator(\' \'),RegExpTree(Guillemet(\'"\'),RegExpMultiply(RegExpMultiply(Normal(\'a\'),RegExpStar(\'*\')),RegExpStar(\'*\')),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Argument(Normal('grep'))RegExpTree(RegExpMultiply(RegExpMultiply(Normal('a')RegExpStar('*'))RegExpStar('*'))))))"
'grep "a*'
'Line(Pipeline(Command(Argument(Normal(\'grep\')),Separator(\' \'),RegExpTree(Unterminated(\'"\'),RegExpMultiply(Normal(\'a\'),RegExpStar(\'*\'))))))'
'Line(Pipeline(Command(Argument(Normal(\'grep\'))RegExpTree(Unterminated(\'"\')RegExpMultiply(Normal(\'a\')RegExpStar(\'*\'))))))'
'grep -F a\\*'
"Line(Pipeline(Command(Argument(Normal('grep')),Separator(' '),Argument(Normal('-F')),Separator(' '),Argument(Normal('a'),Backslash('\\\\'),Normal('*')))))"
"Line(Pipeline(Command(Argument(Normal('grep'))Argument(Normal('-F'))Argument(Normal('a*')))))"
"grep '[a-z]'"
"Line(Pipeline(Command(Argument(Normal('grep')),Separator(' '),RegExpTree(Quote('\\''),RegExpList(RegExpBracket('['),RegExpRange(RegExpListNormal('a'),RegExpListNormal('-'),RegExpListNormal('z')),RegExpBracket(']')),Quote('\\'')))))"
"Line(Pipeline(Command(Argument(Normal('grep'))RegExpTree(RegExpList(RegExpBracket('[')RegExpBracket(']')RegExpRange(RegExpListNormal('a')RegExpListNormal('-')RegExpListNormal('z')))))))"
"grep '[xa-zy]'"
"Line(Pipeline(Command(Argument(Normal('grep')),Separator(' '),RegExpTree(Quote('\\''),RegExpList(RegExpBracket('['),RegExpListNormal('x'),RegExpRange(RegExpListNormal('a'),RegExpListNormal('-'),RegExpListNormal('z')),RegExpListNormal('y'),RegExpBracket(']')),Quote('\\'')))))"
"Line(Pipeline(Command(Argument(Normal('grep'))RegExpTree(RegExpList(RegExpBracket('[')RegExpBracket(']')RegExpListNormal('x')RegExpListNormal('y')RegExpRange(RegExpListNormal('a')RegExpListNormal('-')RegExpListNormal('z')))))))"
"grep '[^x]'"
"Line(Pipeline(Command(Argument(Normal('grep')),Separator(' '),RegExpTree(Quote('\\''),RegExpList(RegExpBracket('['),RegExpNegate('^'),RegExpListNormal('x'),RegExpBracket(']')),Quote('\\'')))))"
"Line(Pipeline(Command(Argument(Normal('grep'))RegExpTree(RegExpList(RegExpBracket('[')RegExpBracket(']')RegExpListNormal('x')RegExpNegate('^'))))))"
"grep '[^x-'"
"Line(Pipeline(Command(Argument(Normal('grep')),Separator(' '),RegExpTree(Quote('\\''),RegExpList(Unterminated('['),RegExpNegate('^'),RegExpListNormal('x'),RegExpListNormal('-'),Quote('\\''))))))"
"Line(Pipeline(Command(Argument(Normal('grep'))RegExpTree(RegExpList(RegExpListNormal('-')RegExpListNormal('x')RegExpNegate('^')Unterminated('['))))))"
'grep "[a-z]*"'
'Line(Pipeline(Command(Argument(Normal(\'grep\')),Separator(\' \'),RegExpTree(Guillemet(\'"\'),RegExpMultiply(RegExpList(RegExpBracket(\'[\'),RegExpRange(RegExpListNormal(\'a\'),RegExpListNormal(\'-\'),RegExpListNormal(\'z\')),RegExpBracket(\']\')),RegExpStar(\'*\')),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Argument(Normal('grep'))RegExpTree(RegExpMultiply(RegExpList(RegExpBracket('[')RegExpBracket(']')RegExpRange(RegExpListNormal('a')RegExpListNormal('-')RegExpListNormal('z')))RegExpStar('*'))))))"
'grep "[a-]*"'
'Line(Pipeline(Command(Argument(Normal(\'grep\')),Separator(\' \'),RegExpTree(Guillemet(\'"\'),RegExpMultiply(RegExpList(RegExpBracket(\'[\'),RegExpListNormal(\'a\'),RegExpListNormal(\'-\'),RegExpBracket(\']\')),RegExpStar(\'*\')),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Argument(Normal('grep'))RegExpTree(RegExpMultiply(RegExpList(RegExpBracket('[')RegExpBracket(']')RegExpListNormal('-')RegExpListNormal('a'))RegExpStar('*'))))))"
'grep "[]]"'
'Line(Pipeline(Command(Argument(Normal(\'grep\')),Separator(\' \'),RegExpTree(Guillemet(\'"\'),RegExpList(RegExpBracket(\'[\'),Unterminated(\']\'),RegExpBracket(\']\')),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Argument(Normal('grep'))RegExpTree(RegExpList(RegExpBracket('[')RegExpBracket(']')Unterminated(']'))))))"
"grep '[''a"
"Line(Pipeline(Command(Argument(Normal('grep')),Separator(' '),RegExpTree(Quote('\\''),RegExpList(Unterminated('['),Quote('\\''),Unterminated('\\''),RegExpListNormal('a'))))))"
"Line(Pipeline(Command(Argument(Normal('grep'))RegExpTree(RegExpList(RegExpListNormal('a')Unterminated('[')Unterminated('\\''))))))"
"a 'b''c"
"Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Argument(Quote('\\''),Normal('b'),Quote('\\''),Unterminated('\\''),Normal('c')))))"
"Line(Pipeline(Command(Argument(Normal('a'))Argument(Normal('b')Unterminated('\\'')Normal('c')))))"
'grep \'[\'\'a\'"-z"\\]'
'Line(Pipeline(Command(Argument(Normal(\'grep\')),Separator(\' \'),RegExpTree(Quote(\'\\\'\'),RegExpList(RegExpBracket(\'[\'),Quote(\'\\\'\'),Quote(\'\\\'\'),RegExpRange(RegExpListNormal(\'a\'),Quote(\'\\\'\'),Guillemet(\'"\'),RegExpListNormal(\'-\'),RegExpListNormal(\'z\')),Guillemet(\'"\'),Backslash(\'\\\\\'),RegExpBracket(\']\'))))))'
"Line(Pipeline(Command(Argument(Normal('grep'))RegExpTree(RegExpList(RegExpBracket('[')RegExpBracket(']')RegExpRange(RegExpListNormal('a')RegExpListNormal('-')RegExpListNormal('z')))))))"
'grep "[""""^a]"'
'Line(Pipeline(Command(Argument(Normal(\'grep\')),Separator(\' \'),RegExpTree(Guillemet(\'"\'),RegExpList(RegExpBracket(\'[\'),Guillemet(\'"\'),Guillemet(\'"\'),Guillemet(\'"\'),Guillemet(\'"\'),RegExpNegate(\'^\'),RegExpListNormal(\'a\'),RegExpBracket(\']\')),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Argument(Normal('grep'))RegExpTree(RegExpList(RegExpBracket('[')RegExpBracket(']')RegExpListNormal('a')RegExpNegate('^'))))))"
'grep -E "(gh)*"'
'Line(Pipeline(Command(Argument(Normal(\'grep\')),Separator(\' \'),Argument(Normal(\'-E\')),Separator(\' \'),RegExpTree(Guillemet(\'"\'),RegExpMultiply(RegExpGroup(RegExpParenthesis(\'(\'),Normal(\'gh\'),RegExpParenthesis(\')\')),RegExpStar(\'*\')),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Argument(Normal('grep'))Argument(Normal('-E'))RegExpTree(RegExpMultiply(RegExpGroup(RegExpParenthesis('(')Normal('gh')RegExpParenthesis(')'))RegExpStar('*'))))))"
'grep -E "(a"'
'Line(Pipeline(Command(Argument(Normal(\'grep\')),Separator(\' \'),Argument(Normal(\'-E\')),Separator(\' \'),RegExpTree(Guillemet(\'"\'),Unterminated(\'(\'),Normal(\'a\'),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Argument(Normal('grep'))Argument(Normal('-E'))RegExpTree(Unterminated('(')Normal('a')))))"
"grep -E 'a|b"
"Line(Pipeline(Command(Argument(Normal('grep')),Separator(' '),Argument(Normal('-E')),Separator(' '),RegExpTree(Unterminated('\\''),Normal('a'),RegExpOr('|'),Normal('b')))))"
"Line(Pipeline(Command(Argument(Normal('grep'))Argument(Normal('-E'))RegExpTree(Unterminated('\\'')Normal('a')RegExpOr('|')Normal('b')))))"
"grep -E 'a|b|c"
"Line(Pipeline(Command(Argument(Normal('grep')),Separator(' '),Argument(Normal('-E')),Separator(' '),RegExpTree(Unterminated('\\''),Normal('a'),RegExpOr('|'),Normal('b'),RegExpOr('|'),Normal('c')))))"
"Line(Pipeline(Command(Argument(Normal('grep'))Argument(Normal('-E'))RegExpTree(Unterminated('\\'')Normal('a')RegExpOr('|')Normal('b')RegExpOr('|')Normal('c')))))"
"grep -E '(a|b)|(c|*d|)*'"
"Line(Pipeline(Command(Argument(Normal('grep')),Separator(' '),Argument(Normal('-E')),Separator(' '),RegExpTree(Quote('\\''),RegExpGroup(RegExpParenthesis('('),Normal('a'),RegExpOr('|'),Normal('b'),RegExpParenthesis(')')),RegExpOr('|'),RegExpMultiply(RegExpGroup(RegExpParenthesis('('),Normal('c'),RegExpOr('|'),Normal('*d'),RegExpOr('|'),RegExpParenthesis(')')),RegExpStar('*')),Quote('\\'')))))"
"Line(Pipeline(Command(Argument(Normal('grep'))Argument(Normal('-E'))RegExpTree(RegExpGroup(RegExpParenthesis('(')Normal('a')RegExpOr('|')Normal('b')RegExpParenthesis(')'))RegExpOr('|')RegExpMultiply(RegExpGroup(RegExpParenthesis('(')Normal('c')RegExpOr('|')Normal('*d')RegExpOr('|')RegExpParenthesis(')'))RegExpStar('*'))))))"
"grep -E '(a|(b|B))'"
"Line(Pipeline(Command(Argument(Normal('grep')),Separator(' '),Argument(Normal('-E')),Separator(' '),RegExpTree(Quote('\\''),RegExpGroup(RegExpParenthesis('('),Normal('a'),RegExpOr('|'),RegExpGroup(RegExpParenthesis('('),Normal('b'),RegExpOr('|'),Normal('B'),RegExpParenthesis(')')),RegExpParenthesis(')')),Quote('\\'')))))"
"Line(Pipeline(Command(Argument(Normal('grep'))Argument(Normal('-E'))RegExpTree(RegExpGroup(RegExpParenthesis('(')Normal('a')RegExpOr('|')RegExpGroup(RegExpParenthesis('(')Normal('b')RegExpOr('|')Normal('B')RegExpParenthesis(')'))RegExpParenthesis(')'))))))"
'grep -E "(|"")"'
'Line(Pipeline(Command(Argument(Normal(\'grep\')),Separator(\' \'),Argument(Normal(\'-E\')),Separator(\' \'),RegExpTree(Guillemet(\'"\'),RegExpGroup(RegExpParenthesis(\'(\'),RegExpOr(\'|\'),Guillemet(\'"\'),Guillemet(\'"\'),RegExpParenthesis(\')\')),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Argument(Normal('grep'))Argument(Normal('-E'))RegExpTree(RegExpGroup(RegExpParenthesis('(')RegExpOr('|')RegExpParenthesis(')'))))))"
'grep -E ")"'
'Line(Pipeline(Command(Argument(Normal(\'grep\')),Separator(\' \'),Argument(Normal(\'-E\')),Separator(\' \'),RegExpTree(Guillemet(\'"\'),Unterminated(\')\'),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Argument(Normal('grep'))Argument(Normal('-E'))RegExpTree(Unterminated(')')))))"
'grep -E "^a$"'
'Line(Pipeline(Command(Argument(Normal(\'grep\')),Separator(\' \'),Argument(Normal(\'-E\')),Separator(\' \'),RegExpTree(Guillemet(\'"\'),RegExpBegin(\'^\'),Normal(\'a\'),RegExpEnd(\'$\'),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Argument(Normal('grep'))Argument(Normal('-E'))RegExpTree(RegExpBegin('^')Normal('a')RegExpEnd('$')))))"
"grep -E '\\^\\$'"
"Line(Pipeline(Command(Argument(Normal('grep')),Separator(' '),Argument(Normal('-E')),Separator(' '),RegExpTree(Quote('\\''),RegExpBackslash('\\\\'),Normal('^'),RegExpBackslash('\\\\'),Normal('$'),Quote('\\'')))))"
"Line(Pipeline(Command(Argument(Normal('grep'))Argument(Normal('-E'))RegExpTree(Normal('^$')))))"
"grep -E '(^*|$*)'"
"Line(Pipeline(Command(Argument(Normal('grep')),Separator(' '),Argument(Normal('-E')),Separator(' '),RegExpTree(Quote('\\''),RegExpGroup(RegExpParenthesis('('),RegExpBegin('^'),Normal('*'),RegExpOr('|'),RegExpEnd('$'),RegExpGarbage('*'),RegExpParenthesis(')')),Quote('\\'')))))"
"Line(Pipeline(Command(Argument(Normal('grep'))Argument(Normal('-E'))RegExpTree(RegExpGroup(RegExpParenthesis('(')RegExpBegin('^')Normal('*')RegExpOr('|')RegExpEnd('$')RegExpGarbage('*')RegExpParenthesis(')'))))))"
"grep '\\1'"
"Line(Pipeline(Command(Argument(Normal('grep')),Separator(' '),RegExpTree(Quote('\\''),RegExpBackslash('\\\\'),RegExpBadEscape('1'),Quote('\\'')))))"
"Line(Pipeline(Command(Argument(Normal('grep'))RegExpTree(RegExpBadEscape('1')))))"
"grep -E '(a)\\1'"
"Line(Pipeline(Command(Argument(Normal('grep')),Separator(' '),Argument(Normal('-E')),Separator(' '),RegExpTree(Quote('\\''),RegExpGroup(RegExpParenthesis('('),Normal('a'),RegExpParenthesis(')')),RegExpBackslashSpecial(RegExpBackslash('\\\\'),RegExpNoHelp('1')),Quote('\\'')))))"
"Line(Pipeline(Command(Argument(Normal('grep'))Argument(Normal('-E'))RegExpTree(RegExpGroup(RegExpParenthesis('(')Normal('a')RegExpParenthesis(')'))RegExpBackslashSpecial(RegExpNoHelp('1'))))))"
"grep -E '(a)\\'1'"
"Line(Pipeline(Command(Argument(Normal('grep')),Separator(' '),Argument(Normal('-E')),Separator(' '),RegExpTree(Quote('\\''),RegExpGroup(RegExpParenthesis('('),Normal('a'),RegExpParenthesis(')')),RegExpBackslashSpecial(RegExpBackslash('\\\\'),Quote('\\''),RegExpNoHelp('1')),Unterminated('\\'')))))"
"Line(Pipeline(Command(Argument(Normal('grep'))Argument(Normal('-E'))RegExpTree(RegExpGroup(RegExpParenthesis('(')Normal('a')RegExpParenthesis(')'))RegExpBackslashSpecial(RegExpNoHelp('1'))Unterminated('\\'')))))"
"grep 'a^'"
"Line(Pipeline(Command(Argument(Normal('grep')),Separator(' '),RegExpTree(Quote('\\''),Normal('a^'),Quote('\\'')))))"
"Line(Pipeline(Command(Argument(Normal('grep'))RegExpTree(Normal('a^')))))"
"grep 'a$b'"
"Line(Pipeline(Command(Argument(Normal('grep')),Separator(' '),RegExpTree(Quote('\\''),Normal('a'),RegExpEnd('$'),RegExpGarbage('b'),Quote('\\'')))))"
"Line(Pipeline(Command(Argument(Normal('grep'))RegExpTree(Normal('a')RegExpEnd('$')RegExpGarbage('b')))))"
'grep -E "a{1,6}b"'
'Line(Pipeline(Command(Argument(Normal(\'grep\')),Separator(\' \'),Argument(Normal(\'-E\')),Separator(\' \'),RegExpTree(Guillemet(\'"\'),RegExpMultiply(Normal(\'a\'),RegExpBloc(RegExpNoHelp(\'{\'),RegExpNoHelp(\'1\'),RegExpNoHelp(\',\'),RegExpNoHelp(\'6\'),RegExpNoHelp(\'}\'))),Normal(\'b\'),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Argument(Normal('grep'))Argument(Normal('-E'))RegExpTree(RegExpMultiply(Normal('a')RegExpBloc(RegExpNoHelp('{')RegExpNoHelp('1')RegExpNoHelp(',')RegExpNoHelp('6')RegExpNoHelp('}')))Normal('b')))))"
'grep -E "a{1;6}b"'
'Line(Pipeline(Command(Argument(Normal(\'grep\')),Separator(\' \'),Argument(Normal(\'-E\')),Separator(\' \'),RegExpTree(Guillemet(\'"\'),RegExpMultiply(Normal(\'a\'),RegExpBloc(RegExpNoHelp(\'{\'),RegExpNoHelp(\'1\'),RegExpBadRange(\';\'),RegExpNoHelp(\'6\'),RegExpNoHelp(\'}\'))),Normal(\'b\'),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Argument(Normal('grep'))Argument(Normal('-E'))RegExpTree(RegExpMultiply(Normal('a')RegExpBloc(RegExpNoHelp('{')RegExpNoHelp('1')RegExpBadRange(';')RegExpNoHelp('6')RegExpNoHelp('}')))Normal('b')))))"
'grep -E "a{6}b"'
'Line(Pipeline(Command(Argument(Normal(\'grep\')),Separator(\' \'),Argument(Normal(\'-E\')),Separator(\' \'),RegExpTree(Guillemet(\'"\'),RegExpMultiply(Normal(\'a\'),RegExpBloc(RegExpNoHelp(\'{\'),RegExpNoHelp(\'6\'),RegExpNoHelp(\'}\'))),Normal(\'b\'),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Argument(Normal('grep'))Argument(Normal('-E'))RegExpTree(RegExpMultiply(Normal('a')RegExpBloc(RegExpNoHelp('{')RegExpNoHelp('6')RegExpNoHelp('}')))Normal('b')))))"
'grep -E "a{""6""}""b"'
'Line(Pipeline(Command(Argument(Normal(\'grep\')),Separator(\' \'),Argument(Normal(\'-E\')),Separator(\' \'),RegExpTree(Guillemet(\'"\'),RegExpMultiply(Normal(\'a\'),RegExpBloc(RegExpNoHelp(\'{\'),Guillemet(\'"\'),Guillemet(\'"\'),RegExpNoHelp(\'6\'),Guillemet(\'"\'),Guillemet(\'"\'),RegExpNoHelp(\'}\'))),Guillemet(\'"\'),Guillemet(\'"\'),Normal(\'b\'),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Argument(Normal('grep'))Argument(Normal('-E'))RegExpTree(RegExpMultiply(Normal('a')RegExpBloc(RegExpNoHelp('{')RegExpNoHelp('6')RegExpNoHelp('}')))Normal('b')))))"
'echo $(grep ^a)'
"Line(Pipeline(Command(Argument(Normal('echo')),Separator(' '),Argument(Replacement(GroupStart('$('),Line(Pipeline(Command(Argument(Normal('grep')),Separator(' '),RegExpTree(RegExpBegin('^'),Normal('a'))))),GroupStop(')'))))))"
"Line(Pipeline(Command(Argument(Normal('echo'))Argument(Replacement(GroupStart Line(Pipeline(Command(Argument(Normal('grep'))RegExpTree(RegExpBegin('^')Normal('a')))))GroupStop )))))"
'grep -E "ab?"'
'Line(Pipeline(Command(Argument(Normal(\'grep\')),Separator(\' \'),Argument(Normal(\'-E\')),Separator(\' \'),RegExpTree(Guillemet(\'"\'),Normal(\'a\'),RegExpMultiply(Normal(\'b\'),RegExpStar(\'?\')),Guillemet(\'"\')))))'
"Line(Pipeline(Command(Argument(Normal('grep'))Argument(Normal('-E'))RegExpTree(Normal('a')RegExpMultiply(Normal('b')RegExpStar('?'))))))"
"sed 's/a+*/&\\&\\/\\1/g'"
"Line(Pipeline(Command(Argument(Normal('sed')),Separator(' '),SedReplacement(Quote('\\''),SedAction('s'),SedSeparator1('/'),RegExpTree(Normal('a'),RegExpMultiply(Normal('+'),RegExpStar('*'))),SedSeparator2('/'),SedReplacementText(SedAmpersand('&'),SedBackslash('\\\\'),Normal('&'),SedBackslash('\\\\'),Normal('/'),SedBackslash('\\\\'),RegExpBadEscape('1')),SedSeparator3('/'),SedOption('g'),Quote('\\'')))))"
"Line(Pipeline(Command(Argument(Normal('sed'))SedReplacement(SedAction('s')SedSeparator1('/')RegExpTree(Normal('a')RegExpMultiply(Normal('+')RegExpStar('*')))SedSeparator2('/')SedReplacementText(SedAmpersand('&')SedBackslash('\\\\')Normal('&')SedBackslash('\\\\')Normal('/')SedBackslash('\\\\')RegExpBadEscape('1'))SedSeparator3('/')SedOption('g')))))"
"sed 'sd"
"Line(Pipeline(Command(Argument(Normal('sed')),Separator(' '),SedReplacement(Unterminated('\\''),SedAction('s'),Unterminated('d'),SedReplacementText()))))"
"Line(Pipeline(Command(Argument(Normal('sed'))SedReplacement(Unterminated('\\'')SedAction('s')Unterminated('d')SedReplacementText()))))"
"sed 's\\"
"Line(Pipeline(Command(Argument(Normal('sed')),Separator(' '),SedReplacement(Unterminated('\\''),SedAction('s'),Unterminated('\\\\'),SedReplacementText()))))"
"Line(Pipeline(Command(Argument(Normal('sed'))SedReplacement(Unterminated('\\'')SedAction('s')Unterminated('\\\\')SedReplacementText()))))"
"sed 's/\\"
"Line(Pipeline(Command(Argument(Normal('sed')),Separator(' '),SedReplacement(Unterminated('\\''),SedAction('s'),SedSeparator1('/'),RegExpTree(Unterminated('\\\\')),SedReplacementText()))))"
"Line(Pipeline(Command(Argument(Normal('sed'))SedReplacement(Unterminated('\\'')SedAction('s')SedSeparator1('/')RegExpTree(Unterminated('\\\\'))SedReplacementText()))))"
"sed 's/a/\\"
"Line(Pipeline(Command(Argument(Normal('sed')),Separator(' '),SedReplacement(Unterminated('\\''),SedAction('s'),SedSeparator1('/'),RegExpTree(Normal('a'),Unterminated('\\\\')),SedSeparator2('/'),SedReplacementText()))))"
"Line(Pipeline(Command(Argument(Normal('sed'))SedReplacement(Unterminated('\\'')SedAction('s')SedSeparator1('/')RegExpTree(Normal('a')Unterminated('\\\\'))SedSeparator2('/')SedReplacementText()))))"
"sed 's/a//\\"
"Line(Pipeline(Command(Argument(Normal('sed')),Separator(' '),SedReplacement(Unterminated('\\''),SedAction('s'),SedSeparator1('/'),RegExpTree(Normal('a')),SedSeparator2('/'),SedReplacementText(),SedSeparator3('/'),Unterminated('\\\\')))))"
"Line(Pipeline(Command(Argument(Normal('sed'))SedReplacement(Unterminated('\\'')SedAction('s')SedSeparator1('/')RegExpTree(Normal('a'))SedSeparator2('/')SedReplacementText()SedSeparator3('/')Unterminated('\\\\')))))"
"sed 's/a//' b"
"Line(Pipeline(Command(Argument(Normal('sed')),Separator(' '),SedReplacement(Quote('\\''),SedAction('s'),SedSeparator1('/'),RegExpTree(Normal('a')),SedSeparator2('/'),SedReplacementText(),SedSeparator3('/'),Quote('\\'')),Separator(' '),Argument(Normal('b')))))"
"Line(Pipeline(Command(Argument(Normal('sed'))SedReplacement(SedAction('s')SedSeparator1('/')RegExpTree(Normal('a'))SedSeparator2('/')SedReplacementText()SedSeparator3('/'))Argument(Normal('b')))))"
"sed -e 's/a//' -e 's/a//' b"
"Line(Pipeline(Command(Argument(Normal('sed')),Separator(' '),Argument(Normal('-e')),Separator(' '),SedReplacement(Quote('\\''),SedAction('s'),SedSeparator1('/'),RegExpTree(Normal('a')),SedSeparator2('/'),SedReplacementText(),SedSeparator3('/'),Quote('\\'')),Separator(' '),Argument(Normal('-e')),Separator(' '),SedReplacement(Quote('\\''),SedAction('s'),SedSeparator1('/'),RegExpTree(Normal('a')),SedSeparator2('/'),SedReplacementText(),SedSeparator3('/'),Quote('\\'')),Separator(' '),Argument(Normal('b')))))"
"Line(Pipeline(Command(Argument(Normal('sed'))Argument(Normal('-e'))SedReplacement(SedAction('s')SedSeparator1('/')RegExpTree(Normal('a'))SedSeparator2('/')SedReplacementText()SedSeparator3('/'))Argument(Normal('-e'))SedReplacement(SedAction('s')SedSeparator1('/')RegExpTree(Normal('a'))SedSeparator2('/')SedReplacementText()SedSeparator3('/'))Argument(Normal('b')))))"
"sed -r 's/(a)b/\\1\\2/'"
"Line(Pipeline(Command(Argument(Normal('sed')),Separator(' '),Argument(Normal('-r')),Separator(' '),SedReplacement(Quote('\\''),SedAction('s'),SedSeparator1('/'),RegExpTree(RegExpGroup(RegExpParenthesis('('),Normal('a'),RegExpParenthesis(')')),Normal('b')),SedSeparator2('/'),SedReplacementText(SedBackslashSpecial('\\\\1'),SedBackslashSpecial('\\\\2')),SedSeparator3('/'),Quote('\\'')))))"
"Line(Pipeline(Command(Argument(Normal('sed'))Argument(Normal('-r'))SedReplacement(SedAction('s')SedSeparator1('/')RegExpTree(RegExpGroup(RegExpParenthesis('(')Normal('a')RegExpParenthesis(')'))Normal('b'))SedSeparator2('/')SedReplacementText(SedBackslashSpecial('\\\\1')SedBackslashSpecial('\\\\2'))SedSeparator3('/')))))"
'sed s/a/b/g'
"Line(Pipeline(Command(Argument(Normal('sed')),Separator(' '),SedReplacement(SedAction('s'),SedSeparator1('/'),RegExpTree(Normal('a')),SedSeparator2('/'),SedReplacementText(Normal('b')),SedSeparator3('/'),SedOption('g')))))"
"Line(Pipeline(Command(Argument(Normal('sed'))SedReplacement(SedAction('s')SedSeparator1('/')RegExpTree(Normal('a'))SedSeparator2('/')SedReplacementText(Normal('b'))SedSeparator3('/')SedOption('g')))))"
