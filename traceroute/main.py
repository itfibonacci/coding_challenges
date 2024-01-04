# let's add command line parsing
import argparse
import re
from sys import exit
import socket
import struct

def main():
	parser = argparse.ArgumentParser("traceroute", description="This is a traceroute application. Use the --num_of_players option to specify the number of players and the --num_of_cards option to specify the number of cards. The number of cards must be greater than or equal to six times the number of players.")
	
	parser.add_argument('endpoint', type=str, help="Pass an http link, example: 'https://docs.python.org/'") 
	args = parser.parse_args()
	traceroute(args.endpoint)

def is_valid_http_url(url):
	# Regular expression for validating an HTTP URL
	url_pattern = re.compile(
		r'^(?:(https?|ftp)://)?'  # http:// or https:// or ftp://
		r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
		r'localhost|'  # localhost...
		r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
		r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
		r'(?::\d+)?'  # optional port
		r'(?:/?|[/?]\S+)$', re.IGNORECASE)
	
	return re.match(url_pattern, url)

def traceroute(endpoint):
	if is_valid_http_url(endpoint):
		print(endpoint)
	else:
		print(f'Error: The provided URL ({endpoint}) is not a valid HTTP URL.')
		exit(1)
	
	# Create a TCP socket 

def create_icmp_packet():
	icmp_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
	ICMP_ECHO_REQUEST = 8  # ICMP Echo Request type
	ICMP_CODE = 0  # ICMP code for Echo Request
	icmp_header = struct.pack('!BBHHH', ICMP_ECHO_REQUEST, ICMP_CODE, 0, 0, 0)
	


def handle_icmp_echo():
	pass


if __name__ == "__main__":
	main()