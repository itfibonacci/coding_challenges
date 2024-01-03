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
import re

from rate_limiter_token_bucket import Bucket

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		if re.match(r'/.*/limited', self.path):
			user = self.path.split('/')[1]
			if user in Bucket.user_bucket:
				bucket = Bucket.get_users_bucket(user)
				if bucket.rate_exceeded():
					self.send_response(429)
					self.end_headers()
					response = b'\n' + user.encode() + b': you have exceeded your limit !'
				else:
					self.send_response(200)
					self.end_headers()
					response = b'\nLimited! Welcome back ' + user.encode() + b'!'
				self.wfile.write(response)
				self.wfile.write(b'\nYour capacity is: ')
				self.wfile.write(str(bucket.capacity).encode())
				self.wfile.write(b'\nYou have: ')
				self.wfile.write(str(bucket.tokens).encode())
				self.wfile.write(b' tokens left')
			else:
				self.send_response(200)
				self.end_headers()
				response = b'Limited! Let\'s Go ' + user.encode() + b'!'
				self.wfile.write(response)
				user_bucket = Bucket(user, 10)
		elif self.path == '/unlimited':
			self.send_response(200)
			self.end_headers()
			self.wfile.write(b'Unlimited! Let\'s go')
		else:
			self.send_response(404)
			self.end_headers()
			self.wfile.write(b'Page not found')

class IPHTTPRequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path == '/limited':
			ip_address = self.client_address[0]
			if ip_address in Bucket.user_bucket:
				bucket = Bucket.get_users_bucket(ip_address)
				if bucket.rate_exceeded():
					self.send_response(429)
					self.end_headers()
					response = b'\n' + ip_address.encode() + b': you have exceeded your limit !'
				else:
					self.send_response(200)
					self.end_headers()
					response = b'\nLimited! Welcome back ' + ip_address.encode() + b'!'
				self.wfile.write(response)
				self.wfile.write(b'\nYour capacity is: ')
				self.wfile.write(str(bucket.capacity).encode())
				self.wfile.write(b'\nYou have: ')
				self.wfile.write(str(bucket.tokens).encode())
				self.wfile.write(b' tokens left')
			else:
				self.send_response(200)
				self.end_headers()
				response = b'Limited! Let\'s Go ' + ip_address.encode() + b'!'
				self.wfile.write(response)
				user_bucket = Bucket(ip_address, 10)
		elif self.path == '/unlimited':
			self.send_response(200)
			self.end_headers()
			self.wfile.write(b'Unlimited! Let\'s go')
		else:
			self.send_response(404)
			self.end_headers()
			self.wfile.write(b'Page not found')

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

server_thread = threading.Thread(target=run)
