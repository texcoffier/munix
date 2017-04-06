#!/usr/bin/python3
# -*- coding: utf-8 -*-

debug = False

try:
    Array.prototype.append = Array.prototype.push
    def str(x):
        return x.toString()
    def __join__(v):
        return v.join(this)
    String.prototype.join = __join__
    def startswith(v):
        return this.substr(0, len(v)) == v
    String.prototype.startswith = startswith
    def endswith(v):
        return this.substr(len(this) - len(v)) == v
    String.prototype.endswith = endswith
    javascript = True
    def classname(obj):
        return obj.__proto__.constructor.name
    debug = window.location.host == "127.0.0.1:8880"
    def floor(f):
        return Math.floor(f)
except:
    javascript = False
    floor = int

nr_arcs = 7
repulsion = 100000
repulsion_power = 2
debug_dist = False

dash_speed = 0.3

arc_length = 20
x_space = arc_length * 8
margin_left = 10
menu_width = 300

question_animation = 100
traveler_speed = 0.005
move_animation = 10

score_multiply = 0.999

color_followed = "#00CCCC"
color_hidden = "#999999"
color_goal = "#00FF00"
color_normal = "#808080"
color_current = "#FF00FF"
color_traveler = "#00FFFF"
color_symlinks = ["#BB8080", "#80BB80","#8080BB", "#60BBBB"]
color_static = "#808080"

translations = {
    'Title': {'en': 'Find Your Path' },
    'Current': {"en": "Current directory",
                "fr": "Répertoire courant"},
    "Input": {"en": "Your answer:",
             "fr": "Votre réponse :"},
    "Goal": {"en": "Catch me!",
             "fr": "Attrape-moi !"},
    "Path": {"en": "On the path",
             "fr": "Noeuds traversés"},
    "Score": {"en": "Your current score:",
              "fr": "Votre score courant :"},
    "GameHigh": {"en": "This game highscore:",
                 "fr": "Pour cette partie :"},
    "High": {"en": "Your highscore:",
             "fr": "Votre meilleur score :"},
    "Help": {"en": "F1: français, F2: english,\nF3: change your name,\nF4: toggle arcs animation.\nF9: toogle goal change animation.\nF11, F12: change pictures.\nTab: completion",
             "fr": "F1 : français, F2 : english,\nF3 : changer de pseudo,\nF4 : animation des arcs.\nF9 : animation du changement d'objectif.\nF11, F12: mettre des images.\nTab: complétion"},
    "Level": {"en": "Level",
             "fr": "Niveau"},
    "EnterAlias": {"en": "Enter your nickname for highscores or leave empty:",
                   "fr": "Entrez votre pseudo (optionnel) :"},
    "current": {"en": "Enter the URL of your picture:",
                   "fr": "Entrez l'URL de votre photo :"},
    "goal": {"en": "Enter the URL of the goal picture:",
             "fr": "Entrez l'URL de la photo de l'objectif :"},
    "/_not_needed": {"en": "The path should not start by '/'",
                     "fr": "Le '/' initial est inutile."},
    "/_needed": {"en": "The path should start by '/'",
                 "fr": "Le chemin doit commencer par '/'"},
    "._needed": {"en": "The path must start by '.'",
                 "fr": "Le chemin doit commencer par '.'"},
    ".._needed": {"en": "The path must start by '..'",
                 "fr": "Le chemin doit commencer par '..'"},
    "../_needed": {"en": "The path must start by '../'",
                 "fr": "Le chemin doit commencer par '../'"},
    "letters": {"en": "letters only are needed",
                "fr": "lettres suffisent pour répondre"},
    "S1": {"en": """You are at the tree root.
Enter the name on the arc
leading to the target disc.""",
           "fr": """Vous êtes à la racine.
Saisissez le nom sur l'arc
menant au disque objectif."""
             },
    "S1_1": {"en": "Read the question above.",
             "fr": "Lisez la consigne au dessus."},
    "S1_2": {"en": "Congratulation. Retry again",
             "fr": "Bravo. Recommencez !",
             },
    "S1_3": {"en": "Very good. Retry a last time.",
             "fr": "Super ! Une dernière fois.",
             },

    "S2": {"en": """You start from the root.
The goal is farer.
Use '/' between arc names.""",
             "fr": """Vous êtes à la racine.
L'objectif est maintenant plus éloigné.
Mettez '/' entre les noms d"arc.""",
             },
    "S2_1": {"en": "Welcome to level 2",
             "fr": "Bienvenue au niveau 2",
             },
    "S2_2": {"en": "It is easy, retry it!",
             "fr": "Facile ! Recommencez.",
             },
    "S2_3": {"en": "A last time.",
             "fr": "Une dernière fois.",
             },

    "S3": {"en": """You are no more at the root.
You indicate only arc names
from the place you are.""",
             "fr": """Vous n'êtes plus à la racine !
Indiquez seulement les noms d'arc
à partir de l'endroit où vous êtes.""",
             },
    "S3_1": {"en": "Welcome to level 3",
             "fr": "Bienvenue au niveau 3",
             },
    "S3_2": {"en": "It is easy, retry it!",
             "fr": "Facile, recommencez.",
             },
    "S3_3": {"en": "A last time.",
             "fr": "Une dernière fois.",
             },

    "S4": {"en": """You are deep in the tree.
Start the name with '/'
to return to the root.""",
             "fr": """Vous êtes plus profond dans l'arbre.
Commencez le chemin par '/'
pour retourner à la racine.""",
             },
    "S4_1": {"en": "Welcome to level 4",
             "fr": "Bienvenue au niveau 4",
             },
    "S4_2": {"en": "It is easy, retry it!",
             "fr": "Facile, recommencez.",
             },
    "S4_3": {"en": "A last time.",
             "fr": "Une dernière fois",
             },

    "S5": {"en": "To designate the current node,\nuse the arc named '.'",
             "fr": "Utilisez l'arc nommé '.'\npour indiquer le noeud courant.",
    },
    "S5_1": {"en": "Welcome to level 5",
             "fr": "Bienvenue au niveau 5",
             },

    "S6": {"en": """You are deep in the tree.
To move up one level:
use the arc named '..'.""",
             "fr": """Vous êtes très profond dans l'arbre.
Pour remonter au noeud précédent :
utilisez l'arc nommé '..'.""",
    },
    "S6_1": {"en": "Welcome to level 6",
             "fr": "Bienvenue au niveau 6",
             },
    "S6_2": {"en": "Great! A last time.",
             "fr": "Super ! Encore une fois",
    },

    "S7": {"en": """You are deep in the tree.
To go to a sibling:
move up and then down.""",
             "fr": """Vous êtes très profond dans l'arbre.
Pour allez sur un frère :
montez puis descendez dans le frère.""",
    },
    "S7_1": {"en": "Welcome to level 7",
             "fr": "Bienvenue au niveau 7",
             },
    "S7_2": {"en": "Do it a last time.",
             "fr": "Faites-le encore une fois",
    },
    "S8": {"en": """Use arc names, '/', '.', '..'
to catch quickly the goal.""",
             "fr": """Utilisez les noms d'arcs,
'/', '.' et '..' pour atteindre
au plus vite à la destination."""
             },
    "S8_1": {"en": "Welcome to level 8",
             "fr": "Bienvenue au niveau 8",
             },
    "S8_2": {"en": "Level 9 in",
             "fr": "Niveau 9 dans",
             },
    "S8_3": {"en": "moves.",
             "fr": "coups.",
             },

    "S9": {"en": """Use the symbolic link
to reach the goal.""",
             "fr": """Utilisez le lien symbolique
pour atteindre la destination."""
             },
    "S9_1": {"en": "Welcome to level 9",
             "fr": "Bienvenue au niveau 9",
             },
    "S9_2": {"en": "Super!",
             "fr": "Super !",
             },
    "S9_3": {"en": "Great!",
             "fr": "Géant !",
             },
    "S9_4": {"en": "Do it a last time.",
             "fr": "Faites-le encore une fois",
    },

    "S10": {"en": """Use any way to
reach quickly the goal.""",
             "fr": """Utilisez n'importe quel
moyen pour atteindre
au plus vite à la destination."""
             },
    "S10_1": {"en": "Final level",
             "fr": "Dernier niveau",
             },
}

def _(txt):
    t = translations[txt]
    if not t:
        return
    return t[_.language] or t['en']

if javascript:
    _.language = window.navigator.language.split('-')[0]

def dirname(path):
    return '/'.join(path.split("/")[:-1])

def basename(path):
    return path.split("/")[-1]

def interpolate(pos, v1, v2):
    return (1 - pos) * v1 + pos * v2

def hex(t):
    t *= 256
    return "0123456789ABCDEF"[floor(t/16)] + "0123456789ABCDEF"[floor(t) % 16]

class Particle:
    def __init__(self, fixed):
        self.x = self.y = None
        self.fx = self.fy = 0
        self.fixed = fixed
        self.links = []
    def copy(self):
        p = Particle(self.fixed)
        p.x = self.x
        p.y = self.y
        return p
    def add(self, particle):
        self.links.append(particle)
    def string(self):
        return '(' + str(self.x) + "," + str(self.y) + ")"
    def diff(self, other):
        return (self.x - other.x, self.y - other.y)
    def distance(self, other):
        x, y = self.diff(other)
        return (x*x + y*y) ** 0.5
    def sum(self, other):
        return (self.x + other.x, self.y + other.y)
    def spring(self, others, arc_length):
        for link in self.links:
            vx, vy = self.diff(link)
            n = (vx*vx + vy*vy)**0.5
            d2 = 1 - arc_length / n
            vx *= d2
            vy *= d2
            self.fx -= vx
            self.fy -= vy
            link.fx += vx
            link.fy += vy
        for p in others:
            vx, vy = self.diff(p)
            d2 = (vx*vx + vy*vy)**repulsion_power / repulsion
            if d2 < 0.001:
                d2 = 0.001
            vx /= d2
            vy /= d2            
            self.fx += vx
            self.fy += vy
            p.fx -= vx
            p.fy -= vy
    def update(self):
        if self.fixed:
            return
        while self.fx > 10 or self.fy > 10:
            self.fx /= 2
            self.fy /= 2
        self.x += self.fx / 4
        self.y += self.fy / 4
        self.fx = 0
        self.fy = 0
        
class Node:
    translate_y = 0
    def __init__(self, name, link_to=None):
        self.link_to = link_to
        self.is_a_file = name[-1] != '/'
        if not self.is_a_file:
            name = name[:-1]
        self.name = name
        self.edges = []
        self.particle = Particle(True)
        self.depth = 0

    def copy(self):
        n = Node(self.name, self.link_to)
        n.particle = self.particle.copy()
        return n
        
    def add(self, edge):
        self.edges.append(edge)

    def get(self, node):
        for edge in self.edges:
            if edge.destination is node:
                return edge

    def nr_visible_children(self):
        return len(self.get_visible_children())

    def get_visible_children(self):
        t = []
        for edge in self.edges:
            if edge.hide:
                continue
            if edge.destination.hide:
                continue
            t.append(edge.destination.name)
        return t

    def get_a_child(self):
        t = self.get_visible_children()
        return t[floor(Math.random()*len(t))]

    def init_position(self, x, y):
        y_start = y
        self.x = x
        x += x_space
        if self.is_a_file:
            if not self.hide:
                y += arc_length * 2
        else:
            if self.nr_visible_children() == 0:
                y += arc_length * 2
        y += self.translate_y
        for edge in self.edges:
            if not edge.hide:
                y = edge.destination.init_position(x, y)
        self.y = (y_start + y) / 2
        if self.particle.x is None:
            self.particle.x = self.x
            self.particle.y = self.y
        return y
        
    def string(self):
        s = [self.name, self.particle.string()]
        for edge in self.edges:
            s.append('\n\t' + edge.string())
        return ''.join(s)

    def plot_image(self, ctx, imgid):
        img = document.getElementById(imgid)
        if not img:
            return
        if img.width == 0 or img.height == 0:
            return
        radius = arc_length
        if img.width > img.height:
            w = radius
            h = radius * img.height / img.width
        else:
            w = radius * img.width / img.height
            h = radius
        ctx.globalAlpha = 0.7
        ctx.drawImage(img,
                      0, 0, img.width, img.height,
                      self.particle.x - w, self.particle.y - h, 2*w, 2*h)
        ctx.globalAlpha = 1
        return True

    def plot_disc_current(self, ctx, t):
        ctx.fillStyle = color_current
        ctx.beginPath()
        ctx.arc(self.particle.x, self.particle.y, arc_length / 2,
                0, 2 * Math.PI)
        ctx.fill()

    def plot_disc_goal(self, ctx, t):
        radius = 1.4 * arc_length / 2
        p =  2 * Math.PI * radius / 16
        ctx.lineDashOffset = t * dash_speed
        ctx.strokeStyle = color_goal
        ctx.lineWidth = 18
        ctx.setLineDash([p, p])
        ctx.beginPath()
        ctx.arc(self.particle.x, self.particle.y, radius,
                0, 2 * Math.PI)
        ctx.stroke()
        ctx.lineWidth = 1
        self.plot_image(ctx, "goal")

    def plot_disc(self, ctx, t):
        if self.hide:
            return
        radius = arc_length / 2
        t /= -10
        if self.followed:
            ctx.fillStyle = color_followed
        else:
            ctx.fillStyle = color_normal

        ctx.beginPath()
        ctx.arc(self.particle.x, self.particle.y, arc_length / 2,
                0, 2 * Math.PI)
        ctx.fill()


    def plot_text(self, ctx):
        if self.hide:
            return
        if self.followed:
            ctx.fillStyle = color_followed
        else:
            ctx.fillStyle = "#000000"
        ctx.textAlign = "center"
        ctx.font = '12px sans-serif'
        ctx.fillText(self.name, self.particle.x,
                     self.particle.y - arc_length/2)

    def is_dir(self):
        return not self.is_a_file

    def distance(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return (x*x + y*y) ** 0.5

class Edge:
    def __init__(self, name, origin, destination, nb_arcs):
        self.name = name
        self.origin = origin
        self.destination = destination
        self.particles = [Particle(False) for i in range(nb_arcs)]
        if nb_arcs != 0:
            for i, p in enumerate(self.particles[:-1]):
                p.add(self.particles[i+1])
            origin.particle.add(self.particles[0])
            self.particles[-1].add(destination.particle)
        self.hide = name in (".", "..")
        if origin.link_to:
            origin.link_to_edge = self
        else:
            origin.edges.append(self)

    def string(self):
        return self.name + ''.join([p.string() for p in self.particles])

    def move(self, avoid, length):
        self.origin.particle.spring([], length)
        for p in self.particles:
            p.spring(avoid, length)
        for p in self.particles:
            p.update()
    
    def init_position(self):
        x1, y1 = self.origin.particle.x, self.origin.particle.y
        nb = len(self.particles) + 1
        if self.origin is self.destination:
            if self.name == '.':
                d = -0.7
            else:
                d = 0.8
            y1 -= d * arc_length
            for i, p in enumerate(self.particles):
                i = (i-1) * Math.PI / (nb-4)
                p.x = x1 - d * Math.cos(i) * arc_length / 2
                p.y = y1 - d * Math.sin(i) * arc_length / 2
            return
        x2, y2 = self.destination.particle.x, self.destination.particle.y
        if self.name == '..':
            vx = x1 - x2
            vy = y1 - y2
            n = arc_length / (vx*vx + vy*vy) ** 0.5 / 2
            vx *= n
            vy *= n
            self.particles[0].x = x1 - vy - vx/n/4
            self.particles[0].y = y1 + vx - vy/n/4
            self.particles[1].x = (x1+x2)/2 - vy
            self.particles[1].y = (y1+y2)/2 + vx
            self.particles[2].x = x2 - vy + vx/n/4
            self.particles[2].y = y2 + vx + vy/n/4
            return

        if not self.init_done:
            x1, y1 = self.origin.x, self.origin.y
            x2, y2 = self.destination.x, self.destination.y
            vx = x1 - x2
            vy = y1 - y2
            for i, p in enumerate(self.particles):
                i = ( i + 1. ) / nb
                p.x = interpolate(i, x1, x2) + vy / 2
                p.y = interpolate(i, y1, y2) - vx / 2
        self.init_done = True

    def middle_particle(self):
        if len(self.particles):
            return self.particles[len(self.particles) // 2]
        else:
            m = Particle()
            m.x, m.y = self.origin.particle.sum(self.destination.particle)
            m.x /= 2
            m.y /= 2
            return m

    def get_particle(self, p):
        if p <= 0:
            return self.origin.particle
        elif p >= len(self.particles) + 1:
            return self.destination.particle
        else:
            return self.particles[p-1]
        
    def get_pos(self, vv):
        v = vv * (len(self.particles) + 1)
        p = floor(v)
        d = v - p
        p1 = self.get_particle(p)
        p2 = self.get_particle(p+1)
        return interpolate(d, p1.x, p2.x), interpolate(d, p1.y, p2.y)

    def symbolic_link_color(self):
        return color_symlinks[self.symbolic_link % len(color_symlinks)]

    def plot_arc(self, ctx, animate, t, draw_particles):
        if self.destination.hide:
            return
        ctx.strokeStyle = "#000000"
        if self.symbolic_link:
            ctx.lineDashOffset = -t * dash_speed
            ctx.lineWidth = 6
            ctx.strokeStyle = self.symbolic_link_color()
            ctx.setLineDash([6, 6])
        else:
            ctx.lineDashOffset = -t * dash_speed
            ctx.lineWidth = 1
            if animate:
                ctx.setLineDash([6, 2])
            else:
                ctx.setLineDash([6, 0])
        if self.hide:
            ctx.strokeStyle = color_hidden
        if self.followed:
            ctx.strokeStyle = color_followed
        ctx.beginPath()
        ctx.moveTo(self.origin.particle.x, self.origin.particle.y)
        for p in self.particles:
            ctx.lineTo(p.x, p.y)
        ctx.lineTo(self.destination.particle.x, self.destination.particle.y)
        ctx.stroke()

        if draw_particles:
            ctx.fillStyle = "#000000"
            for p in self.particles:
                ctx.beginPath()
                ctx.arc(p.x, p.y, arc_length/10, 0, 2 * Math.PI)
                ctx.fill()
        
    def plot_txt(self, ctx):
        if self.destination.hide:
            return
        if self.symbolic_link:
            ctx.fillStyle = self.symbolic_link_color()
            ctx.font = 'bold 20px sans-serif'
            m = self.origin.particle
            x, y = m.x, m.y
            y += arc_length
        else:
            ctx.fillStyle = "#000000"
            ctx.font = 'bold 16px sans-serif'
            m = self.middle_particle()
            x, y = m.x, m.y
            y -= arc_length/8
        if self.hide:
            ctx.fillStyle = color_hidden
        if self.followed:
            ctx.fillStyle = color_followed

        ctx.textAlign = "center"
        ctx.fillText(self.name, x, y)
        if debug_dist:
            ctx.font = '10px sans-serif'
            ctx.fillText(floor(self.origin.particle.distance(
                self.destination.particle)), m.x, m.y + arc_length/2)
        
class Graph:
    def __init__(self):
        self.nodes = {}
        self.time = 0
        self.t_frozen = self.time
        self.this_time_highscore = self.score = 0
        self.highscore = int(localStorage["highscore"] or 0)
        if not localStorage["name"] and localStorage["name"] != '':
            self.askname()
        self.name = localStorage["name"]
        self.animate = True
        self.traveler_pos = 0
        self.show_absolute_path = True
        self.score_add = 10
        self.nr_symbolic_links = 0
        self.do_goal_animation = True

    def askname(self):
        name = prompt(_("EnterAlias"), localStorage["name"] or '')
        if not name and name != '':
            return
        self.name = localStorage["name"] = name

    def add(self, name, link_to=None):
        node = Node(name, link_to)
        name = node.name
        self.nodes[name] = node
        if name != '':
            node.parent = self.nodes[dirname(name)]
            node.depth = node.parent.depth + 1
            Edge(basename(name), node.parent, node, 0)
        else:
            node.parent = node
            self.root = node
        return node

    def add_dot(self):
        for node in self.nodes:
            node = self.nodes[node]
            if node.init_done:
                continue
            node.init_done = True
            if node.is_dir():
                Edge(".", node, node, nr_arcs)
                if node.name == '':
                    Edge("..", node, node.parent, nr_arcs)
                else:
                    Edge("..", node, node.parent, 3)
            
    def init_position(self, x):
        self.add_dot()
        self.root.init_position(x, 10)
        for node in self.nodes:
            node = self.nodes[node]
            for edge in node.edges:
                edge.init_position()
            if node.link_to and not node.link_to_edge:
                destination = node.link_to
                parent = node.parent
                while destination.startswith('../'):
                    destination = destination[3:]
                    parent = parent.parent
                if destination[0] != '/':
                    if destination != '..':
                        destination = parent.name + '/' + destination
                    else:
                        destination = parent.name
                d = node.distance(self.nodes[destination])
                Edge(node.link_to, node,
                     self.nodes[destination], floor(d / arc_length))
                self.nr_symbolic_links += 1
                node.link_to_edge.symbolic_link = self.nr_symbolic_links
                node.link_to_edge.init_position()


    def string(self):
        s = []
        for node in self.nodes:
            s.append(self.nodes[node].string())
        return '\n'.join(s)

    def move_particles(self):
        n = []
        for node in self.nodes:
            node = self.nodes[node]
            n.append(node.particle)
        for node in self.nodes:
            node = self.nodes[node]
            if node.link_to_edge:
                d = node.particle.distance(
                    node.link_to_edge.destination.particle)
                node.link_to_edge.move(n, d / (len(node.link_to_edge.particles) + 1))

    def reset(self):
        for node in self.nodes:
            node = self.nodes[node]
            node.followed = False
            if node.tmp:
                node.hide = True
            for edge in node.edges:
                edge.followed = False
            if node.link_to_edge:
                node.link_to_edge.followed = False

    def get_a_node(self, min_depth, min_sibling, only_dir):
        t = []
        for node in self.nodes:
            node = self.nodes[node]
            if node.tmp:
                continue
            if only_dir and not node.is_dir():
                continue
            depth = len(node.name.split("/"))
            if depth < min_depth:
                continue
            if node.parent.nr_visible_children() < min_sibling:
                continue
            t.append(node.name)
        return t[floor(Math.random() * len(t))]

    def get_a_dir(self, min_depth, min_sibling):
        return self.get_a_node(min_depth, min_sibling, True)

    def create_path(self):
        self.traveler_path = []
        if self.answer and self.answer[0] == '/':
            node = self.nodes['']
            path = self.answer[1:]
        else:
            node = self.nodes[self.current]
            path = self.answer
        if self.answer == "":
            return
        for x in path.split('/'):
            found = False
            for edge in node.edges:
                if edge.name == x:
                    self.traveler_path.append(edge)
                    edge.followed = True
                    node = edge.destination
                    found = True
                    break
            if not found and x != '':
                if node.tmp:
                    return False
                if x in (".", ".."):
                    return False
                n = self.add(node.name + "/" + x)
                n.tmp = True
                node.edges[-1].followed = True
                self.traveler_path.append(node.edges[-1])
                node = n
            node.followed = True
            node.hide = False
            self.new_current_real = node.name
            while node.link_to:
                node.followed = True
                node.hide = False
                node.link_to_edge.followed = True
                self.traveler_path.append(node.link_to_edge)
                node = node.link_to_edge.destination
        node.followed = True
        node.hide = False
        self.new_current = node.name
        return True

    def move_nodes(self):
        for node in self.nodes:
            node = self.nodes[node]
            if node.particle.x is not None and not node.tmp:
                node.particle.x = (node.x + 9*node.particle.x) / 10
                node.particle.y = (node.y + 9*node.particle.y) / 10
            else:
                node.particle.x = node.x
                node.particle.y = node.y

    def move(self):
        self.score *= score_multiply
        self.reset()
        self.path_valid = self.create_path()
        self.init_position(margin_left + menu_width + arc_length)
        if not self.stop:
            self.move_nodes()
            self.move_particles()

    def update_score(self):
        self.score += self.score_add
        if self.score <= self.this_time_highscore:
            return
        self.this_time_highscore = self.score
        self.update_score_iframe()
        if self.score < self.highscore:
            return
        self.highscore = self.score
        localStorage["highscore"] = str(self.score)
        self.highlight_highscore = True

    def update_score_iframe(self):
        iframe = document.getElementsByTagName("IFRAME")[0]
        iframe.src = ("?name=" + encodeURIComponent(self.name)
                      + '&score=' + floor(self.score))

    def plot_traveler(self, ctx, x, y):
        traveler = Node("")
        traveler.particle.x, traveler.particle.y = x, y
        if not traveler.plot_image(ctx, "current"):
            ctx.fillStyle = color_traveler
            ctx.beginPath()
            ctx.arc(x, y, arc_length / 4, 0, 2 * Math.PI)
            ctx.fill()
        
    def traveler(self, ctx):
        if len(self.traveler_path) == 0:
            return
        goal = False
        if len(self.answer) < self.traveler_last_len:
            self.traveler_pos = floor(self.traveler_pos - 0.000001)
            self.traveler_pos = len(self.traveler_path) - 1
        self.traveler_last_len = len(self.answer)
        if (self.traveler_pos >= len(self.traveler_path)
            and (self.new_current == self.goal
                 or self.new_current_real == self.goal)
            or debug and self.answer.startswith('*')
        ):
                goal = True
                self.traveler_last_len = 1000
        if self.traveler_pos > len(self.traveler_path):
            self.traveler_pos = len(self.traveler_path)
            p = self.traveler_pos - 1
        else:
            p = floor(self.traveler_pos)
        edge = self.traveler_path[p]
        x, y = edge.get_pos(self.traveler_pos - p)
        self.plot_traveler(ctx, x, y)
        self.traveler_pos += traveler_speed * Math.log(
            (self.score + self.score_add))
        return goal

    def plot(self, ctx):
        for node in self.nodes:
            self.nodes[node].plot_disc(ctx, self.t_frozen)
        t = (self.time - self.start_animation) / move_animation
        if t >= 1 or not self.do_goal_animation:
            t = 0.999
        n = Node("")
        n.particle.x, n.particle.y = self.current_anim.get_pos(t)
        n.plot_disc_current(ctx, self.t_frozen)
        
        n.particle.x, n.particle.y = self.goal_anim.get_pos(t)
        n.plot_disc_goal(ctx, self.t_frozen)

        goal = self.traveler(ctx)
        if self.show_absolute_path:
            for node in self.nodes:
                self.nodes[node].plot_text(ctx)
        for node in self.nodes:
            node = self.nodes[node]
            for edge in node.edges:
                edge.plot_arc(ctx, self.animate, self.time,
                              self.draw_particles)
            if node.link_to_edge:
                node.link_to_edge.plot_arc(ctx, True, self.time,
                                           self.draw_particles)
        for node in self.nodes:
            node = self.nodes[node]
            for edge in node.edges:
                edge.plot_txt(ctx)
            if node.link_to_edge:
                node.link_to_edge.plot_txt(ctx)

        ctx.textAlign = "left"

        line_height = 2 * arc_length
        x = margin_left
        y = 20

        ###################################### TITLE
        
        ctx.fillStyle = "#000000"
        ctx.font = 'bold 20px sans-serif'
        ctx.fillText(_("Title") + " " + self.name, x, y)
        y += line_height / 4
        
        ###################################### QUESTION
        
        ctx.font = '16px sans-serif'
        yy = y
        if (self.start_animation
            and self.time < self.start_animation + question_animation
            and self.stage.highlight_question()):
            c = hex((self.time - self.start_animation) / question_animation
                    * 14 / 16.) # DD
            ctx.fillStyle = "#" + c + "DD" + c
        else:
            ctx.fillStyle = "#DDDDDD"
        ctx.fillRect(x - 5, y, menu_width + 5, 1.7 * line_height)
        ctx.fillStyle = "#000000"
        for m in self.stage.get_question().split("\n"):
            y += line_height / 2
            ctx.fillText(m, x, y)
        y = yy + 1.7 * line_height
            
        ###################################### FEEDBACK
        
        ctx.font = '16px sans-serif'
        yy = y
        if (self.start_animation
            and self.time < self.start_animation + question_animation
            and self.stage.highlight_message()):
            c = hex((self.time - self.start_animation) / question_animation)
            ctx.fillStyle = "#" + c + "FF" + c
            ctx.fillRect(x - 5, y + 5, menu_width + 5, line_height/2)

        for m in self.stage.message().split("\n"):
            if '**' in m:
                ctx.fillStyle = "#FF8000"
                ctx.fillRect(x - 5, y + 5, menu_width + 5, line_height/2)
                m = m[2:]
            y += line_height / 2
            ctx.fillStyle = "#000000"
            ctx.fillText(m, x, y)

        y = yy + 1.6 * line_height

        ###################################### INPUT

        ctx.fillStyle = "#000000"
        # ctx.fillText(_("Input"), x, y)
        # y += line_height / 2
        ctx.font = 'bold 16px sans-serif'
        if self.path_valid or self.answer == '':
            ctx.fillStyle = "#000000"
        else:
            ctx.fillStyle = "#FF0000"
        ctx.fillRect(x - 5, y - 16, menu_width + 5, 24)
        ctx.fillStyle = "#FFFFFF"
        if (self.time // 10) % 2:
            ctx.fillText(self.answer, x, y)
        else:
            ctx.fillText(self.answer + '|', x, y)
        y += line_height

        ###################################### HELP

        ctx.font = '16px sans-serif'
        n = Node("CD")
        n.particle.x = x + arc_length
        n.particle.y = y
        n.plot_disc_current(ctx, self.t_frozen)
        ctx.fillStyle = color_static
        ctx.fillText(_("Current"), x + 2 * arc_length, y + 6)

        y += line_height
        n.particle.x = x + arc_length
        n.particle.y = y
        n.plot_disc_goal(ctx, self.t_frozen)
        ctx.fillStyle = color_static
        ctx.fillText(_("Goal"), x + 2 * arc_length, y + 6)

        y += line_height
        n.particle.x = x + arc_length
        n.particle.y = y
        n.followed = True
        n.plot_disc(ctx, self.t_frozen)
        ctx.fillStyle = color_static
        ctx.fillText(_("Path"), x + 2 * arc_length, y + 6)

        ###################################### SCORE
        
        y += line_height
        ctx.fillText(_("Score") + " " + floor(self.score), x, y)
        y += line_height / 2
        ctx.fillText(_("GameHigh") +' ' + floor(self.this_time_highscore), x, y)
        y += line_height / 2
        if self.highlight_highscore:
            ctx.fillStyle = "#00C000"
        ctx.fillText(_("High") + ' ' + floor(self.highscore), x, y)

        ctx.fillStyle = color_static
        y += line_height / 2
        for m in _("Help").split('\n'):
            y += line_height / 2
            ctx.fillText(m, x, y)

        y += line_height
        ctx.fillText(_("Level")
                     + ' ' + classname(self.stage)[1:].replace("_", ".")
                     + '.' + self.stage.nr_times,
                     x, y)

        if goal:
            self.start_animation = self.time
            self.stage.next()
            self.update_score()
            return

    def keypress(self, event):
        if event.ctrlKey:
            return
        if event.key == 'Backspace':
            self.answer = self.answer[:-1]
        elif event.key == 'Shift':
            pass
        elif event.key == 'Tab':
            t = []
            name = self.answer.split("/")[-1]
            is_dir = {}
            if name != '':
                for i in self.nodes[self.new_current].parent.edges:
                    if not i.destination.tmp and i.name.startswith(name):
                        t.append(i.name)
                        is_dir[i.name] = i.destination.is_dir()
            if len(t) != 0:
                t.sort()
                self.answer = self.answer[:-len(name)] + t[0]
                if is_dir[t[0]]:
                    self.answer += '/'
        elif event.key == 'F1':
            _.language = 'fr'
        elif event.key == 'F2':
            _.language = 'en'
        elif event.key == 'F3':
            self.askname()
        elif event.key == 'F4':
            self.animate = not self.animate
        elif event.key == 'F5':
            return
        elif event.key == 'F6':
            self.draw_particles = not self.draw_particles
        elif event.key == 'F9':
            self.do_goal_animation = not self.do_goal_animation
        elif event.key == 'F11' or event.key == 'F12':
            if event.key == 'F11':
                what = "current"
            else:
                what = "goal"
            document.getElementById(what).src = prompt(_(what))
            t = []
            for i in ["current", "goal"]:
                src = document.getElementById(i).src
                if src.endswith('/undefined') or src.endswith('/null'):
                    src = ''
                t.append(src)
            window.location.hash = '¤'.join(t)
        elif len(event.key) == 1:
            self.answer += event.key
        else:
            print(event)
            return
        event.stopPropagation()
        event.preventDefault()

def shuffle(table):
    t = []
    for i in table:
        t.push(i)
    for i in range(len(t)):
        n1 = floor(Math.random() * len(t))
        n2 = floor(Math.random() * len(t))
        t[n1], t[n2] = t[n2], t[n1]
    return t

    
class S2: pass
class S3: pass
class S4: pass
class S5: pass
class S6: pass
class S7: pass
class S8: pass
class S9: pass
class S10: pass
        
class S1:
    nodes = ["/", "/bin/", "/etc/", "/tmp/", "/lib/", "/usr/"]
    no_slash = True
    need_slash = False
    goals = ["/bin", "/etc", "/lib", "/tmp", "/usr"]
    currents = [""]
    current_and_goal = []
    links = []

    # constants
    random_goals = []
    random_currents = []
    random_current_and_goal = []
    nr_times = 0
        
    def __init__(self, graph):
        self.graph = graph
        self.graph.stage = self
        for i in self.nodes:
            self.graph.add(i)
        for i, link in self.links:
            self.graph.add(i, link_to=link)
        self.init()
        self.graph.score_add *= 2

    def init(self):
        n = Node("")
        n.particle.x = 0
        n.particle.y = 0
        current = self.graph.nodes[self.graph.current]
        goal = self.graph.nodes[self.graph.goal]
        if current:
            old_current = current.copy()
        else:
            old_current = n
        if goal:
            old_goal = goal.copy()
        else:
            old_goal = n
        self.set_current_and_goal()
        self.graph.answer = ""
        self.graph.current_anim = Edge("", old_current,
                                       self.graph.nodes[self.graph.current], 0)
        self.graph.goal_anim = Edge("", old_goal,
                                    self.graph.nodes[self.graph.goal], 0)
        
    def set_current(self):
        if len(self.random_currents) == 0:
            self.random_currents = shuffle(self.currents)
        self.graph.current = self.random_currents.pop()
        
    def set_goal(self):
        if len(self.random_goals) == 0:
            self.random_goals = shuffle(self.goals)
        self.graph.goal = self.random_goals.pop()

    def set_current_and_goal_(self):
        if len(self.current_and_goal) != 0:
            if len(self.random_current_and_goal) == 0:
                self.random_current_and_goal = shuffle(self.current_and_goal)
            (self.graph.current, self.graph.goal
            ) = self.random_current_and_goal.pop()
        else:
            self.set_current()
            self.set_goal()

    def set_current_and_goal(self):
        self.set_current_and_goal_()

    def get_question(self):
        return _(classname(self))
            
    def get_message(self):
        return _(classname(self) + '_' + (1+self.nr_times))

    def message(self):
        m = self.get_message()
        if self.graph.answer:
            a = self.graph.answer
            if self.no_slash and a.startswith('/'):
                m += "\n**" + _("/_not_needed")
            if self.need_slash and not a.startswith('/'):
                m += "\n**" + _("/_needed")
            if self.need_dot and not a.startswith('.'):
                m += "\n**" + _("._needed")
            if self.need_dotdot and len(a) == 2 and not a.startswith('..'):
                m += "\n**" + _(".._needed")
            if self.need_dotdot and len(a) > 2 and not a.startswith('../'):
                m += "\n**" + _("../_needed")
        return m

    def next_stage(self):
        return S2(self.graph)

    def next(self):
        self.nr_times += 1
        if not self.get_message():
            self.graph.stage = self.next_stage()
        else:
            self.init()

    def highlight_message(self):
        return True

    def highlight_question(self):
        return self.nr_times == 0

class S2(S1):
    nodes = ["/bin/ls", "/bin/cp", "/bin/mv"]
    goals = nodes
    def next_stage(self):
        return S3(self.graph)

class S3(S2):
    nodes = []
    currents = ["/bin"]
    def next_stage(self):
        return S4(self.graph)

class S4(S2):
    no_slash = False
    need_slash = True
    nodes = ["/usr/bin/", "/usr/lib/", "/usr/bin/emacs", "/usr/bin/vim.tiny",
             "/usr/lib/ssl/"]
    currents = ["/usr/lib", "/usr/bin"]
    goals = ["/bin", "/etc", "/tmp"]
    def next_stage(self):
        return S5(self.graph)

class S5(S1):
    no_slash = False
    need_dot = True
    nodes = []
    current_and_goal = [
        ["/bin", "/bin"],
        ["/usr/bin", "/usr/bin"],
        ["/usr/lib/ssl", "/usr/lib/ssl"]
    ]
    def next_stage(self):
        return S6(self.graph)

class S6(S1):
    no_slash = False
    nodes = ["/usr/include/", "/usr/include/GL/", "/usr/include/GL/gl.h"]
    current_and_goal = [ ["/usr/include/GL", "/usr/include"],
                         ["/usr/lib/ssl", "/usr/lib"] ]
    def next_stage(self):
        return S7(self.graph)


class S7(S1):
    no_slash = False
    need_dotdot = True
    nodes = ["/etc/emacs/", "/etc/alternatives/",
             "/usr/bin/ssh"]
    current_and_goal = [
        ["/usr/bin", "/usr/lib"],
        ["/usr/include", "/usr/bin"],
        # ["/etc/ssh", "/etc/emacs"],
    ]
    def next_stage(self):
        return S8(self.graph)

class S8(S1):
    no_slash = False
    nodes = []
    goals = []
    currents = []
    level = 4

    def set_current_and_goal(self):
        while True:
            r = floor(Math.random() * self.level)
            if r == 0:
                # .
                g = c = self.graph.get_a_dir(2, 0)
            elif r == 1:
                # ..
                c = self.graph.get_a_dir(3, 0)
                g = self.graph.nodes[c].parent.name
            elif r == 2:
                # ../sibling
                c = self.graph.get_a_dir(3, 2)
                while True:
                    g = self.graph.nodes[c].parent.get_a_child()
                    if g != c:
                        break
            elif r == 3:
                # From top
                c = self.graph.get_a_dir(4, 0)
                g = self.graph.nodes[''].get_a_child()
            elif r == 4:
                # Use symbolic link
                self.set_current_and_goal_()
                return
            else:
                c = self.graph.get_a_dir(0, 0)
                g = self.graph.get_a_node(0, 0)
            if self.graph.current != c and self.graph.goal != g:
                break
        self.graph.current = c
        self.graph.goal = g

    def next_stage(self):
        self.graph.show_absolute_path = False
        self.graph.nodes["/usr"].translate_y = -4 * arc_length
        return S9(self.graph)

    def n(self):
        if debug:
            return 1
        else:
            return 10
        
    def get_message(self):
        if self.nr_times == 0:
            return _("S8_1")
        if self.nr_times == self.n():
            return # Next stage
        return _("S8_2") + ' ' + (self.n() - self.nr_times) + ' ' + _("S8_3")

    def highlight_message(self):
        return self.nr_times == 0

class S9(S1):
    nodes = []
    links = [["/etc/alternatives/vi", "/usr/bin/vim.tiny"],
             ["/usr/bin/vi", "/etc/alternatives/vi"],
             ["/usr/bin/rlogin", "ssh"],
             ["/tmp/toto", "../usr/include/GL/gl.h"],
             ]
    current_and_goal = [
        ["/etc/alternatives", "/usr/bin/vim.tiny"],
        ["/tmp", "/usr/include/GL/gl.h"],
        ["/usr/bin", "/usr/bin/vim.tiny"],
        ["", "/usr/include/GL/gl.h"],        
        ]
    def next_stage(self):
        return S10(self.graph)
    def message(self):
        length = len(self.graph.answer)
        c = self.graph.current
        if self.graph.goal == '/usr/bin/vim.tiny' and length > 2:
            return "**2 " + _("letters")
        if c == '/tmp' and length > 4:
            return "**4 " + _("letters")
        if c == '' and length > 9:
            return "**9 " + _("letters")
        return ''

class S10(S8):
    level = 10
    current_and_goal = [
        ["/etc/alternatives", "/usr/bin/vim.tiny"],
        ["/tmp", "/usr/include/GL/gl.h"],
        ["/usr/bin", "/usr/bin/vim.tiny"],
        ["", "/usr/include/GL/gl.h"],        
        ]
    def get_message(self):
        return _("S10_1")
    def next_stage(self):
        return self

def fyp():
    g = Graph()
    s = S1(g)
    g.start_animation = g.time - 1
            
    if javascript:
        (document.getElementById("current").src, document.getElementById("goal").src) = decodeURI(window.location.hash[1:]).split('¤')
        def keypress(event):
            g.keypress(event)
        document.addEventListener("keydown", keypress);

        c = document.getElementsByTagName("CANVAS")[0]
        ctx = c.getContext("2d")
        def animate():
            if g.stop:
                return
            g.time += 1
            if g.animate:
                g.t_frozen += 1
            ctx.fillStyle = "#FFFFFF"
            ctx.fillRect(0, 0, c.width, c.height)
            g.move()
            g.plot(ctx)

        g.update_score_iframe()
        animate()
        animate()
        setInterval(animate, 40)

fyp()
