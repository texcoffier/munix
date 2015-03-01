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

def sheexp():
    document.write("""
    <link rel="stylesheet" href="colorize.css" type="text/css">
    <div id="sheexp_editor">
        <input id="sheexp_input"
           onkeyup="update();setTimeout(update,1)"
           onkeydown="update();setTimeout(update,1)"
           onclick="update();setTimeout(update,1)"
           onpaste="update()"
           onkeypress="setTimeout(update,1)"
           >
        <div id="sheexp_output"></div>
        <div id="sheexp_help"></div>
        </div>
    <pre id="sheexp_debug"></pre>
    """)
    update.editor  = document.getElementById("sheexp_editor")
    update.input   = document.getElementById("sheexp_input")
    update.output  = document.getElementById("sheexp_output")
    update.help    = document.getElementById("sheexp_help")
    update.debug   = document.getElementById("sheexp_debug")
    update.display_debug = False
    update.input.focus()
    update()
    setTimeout("update.last = undefined ; update()", 1)

def update():
    position = update.input.selectionStart
    if update.input.value == update.last and position == update.last_position:
        return
    update.last = update.input.value
    update.last_position = position
    p = Parser(update.last).parse()
    update.debug.innerHTML = update.display_debug and p.nice() or ''
    update.output.innerHTML = p.html(position)
    update.help.innerHTML = p.help(position)
    if (update.input.selectionEnd == update.input.textLength
        and update.editor.scrollLeft != 0 ):
        update.editor.scrollLeft += 4
    create_links(update.help, update.editor.scrollLeft)

link_opacity = "1"
colors = [
    'rgba(180,255,255,' + link_opacity + ')',
    'rgba(255,255,180,' + link_opacity + ')',
    'rgba(255,180,255,' + link_opacity + ')',
    'rgba(180,180,255,' + link_opacity + ')',
    'rgba(180,255,180,' + link_opacity + ')',
    'rgba(230,230,230,' + link_opacity + ')',
    ]

def create_links(output, scrollLeft):
    border = 0
    i = 0
    help_boxes = []
    for item in output.childNodes:
        if item.id:
            if document.getElementById('P' + item.id[1:]):
                help_boxes.append(item)
                item.style.width = item.firstChild.offsetWidth + 'px'
    nr_help = len(help_boxes)
    for help_box in help_boxes:
        place = document.getElementById('P' + help_box.id[1:])
        n = document.createElement('VAR')
        n.className = "link " + help_box.className
        n.id = 'L' + help_box.id[1:]
        n.style.left = place.offsetLeft + "px"
        top = place.offsetHeight + border
        color = colors[(nr_help+i+100)%len(colors)]
        n.style.top = str(top) + "px"
        n.style.height = str(help_box.offsetTop - place.offsetHeight
                             - 2*border) + "px"
        n.style.width = place.offsetWidth + "px"
        n.style.zIndex = i*2
        n.style.background = color
        n.style.paddingLeft = 0
        help_box.style.zIndex = 2*i - 1
        help_box.style.background = color
        editor_width = help_box.parentNode.parentNode.offsetWidth
        slack = (place.offsetWidth - help_box.offsetWidth)/2
        left = place.offsetLeft + slack
        if slack < 0:
            help_box.style.borderTopLeftRadius = '1em'
            help_box.style.borderTopRightRadius = '1em'
        if left < scrollLeft:
            left = scrollLeft
        elif left + help_box.offsetWidth > scrollLeft + editor_width:
            left -= (left + help_box.offsetWidth) - (scrollLeft + editor_width)
        help_box.style.marginLeft = left + 'px'
        i -= 1
        output.appendChild(n)
