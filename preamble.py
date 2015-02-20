
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
    return o.toString()
str = repr

def __join__(t):
    return t.join(this)
String.prototype.join = __join__

