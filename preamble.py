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

String.prototype.lower = String.prototype.toLowerCase
String.prototype.strip = String.prototype.trim
o = Object
o.defineProperty(Array.prototype, 'append' ,
                 {'enumerable': False,'value': Array.prototype.push}) ;

def sum(t):
    v = 0
    for x in t:
        v += x
    return v

def repr(o):
    return JSON.stringify(o)
str = repr

def __join__(t):
    return t.join(this)
String.prototype.join = __join__

