# -*- coding: utf-8
#    SHEEXP: SHEll EXPlainer
#    Copyright (C) 2015 Thierry EXCOFFIER, Universite Claude Bernard
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#    Contact: Thierry.EXCOFFIER@univ-lyon1.fr

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
    def __init__(self, chars, message=""):
        self.content = chars
        self.message = message
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
    def init_position(self, i=0, ident=0):
        self.start = i
        self.end = i + len(self.content)
        self.ident = ident
        return self.end
    def help(self, position):
        s = '<div '
        if position != -1:
            s += 'id="H' + str(self.ident) + '" '
        return (s + 'class="help help_' + name(self) + '"><div>'
                + (self.message or self.local_help(position))
                + '</div></div>')
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
    def merge_separator(self):
        pass # To easely stop container recursion
    def remove_empty(self):
        pass # To easely stop container recursion
    def text(self):
        return self.content # To easely stop container recursion
    
class Normal(Chars):
    def local_help(self, dummy_position):
        return 'Caractères : ' + protect(self.content)
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
        if '"' in self.content:
            return ("Pour terminer le texte protégé, il faut mettre"
                    + " un deuxième guillemet")
        if "'" in self.content:
            return ("Pour terminer le texte protégé, il faut mettre"
                    + " une deuxième cote")
        if "\\" in self.content:
            return "Le caractère suivant n'aura pas de signification particulière"
        if ";" in self.content:
            return "Vous pouvez taper une autre autre commande ou faire un pipeline"
        if "&&" in self.content:
            return "Vous pouvez taper une autre autre commande ou faire un pipeline qui sera exécuter si la précédente se termine bien"
        if "(" in self.content:
            return "Les commandes jusqu'à la parenthèse fermante seront exécutées dans un nouveau processus"
        if ">" in self.content or '<' in self.content:
            return "Indiquez le nom du fichier ou bien «&amp;» et le numéro du fildes"
        if "|" in self.content:
            if self.parent.content[0] is self:
                return "Il manque une commande à gauche du pipe"
            else:
                return "Tapez la commande qui va traiter la sortie standard de la commande de gauche"
        return "Il manque une suite pour ce symbole : «" + self.content + "»"

class Unexpected(Chars):
    def local_help(self, dummy_position):
        return "Il est interdit d'avoir «" + self.content + "» à cet endroit"

class Invisible(Chars):
    def itext(self, txt):
        return "Le caractère «" + self.content + "» disparaît. " + txt
class Backslash(Invisible):
    def local_help(self, dummy_position):
        return self.itext("Il annule la signification du caractère suivant.")
class Quote(Invisible):
    def local_help(self, dummy_position):
        return self.itext("La signification de tous les caractères entres les deux cotes est annulée.")
class Guillemet(Invisible):
    def local_help(self, dummy_position):
        return self.itext("La signification de tous les caractères entres les 2 guillemets est annullée sauf l'anti-slash et le dollar.")
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
        return 'Lancement en arrière plan'        

class For(Chars):
    def local_help(self, dummy_position):
        return "Premier argument : le nom de la variable d'indice"

class While(Chars):
    def local_help(self, dummy_position):
        return "Indiquer la commande à exécuter"

class In(Chars):
    def local_help(self, dummy_position):
        return "Indiquer les valeurs que la variable va prendre"

class EndOfValues(Chars):
    def local_help(self, dummy_position):
        if isinstance(self.parent, ForLoop):
            return "Termine la liste des valeurs prises par la variable"
        else:
            return "Termine la commande précédente"

class EndOfCommand(Chars):
    def local_help(self, dummy_position):
        return "Termine la commande"

class Do(Chars):
    def local_help(self, dummy_position):
        return "Indiquez les instructions qui seront dans la boucle"

class Done(Chars):
    def local_help(self, dummy_position):
        return "Fin de la définition du corps de la boucle"
  
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
        return s + 'class="help help_' + name(self) + '"><div>'+h+'</div></div>'
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
                if i != 0 and name(self.content[i-1]) == 'Separator':
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
        for i, content in enumerate(self.content):
            if (isinstance(content, Command)
                and len(content.content) == 1
                and isinstance(content.content[0], Separator)
            ):
                content = content.content[0]
                self.content[i] = content

            if not content.empty():
                content.replace_empty()
        if self.empty():
            return
        def separator(x):
            return (isinstance(x, DotComa)
                    or isinstance(x, Pipe)
                    or isinstance(x, And)
                    or isinstance(x, Comment)
            )
        for i in range(len(self.content)):
            if (separator(self.content[i])
                and (i == len(self.content)-1 or i == 0
                     or separator(self.content[i+1])
                     or name(self.content[i-1]) == 'Separator'
                 )):
                if not isinstance(self.content[i], Comment):
                    self.content[i] = Unterminated(self.content[i].content)
    def text(self):
        return ''.join([x.text() for x in self.content])

class Line(Container):
    def local_help(self, dummy_position):
        nr_pipeline = 0
        nr_command = 0
        for x in self.content:
            if isinstance(x, Pipeline):
                if x.number_of(Command) == 1:
                    nr_command += 1
                else:
                    nr_pipeline += 1
        if nr_command + nr_pipeline == 0:
            return 'Une ligne de commande vide.'
        if nr_pipeline == 0:
            return ('Une ligne de commande avec ' + str(nr_command)
                    + ' commande.')
        if nr_command == 0:
            return ('Une ligne de commande avec ' + str(nr_pipeline)
                    + ' pipeline.')
        return ('Une ligne de commande avec ' + str(nr_command)
                + ' commande et ' + str(nr_pipeline) + ' pipeline.')
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
    def local_help(self, dummy_position):
        if isinstance(self.parent, ForValues):
            return ""
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
        return "Les crochets indiquent que l'on veut un seul caractère de la liste"
class Group(Command):
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

class Backgrounded(Container):
    def local_help(self, dummy_position):
        return 'Lancé en arrière plan'

class Anded(Container):
    def local_help(self, dummy_position):
        return "La suite est exécutée seulement si le début s'est bien passé"

class Affectation(Container):
    def local_help(self, dummy_position):
        v = ''
        for content in self.content[2:]:
            v += content.html()
        return ('Affectation dans la variable : «'
                + self.content[0].html() + '» de la valeur «' + v + '»')

class ForLoop(Command):
    def local_help(self, dummy_position):
        return "Boucle for"
        
class WhileLoop(Command):
    def local_help(self, dummy_position):
        return "Boucle while"

class ForValues(Command):
    def local_help(self, dummy_position):
        return "Les valeurs que va prendre la variable"

class Body(Command):
    def local_help(self, dummy_position):
        if isinstance(self.content[-1], Done):
            return "Les commandes qui sont répétées"
        else:
            return "Terminer le bloc de commande avec le mot-clef «done»"

class LoopVariable(Container):
    def local_help(self, dummy_position):
        return "Nom de la variable qui va changer de valeur"


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
            pipeline = self.parse_pipeline()
            if not parsed.empty() and isinstance(parsed.content[-1], Anded):
                parsed.content[-1].append(pipeline)
            else:
                parsed.append(pipeline)
            if isinstance(pipeline.content[-1], Done):
                break
            if not self.empty() and self.get() == ';':
                self.next()
                parsed.append(DotComa(";" + self.skip(" \t")))
            if not self.empty() and self.get() == '&':
                self.next()
                if not self.empty() and self.get() == '&':
                    self.next()
                    if parsed.empty():
                        parsed.append(Unterminated("&&"))
                    else:
                        b = Anded()
                        b.append(parsed.content.pop())
                        b.append(And("&&" + self.skip(" \t")))
                        parsed.append(b)
                else:
                    if parsed.empty():
                        parsed.append(Unterminated("&"))
                    else:
                        b = Backgrounded()
                        b.append(parsed.content.pop())
                        b.append(Background("&" + self.skip(" \t")))
                        parsed.append(b)
        if init:
            parsed.raise_comment()
            parsed.remove_empty()
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
                if isinstance(parsed.content[-1], Done):
                    return parsed
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

    def parse_while(self):
        parsed = WhileLoop()
        parsed.append(While('while' + self.skip(" \t")))
        ok = not self.empty()
        if ok:
            parsed.append(self.parse_command())
            if (len(parsed.content[-1].content)
                and self.empty()
                and name(parsed.content[-1]) == 'Command'
                and name(parsed.content[-1].content[-1]) == 'Separator'):
                print '***'
                parsed.content[-1].content[-1] = Unterminated(
                    parsed.content[-1].content[-1].content,
                    "Ajoutez un point-virgule pour finir la liste")
        else:
            parsed.content[0] = Unterminated(parsed.content[0].content,
                                             "Indiquez une commande")
            ok = False
        return self.parse_do_done(ok, parsed)
        
    def parse_for(self):
        parsed = ForLoop()
        parsed.append(For('for' + self.skip(" \t")))
        ok = not self.empty()
        if ok:
            v = LoopVariable()
            v.append(self.parse_argument())
            parsed.append(v)
        else:
            parsed.content[0] = Unterminated(parsed.content[0].content,
                                             "Indiquez le nom de la variable")
        ok &= not self.empty()
        if ok:
            self.read_separator(parsed)
            if self.empty():
                parsed.content[-1] = Unterminated(parsed.content[-1].content,
                                                  "Mettre le mot-clef «in»")
            
        ok &= not self.empty()
        if ok:
            v = self.parse_argument()
            if v.text() == 'in':
                parsed.append(In('in' + self.skip(' \t')))
            else:
                parsed.append(Unexpected(v.text() + self.skip(' \t'),
                                         'Il manque le mot-clef «in»'))
                ok = False
        ok &= not self.empty()
        if ok:
            v = ForValues()
            parsed.append(v)
            while not self.empty():
                if self.get() in ';>()&|':
                    break
                v.append(self.parse_argument())
                self.read_separator(v)
            if (len(v.content)
                and self.empty()
                and name(v.content[-1]) == 'Separator'):
                v.content[-1] = Unterminated(
                    v.content[-1].content,
                    "Ajoutez un point-virgule pour finir la liste")
        return self.parse_do_done(ok, parsed)

    def parse_do_done(self, ok, parsed):
        ok &= not self.empty()
        if ok:
            if self.get() == ';':
                self.next()
                parsed.append(EndOfValues(';'))
                if not self.empty():
                    self.read_separator(parsed)
                if self.empty() and name(parsed.content[-1]) == 'Separator':
                    parsed.content[-1] = Unterminated(
                        parsed.content[-1].content,
                        "Ajoutez le mot-clef «do»")
            else:
                parsed.append(Unexpected(self.get()))
                self.next()
                ok = False
        ok &= not self.empty()
        if ok:
            v = self.parse_argument()
            if v.text() == 'do':
                b = Body()
                parsed.append(b)
                b.append(Do('do' + self.skip(' \t')))
                ok = True
            else:
                parsed.append(Unexpected(v.text() + self.skip(' \t')))
                ok = False
        ok &= not self.empty()
        if ok:
            for content in self.parse(0).content:
                b.append(content)
            if (len(b.content) >= 3
                and b.content[-2].text().strip() == ';'
                and b.content[-1].text() == 'done'
                ):
                b.content[-1] = b.content[-1].content[0]
            else:
                ok = False
        if ok:
            while (not self.empty()
                   and (not self.read_separator(parsed)
                        or not self.read_redirection(parsed))):
                pass
        if not ok and not isinstance(parsed.content[0], Unterminated):
            parsed.content[0] = Unterminated(parsed.content[0].content)
        return parsed

    def parse_command(self):
        parsed = Command()
        i = self.i
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
                if parsed.number_of(Argument) == 1:
                    if parsed.content[-1].text() == 'for':
                        return self.parse_for()
                    if parsed.content[-1].text() == 'while':
                        return self.parse_while()
                    if parsed.content[-1].text() == 'done':
                        return Done('done')
                    
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
        if self.empty() or self.get() in '#<>;|)':
            parsed.append(Unterminated(fildes + c))
            return
        redirection = Redirection()
        redirection.append(Fildes(fildes))
        redirection.append(Direction(c))
        if self.get() == '&':
            if len(c) == 1:
                self.next()
                fildes = self.skip(digit)
                if fildes:
                    redirection.append(Fildes('&' + fildes))
                else:
                    redirection.append(Unterminated("&"))
            else:
                redirection.content[1] = Unterminated(c)
                redirection.append(Unterminated(''))
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
                parsed.append(Normal('['))
                return
            i = self.i
            sb = SquareBracket()
            sb.append(SquareBracketStart('['))
            empty = 1
            while not self.empty():
                if self.get() == ']' and len(sb.content) != empty:
                    break
                if self.get() == '!' and len(sb.content) == empty and empty==1:
                    empty = 2
                    sb.append(SquareBracketNegate('!'))
                    self.next()
                    continue
                if self.get() == '$':
                    self.read_dollar(sb)
                    continue
                if self.get() == '"':
                    self.read_guillemet(sb)
                    continue
                if self.get() == "'":
                    self.read_quote(sb)
                    continue
                if self.get() == "\\":
                    self.read_backslash(sb)
                    continue
                if self.get() in ' \t':
                    parsed.append(Normal('['))
                    self.i = i
                    return
                c = self.get()
                self.next()
                if self.empty():
                    sb.append(Normal(c))
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
                parsed.append(Normal('['))
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
            if c in ' \t><|;)(&':
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
