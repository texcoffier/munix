#!/usr/bin/python

# Missing $() & &&

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha = upper + upper.lower() + '_'
digit = "0123456789"
name  = alpha + digit

class Container(object):
    def __init__(self, content=()):
        self.content = list(content)
    def append(self, item):
        self.content.append(item)
    def __str__(self):
        return self.__class__.__name__ + '(' + ','.join(str(x)
                                                        for x in self.content
                                                    ) + ')'
    def extract_last_separator(self):
        if not self.content:
            return ''
        if  isinstance(self.content[-1], Separator):
            return self.content.pop().content
        try:
            return self.content[-1].extract_last_separator()
        except AttributeError:
            return ''
    def nice(self, depth=0):
        return ('C'
                + ' '*depth
                + self.__class__.__name__ + '[%d]\n' % len(self.content)
                + ''.join(x.nice(depth+4)
                          for x in self.content)
            )
    def nr_arguments(self):
        return sum(x.nr_arguments()
                   for x in self.content)
        
class Line(Container):
    pass
class Pipeline(Container):
    pass
class Command(Container):
    pass
class Argument(Container):
    def append(self, item):
        if self.content and self.content[-1].__class__ is item.__class__:
            self.content[-1].content += item.content
        else:
            self.content.append(item)
    def nice(self, depth=0):
        return 'A' + ' '*depth + ' '.join(str(x) for x in self.content) + '\n'
    def nr_arguments(self):
        return 1
class Redirection(Argument):
    pass
class File(Container):
    pass

class Chars(object):
    def __init__(self, chars):
        self.content = chars
    def __str__(self):
        return '%s(%s)' % (self.__class__.__name__, repr(self.content))
    def nice(self, depth):
        return 'C' + ' '*depth + str(self) + '\n'
    def nr_arguments(self):
        return 0
    
class Normal(Chars):
    pass
class Separator(Chars):
    def nice(self, depth):
        return  'S' + ' '*depth + '%s(%s)\n' % (
            self.__class__.__name__, repr(self.content))
class Pipe(Separator):
    pass
class DotComa(Separator):
    pass
class Variable(Chars):
    pass
class Unterminated(Chars):
    pass

class Invisible(Chars):
    pass
class Backslash(Invisible):
    pass
class Quote(Invisible):
    pass
class Guillemet(Invisible):
    pass
class Dollar(Invisible):
    pass
class Fildes(Invisible):
    pass
class Direction(Invisible):
    pass

class Parser:
    def __init__(self, text):
        self.text = text.strip()
        self.len = len(self.text)
    def empty(self):
        assert self.i <= self.len
        return self.len == self.i
    def get(self):
        return self.text[self.i]
    def next(self):
        self.i += 1
    def skip(self, chars):
        s = ""
        while not self.empty():
            if self.text[self.i] in chars:
                s += self.text[self.i]
                self.next()
            else:
                break
        return s
    def merge_separator(self, parsed, char, classe):
        if self.empty() or self.get() != char:
            return
        text = parsed.content[-1].extract_last_separator() + self.get()
        self.next()
        text += self.skip(" \t")
        if parsed.content[-1].nr_arguments() == 0:
            parsed.append(Unterminated(text))
        else:
            parsed.append(classe(text))
    def parse(self):
        self.i = 0
        parsed = Line()
        while not self.empty():
            parsed.append(self.parse_pipeline())
            self.merge_separator(parsed, ';', DotComa)
        if parsed.content and isinstance(parsed.content[-1], DotComa):
            parsed.content[-1] = Unterminated(parsed.content[-1].content)
        return parsed
    def parse_pipeline(self):
        parsed = Pipeline()
        while not self.empty():
            parsed.append(self.parse_command())
            self.merge_separator(parsed, '|', Pipe)
            if not self.empty() and self.get() == ';':
                break
        if parsed.content and isinstance(parsed.content[-1], Pipe):
            parsed.content[-1] = Unterminated(parsed.content[-1].content)
        return parsed
    def read_comment(self, parsed):
        if (self.get() != '#'
            or len(parsed.content) == 0
            or not isinstance(parsed.content[-1], Separator)
            ):
            return True
        parsed.content[-1].content += self.text[self.i:]
        self.i = self.len
    def parse_command(self):
        parsed = Command()
        while not self.empty():
            while (not self.empty()
                   and (not self.read_separator(parsed)
                        or not self.read_redirection(parsed))):
                pass
            if not self.empty():
                if not self.read_comment(parsed):
                    return parsed
                if self.get() in '|;':
                    return parsed
            if not self.empty():
                parsed.append(self.parse_argument())
        return parsed
    def read_separator(self, parsed):
        c = self.get()
        if c not in ' \t':
            return True
        parsed.append(Separator(self.skip(" \t")))        
    def read_redirection(self, parsed):
        i = self.i
        fildes = self.skip(digit)
        c = self.get()
        if c not in '<>':
            self.i = i
            return True
        self.next()
        if self.get() == c:
            c += c
            self.next()
        redirection = Redirection()
        redirection.append(Fildes(fildes))
        redirection.append(Direction(c))
        if self.get() == '&':
            self.next()
            fildes = self.skip(digit)
            if fildes:
                redirection.append(Fildes('&' + fildes))
            else:
                redirection.append(Unterminated("&"))
        else:
            redirection.append(File(self.parse_argument().content))
        parsed.append(redirection)
        
    def read_backslash(self, parsed):
        if self.get() != '\\':
            return True
        self.next()
        if self.empty():
            parsed.append(Unterminated("\\"))
        else:
            parsed.append(Backslash("\\"))
            parsed.append(Normal(self.get()))
            self.next()
    def read_dollar(self, parsed):
        if self.get() != '$':
            return True
        self.next()
        if self.empty():
            parsed.append(Normal("$"))
        else:
            c = self.get()
            if c in alpha:
                parsed.append(Dollar('$'))
                parsed.append(Variable(self.skip(name)))
            else:
                parsed.append(Normal('$')) # Assume its signification disapear
    def read_quote(self, parsed):
        if self.get() != "'":
            return True
        self.next()
        if self.empty():
            parsed.append(Unterminated("'"))
        else:
            i = len(parsed.content)
            parsed.append(Quote("'"))
            while not self.empty():
                c = self.get()
                self.next()
                if c == "'":
                    parsed.append(Quote(c))
                    break
                parsed.append(Normal(c))
            if not isinstance(parsed.content[-1], Quote):
                parsed.content[i] = Unterminated("'")
    def read_guillemet(self, parsed):
        if self.get() != '"':
            return True
        self.next()
        if self.empty():
            parsed.append(Unterminated('"'))
        else:
            i = len(parsed.content)
            parsed.append(Guillemet('"'))
            while not self.empty():
                if (self.read_backslash(parsed)
                    and self.read_dollar(parsed)):
                    c = self.get()
                    self.next()
                    if c == '"':
                        parsed.append(Guillemet(c))
                        return
                    parsed.append(Normal(c))
            if not isinstance(parsed.content[-1], Guillemet):
                parsed.content[i] = Unterminated("'")
    def parse_argument(self):
        parsed = Argument()
        while not self.empty():
            c = self.get()
            if c in ' \t><|;':
                return parsed
            if (self.read_backslash(parsed)
                and self.read_dollar(parsed)
                and self.read_quote(parsed)
                and self.read_guillemet(parsed)
                ):
                parsed.append(Normal(c))
                self.next()
        return parsed


def check(input, output):
    p = Parser(input)
    result = str(p.parse())
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
check("a\\ a\\ \\   \\    \\", r"Line(Pipeline(Command(Argument(Normal('a'),Backslash('\\'),Normal(' a'),Backslash('\\'),Normal(' '),Backslash('\\'),Normal(' ')),Separator('  '),Argument(Backslash('\\'),Normal(' ')),Separator('   '),Argument(Unterminated('\\')))))")
check("' ' '  ' '\\' '\\\\' '\\\\\\' '", r"""Line(Pipeline(Command(Argument(Quote("'"),Normal(' '),Quote("'")),Separator(' '),Argument(Quote("'"),Normal('  '),Quote("'")),Separator(' '),Argument(Quote("'"),Normal('\\'),Quote("'")),Separator(' '),Argument(Quote("'"),Normal('\\\\'),Quote("'")),Separator(' '),Argument(Quote("'"),Normal('\\\\\\'),Quote("'")),Separator(' '),Argument(Unterminated("'")))))""")
check("a'b", """Line(Pipeline(Command(Argument(Normal('a'),Unterminated("'"),Normal('b')))))""")
check("$A '$B' \\$B $/ $B1/ $", r"""Line(Pipeline(Command(Argument(Dollar('$'),Variable('A')),Separator(' '),Argument(Quote("'"),Normal('$B'),Quote("'")),Separator(' '),Argument(Backslash('\\'),Normal('$B')),Separator(' '),Argument(Normal('$/')),Separator(' '),Argument(Dollar('$'),Variable('B1'),Normal('/')),Separator(' '),Argument(Normal('$')))))""")
check("$A$B", "Line(Pipeline(Command(Argument(Dollar('$'),Variable('A'),Dollar('$'),Variable('B')))))")
check('"A $B \\$C \\"" "', r"""Line(Pipeline(Command(Argument(Guillemet('"'),Normal('A '),Dollar('$'),Variable('B'),Normal(' '),Backslash('\\'),Normal('$C '),Backslash('\\'),Normal('"'),Guillemet('"')),Separator(' '),Argument(Unterminated('"')))))""")
check('"$" "a', """Line(Pipeline(Command(Argument(Guillemet('"'),Normal('$'),Guillemet('"')),Separator(' '),Argument(Unterminated("'"),Normal('a')))))""")
check('a>b', "Line(Pipeline(Command(Argument(Normal('a')),Redirection(Fildes(''),Direction('>'),File(Normal('b'))))))")
check('a >$C >>\\$ <" $A"', r"""Line(Pipeline(Command(Argument(Normal('a')),Separator(' '),Redirection(Fildes(''),Direction('>'),File(Dollar('$'),Variable('C'))),Separator(' '),Redirection(Fildes(''),Direction('>>'),File(Backslash('\\'),Normal('$'))),Separator(' '),Redirection(Fildes(''),Direction('<'),File(Guillemet('"'),Normal(' '),Dollar('$'),Variable('A'),Guillemet('"'))))))""")
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

print "OK"

        
