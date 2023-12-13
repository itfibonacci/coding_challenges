#
# Language Statistics: Calculate statistics about the languages used across all repositories.
import requests
import json

def fetch_user_info(username):
	url = f"https://api.github.com/users/{username}"
	response = requests.get(url)
	data = response.json()
	return data

user_info = fetch_user_info('itfibonacci')

print(json.dumps(user_info))