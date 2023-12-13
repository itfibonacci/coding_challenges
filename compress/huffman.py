#!/opt/homebrew/Caskroom/miniconda/base/bin/python3
#https://codingchallenges.fyi/challenges/challenge-huffman

# start by building a frequency counter
import time

def frequency_counter(filename):
	start = time.time()
	frequencies = {}
	with open(filename) as file:
		for line in file:
			for char in line:
				if char in frequencies:
					frequencies[char] += 1
				else:
					frequencies[char] = 1
	end = time.time()
	print(f'Elapsed time is: {end - start}')
	return frequencies

def time_it(filename):
	start = time.time()
	end = time.time()
	print(f'Elapsed time is: {end - start}')

def sort_dictionary(dictionary):
	return dict(sorted(dictionary.items(), key=lambda item: item[1]))

print(sort_dictionary(frequency_counter("./135-0.txt")))
#bad_frequency_counter("./135-0.txt")