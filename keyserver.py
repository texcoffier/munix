#!/usr/bin/python3

import json
import time
import collections
import os
import sys
import http.server

import key

FILES = {
    '/': ('key.html', 'text/html'),
    '/key.js': ('key.js', 'application/javascript'),
    '/favicon.ico': ('key.png', 'image/png'),
}

def read(filename):
    """Returns the file content as bytes"""
    with open(filename, 'rb') as file:
        return file.read()

filenames = {}
def index(filename):
    """Get a number for the filename."""
    if filename not in filenames:
        filenames[filename] = len(filenames)
    return filenames[filename]
    


class Stats:
    """Progressive stats.
    Nr_digits => list of full tests (student) => list of average,stddev times (methods)
    """
    def __init__(self):
        self.stats = collections.defaultdict(list)
        for filename in os.listdir('LOGS-KEYS'):
            with open('LOGS-KEYS/' + filename, 'r') as file:
                filekey = index(filename)
                for line in file:
                    self.add_line(json.loads(line), filekey)

    def add_line(self, line, filekey):
        """Update with a new stat"""
        stat_average = [0] * len(key.METHODS)
        stat_stddev = [0] * len(key.METHODS)
        self.stats[line['nr_digits']].append([stat_average, stat_stddev, filekey])
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
            if nr_time == len(times) - 1:
                stat_average[i] = int(sum_time / nr_time)
                stat_stddev[i] = int((sum_time2 / nr_time - (sum_time / nr_time) ** 2) ** 0.5)
            else:
                stat_stddev[i] = int(100 * nr_time / (len(times) - 1))

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
        print("BUG")

try:
    HOST = sys.argv[1]
except IndexError:
    HOST = '127.0.0.1'
try:
    PORT = int(sys.argv[2])
except IndexError:
    PORT = 17171

if not os.path.exists('LOGS-KEYS'):
    os.mkdir('LOGS-KEYS')

SERVER = http.server.HTTPServer((HOST, PORT), MyRequestBroker)

print(f"http://{HOST}:{PORT}/")

while True:
    SERVER.handle_request()
