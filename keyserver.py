#!/usr/bin/python3

"""
Log are stored one file per browser IP

Each lineof the log file is a game, defined by a dictionnary:

  * nr_tests:int
  * nr_digits:int
  * time:int seconds
  * tests:List of List
    * name:str
    * List[int] the 'nr_tests' times

When sending stats to the browser, they are averaged. It is a dictionnary

* n: nr digits
   * n: the game number
     * 0: List[int] the average time for each method played
     * 1: List[int] the stddev time for each method played
     * 2: List[int] the number of good answer for each method played
     * 3: int an anonymous ID

"""


import json
import time
import collections
import os
import sys
import http.server

import key

FILES = {
    '/key.html': ('key.html', 'text/html'),
    '/': ('intro.html', 'text/html'),
    '/key.js': ('key.js', 'application/javascript'),
    '/favicon.ico': ('key.png', 'image/png'),
}

if not os.path.exists('LOGS-KEYS'):
    os.mkdir('LOGS-KEYS')

def read(filename):
    """Returns the file content as bytes"""
    with open(filename, 'rb') as file:
        return file.read()

FILENAMES = {}
def index(filename):
    """Get a number for the filename."""
    if filename not in FILENAMES:
        FILENAMES[filename] = len(FILENAMES)
    return FILENAMES[filename]

class Stats:
    """Progressive stats.
    Nr_digits => list of full tests (student) => list of average,stddev times (methods)
    """
    def __init__(self):
        self.stats = collections.defaultdict(list)
        for filename in sorted(
                os.listdir('LOGS-KEYS'),
                key=lambda name: os.path.getmtime('LOGS-KEYS/' + name)
                ):
            with open('LOGS-KEYS/' + filename, 'r') as file:
                filekey = index(filename)
                for line in file:
                    self.add_line(json.loads(line), filekey)

    def add_line(self, line, filekey):
        """Update with a new stat"""
        stat_average = [0] * len(key.METHODS)
        stat_stddev = [0] * len(key.METHODS)
        stat_nr_goods = [0] * len(key.METHODS)
        self.stats[line['nr_digits']].append(
            [stat_average, stat_stddev, stat_nr_goods, filekey])
        for method, times in line['tests']:
            sum_time = 0
            sum_time2 = 0
            nr_time = 0
            for value in times[1:]: # Remove first
                if value > 0:
                    sum_time += value
                    sum_time2 += value * value
                    nr_time += 1
            i = key.METHODS.index(method)
            if nr_time:
                stat_average[i] = int(sum_time / nr_time)
                stat_stddev[i] = int((sum_time2 / nr_time - (sum_time / nr_time) ** 2) ** 0.5)
                stat_nr_goods[i] = nr_time

    def json(self):
        """..."""
        return json.dumps(self.stats, separators=(',', ':'))

STATS = Stats()

class MyRequestBroker(http.server.BaseHTTPRequestHandler):
    """Record tests and send application and stats"""
    def do_POST(self): # pylint: disable=invalid-name
        """Record tests"""
        client_ip = self.headers["x-forwarded-for"] or self.client_address[0]
        try:
            charset = self.headers['Content-Type'].split('charset=')[1]
        except IndexError:
            charset = 'utf-8'
        assert '/' not in client_ip
        assert '\n' not in client_ip
        assert '\r' not in client_ip
        data = self.rfile.read(int(self.headers['Content-Length']))
        if data:
            data = json.loads(data.decode(charset))
            data['time'] = time.time()
            with open(f'LOGS-KEYS/{client_ip}', 'a') as file:
                file.write(json.dumps(data) + '\n')
            STATS.add_line(data, index(client_ip))
        self.send_stats()

    def send_stats(self):
        """Send the JSON files with the stats to the browser"""
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('Connection', 'close')
        self.end_headers()
        self.wfile.write(STATS.json().encode('latin1'))

    def do_GET(self): # pylint: disable=invalid-name
        """Send data"""
        if self.path in FILES:
            self.send_response(200)
            self.send_header('Content-Type', FILES[self.path][1])
            self.send_header('Cache-Control', 'no-cache')
            self.send_header('Connection', 'close')
            self.end_headers()
            self.wfile.write(read(FILES[self.path][0]))
            return
        if self.path == '/stats.json':
            self.send_stats()
            return
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('Connection', 'close')
        self.end_headers()
        self.wfile.write(b'On essaye de me pirater !')

try:
    HOST = sys.argv[1]
except IndexError:
    HOST = '127.0.0.1'
try:
    PORT = int(sys.argv[2])
except IndexError:
    PORT = 17171

SERVER = http.server.HTTPServer((HOST, PORT), MyRequestBroker)

print(f"http://{HOST}:{PORT}/")

while True:
    SERVER.handle_request()
