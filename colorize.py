# -*- coding: utf-8

# Missing  && & : message explicites

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

##############################################################################
##############################################################################
##############################################################################

class Chars:
    def __init__(self, chars):
        self.content = chars
    def str(self):
        return name(self) + '(' + repr(self.content) + ')'
    def nice(self, depth):
        return 'C' + pad(depth) + self.str() + '\n'
    def html(self, position=-1):
        s = '<div '
        if position != -1:
            s += 'id="P' + str(self.ident) + '" '
        return (s + 'class="Parsed ' + self.active(position) + name(self)
                + '">' + protect(self.content) + '</div>')
    def nr_arguments(self):
        return 0
    def init_position(self, i=0, ident=0):
        self.start = i
        self.end = i + len(self.content)
        self.ident = ident
        return self.end
    def help(self, position):
        s = '<div '
        if position != -1:
            s += 'id="H' + str(self.ident) + '" '
        return (s + 'class="help help_' + name(self) + '">'
                + self.local_help(position) + '</div>')
    def local_help(self, dummy_position):
        return name(self) + ':' + protect(self.content)
    def active(self, position):
        if self.start < position <= self.end:
            return "active "
        else:
            return ""
    def is_a_pattern(self):
        return False
    def empty(self):
        return True # To easely stop container recursion
    def raise_separator(self):
        return [self] # To easely stop container recursion
    def merge_separator(self):
        pass # To easely stop container recursion
    def remove_empty(self):
        pass # To easely stop container recursion
    
class Normal(Chars):
    def local_help(self, dummy_position):
        return 'Verbatim : ' + protect(self.content)
class Pattern(Chars):
    def is_a_pattern(self):
        return True
class Star(Pattern):
    def local_help(self, dummy_position):
        return ("L'étoile représente une suite quelconque de caractères"
                + " pouvant être vide.")
class QuestionMark(Pattern):
    def local_help(self, dummy_position):
        return "Le point d'intérogation représente un caractère quelconque."
class Separator(Chars):
    def nice(self, depth):
        return  'S' + pad(depth) + name(self) + '(' +repr(self.content)+ ')\n'
    def local_help(self, dummy_position):
        return 'Un espace ou plus pour séparer les arguments.'
class Comment(Separator):
    def local_help(self, dummy_position):
        return ("Un commentaire jusqu'à la fin de la ligne."
                + " Il n'est pas passé à la commande."
                + " Ce n'est pas un argument."
                + " Le shell ne regarde pas dedans.")
class Pipe(Separator):
    def local_help(self, dummy_position):
        return ('Le | redirige la sortie standard de la commande de gauche'
                + " sur l'entrée standard de la commande de droite."
            )
class DotComa(Separator):
    def local_help(self, dummy_position):
        return "Le ';' permet de séparer les commandes."
class Variable(Chars):
    def local_help(self, dummy_position):
        return (self.html()
                + " est remplacé par le shell par le contenu de la variable «"
                + self.content[1:] + '».'
                + ' Le nom de la variable disparaît.'
            )
class Unterminated(Chars):
    def local_help(self, dummy_position):
        return "Il manque une suite pour ce symbole : «" + self.content + "»"

class Unexpected(Chars):
    def local_help(self, dummy_position):
        return "Il est interdit d'avoir «" + self.content + "» à cet endroit"

class Invisible(Chars):
    def text(self, txt):
        return "Le caractère «" + self.content + "» disparaît. " + txt
class Backslash(Invisible):
    def local_help(self, dummy_position):
        return self.text("Il annule la signification du caractère suivant.")
class Quote(Invisible):
    def local_help(self, dummy_position):
        return self.text("La signification de tous les caractères entres les deux cotes est annulée.")
class Guillemet(Invisible):
    def local_help(self, dummy_position):
        return self.text("La signification de tous les caractères entres les 2 guillemets est annullée sauf l'anti-slash et le dollar.")
class Fildes(Invisible):
    def local_help(self, dummy_position):
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
        return 'Le fildes «' + self.content + "» représentant " + s
class Direction(Invisible):
    def local_help(self, dummy_position):
        c = self.content.strip()
        if c == self.content:
            more = ''
        else:
            more = (" <b>Ce n'est pas une bonne idée de mettre des espaces "
                    + "après la redirection car ce n'est pas un opérateur "
                    + "symétrique.</b>")
        if self.parent.content[2].content[0] == '&':
            s = "On mélange la sortie avec le fildes indiqué."
        elif c == '>>':
            s = "On ajoute à la fin du fichier destination."
        elif c == '>':
            s = "On vide le fichier destination."
        elif c == '<':
            s = "On lit à partir du fichier indiqué."
        else:
            s = 'bug'
        return s + more
class SquareBracketStart(Pattern):
    def local_help(self, dummy_position):
        return "Début de la liste des caractères possibles."
class SquareBracketStop(Pattern):
    def local_help(self, dummy_position):
        return "Fin de la liste des caractères possibles."
class SquareBracketChar(Pattern):
    def local_help(self, dummy_position):
        return "Le caractère «" + self.content + "» est autorisé"
class SquareBracketInterval(Pattern):
    def local_help(self, dummy_position):
        return ("Tous les caractères dans l'intervalle «" + self.content
                + "» sont autorisés")
class SquareBracketNegate(Pattern):
    def local_help(self, dummy_position):
        return ("Ce caractère indique que les caractères listés"
                + " sont ceux dont on ne veux pas.")
class GroupStart(Pattern):
    def local_help(self, dummy_position):
        return "Début du groupement"
class GroupStop(Pattern):
    def local_help(self, dummy_position):
        return "Fin du groupement"
class Equal(Chars):
    def local_help(self, dummy_position):
        return "Affectation dans la variable dont le nom est à gauche de la valeur à droite."
class And(Chars):
    def local_help(self, dummy_position):
        return ("La commande de droite ne s'exécute que"
                + " si la commande de gauche s'est terminée sans erreur")

class Background(Chars):
    def local_help(self, dummy_position):
        return 'La commande de gauche est lancée en arrière plan'
        

##############################################################################
##############################################################################
##############################################################################

class Container:
    def __init__(self):
        self.content = []
    def append(self, item):
        self.content.append(item)
    def str(self):
        return name(self) + '(' + ','.join([x.str()
                                            for x in self.content
                                        ]) + ')'
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
                    for x in self.content
                    is isinstance(x, Argument)
                ])
    def active(self, position):
        if self.start < position <= self.end:
            return "active "
        else:
            return ""
    def html(self, position=-1):
        s = '<div '
        if position != -1:
            s += 'id="P' + str(self.ident) + '" '
        return (s + 'class="Parsed ' + self.active(position) + name(self)
                + '">' + ''.join([x.html(position)
                                  for x in self.content
                              ])
                + '</div>')
    def init_position(self, i=0, ident=0):
        self.start = i
        for content in self.content:
            content.init_position(i, ident)
            i = content.end
            ident = content.ident + 1
            content.parent = self
        self.ident = ident
        self.end = i
        return i
    def help(self, position):
        s = ''
        for content in self.content:
            if content.start <= position <= content.end:
                s += content.help(position)
                break
        h = self.local_help(position)
        if h == '':
            return s
        s += '<div '
        if position != -1:
            s += 'id="H' + str(self.ident) + '" '
        return s + 'class="help help_' + name(self) + '">' + h + '</div>'
    def local_help(self, dummy_position):
        return name(self) + ':<br>'
    def number_of(self, classe):
        return len([x
                  for x in self.content
                    if isinstance(x, classe)
                  ])
    def first_of(self, classe):
        for x in self.content:
            if isinstance(x, classe):
                return x
    def is_a_pattern(self):
        for c in self.content:
            if c.is_a_pattern():
                return True
    def empty(self):
        return len(self.content) == 0
    def raise_separator(self):
        if self.empty():
            return [self]
        new_content = []
        for content in self.content[:]:
            for i in content.raise_separator():
                new_content.append(i)
        self.content = new_content
        value = []
        if name(self.content[0]) == 'Separator':
            value.append(self.content[0]) # pop(0) not working with rapydscript
            self.content = self.content[1:]
        value.append(self)
        if not self.empty() and name(self.content[-1]) == 'Separator':
            value.append(self.content.pop())
        return value
    def merge_separator(self):
        for content in self.content:
            content.merge_separator()
        i = 0
        new_content = []
        while i < len(self.content):
            current = self.content[i]
            if (isinstance(self.content[i], Pipe)
                or isinstance(self.content[i], DotComa)
                or isinstance(self.content[i], GroupStop)
                or isinstance(self.content[i], GroupStart)
                or isinstance(self.content[i], And)
                or isinstance(self.content[i], Background)
                ):
                v = self.content[i].content
                if i != 0 and isinstance(self.content[i-1], Separator):
                    v = self.content[i-1].content + v
                    new_content.pop() # Remove the separator before
                if (i != len(self.content)-1
                    and name(self.content[i+1]) == 'Separator'
                    ):
                    v += self.content[i+1].content
                    self.content[i+1] = Unterminated("FAKE")
                    i += 1 # Jump over beware of '|'  ' '  '|'
                current.content = v
                new_content.append(current)
            else:
                new_content.append(current)
            i += 1
        self.content = new_content
    def raise_comment(self):
        if self.empty():
            return
        if self.content[-1].empty():
            return
        self.content[-1].raise_comment()
        if isinstance(self.content[-1].content[-1], Comment):
            self.append(self.content[-1].content.pop())
    def remove_empty(self):
        for content in self.content:
            content.remove_empty()
        self.content = [
            content
            for content in self.content
            if (not content.empty() or
                (not isinstance(content, Command)
                 and not isinstance(content, Pipeline)
                 ))
            ]
    def replace_empty(self):
        for content in self.content:
            if not content.empty():
                content.replace_empty()
        if self.empty():
            return
        if (isinstance(self.content[0], Pipe)
            or isinstance(self.content[0], DotComa)
            ):
            self.content[0] = Unterminated(self.content[0].content)
        if (isinstance(self.content[-1], Pipe)
            or isinstance(self.content[-1], DotComa)
            ):
            self.content[-1] = Unterminated(self.content[-1].content)
        if (len(self.content) > 1
            and isinstance(self.content[-1], Comment)
            and (
                isinstance(self.content[-2], Pipe)
                or isinstance(self.content[-2], DotComa)
            )):
            self.content[-2] = Unterminated(self.content[-2].content)

class Line(Container):
    def local_help(self, dummy_position):
        nr = self.number_of(Pipeline)
        if nr == 0:
            return 'Une ligne de commande vide.'
        if nr == 1:
            return 'Une ligne de commande avec une seule commande.'
        return ('Une ligne de commande avec ' + str(nr) + ' pipeline.')
class Pipeline(Container):
    def local_help(self, dummy_position):
        nr = self.number_of(Command)
        if nr == 0:
            return 'Un pipeline vide !'
        if nr == 1:
            return ''
        return 'Un pipeline enchainant ' + str(nr) + ' commandes.'
class Command(Container):
    def local_help(self, dummy_position):
        nr = self.number_of(Argument)
        if nr == 0:
            return 'Une commande vide !'
        if nr == 1:
            return 'Commande : ' + self.content[0].html() + ' sans argument'
        return ('La commande '
                + self.first_of(Argument).html() + ' avec '
                + str(nr-1) + ' arguments.')
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
    def local_help(self, dummy_position):
        pos = 0
        for child in self.parent.content:
            if isinstance(child, Argument):
                if child is self:
                    break
                pos += 1
        if pos == 0:
            return ''
        if self.is_a_pattern():
            more = (" c'est un pattern qui est remplacé par tous les noms"
                    + " de fichiers existant qui rentrent dans le moule.")
        else:
            more = ''
        return 'Argument ' + str(pos) + ' : ' + self.html() + more + '<br>'
class Redirection(Container):
    def local_help(self, dummy_position):
        m = ''
        if self.content[0].content == '':
            if self.content[1].content == '>':
                m = " de la sortie standard"
            elif self.content[1].content == '<':
                m = " de l'entrée standard"
        return "C'est une redirection" +m+ ", pas un argument de la commande."
class SquareBracket(Container):
    def local_help(self, dummy_position):
        return "Les crochets indiquent que l'on veut un seul caractère."
class Group(Container):
    def local_help(self, dummy_position):
        return "Lance un nouveau processus pour évaluer le contenu."
class Replacement(Container):
    def is_a_pattern(self):
        return False
    def local_help(self, dummy_position):
        return ("Lance un nouveau processus pour évaluer le contenu. "
                + "Ces caractères sont remplacés par ce qui a été "
                + "écrit par le processus sur sa sortie standard."
                )
class File(Container):
    def local_help(self, dummy_position):
        return 'Le fichier dont le nom est : ' + self.html()

class Affectation(Container):
    def local_help(self, dummy_position):
        v = ''
        for content in self.content[2:]:
            v += content.html()
        return ('Affectation dans la variable : «'
                + self.content[0].html() + '» de la valeur «' + v + '»')

##############################################################################
##############################################################################
##############################################################################

class Parser:
    def __init__(self, text):
        self.text = text
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
    def parse(self, init=True):
        if init:
            self.i = 0
        parsed = Line()
        while not self.empty():
            if self.get() == ')':
                break
            parsed.append(self.parse_pipeline())
            if not self.empty() and self.get() == ';':
                self.next()
                parsed.append(DotComa(";" + self.skip(" \t")))
            if not self.empty() and self.get() == '&':
                self.next()
                if not self.empty() and self.get() == '&':
                    self.next()
                    parsed.append(And("&&" + self.skip(" \t")))
                else:
                    parsed.append(Background("&" + self.skip(" \t")))
        if init:
            parsed.raise_comment()
            parsed.raise_separator()
            parsed.remove_empty()
            parsed.raise_separator()
            parsed.merge_separator()
            parsed.replace_empty()
            parsed.init_position()
        return parsed
    def parse_pipeline(self):
        parsed = Pipeline()
        while not self.empty():
            if self.get() == '(':
                parsed.append(self.parse_group())
            else:
                parsed.append(self.parse_command())
            if not self.empty() and self.get() in ';)&':
                break
            if not self.empty() and self.get() == '|':
                self.next()
                parsed.append(Pipe("|" + self.skip(" \t")))
        return parsed
    def parse_group(self, eat_separator=True):
        parsed = Group()
        self.next()
        parsed.append(GroupStart("("))
        parsed.append(self.parse(0))
        if self.empty():
            parsed.content[0] = Unterminated("(")
        else:
            if self.get() == ')':
                self.next()
                c = ")"
                if eat_separator:
                    c += self.skip(" \n")
                parsed.append(GroupStop(c))
                if not self.empty():
                    self.read_redirection(parsed)
        return parsed
    def read_comment(self, parsed):
        if (self.get() != '#'
            or (len(parsed.content) != 0
                and not isinstance(parsed.content[-1], Separator))
            ):
            return True
        parsed.append(Comment(self.text[self.i:]))
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
                if self.get() in '|;)&':
                    return parsed
                while not self.empty() and self.get() in '(':
                    parsed.append(Unexpected("("))
                    self.next()
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
        while self.get() in ' \t#':
            c += self.get()
            self.next()
        if self.empty() or self.get() in '#<>;|':
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
            elif c == '(':
                r = Replacement()
                for content in self.parse_group(False).content:
                    r.append(content)
                r.content[0].content = '$' + r.content[0].content
                parsed.append(r)
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
    def read_pattern(self, parsed):
        if self.get() == '*':
            parsed.append(Star("*"))
        elif self.get() == '?':
            parsed.append(QuestionMark("?"))
        elif self.get() == '[':
            self.next()
            if self.empty():
                parsed.append(Unterminated('['))
                return
            i = self.i
            sb = SquareBracket()
            sb.append(SquareBracketStart('['))
            while not self.empty():
                if self.get() == ']' and len(sb.content) != 0:
                    break
                if self.get() == '!' and len(sb.content) == 0:
                    sb.append(SquareBracketNegate('!'))
                    self.next()
                    continue
                c = self.get()
                self.next()
                if self.empty():
                    sb.append(Unterminated(c))
                    break
                if self.get() == '-':
                    self.next()
                    if self.empty():
                        break
                    if self.get() == ']':
                        sb.append(SquareBracketChar(c))
                        sb.append(SquareBracketChar('-'))
                    else:
                        sb.append(SquareBracketInterval(c + '-' + self.get()))
                        self.next()
                else:
                    sb.append(SquareBracketChar(c))
            if self.empty():
                parsed.append(Unterminated('['))
                self.i = i
                return
            sb.append(SquareBracketStop(']'))
            parsed.append(sb)
        else:
            return True
        self.next()
    def read_equal(self, parsed):
        if len(parsed.content) != 1 or self.get() != '=':
            return True
        self.next()
        if name(parsed.content[0]) != 'Normal':
            return True
        a = Affectation()
        a.append(parsed.content.pop())
        a.append(Equal("="))
        for content in self.parse_argument().content:
            a.append(content)
        parsed.append(a)
    def parse_argument(self):
        parsed = Argument()
        while not self.empty():
            c = self.get()
            if c in ' \t><|;)(':
                break
            if (self.read_backslash(parsed)
                and self.read_dollar(parsed)
                and self.read_quote(parsed)
                and self.read_guillemet(parsed)
                and self.read_pattern(parsed)
                and self.read_equal(parsed)
                ):
                parsed.append(Normal(c))
                self.next()
        if isinstance(parsed.content[0], Affectation):
            return parsed.content[0]
        return parsed

def findPos(x):
    curleft = 0
    curtop = 0
    obj = x
    if obj.offsetParent:
        while obj:
            curleft += obj.offsetLeft
            curtop += obj.offsetTop
            obj = obj.offsetParent

        while x and x.scrollTop == 0:
            x = x.parentNode
        if x and x.tagName != 'HTML' and x.tagName != 'BODY' and x.scrollTop:
            curleft -= x.scrollLeft
            curtop -= x.scrollTop
    return curleft, curtop

def create_links(help):
    border = 1
    output = document.getElementById(help)
    for help_box in output.getElementsByTagName('DIV'):
        place = document.getElementById('P' + help_box.id[1:])
        if not place:
            continue
        place_pos = findPos(place)
        n = document.createElement('VAR')
        n.className = "link " + help_box.className
        n.id = 'L' + help_box.id[1:]
        n.style.left = str(place_pos[0]) + "px"
        top = place_pos[1] + place.offsetHeight + border
        n.style.top = str(top) + "px"
        n.style.height = str(findPos(help_box)[1] - top - 2*border) + "px"
        n.style.width = place.offsetWidth + "px"
        output.appendChild(n)
