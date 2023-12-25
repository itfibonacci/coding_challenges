from frequency_counter import frequency_counter
from priority_queue import priority_queue
from huffman_tree import HuffmanTree

from heapq import heappop

def main():

	frequencies = frequency_counter("./135-0.txt")

	#frequencies = frequency_counter("./small_sample.txt")

	heaped_frequencies = priority_queue(frequencies)
	print(len(heaped_frequencies))
	
	huffman_tree = HuffmanTree()
	huffman_tree.build_tree(heaped_frequencies=heaped_frequencies)
	print(huffman_tree.print_codes())


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