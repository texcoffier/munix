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
logins= names + '-.'

il_est_plus_court = """Il est plus court de taper <tt>a</tt>
plutôt que <tt>[a]</tt>.<br>
Il est plus court de taper <tt>\\*</tt>
plutôt que <tt>[*]</tt>."""

def name(obj):
    try:
        return obj.__class__.__name__
    except:
        return obj.__proto__.constructor.name

def pad(x):
    return "                                                         "[:x]

def protect(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

try:
    slashslash = RegExp("\\\\", "g")
    quote = RegExp("'", "g")
except:
    slashslash = "\\"
    quote = "'"

def string(t):
    return "'" + t.replace(slashslash, "\\\\").replace(quote, "\\'") + "'"

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
    def __init__(self, option, short, message, argument=False, display=True,
                 cleanup=False):
        self.option   = option   # long option as --verbose
        self.short    = short    # short option as -v
        self.message  = message  # HTML Explanation about the option
        self.argument = argument # This option need an argument
        self.display  = display  # on the HTML help page
        self.cleanup  = cleanup  # remove this option when doing the cleanup

class Options:
    def __init__(self, *options):
        self.options = options
        self.long_opt = {}
        self.single_letter_option = True
        for option in options:
            self.long_opt[option.option] = option
            if len(option.option) > 2 and option.option[1] != '-':
                self.single_letter_option = False # kill, find
        self.short_opt = {}
        for option in options:
            if option.short != '':
                if not self.single_letter_option:
                    it_is_no_possible
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
    
list_stopper = '&<>;|()\n'
redirection_stopper = '#<>;|()\n'
argument_stopper = ' \t' + list_stopper
pipeline_stopper = ';)&\n'

##############################################################################
##############################################################################
##############################################################################

class ArgumentGroup:
    pass # To turn around a RapydScript bug
class Char:
    pass # To turn around a RapydScript bug

def nothing(txt):
    return txt

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
        "options": None,
        "cleanup": nothing, # sleep 1m => sleep 60
        "analyse": nothing,  # see 'define_test'
        "color": ["#000", "#CFC"]
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

def define_read():
    d = define_builtin()
    d['name'] = 'read'
    d['description'] = "Lecture d'une ligne de l'entrée standard"
    d['message'] = "La ligne est stockée dans les variables indiquées"
    d['syntax'] = "read TITI TATA TOTO"
    d['*'] = "Nom de la variable où stocker le n<sup>ème</sup> mot"
    d['$'] = "Nom de la variable où stocker le reste de la ligne"
    d['options'] = Options(
        Option('', '-r', "(r=raw) traite les <tt>\\</tt> comme des caractères normaux.",
               False, False, True)
    )
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
    d['1'] = "Nom du premier fichier/répertoire à copier ailleurs"
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
    d['message'] = "Si aucun nom de fichier n'est donné c'est un filtre"
    d['syntax'] = "less <var>fichier1</var> <var>fichier2</var>"
    return d

def define_man():
    d = define_command()
    d['name'] = 'man'
    d['description'] = "(<b>man</b>uel) affiche la documentation"
    d['syntax'] = "man commande"
    d['1'] = "Nom de la commande à expliquer"
    d['min_arg'] = 0
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

def define_date():
    d = define_command()
    d['name'] = 'date'
    d['description'] = "affiche la date et l'heure actuelle"
    d['syntax'] = "date"
    d['options'] = Options(
        Option('--date', '-d', "Indique la date à afficher",
               "Par exemple : 2004-02-29 ou @451642800")
    )
    return d

def define_df():
    d = define_command()
    d['name'] = 'df'
    d['description'] = "(<em><b>d</b>isk <b>f</b>ree</em>) affiche les systèmes de fichier"
    d["message"] = "On peut indiquer un nom de répertoire pour ne pas tout afficher"
    d['options'] = Options(
        Option('--human-readable', '-h', "Tailles lisibles pour un humain")
    )
    return d

def define_sort():
    d = define_command()
    d['name'] = 'sort'
    d['description'] = "affiche les lignes des fichiers en les triant"
    d['options'] = Options(
        Option('--numeric-sort', '-n', "Pour trier des nombres")
    )
    return d

def define_wc():
    d = define_command()
    d['name'] = 'wc'
    d['description'] = "(<em><b>w</b>ord <b>c</b>ount</b></em>) affiche le nombre de lignes/mots/octets des fichiers"
    d['*'] = "Analyse ce fichier"
    d['options'] = Options(
        Option('--lines', '-l', "Affiche seulement le nombre de lignes"),
        Option('--words', '-w', "Affiche seulement le nombre de mots"),
        Option('--bytes', '-c', "Affiche seulement le nombre d'octets", False),
        Option('--chars', '-m', "Affiche seulement le nombre de caractères", False)
    )
    return d

def define_uniq():
    d = define_command()
    d['name'] = 'uniq'
    d['description'] = "affiche les fichiers en éliminant les lignes identiques"
    d['message'] = "Il faut qu'elles soient cote à cote."
    d['*'] = "Affiche ce fichier"
    return d

def define_gzip():
    d = define_command()
    d['name'] = 'gzip'
    d['description'] = "(<em>GNU zip</em>) comprime des fichiers"
    d['*'] = "Comprime ce fichier"
    d['options'] = Options(
        Option('--recursive', '-r', "Comprime les fichiers d'une hiérarchie"),
        Option('--verbose', '-v', "Affiche ce qui est fait"),
        Option('--best', '-9', "Comprime un maximum", False, False),
        Option('--fast', '-1', "Comprime le plus rapidement", False, False)
    )
    return d

def define_gunzip():
    d = define_command()
    d['name'] = 'gunzip'
    d['description'] = "(<em>GNU unzip</em>) décomprime des fichiers"
    d['*'] = "Décomprime ce fichier"
    d['options'] = Options(
        Option('--recursive', '-r', "Décomprime les fichiers d'une hiérarchie"),
        Option('--verbose', '-v', "Affiche ce qui est fait")
    )
    return d

def define_zcat():
    d = define_command()
    d['name'] = 'zcat'
    d['description'] = "affiche les fichiers en les décomprimant"
    d['message'] = "Elle n'écrit ni ne modifie rien sur le disque"
    d['*'] = "Affiche ce fichier"
    return d

def replace_minutes(txt):
    t = txt.split("'")
    for i, mot in enumerate(t):
        if mot and mot[-1] == "m":
            try:
                minutes = int(mot[:-1])
                t[i] = str(minutes * 60)
                return "'".join(t)
            except ValueError:
                pass
    return txt

def define_sleep():
    d = define_command()
    d['name'] = 'sleep'
    d['description'] = "attend le nombre de secondes indiqué"
    d['message'] = "Arrêtez-la en tapant <tt>Ctrl+C</tt>"
    d['1'] = "Nombre de secondes à attendre"
    d['cleanup'] = replace_minutes
    return d

def analyse_tar(command):
    (position, dummy_t, dummy_v) = get_argument(command, 0)
    (position, t, v) = get_argument(command, position)
    if t and len(t) > 0 and t[0] != '-':
        v.make_comment("""Bien que la commande accepte les options sans tiret,
        c'est une très mauvaise pratique et votre réponse sera refusée.""",
                       "#F00")
    return command

def define_tar():
    d = define_command()
    d['name'] = 'tar'
    d['description'] = "(<em><b>t</b>ape <b>a</b>archiving</em>) manipulation d'archive"
    d['message'] = "La syntaxe dépend des options indiquées"
    d['options'] = Options(
        Option('--extract', '-x', "1 fichier &#8594; hiérarchie"),
        Option('--create', '-c', "Hiérarchie &#8594; 1 fichier"),
        Option('--file', '-f', "Pour choisir le nom de l'archive",
               "Le nom de l'archive générée ou lue", True),
        Option('--verbose', '-v', "Mode verbeux", False, False, True)
        )
    d['analyse'] = analyse_tar
    return d

def define_echo():
    d = define_builtin()
    d['name'] = 'echo'
    d['description'] = "affiche ses arguments"
    d['message'] = "Elle affiche un espace entre chaque argument"
    d['syntax'] = "echo arg1 arg2 arg3..."
    return d

def get_argument(command, position):
    """Returns : position, argument or None"""
    while position < len(command.content):
        v = command.content[position]
        position += 1
        if isinstance(v, Argument):
            return (position, v.text_content(), v)
    return (position, None, None)        

def merge_into(command, begin, end, node, comment):
    node.content = []
    node.message = comment
    t = []
    for i, n in enumerate(command.content):
        if begin <= i < end:
            node.content.append(n)
            if i == begin:
                t.append(node)
        else:
            t.append(n)
    command.content = t
    return begin + 1

test_operators = {
    '=': ["=", False],
    '!=': ["&ne;", False],
    '-eq': ["=", True],
    '-ne': ["&ne;", True],
    '-gt': ["&gt;", True],
    '-ge': ["&ge;", True],
    '-lt': ["&lt;", True],
    '-le': ["&le;", True],
   }

def need_operator(command, v):
    s = []
    for i in test_operators:
        s.append(i)
    s.sort()
    v.make_comment('Ici on attend un opérateur : ' + ' '.join(s), "#F00")
    command.fail = True

def parse_test(command, position, allow_bool=True):
    (position, t, v) = get_argument(command, position)
    old_position = position - 1
    if v is None:
        command.fail = "empty"
        return position
    if t == "!":
        v.make_comment("Négation de l'expression qui suit", "#080")
        position = parse_test(command, position, allow_bool=False)
        position = merge_into(command, old_position, position,
                              ArgumentGroup(),
                              "Négation booléenne")
    elif t == '(':
        v.make_comment(foreground="#080")
        position = parse_test(command, position)
        (position, t2, v2) = get_argument(command, position)
        if v2 is None:
            v.make_comment("Il manque la parenthèse fermante", "#F00")
            command.fail = True
            return position
        if t2 != ')':
            v2.make_comment("Il devrait y avoir une parenthèse fermante",
                            "#F00")
        else:
            v.make_comment(foreground="#080")
            position = merge_into(command, old_position, position,
                                  ArgumentGroup(),
                                  "Regroupe ces opérations")
    elif t in ('-e', '-d'):
        v.make_comment(
           {
               '-e': "Vrai si le chemin pointe sur une entité qui existe",
               '-d': "Vrai si le chemin suivant pointe sur un répertoire"
           }[t], "#080")
        (position, t2, v2) = get_argument(command, position)
        if v2 is None:
            v.make_comment(foreground="#F00")
            command.content[position-1].message = "Indiquez le chemin"
            command.fail = True
            return position
        else:
            m = {
               '-e': "une entité qui existe",
               '-d': "un répertoire"
            }[t]
            v2.make_comment("Le chemin testé")
            position = merge_into(command, old_position, position,
                                  ArgumentGroup(),
                                  "Vrai si «" + v2.html()
                                  + '» est ' + m)
    else:
        (position, t2, v2) = get_argument(command, position)
        if v2 is None:
            command.fail = True
            return position
        if t2 in test_operators:
            (position, t3, v3) = get_argument(command, position)
            if v3 is None:
                v2.make_comment("Il manque la valeur de droite", "#F00")
                if isinstance(command.content[position-1], Unterminated):
                    command.content[position-1].message = "Argument de droite"
                command.fail = True
                return position
            else:
                if test_operators[t2][1]:
                    v2.make_comment("Comparaison d'entiers", "#080")
                else:
                    v2.make_comment("Comparaison de chaînes de caractères",
                                    "#080")
                position = merge_into(command, old_position, position,
                                      ArgumentGroup(),
                                      "Test si "
                                      + "«" + v.html() + "»"
                                      + " " + test_operators[t2][0] + " "
                                      + "«" + v3.html() + "»")
        else:
            need_operator(command, v2)
            return position

    if not allow_bool:
        return position

    (position, t, v) = get_argument(command, position)

    for operator, humain, allow_bool2 in [
            ['-a', 'ET', False],
            ['-o', 'OU', 'allow-and']
            ]:
        if v is None:
            return position
        while t == operator:
            v.make_comment(
                "'" + humain + "' booléen entre ce qui est à gauche et à droite",
                "#080")
            save_position = position
            position = parse_test(command, position, allow_bool=allow_bool2)
            if (save_position+1 == position
                and isinstance(command.content[position-1], Unterminated)):
                command.content[position-1].message = "Indiquez une expression"
                command.fail = True
            (position, t, v) = get_argument(command, position)
            if t != operator:
                position = merge_into(command, old_position, position-1,
                                      ArgumentGroup(), humain + " booléen") +1
        if allow_bool == 'allow-and':
            return position-1

    if t in (']', ')'):
        return position-1

    if v:
        command.fail = True
        v.make_comment("Ici on devrait trouver '-o' ou '-a'", "#F00")
    return position
            

def analyse_test(command):
    command.fail = False
    (position1, t1, v1) = get_argument(command, 0)
    position = parse_test(command, position1)
    (position, t, v) = get_argument(command, position)
    if t1 == '[':
        if v is None:
            if command.nr_argument == 0:
                v1.make_comment("Tapez un espace puis la condition", "#F00")
            else:
                v1.make_comment("Manque le ']' final", "#F00")
            last = command.content[position-1]
            space = (isinstance(last, Separator)
                     or isinstance(last, Unterminated))
            if space and command.nr_argument >= 1 and command.fail == False:
                last.message = "Vous pouvez terminer le test avec un ']'"
            elif space and command.nr_argument == 0 and command.fail != True:
                last.message = "Indiquez la condition à tester"
            elif space and command.nr_argument == 1:
                last.message = "Continuez la condition"
            # else: last.message = name(last) + str(command.nr_argument)
        else:
            v1.make_comment(foreground="#080")
            if t != ']':
                v.make_comment("Cela devrait être un ']'", "#F00")
            else:
                v.make_comment(foreground="#080")
            (position, t, v) = get_argument(command, position)
            
    while v:
        v.make_comment("Arguments en trop", "#F00")
        (position, t, v) = get_argument(command, position)
    return command

def define_test():
    d = define_command()
    d['name'] = 'test'
    d['description'] = "Evaluateur de condition"
    d['message'] = "La commande termine sans erreur si la condition est vraie"
    d['analyse'] = analyse_test
    return d

final_bracket = "Argument(Normal(']')))"
def remove_brackets(txt):
    txt = txt.replace("Normal('[')", "Normal('test')", 1)
    if txt[-len(final_bracket):] == final_bracket:
        txt = txt[:-len(final_bracket)] + ')'
    return txt

def define_test_bracket():
    d = define_test()
    d['name'] = '['
    d['cleanup'] = remove_brackets
    return d

def analyse_grep(command):
    (position, dummy_t, dummy_v) = get_argument(command, 0)
    state = "start"
    is_a_filter = True
    regexp = "normal"
    while True:
        (position, t, v) = get_argument(command, position)
        if v is None:
            break
        if len(t) > 0 and t[0] == '-' and state != "regexp":
            if state == "only-filename":
                v.make_comment("Les options doivent être en début de commande",
                               "#F00")
                continue
            if t == '-v':
                continue
            t = t.replace('-v', '-')
            if t == '-e':
                state = "regexp"
                continue
            if t == '-E':
                regexp = "extended"
                continue
            if t == '-F':
                regexp = "fast"
                continue
            v.make_comment("Option non prévue par ce logiciel", "#F00")
            continue

        if state == "start" or state == "regexp":
            c = v.cleanup(replace_option=False)
            if v.first_of(Pattern):
                v.make_comment("""Attention le shell va remplacer
                le <em>pattern</em> et donc la commande <tt>grep</tt>
                ne verra pas l'expression à chercher.""")
            elif 'Variable' in c:
                v.make_comment("""L'expression à chercher va dépendre
                du contenu de la variable.""")
            else:
                if regexp == 'normal':
                    v.message = "Expression régulière à rechercher"
                    command.content[position-1] = regexpparser_top(v, False)
                elif regexp == 'extended':
                    v.message = "Expression régulière étendue à rechercher"
                    command.content[position-1] = regexpparser_top(v, True)
                else:
                    v.message = "Texte à rechercher"
            if state == "start":
                state = "only-filename"
            else:
                state = "filename"
            continue
        if state == "filename" or state == "only-filename":
            v.make_comment("Chemin du fichier ou l'on cherche les lignes",
                           "#000")
            state = "only-filename"
            is_a_filter = False
            continue
        v.make_comment("Il y a un bug, prévenez l'enseignant", "#F00")
    if is_a_filter:
        command.make_comment("""Comme il n'y a pas de nom de fichier,
        <tt>grep</tt> cherche les lignes sur son entrée standard.""")
    return command

def define_grep():
    d = define_command()
    d['name'] = 'grep'
    d['description'] = "Affiche les lignes du fichier qui passent le crible."
    d['message'] = "Le «-e» est optionnel s'il y a une seule chaîne. Quand il y en a plusieurs, on cherche l'une des chaînes."
    d['analyse'] = analyse_grep
    d['syntax'] = "grep -e expreg1 -e expreg2 <var>file1</var> <var>file2</var>..."

    d['options'] = Options(
        Option('--extended-regexp', '-E',
               "Expressions régulières <b>étendues</b>."),
        Option('--fixed-strings', '-F',
               "Simple texte au lieu d'une exp. régulière."),
        Option('--regexp', '-e',
               "L'argument suivant est ce qu'il faut rechercher.", True),
        Option('--ignore-case', '-i',
               "Ne tient pas compte de la casse."),
        Option('--invert-match', '-v',
               "Les lignes ne passant pas le crible.")
        )
    return d

def analyse_sed(command):
    (position, dummy_t, dummy_v) = get_argument(command, 0)
    state = "start"
    is_a_filter = True
    regexp = "normal"
    in_place = False
    while True:
        (position, t, v) = get_argument(command, position)
        if v is None:
            break
        if len(t) > 0 and t[0] == '-' and state != "expression":
            if state == "only-filename":
                v.make_comment("Les options doivent être en début de commande",
                               "#F00")
                continue
            if t == '-e':
                state = "expression"
                continue
            if t == '-r':
                regexp = "extended"
                continue
            if t == '-i':
                in_place = True
                continue
            v.make_comment("Option non prévue par ce logiciel", "#F00")
            continue

        if state == "start" or state == "expression":
            c = v.cleanup(replace_option=False)
            if v.first_of(Pattern):
                v.make_comment("""Attention le shell va remplacer
                le <em>pattern</em> et donc la commande <tt>sed</tt>
                ne verra pas la transformation à faire.""")
            elif 'Variable' in c:
                v.make_comment("""La transformation va dépendre
                du contenu de la variable.""")
            else:
                v.message = "Transformation à effectuer sur les lignes"
                if regexp == 'extended':
                    v.message += " Expression régulière étendue"
                command.content[position-1] = sedparser_top(
                    v, regexp == "extended")
            if state == "start":
                state = "only-filename"
            else:
                state = "filename"
            continue
        if state == "filename" or state == "only-filename":
            v.make_comment("Chemin du fichier à traiter", "#000")
            state = "only-filename"
            is_a_filter = False
            continue
        v.make_comment("Il y a un bug, prévenez l'enseignant", "#F00")
    if is_a_filter:
        command.make_comment("""Comme il n'y a pas de nom de fichier,
        <tt>sed</tt> traite les lignes lues sur son entrée standard.""")
    return command

def define_sed():
    d = define_command()
    d['name'] = 'sed'
    d['description'] = "Transforme un flux de lignes de textes"
    d['message'] = ""
    d['analyse'] = analyse_sed
    d['syntax'] = "sed -e 's/expreg/texte/g' <var>f1</var> <var>f2</var>..."

    d['options'] = Options(
        Option('--regexp-extended', '-r',
               "Expressions régulières <b>étendues</b>."),
        Option('--expression', '-e',
               "L'argument suivant indique le traitement.", True),
        Option('--in-place', '-i',
               "Modifie les fichiers au lieu d'afficher le résultat.")
        )
    return d

def define_ps():
    d = define_command()
    d['name'] = 'ps'
    d['description'] = "Liste les processus"

    d['options'] = Options(
        Option('', '-e', "Tous les processus."),
        Option('', '-H', "Hiérarchie des processus."),
        Option('', '-f', "(<em>full</em>) Affiche plus d'informations.")
        )
    d['unknown'] = """La syntaxe UNIX BSD n'est pas acceptée,
    vous devez donc mettre un tiret devant les options."""
    return d

all_signals = [
    ['HUP' , 1, 'Hangup detected on controlling terminal'],
    ['INT' , 2, 'Interrupt from keyboard'],
    ['QUIT', 3, 'Quit from keyboard'],
    ['ILL' , 4, 'Illegal Instruction'],
    ['ABRT', 6, 'Abort signal from abort(3)'],
    ['FPE' , 8, 'Floating point exception'],
    ['KILL', 9, 'Kill signal'],
    ['SEGV',11, 'Invalid memory reference'],
    ['PIPE',13, 'Broken pipe: write to pipe with no readers'],
    ['ALRM',14, 'Timer signal from alarm(2)'],
    ['TERM',15, 'Termination signal']
]

def signal_to_numbers(txt):
    for name, number, message in all_signals:
        txt = txt.replace('Normal(SIG' + name + ')', str(number))
        txt = txt.replace('Normal(' + name + ')', str(number))
    return txt

def define_kill():
    d = define_command()
    d['name'] = 'kill'
    d['description'] = "Envoit un signal aux processus"
    d['*'] = "PID a qui envoyer le signal"
    d['syntax'] = "kill -SIGNAL PID1 PID2..."
    d['cleanup'] = signal_to_numbers
    options = []
    for name, number, message in all_signals:
        options.append(Option('-' + name, '', message, False, False))
        options.append(Option('-SIG' + name, '', message, False, False))
        options.append(Option('-' + str(number), '', message, False, False))
    d['options'] = Options(*options)
    return d


def define_manque_point_virgule(name):
    d = define_command()
    d['description'] = '<span class="command_help_error">N\'auriez-vous pas oublié un point-virgule avant ?</span>'
    d['name'] = name
    return d

def define_done (): return define_manque_point_virgule('done')
def define_for  (): return define_manque_point_virgule('for')
def define_while(): return define_manque_point_virgule('while')
def define_if   (): return define_manque_point_virgule('if')
def define_then (): return define_manque_point_virgule('then')
def define_else (): return define_manque_point_virgule('else')
def define_fi   (): return define_manque_point_virgule('fi')

def define_bash(name):
    d = define_command()
    d['description'] = "<span class=\"command_help_error\">C'est une commande 'bash'. Elle ne fonctionne pas en shell.</span>"
    d['name'] = name
    d["color"] = ["#F00", "#FCC"]
    d["builtin"] = None
    return d


command_aliases = {
    'more': 'less'
}

commands = {}
for x in [define_cd(), define_pwd(), define_ls(), define_cat(), define_cp(),
          define_mkdir(), define_rm(), define_ln(), define_less(),
          define_man(), define_tail(), define_du(), define_date(),
          define_df(), define_sort(), define_wc(), define_uniq(),
          define_gzip(), define_gunzip(), define_zcat(), define_sleep(),
          define_tar(), define_echo(),
          
          define_done(), define_for(),
          define_if(), define_then(), define_else(), define_fi(),
          define_read(), define_test(), define_test_bracket(),
          define_grep(), define_sed(),

          define_ps(), define_kill(),

          define_bash('[[')
]:
    if x['name'] in commands:
        print("duplicate_name: " + x['name'])
        exit(1)
        
    commands[x['name']] = x

def format_help(definition):
    return "help " + definition["name"]

def format_man(definition):
    return ('<a target="_blank" href="http://linux.die.net/man/' +
            definition["section"] + '/' + definition["name"]
            + '">man ' + definition["name"] + "</a>")

def valid_variable_name(name):
    if len(name) == 0:
        return False
    if name[0] not in alpha:
        return False
    for i in name:
        if i not in names:
            return False
    return True

##############################################################################
##############################################################################
##############################################################################

class Chars:
    hide = False
    foreground = "#000"
    background = "#FFF"
    begin_regexp = False
    def __init__(self, chars, message=""):
        self.content = chars
        self.message = message
    def color(self):
        return [self.foreground, self.background]
    def str(self):
        return name(self) + '(' + string(self.content) + ')'
    def nice(self, depth):
        return 'C' + pad(depth) + self.str() + '\n'
    def cleanup(self, replace_option):
        return name(self) + "(" + string(self.content) + ")"
    def html(self, position=-1):
        s = '<qdiv '
        if position != -1:
            s += 'id="P' + str(self.ident) + '" '
        return (s + 'class="Parsed ' + self.active(position) + name(self)
                + '" style="color:' + self.color()[0]
                + '">' + protect(self.content) + '</qdiv>')
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
                + '"><div>' + message + '</div></div>\n')
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
    def analyse(self):
        return self # To easely stop container recursion
    def make_comment(self, comment=None, foreground=None):
        pass # To easely stop container recursion
    def init_group_number(self, group_number):
        return group_number # To easely stop container recursion
        

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
class Home(Chars):
    def local_help(self, dummy_position):
        if self.content == '~':
            return "Le tilde représente votre répertoire de connexion"
        else:
            return ("C'est le répertoire de connexion de l'utilisateur «"
                    + self.content[1:] + '»')
    def color(self):
        return ["#F0F", "#FAF"]
            
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

class NewLine(Separator):
    def local_help(self, dummy_position):
        return "Le retour à la ligne permet de séparer les commandes."

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
class VariableName(Variable):
    def local_help(self, dummy_position):
        return "Nom de la variable"
class LoopVariable(VariableName):
    def local_help(self, dummy_position):
        return "Nom de la variable qui va changer de valeur dans la boucle"
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
            return """Vous pouvez taper une autre commande ou faire un pipeline.
            Si vous n'ajoutez rien derrière, votre réponse sera refusée
            car inutilement allongée."""
        if "&&" in self.content:
            return "Vous pouvez taper une autre commande ou faire un pipeline qui sera exécutée si la précédente se termine bien"
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
        return ["#999", "#FFF"]
    def itext(self, txt):
        if isinstance(self.parent, SquareBracket):
            txt += ".<br><b>Même le tiret dans ce contexte</b>"
        return "Le caractère «" + self.content + "» disparaît. " + txt
class Backslash(Invisible):
    def local_help(self, dummy_position):
        return self.itext("Il annule la signification du caractère suivant pour le shell.")
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
        # BASH
        # elif c == '&':
        #    s = "la sortie d'erreur et la sortie standard."
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
    def unsane(self):
        if not hasattr(self, 'parent'):
            return False
        p = self.parent.content
        return (len(p) == 3
                and self is p[1]
                and isinstance(p[2], SquareBracketStop)
        )
    def color(self):
        if self.unsane():
            return ["#F00", "#F88"]
        else:
            return Pattern.color(self)

    def local_help(self, dummy_position):
        if self.unsane():
            return il_est_plus_court
        else:
            return "Le caractère «" + self.content + "» est autorisé"
class SquareBracketInterval(Pattern):
    def color(self):
        return ["#808", "#D8D"]
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

class ReplacementProtected:
    pass # To turn around a RapydScript bug
class Argument:
    pass # To turn around a RapydScript bug

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
    def cleanup(self, replace_option, sort_content=False):
        protected = False
        content = []
        for c in self.content:
            n = name(c)
            if c.hide:
                if n == 'Guillemet':
                    protected = not protected
                continue
            if n == 'Variable':
                if protected or name(self) == 'Affectation':
                    c = VariableProtected(c.content)
            elif n == 'Replacement':
                if protected or name(self) == 'Affectation':
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
            if (getattr(c, 'is_an_option', False)
                and txt == "Argument(Normal('-'))"):
                # Once cleaned, there is no option remaining.
                # So the argument must be removed
                continue
            if name(c) == 'Argument':
                if first_argument:
                    first_argument = False
                    command = txt.replace(
                        "Argument(Normal('", "").replace("'))", "")
                    if command in command_aliases:
                        txt ="Argument(Normal('"+command_aliases[command]+"'))"
            clean.append(txt)
        if sort_content:
            clean.sort()
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
        s = '<qdiv '
        if position != -1:
            s += 'id="P' + str(self.ident) + '" '
        return (s + 'class="Parsed ' + self.active(position) + name(self)
                + '">' + ''.join([x.html(position)
                                  for x in self.content
                              ])
                + '</qdiv>')
    def init_position(self, i=0, ident=0):
        self.start = i
        for content in self.content:
            content.parent = self
            content.init_position(i, ident)
            i = content.end
            ident = content.ident + 1
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
        h += '\n'
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
    def last_of(self, classe):
        for x in self.content[::-1]:
            if isinstance(x, classe):
                return x
    def all_of(self, classe):
        return [x
                for x in self.content
                if isinstance(x, classe)
        ]
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
    def analyse(self):
        self.content = [i.analyse()
                        for i in self.content
        ]
        return self
    def make_comment(self, comment=None):
        self.message = comment

    def init_group_number(self, group_number):
        if isinstance(self, RegExpGroup):
            self.group_number = group_number
            self.get_groups().append(self)
            group_number += 1
        for c in self.content:
            group_number = c.init_group_number(group_number)
        return group_number

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
    message = None
    def color(self):
        #if getattr(self, "command", None):
        #    return commands[self.command]["color"]
        return ["#000", "#CFC"]
    def local_help(self, position):
        if self.message:
            return self.message + self.contextual_help(position)
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
                        def color():
                            return commands[command]['color']
                        content.content[0].color = color
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
        self.nr_argument = arg_number - 1 # Real one, not option argument
    def contextual_help(self, dummy_position):
        if not self.command:
            return ''
        definition = commands[self.command]
        s = ['<div class="command_help">',
             '<b>' + self.command + '</b> : ' + definition["description"]]
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
        if definition["builtin"] == True:
            h = format_help(definition)
        elif definition["builtin"] == False:
            h = format_man(definition)
        else:
            h = None
        if h:
            s.append("Aide : <tt>" + h + "</tt><br>")
        if self.nr_argument < definition["min_arg"]:
            s.append('<span class="command_help_error">'
                     + 'Votre commande manque d\'argument !</span><br>')
        s.append('</div>')
        return '\n'.join(s)

    def cleanup(self, replace_option):
        s = Container.cleanup(self, replace_option)
        if not self.command:
            return s
        return commands[self.command]["cleanup"](s)

    def analyse(self):
        self = Container.analyse(self)
        if self.command:
            definition = commands[self.command]
            if definition:
                return definition['analyse'](self)
        return self

class Argument(Container):
    message = None
    def color(self):
        return ["#000", "#FFA"]
    def append(self, item):
        if (len(self.content) != 0
            and name(self.content[-1]) == name(item)
            and not isinstance(item, Variable)
            and not isinstance(item, SquareBracket)
            and not isinstance(item, Invisible)
            ):
            self.content[-1].content += item.content
        else:
            self.content.append(item)
    def nice(self, depth=0):
        return 'A' + pad(depth) + ' '.join([x.str() for x in self.content])+'\n'
    def local_help(self, position):
        if isinstance(self.parent, ArgumentGroup):
            return ''
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
                if self.message is None:
                    return ''
                text = self.message
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
            and options.single_letter_option
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
        # if definition['analyse'] != nothing:
        #    return
        if not definition['options']:
            return
        options = definition['options']
        d = c.split("=")[0]
        if c[1] == "-" or not options.single_letter_option:
            self.option_argument_position = len(d)
            if d in options.long_opt:
                option = options.long_opt[d]
                if option.argument:
                    self.option_argument_help = d + ' : ' + option.message
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
            if option.cleanup:
                opts.pop()
                continue
            if option and option.argument:
                self.option_argument_help = ('-' + option.short[1] + ' : '
                                             + option.message)
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

    def make_comment(self, comment=None, foreground=None):
        for i in self.content:
            if name(i) != 'Normal':
                continue
            if comment:
                i.message = comment
            if foreground:
                i.foreground = foreground
        
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
    def cleanup(self, replace_option=None):
        # The char order is not important
        return Container.cleanup(self, replace_option, True)

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

class ArgumentGroup(Argument):
    is_an_option = False
    command = False
    def local_help(self, dummy_position):
        return self.message + '\n'


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
            if self.get() == '\n':
                self.next()
                parsed.append(NewLine("\n" + self.skip(" \t\n")))
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
            parsed.analyse()
            parsed.init_position()
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
                parsed.append(Pipe("|" + self.skip(" \t\n")))
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
            return 'Commande incomplète'
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
                v = keyword + self.skip(' \t\n')
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
        parsed.append(If('if' + self.skip(" \t\n")))
        error = self.parse_test(parsed)
        error = self.parse_keyword(error, parsed.content, "then")
        if error == '':
            err = self.parse_until(parsed.content[-1], ['fi','else'], True)
            if err == 'fi':
                parsed.append(Fi(err))
            elif err == 'else':
                else_block = ElseBloc()
                parsed.append(else_block)
                else_block.append(Else(err + self.skip(' \t\n')))
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
            c = self.parse_argument()
            if (len(c.content) == 1
                and name(c.content[0]) == 'Normal'
                and valid_variable_name(c.content[0].content)
                ):
                parsed.append(LoopVariable(c.content[0].content))
            else:
                parsed.append(Unterminated(c.text(),
                                           "Nom de variable invalide"))
        else:
            parsed.content[0] = Unterminated(parsed.content[0].content,
                                             "Indiquez le nom de la variable")
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
            if self.get() in ';\n':
                parsed.append(EndOfValues(self.get()))
                self.next()
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
                    and parsed.content[-2].text().strip() in ';\n'
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
                if self.get() in '|;)&\n':
                    return parsed
                if self.get() == '`' and self.in_back_cote:
                    return parsed
                while not self.empty() and self.get() in '(':
                    parsed.append(Unexpected("("))
                    self.next()
            if not self.empty():
                before_command = parsed.number_of(Argument)==0
                parsed.append(self.parse_argument(parse_equal = before_command))
                if (parsed.number_of(Argument) == 1
                    and not isinstance(parsed.content[0], Affectation)
                    ):
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
        # BASH
        # if fildes == "" and self.get() == '&':
        #     fildes = "&"
        #     self.next()
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
                c = self.get()
                if c == ']' and len(sb.content) != empty:
                    break
                if c == '!' and len(sb.content) == empty and empty==1:
                    empty = 2
                    sb.append(SquareBracketNegate('!'))
                    self.next()
                    continue
                if c == '$':
                    self.read_dollar(sb)
                    continue
                if c == '"':
                    self.read_guillemet(sb)
                    continue
                if c == "'":
                    self.read_quote(sb)
                    continue
                if c == "\\":
                    self.read_backslash(sb)
                    sb.content[-1] = SquareBracketChar(sb.content[-1].content)
                    continue
                if c in ' \t|;&':
                    parsed.append(Normal('['))
                    self.i = i
                    return
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
        if not valid_variable_name(parsed.content[0].content):
            return True
        self.next()
        a = Affectation()
        a.append(VariableName(parsed.content.pop().content))
        a.append(Equal("="))
        for content in self.parse_argument(False, False).content:
            a.append(content)
        parsed.append(a)
    def read_home(self, parsed):
        if len(parsed.content) != 0  or  self.get() != '~':
            return True
        self.next()
        n = self.skip(logins)
        if self.empty() or self.get() == '/':
            parsed.append(Home("~" + n))
        else:
            parsed.append(Unterminated("~" + n))
    def parse_argument(self, parse_equal=True, parse_pattern=True):
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
                and (not parse_pattern or self.read_pattern(parsed))
                and self.read_replacement(parsed)
                and self.read_home(parsed)
                ):
                if not parse_equal or self.read_equal(parsed):
                    parsed.append(Normal(c))
                    self.next()
        if not parsed.empty() and isinstance(parsed.content[0], Affectation):
            return parsed.content[0]
        return parsed

##############################################################################
##############################################################################
##############################################################################

class RegExpTree(Argument):
    is_an_option = False
    is_an_option_argument = False
    argument_position = ""
    begin_regexp = False
    def local_help(self, position):
        r = Argument.local_help(self, position)
        if r != '':
            r += ' : '
        if not isinstance(self.parent, RegExpTree):
            r += "une expression régulière"
            if self.extended:
                r += " <b>étendue</b>"
            r += self.or_list(self.content)
        if self.message:
            r += self.message
        return r
    def color(self):
        return ["#080", "#8F8"]
    def init_position(self, i=0, ident=0):
        if (isinstance(self, RegExpMultiply)
            and isinstance(self.content[1], RegExpBloc)
            and not self.parse_done):
            self.content[1].content[0] = Unterminated(
                '{',
                """Indiquez le nombre de répétition ou bien un intervalle
                comme {3,7} qui autorise de 3 à 7 répétitions""")

        r = Container.init_position(self, i, ident)
        if not isinstance(self.parent, RegExpTree):
            self.groups = []
            self.init_group_number(1)
        return r

    def get_groups(self):
        top = self
        while isinstance(top.parent, RegExpTree):
            top = top.parent
        return top.groups

    def or_list(self, content):
        t = []
        s = ''
        for i in content:
            if isinstance(i, RegExpOr):
                t.append(s)
                s = ''
            else:
                if i.content != "" and not isinstance(i, Invisible):
                    s += i.html()
        if len(t) == 0:
            return ''
        t.append(s)
        tt = []
        for s in t:
            if s == '':
                s = "UNE CHAINE VIDE"
            else:
                s =  '«' + s + '»'
            tt.append('<li>' + s)
        return ("\n<br>Correspond à l'une des possibilités suivantes :\n<ul>"
                + '\n'.join(tt) + '</ul>')

class RegExpMultiply(RegExpTree):
    parse_done = False
    def local_help(self, dummy_position):
        return ("Répète «" + self.content[0].html() + '» '
                + self.content[1].how_many())

class RegExpBloc(RegExpTree):
    def how_many(self):
        middle = None
        for i, element in enumerate(self.content):
            if element.text() == ',':
                middle = i
                break
        if middle is None:
            return ("exactement "
                    + ''.join([element.html()
                               for element in self.content[1:-1]])
                    + ' fois')
        return ('de '
                + ''.join([element.html()
                           for element in self.content[1:middle]])
                + ' à '
                + ''.join([element.html()
                           for element in self.content[middle+1:-1]])
                + " fois")
    def local_help(self, dummy_position):
        return ""

class RegExpGroup(RegExpTree):
    def local_help(self, dummy_position):
        return ("Groupement numéro " + str(self.group_number)
                + self.or_list(self.content[1:-1]))

class RegExpBackslashSpecial(RegExpTree):
    def local_help(self, dummy_position):
        if self.content[-1].content == 'b':
            return "Ceci représente l'emplacement aux extrémités de mot. Cet emplacement ne contient aucun caractère car il est entre 2 lettres."
        groups = self.get_groups()
        n = int(self.content[-1].content) - 1
        if n < len(groups):
            more = "qui correspond à : «" + groups[n].html() + "»"
        else:
            more = "mais ce groupe n'existe pas"
        return ("Remplacé par ce qui a été trouvé par le groupe "
                + str(n+1) + '<br>\n' + more)

class RegExpList(RegExpTree):
    def local_help(self, dummy_position):
        if self.first_of(RegExpNegate):
            return "Remplace un unique caractère qui n'est <b>pas</b> dans la liste"
        else:
            return "Remplace un unique caractère de la liste"
    def cleanup(self, replace_option=None):
        # The char order is not important
        return Container.cleanup(self, replace_option, True)

class RegExpRange(RegExpTree):
    def local_help(self, dummy_position):
        return ("Un caractère dont le code ASCII est entre celui de «"
                + self.content[0].content + '» et celui de «'
                + self.content[-1].content + '»')

class RegExpChar(Normal):
    def color(self):
        return ["#080", "#8F8"]

class RegExpDot(RegExpChar):
    def local_help(self, dummy_position):
        return "Un caractère quelconque."

class RegExpStar(RegExpChar):
    def how_many(self):
        if self.content == '*':
            return "de 0 fois (rien) à l'infini"
        elif self.content == "+":
            return "de une fois à l'infini"
        elif self.content == "?":
            return "zéro ou une fois"
        else:
            return "Il y a un bug dans le programme !"
    def local_help(self, dummy_position):
        return "Répète l'entité précédente"

class RegExpReset(RegExpChar):
    begin_regexp = True
class RegExpOr(RegExpReset):
    def local_help(self, dummy_position):
        return "«OU» entre la partie gauche et la droite"
class RegExpParenthesis(RegExpReset):
    def local_help(self, dummy_position):
        if self.content == '(':
            return "Début du groupe"
        else:
            return "Fin du groupe"
class RegExpBegin(RegExpReset):
    def local_help(self, dummy_position):
        return "Le début de ligne"
class RegExpEnd(RegExpChar):
    def local_help(self, dummy_position):
        return "La fin de ligne"

class RegExpGarbage(RegExpChar):
    def local_help(self, dummy_position):
        return "Ces caractères n'ont aucun sens après la fin de ligne"
    def color(self):
        return ["#F00", "#F88"]

class RegExpBadRange(RegExpGarbage):
    def local_help(self, dummy_position):
        return "Les seul caractères autorisés sont les chiffres et la virgule"

class RegExpBadEscape(RegExpGarbage):
    def local_help(self, dummy_position):
        return "Ce n'était pas la peine d'échapper ce caractère qui est normal, cela peut au contraire lui donner un sens."

class RegExpBracket(RegExpChar):
    def local_help(self, dummy_position):
        if self.content == '[':
            return "Début de liste de caractères"
        else:
            return "Fin de liste de caractères"

class RegExpNegate(RegExpBracket):
    def local_help(self, dummy_position):
        return "Un caractère qui n'est pas dans la liste suivante"

class RegExpListNormal(RegExpChar):
    def local_help(self, dummy_position):
        return "Le caractère «" + self.content + "»"
    def color(self):
        if hasattr(self, "parent") and isinstance(self.parent, RegExpRange):
            return ["#040", "#8F8"]
        else:
            return ["#080", "#8F8"]

class RegExpBackslash(Invisible):
    escape = True
    def local_help(self, dummy_position):
        if self.escape:
            return "Il disparaît en annulant la signification du caractère suivant pour l'expression régulière."
        else:
            return "Il donne une signication au caractère suivant"
    def color(self):
        return ["#8F8", "#8F8"]


class RegExpNoHelp(RegExpReset):
    def local_help(self, dummy_position):
        return ""


def new_content(element, delete_from, delete_to, insert_elements):
    content = []
    for i, e in enumerate(element.content):
        if delete_from <= i < delete_to:
            if i == delete_from:
                for ee in insert_elements:
                    if isinstance(ee, Normal) and len(ee.content) == 0:
                        continue
                    content.append(ee)
            continue
        content.append(e)
    element.content = content
    return element

def split_char(root, element, i, j, char, extended):
    new_content(root, i, i+1,
                [Normal(element.content[:j]),
                 char,
                 Normal(element.content[j+1:])])
    return regexpparser(root, extended)

def regexpparser_multiply(root, i, j, index_last_element, element, char,
                          extended):
    node = RegExpMultiply()
    if char == '{':
        number = RegExpBloc()
        number.content = [RegExpNoHelp(char)]
    else:
        number = RegExpStar(char)
        node.parse_done = True
    if j != 0:
        node.content = [Normal(element.content[j-1]), number]
        root = new_content(root, i, i+1,
                           [Normal(element.content[:j-1]),
                            node,
                            Normal(element.content[j+1:])])
    else:
        last_element = root.content[index_last_element]
        if (isinstance(last_element, Normal)
            and len(last_element.content) > 1):
            new_content(root, index_last_element,
                        index_last_element+1,
                        [Normal(last_element.content[:-1]),
                         Normal(last_element.content[-1])])
            index_last_element += 1
            i += 1
            last_element = root.content[index_last_element]

        if index_last_element + 1 == i:
            bloc = last_element
        else:
            bloc = RegExpBloc()
            bloc.content = root.content[index_last_element:i]
        node.content = [bloc, number]
        root = new_content(root, index_last_element, i+1,
                           [node, Normal(element.content[j+1:])])
    return regexpparser(root, extended)

def regexpparser_get(root, i, j, content):
    if len(root.content[i].content) == j:
        while True: # Search a Normal Element.
            i += 1
            if i == len(root.content):
                return None, None, None
            if isinstance(root.content[i], Normal):
                break
            content.append(root.content[i])
        j = 0
    char = root.content[i].content[j]
    j += 1
    return i, j, char

def regexpparser_list(root, i, j, extended):
    content = [RegExpBracket('[')]
    normals = []
    i_start = i
    j_start = j
    i, j, char = regexpparser_get(root, i, j, content)
    i, j, char = regexpparser_get(root, i, j, content)
    if char == '^':
        content.append(RegExpNegate(char))
        i, j, char = regexpparser_get(root, i, j, content)
    if char == ']':
        content.append(RegExpListNormal(char))
        i, j, char = regexpparser_get(root, i, j, content)
    while i is not None:
        if char == ']':
            content.append(RegExpBracket(char))
            break
        if len(normals) > 1 and normals[-1].content == '-':
            r = RegExpRange()
            r.content = [RegExpListNormal(char)]
            while True:
                r.content.append(content.pop())
                if r.content[-1] is normals[-2]:
                    break
            r.content.reverse()
            content.append(r)
            normals = []
        else:
            content.append(RegExpListNormal(char))
            normals.append(content[-1])
        i, j, char = regexpparser_get(root, i, j, content)

    node = RegExpList()
    node.content = content
    root_content = [Normal(root.content[i_start].content[:j_start]),
                    node]
    if i is None:
        content[0] = Unterminated(
            '[',
            'Une liste de caractères autorisés comme «[aeiou0-9_/@]»')
        i = len(root.content)
    else:
        root_content.append(Normal(root.content[i].content[j:]))
        if len(content) == 3 and isinstance(content[1], RegExpListNormal):
            content[1] = Unterminated(content[1].content, il_est_plus_court)
    root = new_content(root, i_start, i+1, root_content)
    return regexpparser(root, extended)

# Fonction en O(n*n) pour simplifier le code
def regexpparser(root, extended):
    index_last_element = None
    group_start = None
    for i, element in enumerate(root.content):
        if (not isinstance(element, Chars)
            and not isinstance(element, RegExpTree)):
            return # Abort parsing
        if element.begin_regexp:
            if isinstance(element, RegExpParenthesis):
                group_start = i
            index_last_element = None
            continue
        if (index_last_element is not None
            and isinstance(root.content[index_last_element], RegExpMultiply)
            and not root.content[index_last_element].parse_done
        ):
            factor = root.content[index_last_element].content[1]
            if not isinstance(factor, RegExpBloc):
                node = RegExpBloc()
                node.content = [RegExpNoHelp(factor.content)]
                root.content[index_last_element].content[1] = node
            else:
                node = root.content[index_last_element].content[1]
            if name(element) != 'Normal':
                node.append(element)
                new_content(root, i, i+1, [])
                return regexpparser(root, extended)
            char = element.content[0]
            if char not in "0123456789,}":
                node.content.append(RegExpBadRange(char))
            else:
                node.content.append(RegExpNoHelp(char))
            if char == '}':
                root.content[index_last_element].parse_done = True
            new_content(root, i, i+1, [Normal(element.content[1:])])
            return regexpparser(root, extended)
        if not isinstance(element, Normal):
            if (isinstance(element, RegExpTree)
                or isinstance(element, RegExpBackslash)
            ):
                index_last_element = i
            continue
        if isinstance(element, RegExpEnd) or isinstance(element, RegExpDot):
            index_last_element = i
            continue

        if isinstance(element, RegExpGarbage):
            continue

        if (index_last_element
            and isinstance(root.content[index_last_element], RegExpEnd)
            and name(element) == 'Normal'
        ):
            if not extended:
                content = [RegExpGarbage(element.content)]
                new_content(root, i, i+1, content)
                return regexpparser(root, extended)
            split = len(element.content)
            for j, char in enumerate(element.content):
                if char in ')|':
                    split = j
                    break
            if split != 0:
                content = [RegExpGarbage(element.content[:split]),
                           Normal(element.content[split:])]
                new_content(root, i, i+1, content)
                return regexpparser(root, extended)

        # Normal string
        for j, char in enumerate(element.content):
            if (j == 0
                and index_last_element is not None
                and isinstance(root.content[index_last_element],
                               RegExpBackslash)):
                if char == 'b'  or  char in '123456789' and extended:
                    node = RegExpBackslashSpecial()
                    node.content = root.content[index_last_element:i]
                    root.content[index_last_element].escape = False
                    node.content.append(RegExpNoHelp(char))
                    if len(element.content) > 1:
                        element.content = element.content[1:]
                    else:
                        i += 1
                    new_content(root, index_last_element, i, [node]) 
                    return regexpparser(root, extended)
                if (char not in '*.^$\\[.'
                    and (not extended or char not in '()|+')):
                    root.content[index_last_element].escape = 0
                    return split_char(root, element, i, j,
                                      RegExpBadEscape(char), extended)
                continue
            if ((char == '*'
                or char in '?+{' and extended
                 )
                and (j != 0 or index_last_element is not None)
                ):
                return regexpparser_multiply(root, i, j, index_last_element,
                                             element, char, extended)
            elif char == '^' and index_last_element is None and j == 0:
                return split_char(root, element, i, j,
                                  RegExpBegin(char), extended)
            elif char == '$':
                return split_char(root, element, i, j,
                                  RegExpEnd(char), extended)
            elif char == '.':
                return split_char(root, element, i, j,
                                  RegExpDot(char), extended)
            elif char == '\\':
                return split_char(root, element, i, j,
                                  RegExpBackslash(char), extended)
            elif char == '(' and extended:
                return split_char(root, element, i, j,
                                  RegExpParenthesis(char), extended)
            elif char == '|' and extended:
                return split_char(root, element, i, j,
                                  RegExpOr(char), extended)
            elif char == ')' and extended:
                if group_start is None:
                    return split_char(root, element, i, j,
                                      Unterminated(')', "Il manque l'ouvrante"),
                                      extended)
                node = RegExpGroup()
                node.content = root.content[group_start:i]
                if j:
                    node.content.append(Normal(element.content[:j]))
                node.content.append(RegExpParenthesis(')'))
                new_content(root, group_start, i+1,
                            [node, Normal(element.content[j+1:])])
                return regexpparser(root, extended)
            elif char == '[':
                return regexpparser_list(root, i, j, extended)
        index_last_element = i
    if group_start is not None:
        root.content[group_start] = Unterminated(
            '(', 'Groupe ouvert mais pas encore fermé')
    return root

def regexpparser_top(root, extended):
    r = regexpparser(root, extended)
    if not r:
        root.message = """<p style="background:#F00; color:#FFF">Cette expression régulière ne peut être
        analysée car le shell va d'abord la remplacer par la liste
        des fichiers qui rentrent dans le <em>pattern</em>.
        Il faut donc la protéger.</p>"""
        return root
    t = RegExpTree()
    t.content = r.content
    t.extended = extended
    return t

class SedReplacementText(Container):
    def local_help(self, dummy_position):
        if self.parent.first_of(SedSeparator3):
            m = "."
        else:
            m = " <b>il faut la terminer par <em>slash</em> '/'</b>."
        return """La chaîne qui remplacera les textes correspondant
        à l'expression régulière""" + m
    def color(self):
        return ["#088", "#8FF"]

class SedReplacement(SedReplacementText):
    def local_help(self, dummy_position):
        a = self.first_of(SedAction)
        if not a:
            return "Indiquez la lettre 's' pour faire une substitution."
        e = self.first_of(RegExpTree)
        if e:
            e = e.html()
        else:
            e = '?'
        t = self.first_of(SedReplacementText)
        if t:
            t = t.html()
        else:
            t = '?'
        if self.multiple:
            m = "Fait toutes les substitutions sur la ligne"
        else:
            m = "Fait la première substitution sur chaque ligne"
        return m + '<br>' + e + ' &#8594; ' + t

    def color(self):
        if self.first_of(SedSeparator3):
            return ["#088", "#8FF"]
        else:
            return ["#088", "#F88"]

class SedChar(Chars):
    def color(self):
        return ["#088", "#8FF"]

class SedSeparator1(SedChar):
    def local_help(self, dummy_position):
        return "Indique le début de l'expression régulière."

class SedSeparator2(SedChar):
    def local_help(self, dummy_position):
        return "Indique le début de la chaîne qui va remplacer ce qui rentre dans l'expression régulière."

class SedSeparator3(SedChar):
    def local_help(self, dummy_position):
        return "Indique le début des options de remplacement."

class SedOption(SedChar):
    def local_help(self, dummy_position):
        if self.content == 'g':
            return "Le remplacement est fait pour toutes les occurrences trouvées dans la ligne et pas seulement la première."

class SedAmpersand(SedChar):
    def local_help(self, dummy_position):
        return "Représente ce qui a été trouvé par l'expression régulière"

class SedAction(SedChar):
    def local_help(self, dummy_position):
        if self.content == 's':
            t = "Remplacement d'une expression régulière par un texte."
        return ("Le traitement que doit faire la commande :<br>"
                + "'" + self.content + "' : " + t)

class SedBackslash(SedChar):
    def local_help(self, dummy_position):
        return """Annule la signification du caractère suivant pour 'sed'"""

class SedBackslashSpecial(SedChar):
    def local_help(self, dummy_position):
        groups = self.regexptree.groups
        n = int(self.content[-1]) - 1
        if n < len(groups):
            more = "qui correspond à : «" + groups[n].html() + "»"
        else:
            more = "mais ce groupe n'existe pas"
        return ("Remplacé par ce qui a été trouvé par le groupe "
                + str(n+1) + '<br>\n' + more)
    def color(self):
        if len(self.content) == 0 or int(self.content[-1]) - 1 < len(self.regexptree.groups):
            return ["#088", "#8FF"]
        else:
            return ["#F00", "#F88"]

def sedparser_top(root, extended):
    i = 0
    j = 0
    content = []
    while root.content[i] and not isinstance(root.content[i], Normal):
        content.append(root.content[i])
        i += 1
    if not root.content[i]:
        return root
    i, j, char = regexpparser_get(root, i, j, content)
    if char != 's':
        root.make_comment("""Seul le traitement 's' de substitution
        est pris en compte par cette application. Désolé.""", "#F00")
        return root
    content.append(SedAction(char))
    i, j, char = regexpparser_get(root, i, j, content)
    if i is not None:
        if char != '/':
            content.append(Unterminated(char,
                                        "NON : remplacez ce caractère par '/'"))
        else:
            content.append(SedSeparator1(char))

    re = []
    char = None
    while i is not None:
        i, j, char = regexpparser_get(root, i, j, re)
        if i is None:
            break
        if char == '\\':
            i, j, char = regexpparser_get(root, i, j, re)
            if i is None:
                re.append(Unterminated('\\'))
                break
            re.append(RegExpBackslash('\\'))
            re.append(Normal(char))
            continue
        if char == '/':
            break
        if len(re) and isinstance(re[-1], Normal):
            re[-1].content += char
        else:
            re.append(Normal(char))

    if len(re):
        x = RegExpTree()
        x.content = re
        r = regexpparser(x, extended)
        r.extended = extended
        content.append(r)

    if char == '/':
        content.append(SedSeparator2(char))
    else:
        if len(re):
            r.message = " <b>qu'il faut terminer par un <em>slash</em> '/'</b>"

    char = None
    x = SedReplacementText()
    content.append(x)
    while i is not None:
        i, j, char = regexpparser_get(root, i, j, x.content)
        if i is None:
            break
        if char == '&':
            x.content.append(SedAmpersand(char))
            continue
        if char == '\\':
            i, j, char = regexpparser_get(root, i, j, x.content)
            if i is None:
                re.append(Unterminated('\\'))
                break
            if extended and char in "123456789":
                x.content.append(SedBackslashSpecial('\\' + char))
                x.content[-1].regexptree = r
            elif char in '\\&/':
                x.content.append(SedBackslash('\\'))
                x.content.append(Normal(char))
            else:
                x.content.append(SedBackslash('\\'))
                x.content.append(RegExpBadEscape(char))
            continue
        if char == '/':
            break
        if len(x.content) and isinstance(x.content[-1], Normal):
            x.content[-1].content += char
        else:
            x.content.append(Normal(char))

    if char == '/':
        content.append(SedSeparator3(char))

    char = None
    multiple = False
    while i is not None:
        i, j, char = regexpparser_get(root, i, j, content)
        if i is None:
            break
        if char == 'g':
            content.append(SedOption(char))
            multiple = True
        else:
            content.append(Unterminated(char, "Option inconnue"))

    root = SedReplacement()
    root.content = content
    root.multiple = multiple
    return root

