# -*- coding: utf-8

# > seul
# Missing * ? [] () $() & && 

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha = upper + upper.lower() + '_'
digit = "0123456789"
names = alpha + digit

def name(obj):
    try:
        return obj.__class__.__name__
    except:
        return obj.__proto__.constructor.name

def pad(x):
    return "                                                         "[:x]

def protect(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        
class Container:
    def __init__(self):
        self.content = []
    def append(self, item):
        self.content.append(item)
    def str(self):
        return name(self) + '(' + ','.join([x.str()
                                            for x in self.content
                                        ]) + ')'
    def extract_last_separator(self):
        if not self.content:
            return ''
        if  isinstance(self.content[-1], Separator):
            return self.content.pop().content
        try:
            return self.content[-1].extract_last_separator()
        except:
            return ''
    def nice(self, depth=0):
        return ('C'
                + pad(depth)
                + name(self) + '\n'
                + ''.join([x.nice(depth+4)
                           for x in self.content
                       ])
            )
    def nr_arguments(self):
        return sum([x.nr_arguments()
                    for x in self.content])
    def active(self, position):
        if self.start <= position <= self.end:
            return "active "
        else:
            return ""
    def html(self, position=-1):
        return ('<div class="Parsed ' + self.active(position) + name(self)
                + '">' + ''.join([x.html(position)
                                  for x in self.content
                              ])
                + '</div>')
    def init_position(self, i=0):
        self.start = i
        for content in self.content:
            i = content.init_position(i)
            content.parent = self
        self.end = i
        return i
    def help(self, position):
        s = self.local_help()
        for content in self.content:
            if content.start <= position <= content.end:
                s += content.help(position)
                break
        return s
    def local_help(self):
        return name(self) + ':<br>'
    def number_of(self, classe):
        return len([x
                  for x in self.content
                    if isinstance(x, classe)
                  ])
        
class Line(Container):
    def local_help(self):
        nr = self.number_of(Pipeline)
        if nr == 0:
            return '<div class="help_Line">Une ligne de commande vide.</div>'
        if nr == 1:
            return '<div class="help_Line">Une ligne de commande avec une seule commande.</div>'
        return ('<div class="help_Line">Une ligne de commande avec '
                + str(nr) + ' commandes.</div>')
class Pipeline(Container):
    def local_help(self):
        nr = self.number_of(Command)
        if nr == 0:
            return '<div class="help_Pipeline">Un pipeline vide !</div>'
        if nr == 1:
            return ''
        return ('<div class="help_Pipeline">'
                + 'Un pipeline enchainant ' + str(nr) + ' commandes.</div>')
class Command(Container):
    def local_help(self):
        nr = self.number_of(Argument)
        if nr == 0:
            return '<div class="help_Command">Une commande vide !'
        if nr == 1:
            return ('<div class="help_Command">Commande : '
                    + self.content[0].html() + ' sans argument</div>')
        return ('<div class="help_Command">La commande '
                + self.content[0].html() + ' avec '
                + (nr-1) + ' arguments.</div>')
class Argument(Container):
    def append(self, item):
        if (len(self.content) != 0
            and name(self.content[-1]) == name(item)
            and not isinstance(item, Variable)
            ):
            self.content[-1].content += item.content
        else:
            self.content.append(item)
    def nice(self, depth=0):
        return 'A' + pad(depth) + ' '.join([x.str() for x in self.content])+'\n'
    def nr_arguments(self):
        return 1
    def local_help(self):
        pos = 0
        for child in self.parent.content:
            if isinstance(child, Argument):
                if child is self:
                    break
                pos += 1
        if pos == 0:
            return ''
        return 'Argument ' + str(pos) + ' : ' + self.html() + '<br>'
class Redirection(Argument):
    def local_help(self, position):
        m = ''
        if self.content[0].content == '':
            if self.content[1].content == '>':
                m = " de la sortie standard"
            elif self.content[1].content == '<':
                m = " de l'entrée standard"
        return ('<div class="help_Redirection">'
                + "C'est une redirection "
                + m + ", pas un argument de la commande."
                + '</div>')
class File(Container):
    def local_help(self, position):
        return ('<div class="help_Redirection">Le fichier dont le nom est : '
                + self.html() + '</div>')

class Chars:
    def __init__(self, chars):
        self.content = chars
    def str(self):
        return name(self) + '(' + repr(self.content) + ')'
    def nice(self, depth):
        return 'C' + pad(depth) + self.str() + '\n'
    def html(self, position=-1):
        return ('<div class="Parsed ' + self.active(position) + name(self) + '">'
                + protect(self.content) + '</div>')
    def nr_arguments(self):
        return 0
    def init_position(self, i=0):
        self.start = i
        self.end = i + len(self.content)
        return self.end
    def help(self, position):
        return name(self) + ':' + protect(self.content)
    def active(self, position):
        if self.start < position <= self.end:
            return "active "
        else:
            return ""
    
class Normal(Chars):
    def help(self, position):
        return ('Verbatim : ' + protect(self.content))
class Separator(Chars):
    def nice(self, depth):
        return  'S' + pad(depth) + name(self) + '(' +repr(self.content)+ ')\n'
    def help(self, position):
        return ('Un espace ou plus pour séparer les arguments.')
class Pipe(Separator):
    def help(self, position):
        return ('Le | redirige la sortie standard de la commande de gauche'
                + " sur l'entrée standard de la commande de droite."
            )
def _Pipe(x): # RapydScript can not pass class as function argument
    return Pipe(x)
class DotComa(Separator):
    def help(self, position):
        return ("Le ';' permet de séparer les commandes.")
def _DotComa(x): # RapydScript can not pass class as function argument
    return DotComa(x)
class Variable(Chars):
    def help(self, position):
        return (self.html()
                + " est remplacé par le shell par le contenu de la variable «"
                + self.content[1:] + '».'
                + ' Le nom de la variable disparaît.'
            )
class Unterminated(Chars):
    def help(self, position):
        return "Il manque une suite pour ce symbole : " + self.content

class Invisible(Chars):
    def text(self, txt):
        return ("Le caractère «" + self.content
                + "» n'est pas passé à la commande. "
                + txt)
class Backslash(Invisible):
    def help(self, position):
        return self.text("Il annule la signification du caractère suivant.")
class Quote(Invisible):
    def help(self, position):
        return self.text("La signification de tous les caractères entres les deux cotes est annulée.")
class Guillemet(Invisible):
    def help(self, position):
        return self.text("La signification de tous les caractères entres les 2 guillemets est annullée sauf l'anti-slash et le dollar.")
class Fildes(Invisible):
    def help(self, position):
        if self.content[0] == '&':
            c = self.content[1:]
        else:
            c = self.content
        if c == '1':
            s = "la sortie standard."
        elif c == '2':
            s = "la sortie d'erreur."
        elif c == '0':
            s = "l'entrée standard."
        else:
            s = "???"
        return ('<div class="help_Redirection">Le fildes «'
                + self.content + "» représentant " + s + '</div>')
class Direction(Invisible):
    def help(self, position):
        if self.parent.content[2].content[0] == '&':
            s = "On mélange la sortie avec le fildes indiqué."
        elif self.content == '>':
            s = "On vide le fichier destination."
        elif self.content == '>>':
            s = "On ajoute à la fin du fichier destination."
        elif self.content == '<':
            s = "On lit à partir du fichier indiqué."
        else:
            s = 'bug'
        return '<div class="help_Redirection">' + s + '</div>'
class Parser:
    def __init__(self, text):
        self.text = text.strip()
        self.len = len(self.text)
    def empty(self):
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
            self.merge_separator(parsed, ';', _DotComa)
        if len(parsed.content) != 0 and isinstance(parsed.content[-1], DotComa):
            parsed.content[-1] = Unterminated(parsed.content[-1].content)
        parsed.init_position()
        return parsed
    def parse_pipeline(self):
        parsed = Pipeline()
        while not self.empty():
            parsed.append(self.parse_command())
            self.merge_separator(parsed, '|', _Pipe)
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
        if self.empty():
            parsed.append(Unterminated(fildes + c))
            return
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
            f = File()
            f.content = self.parse_argument().content
            redirection.append(f)
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
                parsed.append(Variable('$' + self.skip(names)))
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
                parsed.content[i] = Unterminated('"')
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
