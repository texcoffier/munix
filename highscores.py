#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#    TOMUSS: The Online Multi User Simple Spreadsheetl)
#    Copyright (C) 2017 Thierry EXCOFFIER, Universite Claude Bernard
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

"""
"""

import os
import ast
import cgi
import time
import atexit
import urllib.parse
import http.server

with open("fyp.html", "r") as f:
    html = f.read().encode("utf-8")

with open("fyp.js", "r") as f:
    js = f.read().encode("utf-8")

images = {}
for img in ():
    with open(img[1:], "rb") as f:
        images[img] = f.read()
    
style = """
<style>
BODY { font-family: sans-serif; white-space: nowrap; overflow: hidden }
TD { overflow: auto }
TABLE {
   display: inline-block;
   max-width: 8em;
   min-width: 8em;
   background: #FFF;
   position: relative;
   overflow: hidden;
   vertical-align: top ;
   border: 1px solid #888 ;
   transition: max-width 1s;
   -webkit-transition: max-width 1s;
}
TABLE:hover {
   max-width: 20em ;
   overflow: initial;
}
TR:first-child { font-size: 70% }
TR:nth-child(2) { white-space: nowrap }
TR:last-child { font-size: 70% }
.me { background: #0F0; }
A { cursor: pointer ; position: absolute ; right: 0px }
A:hover { background: #F88 }
</style>
<script>
function d(t)
{
  if ( ! confirm("remove 🗑 SCORE 🗑 delete ") )
      return ;
  while ( t.tagName != 'TABLE' )
    t = t.parentNode ;
  t = t.getElementsByTagName("TD")[1] ;
  var s = window.location.search.split("&delete")[0] ;
  
  window.location.search = s + "&delete=" + encodeURIComponent(t.textContent) ;
}
</script>
"""

class Scores:
    def __init__(self):
        self.last_write = 0
        self.read_scores()
        atexit.register(self.write_scores, force=True)

    def read_scores(self):
        if os.path.exists("scores.py"):
            with open("scores.py", "r") as f:
                self.scores = ast.literal_eval(f.read())
        else:
            self.scores = {}
            i = 10
            for name in ("Titeuf", "Tarzan", "Asterix", "Obelix",
                         "Volverine", "Hulk",
                         "Batman", "Batwoman",
                         "Spider-Man", "Ironman", "Superman",
                         "Wonder Woman"):
                self.scores[name] = i
                i *= 2
            self.write_scores()
        self.sorted = sorted(self.scores,
                             key=self.scores.__getitem__,
                             reverse=True)
            
    def write_scores(self, force=False):
        if not force and time.time() - self.last_write < 60:
            return
        self.last_write = time.time()
        with open("scores.py.new", "w") as f:
            f.write(repr(self.scores))
        os.rename("scores.py.new", "scores.py")
        
    def add(self, user, score):
        if score <= self.scores.get(user, 0):
            return # Not better
        if user not in self.scores:
            self.sorted.append(user)
        self.scores[user] = score
        self.write_scores()

        # Update sorted
        i_old = self.sorted.index(user)
        i = i_old - 1
        while i >= 0 and self.scores[self.sorted[i]] < score:
            i -= 1
        i += 1
        self.sorted[i:i_old+1] = [user] + self.sorted[i:i_old]

    def delete(self, user):
        if user in self.scores:
            self.scores.pop(user)
            self.sorted.remove(user)
            self.write_scores()

    def display(self, i, j, me):
        if not self.scores:
            return []
        if i < 0:
            i = 0
        if j > len(self.scores):
            j = len(self.scores)
        t = []
        for k in self.sorted[i:j]:
            i += 1
            t.append((
                '<table class="{}">'
                '<tr><td>#{}<a onclick="d(this)">×</a></tr>'
                '<tr><td>{}</tr>'
                '<tr><td>{}</tr>'
                '</table>\n').format(
                "me" if k == me else '', i, cgi.escape(k), self.scores[k]))
        return t
        
    def the_scores(self, me):
        nb_scores = 8
        try:
            i = self.sorted.index(me)
        except ValueError:
            i = 0
        if i < nb_scores:
            return self.display(0, max(i, nb_scores), me)
        
        return (self.display(0, nb_scores//2 - 1, me)
                + ['<table style="min-width: initial; border: 0px">'
                   '<tr><td> </tr><td>...</tr><td></tr>'
                   '</table>']
                + self.display(i -  nb_scores//4, i + nb_scores//4 + 1, me)
                )
        
scores = Scores()

class MyRequestBroker(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html;charset=utf-8')
            self.send_header('Cache-Control', 'no-cache')
            self.send_header('Content-Length', str(len(html)))
            self.send_header('Connection', 'close')
            self.end_headers()
            self.wfile.write(html)
        elif self.path == '/fyp.js':
            self.send_response(200)
            self.send_header('Content-Type',
                             'application/x-javascript;charset=utf-8')
            self.send_header('Cache-Control', 'no-cache')
            self.send_header('Content-Length', str(len(js)))
            self.send_header('Connection', 'close')
            self.end_headers()
            self.wfile.write(js)
        elif self.path in images:
            image = images[self.path]
            self.send_response(200)
            self.send_header('Content-Type', 'image/png')
            self.send_header('Cache-Control', 'no-cache')
            self.send_header('Content-Length', str(len(image)))
            self.send_header('Connection', 'close')
            self.end_headers()
            self.wfile.write(js)
        else:
            self.send_response(200)
            self.send_header('Content-Type', 'text/html;charset=utf-8')
            self.send_header('Cache-Control', 'no-cache')
            self.send_header('Connection', 'close')
            self.end_headers()
            f = urllib.parse.parse_qs(self.path.split('?')[-1])
            if 'name' in f:
                me = f['name'][0].title()
            else:
                me = ''
            if 'score' in f:
                score = int(f['score'][0])
            else:
                score = 0
            if me != '':
                scores.add(me, score)
            if 'delete' in f:
                scores.delete(f['delete'][0])

            self.wfile.write((style
                              + ' '.join(scores.the_scores(me))
                              ).encode("utf-8"))
                               

server = http.server.HTTPServer(("0.0.0.0", 8880), MyRequestBroker)
while True:
    server.handle_request()
