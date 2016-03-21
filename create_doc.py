#!/usr/bin/python3

import collections
import colorize

children = collections.defaultdict(list)

for name, value in colorize.__dict__.items():
    try:
        children[value.__bases__[0].__name__].append(value.__name__)
    except (AttributeError, IndexError):
        pass

def tree(node):
    try:
        color = colorize.__dict__[node]().color()
    except TypeError:
        color = colorize.__dict__[node]("").color()
    style = ('<span style="color:%s">%s</span>' % (color[0], color[0])
             + '<span style="background:%s">%s</span>' % (color[1], color[1])
         )
    print(('<div>%s %s<ul>' % (style, node)))
    for child in sorted(children[node]):
        print('<li>')
        tree(child)
    print('</ul>')

tree("Chars")
tree("Container")

