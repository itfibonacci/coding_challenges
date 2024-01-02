"""
Step 1

In this step your goal is to implement a simple API you we can use for testing. For this challenge I’d like you to create two endpoints: /limited and /unlimited.

You can have them return anything you want, for my examples I’ve had them return some text, here is my test to check they work, you should do something similar:

% curl http://127.0.0.1:8080/unlimited
Unlimited! Let's Go!
% curl http://127.0.0.1:8080/limited
Limited, don't over use me!
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/unlimited':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Unlimited! Let\'s Go!')
        elif self.path == '/limited':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Limited, don\'t over use me!')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Page not found')

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

server_thread = threading.Thread(target=run)
