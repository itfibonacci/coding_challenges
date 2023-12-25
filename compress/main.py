from frequency_counter import frequency_counter
from priority_queue import priority_queue
from huffman_tree import HuffmanTree

from heapq import heappop

def main():

	#frequencies = frequency_counter("./135-0.txt")
	txt_file = "./small_sample.txt"

	frequencies = frequency_counter(txt_file)

	heaped_frequencies = priority_queue(frequencies)
	print(len(heaped_frequencies))
	
	huffman_tree = HuffmanTree()
	huffman_tree.build_tree(heaped_frequencies=heaped_frequencies)
	print(huffman_tree.build_codes_dict())
	print(text_to_codes(txt_file, huffman_tree.build_codes_dict()))

def text_to_codes(txt_file, codes_dict):
	result = ""
	with open(txt_file) as file:
		for line in file:
			for char in line:
				result += f"{codes_dict[char]}"
	return result

if __name__ == "__main__":
	main()

"""
hello there

r: 1
t: 1
o: 1
l: 2
h: 2
e: 3

"""