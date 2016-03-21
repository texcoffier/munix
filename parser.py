#!/usr/bin/python3


"""
Parser shell minimal


A FAIRE :
   * ||
   * &&
   * &
   * ()
   * for
   * if
   * while
"""
import os
import re

class Text:
    def __init__(self, text):
        self.text = text
        self.i = 0

    def more_to_do(self):
        return self.i != len(self.text)

    def get(self):
        if self.more_to_do():
            self.i += 1
            return self.text[self.i-1]

    def unget(self):
        self.i -= 1

    def __iter__(self):
        while self.i < len(self.text):
            self.i += 1
            yield self.text[self.i-1]

    def quote(self):
        word = ''
        for char in self:
            if char == "'":
                return word
            word += char
        raise ValueError("Manque : '")

    def guillemet(self):
        word = ''
        for char in self:
            if char == '$':
                word += self.content()
            elif char == '"':
                return word
            elif char == "\\":
                word += self.get()
            else:
                word += char
        raise ValueError('Manque : "')

    def content(self):
        varname = ''
        for char in self:
            if char.lower() in "abcdefghijklmnopqrstuvwxyz" or char == '_':
                varname += char
            else:
                self.unget()
                break
        return os.getenv(varname,'')

    def comment(self):
        the_comment = ''
        for char in self:
            if char == '\n':
                break
            the_comment += char
        return 'COMMENT(' + the_comment + ')'

    def patternise(self, word):
        return re.sub(r"([\[\?\*])", r"PATTERN(\1)", word)

    def word(self, firstword):
        while self.more_to_do() and self.text[self.i] in ' \t':
            self.i += 1
        if not self.more_to_do():
            return ''
        first = self.text[self.i]
        if first == '#':
            self.get()
            return self.comment()
        elif first in ';|\n':
            return '\n'
        elif first in '<>':
            self.get()
        elif first.isdigit() and self.i+1 < len(self.text) and self.text[self.i+1] in '<>':
            self.get()
            first += self.get()
        word = ""
        guillemet = False
        for char in self:
            if char == "'":
                word += self.quote()
            elif char == '"':
                word += self.guillemet()
                guillemet = True
            elif char == "\\":
                word += self.get()
            elif firstword and char == "=":
                word += "AFFECTATION()"
            elif char in "[?*":
                word += self.patternise(char)
            elif char == "$":
                content = self.content()
                content = re.sub("([^[ \t*?])", r"\\\1", content)
                self.text = self.text[:self.i] + content + self.text[self.i:]
            elif char in " \t\n;<>|":
                self.unget()
                break
            elif char == '&' and not ( first.endswith('>') or first.endswith('<')):
                self.unget()
                break
            else:
                word += char
        if word or guillemet:
            if first.endswith('>'):
                if len(first) == 1:
                    fildes = '1'
                else:
                    fildes = first[0]
                return 'OUT(' + fildes + ',' + word + ')'
            if first.endswith('<'):
                if len(first) == 1:
                    fildes = '0'
                else:
                    fildes = first[0]
                return 'IN(' + fildes + ',' + word + ')'
            return 'MOT(' + word +')'
        return ''

    def __str__(self):
        return self.text + '\n' + '*' * self.i + '^'
        
def parse_command(t):
    s = ''
    firstword = True
    while t.more_to_do():
        w = t.word(firstword)
        if w == '\n':
            break
        if 'AFFECTATION()' not in w:
            firstword = False
        s += w
    return 'COMMAND(' + s + ')'

def parse_pipe(t):
    s = ''
    while t.more_to_do():
        s += parse_command(t)
        w = t.get()
        if w == ';':
            break
        if w == '|':
            w = t.get()
            t.unget()
            if w == '|':
                t.unget()
                break
        if w == '&':
            w = t.get()
            if w == '&':
                t.unget()
                t.unget()
                break
            else:
                t.unget()
                s += '&'
                break
    return 'PIPELINE(' + s + ')'

def parse_or_and(t):
    if len(t.text) - t.i > 2:
        w = t.get()
        u = t.get()
        if w == '|' and u == '|':
           return '||' + parse_pipe(t)
        if w == '&' and u == '&':
           return '&&' + parse_pipe(t)

        t.unget()
        t.unget()
    return parse_pipe(t)

def parse(t):
    s = ''
    while t.more_to_do():
        s += parse_or_and(t)
    return s

if __name__ == '__main__':
    os.environ["A"] = "a  b"
    os.environ["B"] = "$A"
    os.environ["C"] = " a  b "
    os.environ["D"] = "* "
    os.environ["E"] = ""
    os.environ["F"] = ";"
    for a, b in (
        (r'a'        , r'PIPELINE(COMMAND(MOT(a)))'),
        (r'a b'      , r'PIPELINE(COMMAND(MOT(a)MOT(b)))'),
        (r'a  b'     , r'PIPELINE(COMMAND(MOT(a)MOT(b)))'),
        (r' a b'     , r'PIPELINE(COMMAND(MOT(a)MOT(b)))'),
        (r"a#b"      , r'PIPELINE(COMMAND(MOT(a#b)))'),
        (r'a\ b'     , r'PIPELINE(COMMAND(MOT(a b)))'),
        (r'a""b'     , r'PIPELINE(COMMAND(MOT(ab)))'),
        (r'a "" b'   , r'PIPELINE(COMMAND(MOT(a)MOT()MOT(b)))'),
        (r'a" "b'    , r'PIPELINE(COMMAND(MOT(a b)))'),
        (r'"a b"'    , r'PIPELINE(COMMAND(MOT(a b)))'),
        (r"'a b'"    , r'PIPELINE(COMMAND(MOT(a b)))'),
        (r"'$A'"     , r'PIPELINE(COMMAND(MOT($A)))'),
        (r"a' 'b"    , r'PIPELINE(COMMAND(MOT(a b)))'),
        (r"a'\'b"    , r'PIPELINE(COMMAND(MOT(a\b)))'),
        (r"\\\"\'"   ,  'PIPELINE(COMMAND(MOT(\\"\')))'),
        (r"$A"       , r'PIPELINE(COMMAND(MOT(a)MOT(b)))'),
        (r'"$A"'     , r'PIPELINE(COMMAND(MOT(a  b)))'),
        (r'"$A"$A'   , r'PIPELINE(COMMAND(MOT(a  ba)MOT(b)))'),
        (r'a #c d'   , r'PIPELINE(COMMAND(MOT(a)COMMENT(c d)))'),
        (r'"\$A"'    , r'PIPELINE(COMMAND(MOT($A)))'),
        (r'$B'       , r'PIPELINE(COMMAND(MOT($A)))'),
        (r'.$A.'     , r'PIPELINE(COMMAND(MOT(.a)MOT(b.)))'),
        (r'.$C.'     , r'PIPELINE(COMMAND(MOT(.)MOT(a)MOT(b)MOT(.)))'),
        (r'.$C'      , r'PIPELINE(COMMAND(MOT(.)MOT(a)MOT(b)))'),
        (r'."$C".'   , r'PIPELINE(COMMAND(MOT(. a  b .)))'),
        (r'a*?[b'    , r'PIPELINE(COMMAND(MOT(aPATTERN(*)PATTERN(?)PATTERN([)b)))'),
        (r'a * b'    , r'PIPELINE(COMMAND(MOT(a)MOT(PATTERN(*))MOT(b)))'),
        (r'a$D'      , r'PIPELINE(COMMAND(MOT(aPATTERN(*))))'),
        (r'a$E.'     , r'PIPELINE(COMMAND(MOT(a.)))'),
        (r'a $E a'   , r'PIPELINE(COMMAND(MOT(a)MOT(a)))'),
        (r'a "$E" a' , r'PIPELINE(COMMAND(MOT(a)MOT()MOT(a)))'),
        (r'$D'       , r'PIPELINE(COMMAND(MOT(PATTERN(*))))'),
        (r'a$D.'     , r'PIPELINE(COMMAND(MOT(aPATTERN(*))MOT(.)))'),
        (r'a>b<c'    , r'PIPELINE(COMMAND(MOT(a)OUT(1,b)IN(0,c)))'),
        (r'a2>b1<c'  , r'PIPELINE(COMMAND(MOT(a2)OUT(1,b1)IN(0,c)))'),
        (r'a 2>b 3<c', r'PIPELINE(COMMAND(MOT(a)OUT(2,b)IN(3,c)))'),
        (r'a >&2'    , r'PIPELINE(COMMAND(MOT(a)OUT(1,&2)))'),
        # Make an error with bash
        (r'a>$A<$D'  , r'PIPELINE(COMMAND(MOT(a)OUT(1,a)MOT(b)IN(0,PATTERN(*))))'),
        (r'a;b'      , r'PIPELINE(COMMAND(MOT(a)))PIPELINE(COMMAND(MOT(b)))'),
        (r'a ; b'    , r'PIPELINE(COMMAND(MOT(a)))PIPELINE(COMMAND(MOT(b)))'),
        (r'a \; b'   , r'PIPELINE(COMMAND(MOT(a)MOT(;)MOT(b)))'),
        (r'a \; b'   , r'PIPELINE(COMMAND(MOT(a)MOT(;)MOT(b)))'),
        (r'a $F b'   , r'PIPELINE(COMMAND(MOT(a)MOT(;)MOT(b)))'),
        (r'a # ; b'  , r'PIPELINE(COMMAND(MOT(a)COMMENT( ; b)))'),
        (r'A=5'      , r'PIPELINE(COMMAND(MOT(AAFFECTATION()5)))'),
        (r'A\=5'     , r'PIPELINE(COMMAND(MOT(A=5)))'),
        (r'a|b'      , r'PIPELINE(COMMAND(MOT(a))COMMAND(MOT(b)))'),
        (r'a\|b'     , r'PIPELINE(COMMAND(MOT(a|b)))'),
        (r'a;b|c;d'  , r'PIPELINE(COMMAND(MOT(a)))PIPELINE(COMMAND(MOT(b))COMMAND(MOT(c)))PIPELINE(COMMAND(MOT(d)))'),
        (r'a||b'     , r'PIPELINE(COMMAND(MOT(a)))||PIPELINE(COMMAND(MOT(b)))'),
        (r'a|b||c|d' , r'PIPELINE(COMMAND(MOT(a))COMMAND(MOT(b)))||PIPELINE(COMMAND(MOT(c))COMMAND(MOT(d)))'),
        (r'a&&b'     , r'PIPELINE(COMMAND(MOT(a)))&&PIPELINE(COMMAND(MOT(b)))'),
        ):
        print(a)
        if parse(Text(a)) != b:
            print(('====OK====>', b))
            print(('====BAD===>', parse(Text(a))))
            break
        
    
