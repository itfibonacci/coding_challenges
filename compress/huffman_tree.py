from heapq import heappop, heappush

from huffman_node import HuffmanNode

"""
In a Huffman tree module, you can have two main classes: `HuffmanNode` and `HuffmanTree`. Each class serves a distinct purpose in representing the nodes of the Huffman tree and managing the overall tree structure. Here's a brief overview of each class:

2. **`HuffmanTree` Class:**
   - Manages the overall structure of the Huffman tree.
   - Handles the construction of the Huffman tree, generation of Huffman codes, and the encoding and decoding processes.
   - May include methods for creating compressed files, reading compressed files, and writing decompressed files.

With these two classes, you can encapsulate the functionality needed for Huffman coding, and the division of responsibilities between the classes helps maintain a clear and modular design.

Additionally, you might have some utility functions or constants that are not encapsulated within a class, depending on the specific needs of your implementation.

Keep in mind that the number of classes can vary based on the design choices and complexity of your implementation. In this case, starting with two main classes (`HuffmanNode` and `HuffmanTree`) provides a good foundation, and you can extend or modify the design as needed based on the specific requirements of your project.

### Additional Considerations:

- Ensure that the Huffman tree is constructed and behaves as expected, with internal nodes representing merged characters based on their frequencies.

- Provide a clean interface for users to interact with the `HuffmanTree` class, allowing them to easily compress and decompress text.

- Encapsulate the implementation details within the classes to promote modularity and maintainability.

- Design methods that handle edge cases gracefully, such as empty input or special characters.

- Implement error handling mechanisms to address potential issues during tree construction, encoding, and decoding.

By designing your Huffman tree module with these considerations in mind, you can create a well-structured and effective implementation for Huffman coding.
"""

"""
### `HuffmanTree` Class:

#### Attributes:
1. **Root (`root`):**
   - Reference to the root of the Huffman tree.

#### Methods:
1. **Build Tree (`build_tree`):**
   - Given a frequency dictionary, build the Huffman tree.
   - This involves constructing `HuffmanNode` instances and arranging them into a tree structure.

2. **Generate Codes (`generate_codes`):**
   - Traverse the Huffman tree to generate codes for each character.
   - Return a dictionary mapping characters to their corresponding Huffman codes.

3. **Encode Text (`encode_text`):**
   - Given a text and the generated Huffman codes, encode the text.

4. **Decode Text (`decode_text`):**
   - Given the encoded text and the Huffman tree, decode the text.

5. **Create Compressed File (`create_compressed_file`):**
   - Create a compressed file containing the Huffman tree information and the encoded text.

6. **Read Compressed File (`read_compressed_file`):**
   - Read a compressed file, extract the Huffman tree information, and return the Huffman tree.

7. **Write Decompressed File (`write_decompressed_file`):**
   - Write the decompressed text to an output file.
"""

class HuffmanTree():
	def __init__(self) -> None:
		self.root = None

	def build_tree(self, heaped_frequencies):
		while len(heaped_frequencies) > 1:
			l_node = heappop(heaped_frequencies)
			r_node = heappop(heaped_frequencies)
			internal_node = HuffmanNode(frequency=r_node.frequency+l_node.frequency, right_child=r_node, left_child=l_node)
			heappush(heaped_frequencies, internal_node)
		self.root = heappop(heaped_frequencies)

	def generate_codes(self, node, current_code, codes):
		if node is None:
			return

		if node.left_child is None and node.right_child is None:  # leaf node
			codes[node.char] = current_code

		self.generate_codes(node.left_child, current_code + "0", codes)
		self.generate_codes(node.right_child, current_code + "1", codes)

		return codes

	def build_codes_dict(self):
		return self.generate_codes(self.root, "", {})

	def _preorder_traversal(self, node, depth=0):
		if node is None:
			return ''
		s = '    ' * depth + str(node) + '\n'
		s += self._preorder_traversal(node.left_child, depth + 1)
		s += self._preorder_traversal(node.right_child, depth + 1)
		return s

	def __str__(self):
		return self._preorder_traversal(self.root)
