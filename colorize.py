# -*- coding: utf-8
#    SHEEXP: SHEll EXPlainer
#    Copyright (C) 2015-2016 Thierry EXCOFFIER, Universite Claude Bernard
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

def string(t):
    return "'" + t.replace("\\", "\\\\").replace("'", "\\'") + "'"

def unused_color(element):
    i = 0
    my_color = element.color()[1]
    p = element.parent
    while p:
        if p.color()[1] == my_color:
            i += 1
        p = p.parent
    color = []
    for c in my_color[1:]:
        c = hex_to_int[c]
        c *= 16
        if c == 15*16:
            c = 255
        color.append(str(int(c * 0.85**i)))
    return 'rgba(' + ','.join(color) + ', 0.8)'

def choices(keywords):
    return ' ou '.join(['«' + k + '»'
                        for k in keywords
                        ])

class Option:
    def __init__(self, option , short, message, argument=False, display=True):
        self.option   = option
        self.short    = short
        self.message  = message
        self.argument = argument
        self.display  = display

class Options:
    def __init__(self, *options):
        self.options = options
        self.long_opt = {}
        for option in options:
            self.long_opt[option.option] = option
        self.short_opt = {}
        for option in options:
            self.short_opt[option.short] = option

    def get_option(self, value):
        if value.split("=")[0] in self.long_opt:
            return value, self.long_opt[value.split("=")[0]]
        if value in self.short_opt:
            return value, self.short_opt[value]
        return

    def html(self):
        s = []
        for option in self.options:
            if not option.display:
                continue
            s.append("   <tt>" + option.option + "</tt> ")
            if option.option != option.short:
                s.append("(<tt>" + option.short + "</tt>) ")
            s.append(" : ")
            s.append(option.message)
            s.append("<br>")
        return ''.join(s)
    
list_stopper = '&<>;|()'
redirection_stopper = '#<>;|()'
argument_stopper = ' \t' + list_stopper
pipeline_stopper = ';)&'

##############################################################################
##############################################################################
##############################################################################

def define_command():
    return {
        "builtin": False,
        "description": '',
        "message": '',
        "syntax": '',
        "1": '',
        "*": '',
        "$": '',
        "unknown": '',
        "section": '1',
        "min_arg": 0,
        "options": None
        }

def define_builtin():
    d = define_command()
    d["builtin"] = True
    return d

def define_cd():
    d = define_builtin()
    d['name'] = 'cd'
    d['description'] = "<b>C</b>hange <b>D</b>irectory"
    d['message'] = "Elle permet de changer de répertoire courant"
    d['syntax'] = "cd <var>chemin_absolu_ou_relatif</var>"
    d['1'] = "Chemin vers ce qui deviendra le nouveau répertoire courant"
    d['unknown'] = "Cet argument est inutile et provoquera une erreur"
    return d

def define_pwd():
    d = define_builtin()
    d['name'] = 'pwd'
    d['description'] = "<b>P</b>rint <b>W</b>orking <b>D</b>irectory"
    d['message'] = "Elle affiche le chemin absolu du répertoire courant"
    d['syntax'] = "pwd"
    d['unknown'] = "Cet argument est complètement inutile et peut éventuellement provoquer des erreurs"
    return d

def define_ls():
    d = define_command()
    d['name'] = 'ls'
    d['description'] = "<b>L</b>i<b>S</b>te directory"
    d['message'] = "Elle permet de lister le contenu de répertoires"
    d['syntax'] = "ls <var>dir1</var> <var>dir2</var>..."
    d['options'] = Options(
        Option('-l', '-l', "(l=long) affiche plein d'informations"),
        Option('--all', '-a',
               "affiche aussi les fichiers dont le nom commence par '.'")
    )
    return d

def define_cat():
    d = define_command()
    d['name'] = 'cat'
    d['description'] = "Con<b>cat</b>ène des fichiers"
    d['message'] = "Elle affiche les contenu des fichiers"
    d['syntax'] = "cat <var>file1</var> <var>file2</var>..."
    return d

def define_cp():
    d = define_command()
    d['name'] = 'cp'
    d['description'] = "<b>c</b>o<b>p</b>ie de fichiers et répertoires"
    d['message'] = "Elle crée ou écrase des fichiers si c'est nécessaire"
    d['syntax'] = "cp <var>source</var> <var>destination</var>"
    d['1'] = "Nom du premier fichier à copier ailleurs"
    d['$'] = "Le fichier ou répertoire destination de la copie"
    d['min_arg'] = 2
    d['options'] = Options(
        Option('--recursive', '-r',
               "copie récursive de répertoire : tout le contenu")
        )
    return d

def define_rm():
    d = define_command()
    d['name'] = 'rm'
    d['description'] = "<b>r</b>e<b>m</b>ove : destruction de fichiers et répertoires"
    d['message'] = "La destruction est définitive sans confirmation"
    d['syntax'] = "rm <var>chemin_vers_fichier</var> <var>autre_fichier</var> ..."
    d['min_arg'] = 1
    d['*'] = "Entité à détruire"
    d['options'] = Options(
        Option('--recursive', '-r',
               "détruit tout le contenu et le répertoire"),
        Option('--interactive', '-i',
               "demande l'autorisation avant de détruire"),
        Option('--force', '-f', 'détruit sans jamais poser de question')
        )
    return d

def define_mkdir():
    d = define_command()
    d['name'] = 'mkdir'
    d['description'] = "<em><b>m</b>a<b>k</b>e <b>dir</b>ectory</em> : création de répertoires"
    d['message'] = "Elle crée les répertoires dans les noms sont indiqués"
    d['syntax'] = "mkdir <var>chemin_du_répertoire_à_créer</var>"
    d['1'] = "chemin vers le répertoire qui va être créé"
    d['min_arg'] = 1
    return d

def define_ln():
    d = define_command()
    d['name'] = 'ln'
    d['description'] = "(<b>l</b>i<b>n</b>k) création de liens physique ou symbolique"
    d['syntax'] = "ln -s <var>source</var> <var>destination</var>"
    d['1'] = "Nom du fichier vers lequel le lien pointera"
    d['$'] = "L'endroit où va être créé le lien"
    d['min_arg'] = 2
    d['options'] = Options(
        Option('--symbolic', '-s', "création d'un lien symbolique")
        )
    return d

def define_less():
    d = define_command()
    d['name'] = 'less'
    d['description'] = "affichage de fichier page par page"
    d['comment'] = "Si aucun nom de fichier n'est donné c'est un filtre"
    d['syntax'] = "less <var>fichier1</var> <var>fichier2</var>"
    return d

def define_man():
    d = define_command()
    d['name'] = 'man'
    d['description'] = "(<b>man</b>uel) affiche la documentation"
    d['syntax'] = "man commande"
    d['1'] = "Nom de la commande à expliquer"
    d['min_arg'] = 1
    d['options'] = Options(
        Option('--apropos', '-k',
               "Liste les commandes avec le mot clef indiqué",
               'Mot clef à rechercher')
        )
    return d

def define_tail():
    d = define_command()
    d['name'] = 'tail'
    d['description'] = "(queue) affiche la fin de fichier"
    d['syntax'] = "tail fichier1 fichier2"
    d['*'] = "Affiche la fin de ce fichier"
    d['options'] = Options(
        Option('--lines', '-n', "Choisir le nombre de lignes",
               'Nombre de lignes à afficher'),
        Option('--follow', '-f', "Affiche la suite si le fichier grossi"),
        Option('--bytes', '-c', "Choisir le nombre d'octets à afficher",
               "Nombre d'octets à afficher", False)
    )
    return d

def define_du():
    d = define_command()
    d['name'] = 'du'
    d['description'] = "(<b>d</b>isck <b>u</b>sage</am>) affiche la place occupée"
    d['syntax'] = "du dir1 dir2..."
    d['*'] = "Affiche la taille occupée par cette hiérarchie"
    d['options'] = Options(
        Option('--human-readable', '-h', "Affiche en Ko, Mo, Go, To..."),
        Option('--summarize', '-s', "Affiche seulement le total")
    )
    return d

command_aliases = {
    'more': 'less',
}

commands = {}
for x in [define_cd(), define_pwd(), define_ls(), define_cat(), define_cp(),
          define_mkdir(), define_rm(), define_ln(), define_less(),
          define_man(), define_tail(), define_du()]:
    if x['name'] in commands:
        duplicate_name
        
    commands[x['name']] = x

def format_help(definition):
    return "help " + definition["name"]

def format_man(definition):
    return ('<a target="_blank" href="http://linux.die.net/man/' +
            definition["section"] + '/' + definition["name"]
            + '">man ' + definition["name"] + "</a>")

##############################################################################
##############################################################################
##############################################################################

class Chars:
    hide = False
    def __init__(self, chars, message=""):
        self.content = chars
        self.message = message
    def color(self):
        return ["#000", "#FFF"]
    def str(self):
        return name(self) + '(' + string(self.content) + ')'
    def nice(self, depth):
        return 'C' + pad(depth) + self.str() + '\n'
    def cleanup(self, replace_option):
        return name(self) + "(" + string(self.content) + ")"
    def html(self, position=-1):
        s = '<div '
        if position != -1:
            s += 'id="P' + str(self.ident) + '" '
        return (s + 'class="Parsed ' + self.active(position) + name(self)
                + '" style="color:' + self.color()[0]
                + '">' + protect(self.content) + '</div>')
    def init_position(self, i=0, ident=0):
        self.start = i
        self.end = i + len(self.content)
        self.ident = ident
        return self.end
    def help(self, position):
        message = self.message or self.local_help(position)
        if len(message) == 0:
            return ''
        s = '<div '
        if position != -1:
            s += 'id="H' + str(self.ident) + '" '
        return (s + 'class="help help_' + name(self)
                + '" style="background:' + unused_color(self)
                + ';border:1px solid black'
                + '"><div>' + message + '</div></div>')
    def local_help(self, dummy_position):
        return name(self) + ':' + protect(self.content)
    def active(self, position):
        if self.start < position <= self.end:
            return "active "
        else:
            return ""
    def is_a_pattern(self):
        return False
    def last_position(self, position):
        return len(self.content) == position - self.start
    def empty(self):
        return True # To easely stop container recursion
    def merge_separator(self):
        pass # To easely stop container recursion
    def remove_empty(self):
        pass # To easely stop container recursion
    def text(self):
        return self.content # To easely stop container recursion
    def raise_separator(self, last=True):
        pass # To easely stop container recursion
    def replace_unexpected(self):
        pass # To easely stop container recursion
    def check_options(self):
        pass # To easely stop container recursion
        

class Normal(Chars):
    def local_help(self, position):
        return 'Texte : «' + self.html(position) + '»'
class Pattern(Chars):
    def color(self):
        return ["#F0F", "#FAF"]
    def is_a_pattern(self):
        return True
class Star(Pattern):
    def local_help(self, dummy_position):
        return ("L'étoile représente une suite quelconque de caractères"
                + " pouvant être vide.")
class QuestionMark(Pattern):
    def local_help(self, dummy_position):
        return "Le point d'intérogation représente un caractère quelconque."
class Home(Pattern):
    def local_help(self, dummy_position):
        if self.content == '~':
            return "Le tilde représente votre répertoire de connexion"
        else:
            return ("C'est le répertoire de connexion de l'utilisateur «"
                    + self.content[1:] + '»')
            
class Separator(Chars):
    hide = True
    def nice(self, depth):
        return  'S' + pad(depth) + name(self) + '('+string(self.content)+')\n'
    def local_help(self, dummy_position):
        return 'Un espace ou plus pour séparer les arguments.'
    
class Comment(Chars):
    def local_help(self, dummy_position):
        return ("Un commentaire jusqu'à la fin de la ligne."
                + " Il n'est pas passé à la commande."
                + " Ce n'est pas un argument."
                + " Le shell ne regarde pas dedans.")
class Pipe(Separator):
    def local_help(self, dummy_position):
        return ('Le «|» redirige la sortie standard de la commande de gauche'
                + " sur l'entrée standard de la commande de droite."
            )
class DotComa(Separator):
    def local_help(self, dummy_position):
        return "Le «;» permet de séparer les commandes."

special_variables = {
    "#": "le nombre d'arguments du script shell",
    "?": "la valeur de retour du processus précédent",
    "$": "le PID du shell en train de s'exécuter",
    "0": "le nom du script shell en train de s'exécuter",
    "*": "tous les arguments du script shell : <b>ne pas utiliser car cela ne permet pas de manipuler les arguments avec un espace</b>",
    "@": "tous les arguments du script shell",
    }
class Variable(Chars):
    def color(self):
        return ["#00F", "#CCF"]
    def local_help(self, dummy_position):
        if self.content[1:] in special_variables:
             message = special_variables[self.content[1:]]
        elif len(self.content[1:]) == 1 and self.content[1:] in digit:
            message = ("la valeur de l'argument numéro " + self.content[1:]
                       + " du script shell")
        elif self.content[1] == '{':
            message = "quelque chose...<br>Cette syntaxe est complexe et rarement utile. Elle n'est pas expliquée par cette application"
        else:
            message = ("le contenu de la variable «" + self.content[1:]
                       + '». Le nom de la variable disparaît.')
        return "«" + self.html() + "» est remplacé par le shell par " + message
class VariableProtected(Variable):
    pass
class Unterminated(Chars):
    def color(self):
        return ["#F00", "#FAA"]
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
            return "Vous pouvez taper une autre commande ou faire un pipeline"
        if "&&" in self.content:
            return "Vous pouvez taper une autre commande ou faire un pipeline qui sera exécuter si la précédente se termine bien"
        if "(" in self.content:
            return "Les commandes jusqu'à la parenthèse fermante seront exécutées dans un nouveau processus"
        if ">" in self.content or '<' in self.content:
            return "Indiquez le nom du fichier ou bien «&amp;» et le numéro du fildes"
        if "|" in self.content:
            if self.parent.content[0] is self:
                return "Il manque une commande à gauche du pipe"
            else:
                return "Tapez la commande qui va traiter la sortie standard de la commande de gauche"
        if self.content[0] == '~':
            return "Le nom de login après le tilde doit être suivi par un «/»"
        return "Il manque une suite pour ce symbole : «" + self.content + "»"

class Unexpected(Unterminated):
    def local_help(self, dummy_position):
        return "Il est interdit d'avoir «" + self.content + "» à cet endroit"

class Invisible(Chars):
    hide = True
    def color(self):
        return ["#BBB", "#FFF"]
    def itext(self, txt):
        if isinstance(self.parent, SquareBracket):
            txt += ".<br><b>Même le tiret dans ce contexte</b>"
        return "Le caractère «" + self.content + "» disparaît. " + txt
class Backslash(Invisible):
    def local_help(self, dummy_position):
        return self.itext("Il annule la signification du caractère suivant.")
class Quote(Invisible):
    def local_help(self, dummy_position):
        return self.itext("La signification de tous les caractères entre les deux cotes est annulée.")
class Guillemet(Invisible):
    def local_help(self, dummy_position):
        return self.itext("La signification de tous les caractères entre les 2 guillemets est annulée sauf l'anti-slash et le dollar.")
class Fildes(Chars):
    def color(self):
        return ["#088", "#AFF"]
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
        elif c == '':
            return ''
        else:
            s = "???"
        return 'Le fildes «' + self.content + "» représentant " + s
class Direction(Fildes):
    def local_help(self, dummy_position):
        c = self.content.strip()
        if c == self.content:
            more = ''
        else:
            more = (" <b>Ce n'est pas une bonne idée de mettre des espaces "
                    + "après la redirection car ce n'est pas un opérateur "
                    + "symétrique.</b>")
        if self.parent.content[2].content[0] == '&':
            s = "On mélange la sortie avec le fildes indiqué"
        elif c == '>>':
            s = "On ajoute à la fin du fichier"
        elif c == '>':
            s = "On vide ou crée le fichier"
        elif c == '<':
            s = "On lit le fichier indiqué"
        elif c == '<<':
            s = "On lit le texte partir de la ligne suivant cette commande"
        else:
            s = 'bug'
        return s + more
    def cleanup(self, replace_option):
        return name(self) + '(' + string(self.content.strip()) + ')'
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
class GroupStart(Variable):
    def local_help(self, dummy_position):
        return "Début du groupement"
    def cleanup(self, replace_option):
        return name(self) + ' '
class GroupStop(GroupStart):
    def local_help(self, dummy_position):
        return "Fin du groupement"
class Equal(Chars):
    def color(self):
        return ["#880", "#FFA"]
    def local_help(self, dummy_position):
        return "Affectation"
class And(Chars):
    def local_help(self, dummy_position):
        return ("La commande de droite ne s'exécute que si la "
                + "dernière exécution à gauche s'est terminée sans erreur")
    def cleanup(self, replace_option):
        return '&&'

class Or(Chars):
    def local_help(self, dummy_position):
        return ("La commande de droite ne s'exécute que si la "
                + "dernière exécution à gauche s'est terminée avec une erreur")
    def cleanup(self, replace_option):
        return '||'

class Background(Separator):
    def local_help(self, dummy_position):
        return 'Lancement en arrière plan'        
    def cleanup(self, replace_option):
        return '&'

class For(Equal):
    def local_help(self, position):
        if self.last_position(position):
            return "Le nom de la variable d'indice"
        return "Début de boucle"
    def cleanup(self, replace_option):
        return '' # Not necessary because implied by the container

class If(For):
    def local_help(self, position):
        if self.last_position(position):
            return "La commande à exécuter"
        return "Si la commande s'exécute sans erreur : alors c'est vrai"

class Then(For):
    def local_help(self, position):
        return "Les instructions qui suivent sont exécutées si le test est vrai"

class Else(For):
    def local_help(self, position):
        return "Les instructions qui suivent sont exécutées si le test est faux"

class Fi(For):
    def local_help(self, position):
        return "Fin du «if»"

class While(For):
    def local_help(self, position):
        if self.last_position(position):
            return "La commande à exécuter"
        return "Début de boucle"

class In(For):
    def local_help(self, dummy_position):
        return "Indiquer les valeurs que la variable va prendre"

class EndOfValues(Separator):
    def local_help(self, position):
        if self.last_position(position):
            if isinstance(self.parent, IfThenElse):
                return "Mettre le mot-clef «then»"
            else:
                return "Mettre le mot-clef «do»"
        if isinstance(self.parent, ForLoop):
            return "Termine la liste des valeurs prises par la variable"
        else:
            return "Termine la commande précédente"

class EndOfCommand(Separator):
    def local_help(self, dummy_position):
        return "Termine la commande"

class Do(For):
    def local_help(self, dummy_position):
        return "Les instructions qui seront dans la boucle"

class Done(For):
    def local_help(self, dummy_position):
        return "Fin de la définition du corps de la boucle"
  
##############################################################################
##############################################################################
##############################################################################

hex_to_int = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
              'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

class Container:
    hide = False
    def __init__(self):
        self.content = []
    def color(self):
        return ["#000", "#F00"]
    def append(self, item):
        self.content.append(item)
    def str(self):
        return name(self) + '(' + ','.join([x.str()
                                            for x in self.content
                                        ]) + ')'
    def cleanup(self, replace_option):
        protected = False
        content = []
        for c in self.content:
            n = name(c)
            if c.hide:
                if n == 'Guillemet':
                    protected = not protected
                continue
            if n == 'Variable':
                if protected:
                    c = VariableProtected(c.content)
            elif n == 'Replacement':
                if protected:
                    r = ReplacementProtected()
                    r.content = c.content
                    c = r
            elif (n == 'Normal'
                  and len(content) != 0
                  and name(content[-1]) == 'Normal'
                  ):
                content[-1] = Normal(content[-1].content + c.content)
                continue
            elif (len(content) != 0
                  and replace_option
                  and getattr(content[-1], 'concatenable_right', False)
                  and (getattr(c, 'concatenable_left', False)
                       or getattr(c, 'is_an_option_argument', False))
              ):
                # option joining
                left = content[-1].option_canon
                if c.is_an_option:
                    right = c.option_canon[1:]
                else:
                    right = c.text_content()
                content[-1] = Argument()
                content[-1].content = [Normal(left + right)]
                content[-1].parent = self
                content[-1].parse_option()
                continue
            content.append(c)
        first_argument = True
        clean = []
        for c in content:
            txt = c.cleanup(replace_option)
            if name(c) == 'Argument':
                if first_argument:
                    first_argument = False
                    command = txt.replace(
                        "Argument(Normal('", "").replace("'))", "")
                    if command in command_aliases:
                        txt ="Argument(Normal('"+command_aliases[command]+"'))"
            clean.append(txt)
        return name(self) + '(' + ''.join(clean) + ')'

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
    def check_options(self):
        for content in self.content:
            content.check_options()
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
        return (s + 'class="help help_' + name(self)
                + '" style="background:' + unused_color(self) + '"><div>'
                + h + '</div></div>')
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
            if (isinstance(self.content[i], Separator)
                or isinstance(self.content[i], GroupStart)
                or isinstance(self.content[i], GroupStop)
                or isinstance(self.content[i], In)
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
    def replace_unexpected(self):
        if (isinstance(self, Pipeline)
            and isinstance(self.content[0], Done)
        ):
            self.content[0] = Unexpected(self.content[0].content)
        for i, content in enumerate(self.content):
            content.replace_unexpected()
            if (isinstance(content, Background)
                and i != len(self.content)-1
                and isinstance(self.content[i+1], DotComa)
                ):
                self.content[i+1] = Unexpected(self.content[i+1].content,
                                               "Non autorisé après un «&»"
                                               )            
    def raise_separator(self, last=True):
        new_content = []
        for i, content in enumerate(self.content):
            last_i = last and (i == len(self.content)-1)
            content.raise_separator(last_i)
            new_content.append(content)
            if content.empty():
                continue
            if (not content.empty()
                and (name(content.content[-1]) == 'Separator'
                     or
                     name(content.content[-1]) == 'Background'
                     )
                and not last_i
                ):
                new_content.append(content.content.pop())
        self.content = new_content
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
        if isinstance(self, ThenBloc):
            return
        if isinstance(self, ElseBloc):
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
    def color(self):
        return ["#000", "#EEE"]
    def local_help(self, dummy_position):
        nr_pipeline = 0
        nr_command = 0
        nr_background = 0
        nr_anded = 0
        for x in self.content:
            if isinstance(x, Backgrounded):
                nr_background += 1
            elif isinstance(x, Conditionnal):
                nr_anded += 1
            elif isinstance(x, Pipeline):
                if x.number_of(Command) == 1:
                    nr_command += 1
                else:
                    nr_pipeline += 1
        if nr_command + nr_pipeline + nr_background + nr_anded == 0:
            return 'Une ligne de commande vide.'
        m = []
        if nr_background:
            if nr_background == 1:
                m.append("un lancement en arrière plan")
            else:
                m.append(str(nr_background) + " lancements en arrière plan")
        if nr_anded:
            if nr_anded == 1:
                m.append("une suite de commandes conditionnelles")
            else:
                m.append(str(nr_anded)+ " suites de commandes conditionnelles")
        if nr_pipeline:
            if nr_pipeline == 1:
                m.append("un pipeline")
            else:
                m.append(str(nr_pipeline) + " pipelines")
        if nr_command:
            if nr_command == 1:
                m.append("une commande simple")
            else:
                m.append(str(nr_command) + " commandes simples")
        return 'Une ligne comportant : ' + ', '.join(m)
class Pipeline(Line):
    def local_help(self, dummy_position):
        nr = self.number_of(Command)
        if nr == 0:
            return 'Un pipeline vide !'
        if nr == 1:
            return ''
        return 'Un pipeline enchainant ' + str(nr) + ' commandes.'
class Command(Container):
    def color(self):
        return ["#000", "#CFC"]
    def local_help(self, position):
        nr = self.number_of(Argument)
        if len(self.content) and isinstance(self.content[-1], Command):
            # Case of the For and While loop
            return ''
        if nr == 0:
            return 'Une commande vide !'
        if nr == 1:
            return ('Commande : «' + self.first_of(Argument).html()
                    + '» sans argument' + self.contextual_help(position))
        if nr == 2:
            a = 'un argument.'
        else:
            a = str(nr-1) + ' arguments.'
        return ('La commande «' + self.first_of(Argument).html()
                + '» avec ' + a + self.contextual_help(position))

    def check_options(self):
        arg_number = 0
        argument_for_option = False
        self.command = False
        for content in self.content:
            content.check_options()
            content.is_an_option = False
            content.argument_position = 0
            content.is_an_option_argument = False
            if not isinstance(content, Argument):
                continue
            if arg_number == 0:
                # Compute command name
                self.command = None
                command = content.content[0].cleanup(False).split("Normal(")
                if command[0] == '': # XXX why ?
                    command = command[1][1:-2]
                    if command in commands:
                        self.command = command
                arg_number += 1
                continue
            if argument_for_option:
                content.is_an_option_argument = option_argument_help
                argument_for_option = False
                continue
            content.parse_option()
            argument_for_option = content.option_argument_after
            option_argument_help = content.option_argument_help
            if content.is_an_option:
                continue
            content.argument_position = arg_number
            arg_number += 1
        self.nr_argument = arg_number # Real one, not option argument
    def contextual_help(self, dummy_position):
        if not self.command:
            return ''
        definition = commands[self.command]
        s = ['<div class="command_help">',
             '<b>', self.command, '</b> : ',  definition["description"]]
        if definition["builtin"]:
            s.append(" (builtin)")
        s.append('<br>')
        if len(definition["message"]):
            s.append(definition["message"])
            s.append('<br>')
        if definition["syntax"]:
            s.append('Syntaxe : <tt>')
            s.append(definition["syntax"])
            s.append("</tt><br>")
        if definition["options"]:
            s.append("Options :<br>")
            s.append(definition["options"].html())
        s.append("Aide : <tt>")
        s.append(definition["builtin"]
                 and format_help(definition)
                 or format_man(definition))
        s.append("</tt><br>")
        if self.nr_argument < definition["min_arg"]:
            s.append('<span class="command_help_error">'
                     + 'Votre commande manque d\'argument !</span><br>')
        s.append('</div>')
        return '\n'.join(s)

class Argument(Container):
    def color(self):
        return ["#000", "#FFA"]
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
    def local_help(self, position):
        pos = 0
        for child in self.parent.content:
            if isinstance(child, Argument):
                if child is self:
                    break
                pos += 1
        if pos == 0 and not isinstance(self.parent, ForValues):
            return ''
        if self.is_a_pattern():
            more = (" c'est un pattern qui est remplacé par tous les noms"
                    + " de fichiers existants qui rentrent dans le moule.")
        else:
            more = ''
        if isinstance(self.parent, ForValues):
            if more == '':
                return '«' + self.html() + "» est une des valeurs possibles"
            else:
                return '«' + self.html() + "» :" + more
        more += self.contextual_help(position)
        return 'Argument ' + str(pos) + ' : «' + self.html() + "»" + more
    def text_content(self):
        c = self.cleanup(False).split("Normal('")
        if len(c) == 1:
            return ''
        return c[1].split("'")[0]
    def contextual_help(self, position):
        command = self.parent.command
        if not command:
            return ''
        definition = commands[command]
        if self.is_an_option:
            option = self.option_definition(position)
            if option:
                return ('<div class="command_help">' + option[0] + " : "
                        + option[1].message + '</div>')
            else:
                if position <= self.option_argument_position:
                    return ''
                else:
                    option = self.option_definition(
                        self.start + self.option_argument_position)
                    if option and option[1].argument:
                        return (
                            '<div class="command_help">' + option[1].argument
                            + " : "
                            + self.option_canon[self.option_argument_position:]
                            + '</div>')
                    return ''
        if self.is_an_option_argument:
            return ('<div class="command_help">Argument de '
                    + self.is_an_option_argument + '</div>')
        place = str(self.argument_position)
        if place in definition and len(definition[place]):
            text = definition[place]
        elif (len(definition['$'])
              and self.argument_position == self.parent.nr_argument):
            text = definition["$"]
        elif len(definition["*"]):
            text = definition["*"]
        else:
            if definition["unknown"]:
                text = ('<div class="command_help_error">'
                        + definition["unknown"] + '</div>')
            else:
                return ''
        return '<div class="command_help">' + text + '</div>'
    def option_definition(self, position=None):
        command = self.parent.command
        if not command:
            return
        definition = commands[command]
        if not definition['options']:
            return
        options = definition['options']
        value = self.text_content()
        if (len(value) > 2
            and value[0] == '-' and value[1] != "-" and position is not None):
            # Single letter option: take the good one
            value = "-" + value[position - self.start - 1]
        return options.get_option(value)
    def parse_option(self):
        self.is_an_option = False
        self.option_argument_help = ''
        self.option_argument_after = False
        c = self.text_content()
        self.option_argument_position = len(c)
        if len(c) <= 1 or c[0] != '-':
            return
        self.concatenable_right = True
        self.concatenable_left = True
        self.is_an_option = True
        self.option_canon = c
        if not self.parent.command:
            return
        definition = commands[self.parent.command]
        if not definition['options']:
            return
        options = definition['options']
        if c[1] == "-":
            d = c.split("=")[0]
            self.option_argument_position = len(d)
            if d in options.long_opt:
                option = options.long_opt[d]
                if option.argument:
                    self.option_argument_help = d + ' : ' + option.argument
                    self.option_canon = option.short
                    if d == c:
                        self.option_argument_after = True
                    else:
                        self.option_canon += c[self.option_argument_position+1:]
                        self.concatenable_right = False
                else:
                    self.option_canon = option.short
            else:
                self.concatenable_right = False
                self.concatenable_left = False
            return
        opts = []
        for i, letter in enumerate(c[1:]):
            opts.append(letter)
            if ('-' + letter) not in options.short_opt:
                continue
            option = options.short_opt['-' + letter]
            if option and option.argument:
                self.option_argument_help = ('-' + option.short[1] + ' : '
                                             + option.argument)
                self.option_argument_position = i+2
                if len(c) == i+2:
                    self.option_argument_after = True
                else:
                    self.concatenable_right = False
                break
        opts.sort()
        self.option_canon = ('-' + ''.join(opts)
                             + c[self.option_argument_position:])
    def cleanup(self, replace_option):
        if not self.is_an_option or not replace_option:
            return Container.cleanup(self, replace_option)
        return "Argument(Normal('" + self.option_canon + "'))"

class Redirection(Container):
    def color(self):
        return ["#000", "#AFF"]
    def local_help(self, dummy_position):
        m = ''
        if self.content[1].content[0] == '>':
            m = " de la sortie "
        elif self.content[1].content[0] == '<':
            m = " de l'entrée "
        if (self.content[0].content == ""
            or self.content[0].content == "0"
            or self.content[0].content == "1"
        ):
            m += "standard"
        elif self.content[0].content[0] == "2":
            m += "d'erreur"
        else:
            m += "dont le fildes a le numéro " + self.content[0].content[0]
        return "C'est une redirection" +m+ ", pas un argument de la commande."
class SquareBracket(Container):
    def color(self):
        return ["#000", "#FAF"]
    def local_help(self, dummy_position):
        return "Les crochets indiquent que l'on veut un seul caractère de la liste"
class Group(Command):
    def local_help(self, dummy_position):
        return "Lance un nouveau processus"
class Replacement(Container):
    def color(self):
        return ["#000", "#CCF"]
    def is_a_pattern(self):
        return False
    def local_help(self, dummy_position):
        return ("Lance un nouveau processus pour évaluer le contenu. "
                + "Ces caractères sont remplacés par ce qui a été "
                + "écrit par le processus sur sa sortie standard."
                )
class ReplacementProtected(Container):
    pass
class File(Redirection):
    def local_help(self, dummy_position):
        return 'Le fichier dont le nom est : «' + self.html() + "»"

class InputStop(Redirection):
    def local_help(self, dummy_position):
        t = self.text()
        if len(t) > 2 and t[0] == "'" and t[-1] == "'":
            more = "Le texte est copié sans substitution des variables"
        else:
            more = "Mettez ce texte entre cote pour empêcher les substitutions de variable"
        return "Les lignes suivant cette commande sont lues jusqu'à trouver le texte «" + self.html() + "» seul sur une ligne. " + more

class Backgrounded(Line):
    def local_help(self, dummy_position):
        return 'Lancé en arrière plan'

class Conditionnal(Line):
    def local_help(self, dummy_position):
        return "Suite conditionnelle de commandes ou pipelines"

class Affectation(Container):
    def color(self):
        return ["#000", "#FFA"]
    def local_help(self, dummy_position):
        v = ''
        for content in self.content[2:]:
            v += content.html()
        return ('Enregistre «' + v + '» dans la variable : «'
                + self.content[0].html() + '»')

class ForLoop(Command):
    def local_help(self, dummy_position):
        return "Boucle en parcourant les valeurs indiquées"
        
class WhileLoop(Command):
    def local_help(self, dummy_position):
        return "Boucle tant que la commande s'exécute sans erreur"

class IfThenElse(Command):
    def local_help(self, dummy_position):
        return "IF"

class ThenBloc(Command):
    def local_help(self, dummy_position):
        return "Exécuté si la commande s'exécute sans erreur"

class ElseBloc(Command):
    def local_help(self, dummy_position):
        return "Exécuté si la commande retourne une erreur"

class ForValues(Command):
    def local_help(self, dummy_position):
        return "Les valeurs que va prendre la variable"

class Body(Line):
    def local_help(self, dummy_position):
        if isinstance(self.content[-1], Done):
            return "Les commandes qui sont répétées"
        else:
            return "Terminer le bloc de commande avec le mot-clef «done»"

class LoopVariable(Command):
    def local_help(self, dummy_position):
        return "Nom de la variable qui va changer de valeur"


##############################################################################
##############################################################################
##############################################################################

class Parser:
    def __init__(self, text):
        if not isinstance(text, str):
            try:
                text = text.encode("utf-8")
            except:
                pass
        self.text = text
        self.len = len(self.text)
        self.in_back_cote = False
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

    def add_to_conditionnal(self, parsed, operator):
        self.next()
        if parsed.empty():
            parsed.append(Unterminated(operator))
        else:
            if (len(parsed.content) >= 1
                and isinstance(parsed.content[-1], Conditionnal)):
                b = parsed.content[-1]
            else:
                b = Conditionnal()
                b.append(parsed.content.pop())
                parsed.append(b)
            op = operator + self.skip(" \t")
            if operator == '&&':
                op = And(op)
            else:
                op = Or(op)
            b.append(op)
        
    def parse(self, init=True):
        if init:
            self.i = 0
        parsed = Line()
        while not self.empty():
            if self.get() == ')':
                if init:
                    parsed.append(Unexpected(")"))
                break
            pipeline = self.parse_pipeline(init)
            if not parsed.empty() and isinstance(parsed.content[-1],
                                                 Conditionnal):
                parsed.content[-1].append(pipeline)
            else:
                parsed.append(pipeline)
            if isinstance(pipeline.content[-1], Done):
                break
            if self.empty():
                break
            if self.get() == '`' and self.in_back_cote:
                break
            if self.get() == ';':
                self.next()
                parsed.append(DotComa(";" + self.skip(" \t")))
                if self.empty():
                    break
            if self.get() == '|':
                self.next()
                if self.get() != '|':
                    bug
                self.add_to_conditionnal(parsed, '||')
                if self.empty():
                    break
            if self.get() == '&':
                self.next()
                if not self.empty() and self.get() == '&':
                    self.add_to_conditionnal(parsed, '&&')
                else:
                    if parsed.empty():
                        parsed.append(Unterminated("&"))
                    else:
                        b = Backgrounded()
                        b.append(parsed.content.pop())
                        b.append(Background("&" + self.skip(" \t")))
                        parsed.append(b)
        if init:
            parsed.parent = None
            parsed.raise_comment()
            parsed.remove_empty()
            parsed.merge_separator()
            parsed.replace_empty()
            parsed.raise_separator()
            parsed.merge_separator()
            parsed.raise_separator()
            parsed.merge_separator()
            parsed.replace_unexpected()
            parsed.init_position()
            parsed.check_options()
        return parsed
    def parse_pipeline(self, init):
        parsed = Pipeline()
        while not self.empty():
            if self.get() == '(':
                parsed.append(self.parse_group())
            else:
                parsed.append(self.parse_command())
                if isinstance(parsed.content[-1], Done):
                    break
            if self.empty():
                break
            if self.get() in pipeline_stopper:
                break
            if self.get() == '`' and self.in_back_cote:
                break
            if self.get() == '|':
                self.next()
                if not self.empty() and self.get() == '|':
                    self.i -= 1
                    break
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

    def error_if_empty(self, error=''):
        if error != '':
            return error
        if self.empty():
            return 'Fin prématurée de la commande'
        return ''

    def parse_test(self, parsed):
        error = self.error_if_empty()
        if error == '':
            parsed.append(self.parse_command())
            if (len(parsed.content[-1].content)
                and self.empty()
                and name(parsed.content[-1]) == 'Command'
                and name(parsed.content[-1].content[-1]) == 'Separator'):
                parsed.content[-1].content[-1] = Unterminated(
                    parsed.content[-1].content[-1].content,
                    "Terminez par un point-virgule")
        else:
            parsed.content[0] = Unterminated(parsed.content[0].content,
                                             "Indiquez une commande")
            error = "Indiquez une commande"
        error = self.parse_end_of_command(error, parsed)
        return self.error_if_empty(error)

    def parse_keyword(self, error, parsed, keyword):
        error = self.error_if_empty(error)
        if error == '':
            self.read_separator(parsed)
            if self.empty():
                parsed.content[-1] = Unterminated(
                    parsed.content[-1].content,
                    "Mettre le mot-clef «" + keyword + "»")
                error = "Il manque le mot clef «" + keyword + "»"
            
        error = self.error_if_empty(error)
        if error == '':
            v = self.parse_argument()
            if v.text() == keyword:
                v = keyword + self.skip(' \t')
                if keyword == 'in':
                    v = In(v)
                elif keyword == 'then':
                    vv = ThenBloc()
                    vv.append(Then(v))
                    v = vv
                elif keyword == 'do':
                    v = Do(v)
                elif keyword == 'done':
                    v = Done(v)
                elif keyword == 'else':
                    v = Else(v)
                elif keyword == 'fi':
                    v = Fi(v)
                parsed.append(v)
            else:
                parsed.append(
                    Unexpected(v.text() + self.skip(' \t'),
                               'Il manque le mot-clef «' + keyword + '»'))
                error = 'Il manque le mot-clef «' + keyword + '»'
        return self.error_if_empty(error)
        
    def parse_if(self):
        parsed = IfThenElse()
        parsed.append(If('if' + self.skip(" \t")))
        error = self.parse_test(parsed)
        error = self.parse_keyword(error, parsed.content, "then")
        if error == '':
            err = self.parse_until(parsed.content[-1], ['fi','else'], True)
            if err == 'fi':
                parsed.append(Fi(err))
            elif err == 'else':
                else_block = ElseBloc()
                parsed.append(else_block)
                else_block.append(Else(err))
                err = self.parse_until(else_block, ['fi'], True)
                if err == 'fi':
                    parsed.append(Fi(err))
                else:
                    error = "Le bloc «else» " + str(err)
            else:
                error = "Le bloc «then» " + str(err)
        return self.parse_after_end_of_bloc(parsed, error, 'fi')

    def parse_while(self):
        parsed = WhileLoop()
        parsed.append(While('while' + self.skip(" \t")))
        return self.parse_do_done(self.parse_test(parsed), parsed)

    def parse_for(self):
        parsed = ForLoop()
        parsed.append(For('for' + self.skip(" \t")))
        error = self.error_if_empty()
        if error == '':
            v = LoopVariable()
            v.append(self.parse_argument())
            parsed.append(v)
        else:
            parsed.content[0] = Unterminated(parsed.content[0].content,
                                             "Indiquez le nom de la variable")
            error = "Il manque le nom de la variable"
            error = ""
        error = self.parse_keyword(error, parsed, "in")
        if error == '':
            v = ForValues()
            parsed.append(v)
            while not self.empty():
                if self.get() in list_stopper:
                    break
                v.append(self.parse_argument())
                if not self.empty():
                    self.read_separator(v)
            if (len(v.content)
                and self.empty()
                and name(v.content[-1]) == 'Separator'):
                v.content[-1] = Unterminated(
                    v.content[-1].content,
                    "Ajoutez un point-virgule pour finir la liste")
                error =  'Il manque un point virgule pour finir la liste'
        error = self.error_if_empty(error)
        error = self.parse_end_of_command(error, parsed)
        return self.parse_do_done(error, parsed)

    def parse_end_of_command(self, error, parsed):
        error = self.error_if_empty(error)
        if error == '':
            if self.get() == ';':
                self.next()
                parsed.append(EndOfValues(';'))
                if not self.empty():
                    self.read_separator(parsed)
            else:
                parsed.append(Unexpected(self.get()))
                error = "Il manque le point virgule"
                self.next()
        return self.error_if_empty(error)

    def parse_until(self, parsed, keywords, return_keyword=False):
        for content in self.parse(0).content:
            parsed.append(content)
        if (
                (
                    len(parsed.content) > 3
                    and parsed.content[-2].text().strip() == ';'
                    and parsed.content[1].text() != ''
                    or
                    isinstance(parsed.content[-2], Backgrounded)
                    and parsed.content[-2].text()[0] != '&'
                )
                and
                parsed.content[-1].text() in keywords
        ):
            if return_keyword:
                return parsed.content.pop().text()
            else:
                parsed.content[-1] = parsed.content[-1].content[0]
        else:
            if len(parsed.content) > 3:
                return " est incomplet, il faut le compléter par " + choices(keywords)
            else:
                return " est vide, il faut indiquer des commandes"
        return ''

    def parse_after_end_of_bloc(self, parsed, error, keyword):
        if error == '':
            while (not self.empty()
                   and (not self.read_separator(parsed)
                        or not self.read_redirection(parsed))):
                pass
        if error != '' and not isinstance(parsed.content[0], Unterminated):
            parsed.content[0] = Unterminated(parsed.content[0].content, error)
        c = ''
        while (not self.empty()
               and self.get() not in list_stopper
               and self.get() not in redirection_stopper):
            c += self.get()
            self.next()
        if c != '':
            parsed.append(Unexpected(
                c,
                "Rien d'autorisé après le «" + keyword + "». "
                + "Il faut mettre un séparateur ou une redirection"))
        return parsed

    def parse_do_done(self, error, parsed):
        error = self.parse_keyword(error, parsed, "do")
        if error == '':
            do_key = parsed.content.pop()
            b = Body()
            b.append(do_key)
            parsed.append(b)
            err = self.parse_until(b, ['done'])
            if err != '':
                error = "Le «do»...«done»" + err
        return self.parse_after_end_of_bloc(parsed, error, 'done')

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
                if self.get() == '`' and self.in_back_cote:
                    return parsed
                while not self.empty() and self.get() in '(':
                    parsed.append(Unexpected("("))
                    self.next()
            if not self.empty():
                before_command = parsed.number_of(Argument)==0
                parsed.append(self.parse_argument(parse_equal = before_command))
                if parsed.number_of(Argument) == 1:
                    text = parsed.content[-1].text()
                    if text == 'for':
                        parsed.content.pop()
                        parsed.append(self.parse_for())
                        return parsed
                    if text == 'while':
                        parsed.content.pop()
                        parsed.append(self.parse_while())
                        return parsed
                    if text == 'if':
                        parsed.content.pop()
                        parsed.append(self.parse_if())
                        return parsed
                    if text in ['case', '{']:
                        return Unexpected(
                            text,
                            "L'analyse de ce mot clef n'a pas encore été faite"
                            + " dans ce logiciel. "
                            + "Vous n'aurez aucune indication")
                    if text in ['else', 'fi', 'done', 'do']:
                        if len(parsed.content) != 1:
                            text = parsed.content[0].text() + text
                        return Done(text)
        return parsed
    def read_separator(self, parsed):
        c = self.get()
        if c not in ' \t':
            return True
        parsed.append(Separator(self.skip(" \t")))
    def read_redirection(self, parsed):
        i = self.i
        fildes = self.skip(digit)
        if self.empty():
            self.i = i
            return True
        c = self.get()
        if c not in '<>':
            self.i = i
            return True
        self.next()
        if not self.empty() and self.get() == c:
            c += c
            self.next()
        while not self.empty() and self.get() in ' \t#':
            c += self.get()
            self.next()
        if self.empty() or self.get() in redirection_stopper:
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
            if self.get() in redirection_stopper:
                redirection.content[1] = Unterminated(c)
                redirection.append(Unterminated(''))
            else:
                if c != '<<':
                    f = File()
                else:
                    f = InputStop()
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
            elif c in special_variables or c in digit:
                parsed.append(Variable('$' + c))
                self.next()
            elif c == '{':
                v = ""
                while not self.empty():
                    c = self.get()
                    v += c
                    self.next()
                    if c == '}':
                        break
                if v[-1] != '}':
                    parsed.append(Unterminated('$' + v))
                else:
                    parsed.append(Variable('$' + v))
            elif c == '(':
                r = Replacement()
                for content in self.parse_group(False).content:
                    r.append(content)
                r.content[0].content = '$' + r.content[0].content
                parsed.append(r)
            else:
                parsed.append(Normal('$')) # Assume its signification disapear
    def read_replacement(self, parsed):
        if self.get() != '`':
            return True
        self.next()
        if self.empty():
            parsed.append(Unterminated("`"))
            return
        r = Replacement()
        r.append(GroupStart("`" + self.skip(" \t")))
        self.in_back_cote = True
        for content in self.parse(0).content:
            r.append(content)
        self.in_back_cote = False
        if self.empty() or self.get() != '`':
            r.content[0] = Unterminated(r.content[0].content)
        else:
            self.next()
            r.append(GroupStop("`" + self.skip(" \t")))
        parsed.append(r)

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
                    and self.read_dollar(parsed)
                    and self.read_replacement(parsed)):
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
        if name(parsed.content[0]) != 'Normal':
            return True
        self.next()
        a = Affectation()
        a.append(parsed.content.pop())
        a.append(Equal("="))
        for content in self.parse_argument().content:
            a.append(content)
        parsed.append(a)
    def read_home(self, parsed):
        if len(parsed.content) != 0  or  self.get() != '~':
            return True
        self.next()
        n = self.skip(names)
        if self.empty() or self.get() == '/':
            parsed.append(Home("~" + n))
        else:
            parsed.append(Unterminated("~" + n))
    def parse_argument(self, parse_equal=True):
        parsed = Argument()
        while not self.empty():
            c = self.get()
            if c in argument_stopper:
                break
            if c == '`' and self.in_back_cote:
                break
            if (self.read_backslash(parsed)
                and self.read_dollar(parsed)
                and self.read_quote(parsed)
                and self.read_guillemet(parsed)
                and self.read_pattern(parsed)
                and self.read_replacement(parsed)
                and self.read_home(parsed)
                ):
                if not parse_equal or self.read_equal(parsed):
                    parsed.append(Normal(c))
                    self.next()
        if not parsed.empty() and isinstance(parsed.content[0], Affectation):
            return parsed.content[0]
        return parsed
