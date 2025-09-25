#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler, test
import sys
import os

web_dir = os.path.dirname(__file__)

class RequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    os.chdir(web_dir)
    test(RequestHandler, HTTPServer, port=int(sys.argv[1]) if len(sys.argv) > 1 else 8765)
