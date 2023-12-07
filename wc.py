#!/opt/homebrew/bin/python3

# https://codingchallenges.fyi/challenges/challenge-wc
# The functional requirements for wc are concisely described by it’s man page - give it a go in your local terminal now:
import sys

def count_bytes(filename):
	with open(filename, 'rb') as file:
		return len(file.read())
	
def count_lines(filename):
	lines = 0
	with open(filename) as file:
		file_data = file.read()
		for ch in file_data:
			if (ch == "\n"):
				lines += 1
	return lines

def count_lines_efficient(filename):
    with open(filename) as file:
        return sum(1 for line in file)

def count_chars(filename):
	chars = 0
	with open(filename) as file:
		for line in file:
			chars += len(line)
	return chars

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print(f"Expecting one argument but got: {len(sys.argv) - 1}")
		sys.exit(1)
	else:
		text_file = sys.argv[2]
		if (sys.argv[1] == "-c"):
			print(f"Counting the bytes in: {text_file}")
			print(count_bytes(text_file))
		elif (sys.argv[1] == "-l"):
			print(f"Counting the lines in: {text_file}")
			print(count_lines(text_file))
		elif (sys.argv[1] == "-m"):
			print(f"Counting the characters in: {text_file}")
			print(count_chars(text_file))
