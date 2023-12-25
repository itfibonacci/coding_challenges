import heapq
from huffman_node import HuffmanNode

# accepts the frequency table
# build a priority queue based on the frequency table / dictionary

def priority_queue(frequencies):

	frequency_nodes = [ HuffmanNode(char=char, frequency=frequency) for char, frequency in frequencies.items() ]

	# Heapify the list
	heapq.heapify(frequency_nodes)

	return frequency_nodes
