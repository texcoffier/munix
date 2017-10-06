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

def sheexp(container):
    e = document.createElement('DIV')
    e.id = "sheexp_editor"
    e.innerHTML = """
        <input id="sheexp_input"
           spellcheck="off"
           autocorrect="off"
           autocapitalize="off"
           autocomplete="off"
           >
        <div tabindex="-1" id="sheexp_output"></div>
        <div id="sheexp_help"></div>
        <pre id="sheexp_debug"></pre>"""
    e.style.width = container.offsetWidth
    container.appendChild(e)
    update.editor  = document.getElementById("sheexp_editor")
    update.input   = document.getElementById("sheexp_input")
    update.output  = document.getElementById("sheexp_output")
    update.help    = document.getElementById("sheexp_help")
    update.debug   = document.getElementById("sheexp_debug")
    update.display_debug = False
    update.input.onkeyup    = update
    update.input.onkeydown  = update
    update.input.onkeypress = update
    update.input.onclick    = update
    update.input.onpaste    = update
    update.input.focus()
    setInterval(update, 20)

def update():
    update_real_fast()
    setTimeout(update_real_slow, 1)

def update_real_fast():
    if update.input.value == update.last:
        return
    update.last = update.input.value
    update.last_position = -1
    update.parsed = Parser(update.last).parse()
    update.debug.innerHTML = update.display_debug and p.nice() or ''
    update.output.innerHTML = update.parsed.html(update.input.selectionStart)
    if (update.input.selectionEnd == update.input.textLength
        and update.editor.scrollLeft != 0 ):
        update.editor.scrollLeft += 4

def update_real_slow():
    position = update.input.selectionStart
    if position == update.last_position:
        return
    update.last_position = position
    update.help.innerHTML = update.parsed.help(position)
    if (update.input.selectionEnd == update.input.textLength
        and update.editor.scrollLeft != 0 ):
        update.editor.scrollLeft += 4
    create_links(update.help, update.editor.scrollLeft)

def create_links(output, scrollLeft):
    border = 0
    help_boxes = []
    for item in output.childNodes:
        if item and item.id:
            if document.getElementById('P' + item.id[1:]):
                help_boxes.append(item)
                # + 4 for border width ?
                item.style.width = item.firstChild.offsetWidth + 4 + 'px'
    nr_help = len(help_boxes)
    for help_box in help_boxes:
        place = document.getElementById('P' + help_box.id[1:])
        n = document.createElement('VAR')
        n.className = "link " + help_box.className
        n.id = 'L' + help_box.id[1:]
        n.style.left = place.offsetLeft + "px"
        top = place.offsetHeight + border + 2
        n.style.top = str(top) + "px"
        n.style.height = str(help_box.offsetTop - place.offsetHeight
                             - 2*border) + "px"
        n.style.width = place.offsetWidth + "px"
        n.style.verticalAlign = "bottom"
        n.style.background = help_box.style.background
        n.style.borderLeft = help_box.style.border
        n.style.borderRight = help_box.style.border
        n.style.paddingLeft = 0
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
        help_box.parentNode.insertBefore(n, help_box.parentNode.firstChild)
