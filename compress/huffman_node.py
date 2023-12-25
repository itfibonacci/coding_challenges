"""
1. **`HuffmanNode` Class:**
   - Represents an individual node in the Huffman tree.
   - Handles the attributes and methods associated with individual nodes, such as character, frequency, and child nodes.

### `HuffmanNode` Class:

#### Attributes:
1. **Character (`char`):**
   - Represents the character associated with the node. For internal nodes, this can be `None`.

2. **Frequency (`frequency`):**
   - Holds the frequency of the character associated with the node.

3. **Left Child (`left`):**
   - Reference to the left child of the node. For leaf nodes, this can be `None`.

4. **Right Child (`right`):**
   - Reference to the right child of the node. For leaf nodes, this can be `None`.

#### Methods:
1. **Initialization (`__init__`):**
   - Initialize a `HuffmanNode` instance with a character, frequency, and optional left and right children.
"""

class HuffmanNode():
	def __init__(self, char=None, frequency=0, right_child=None, left_child=None):
		self.char = char
		self.frequency = frequency
		self.right_child = right_child
		self.left_child = left_child

	def is_leaf(self):
		return not self.left_child and not self.right_child

	def __str__(self) -> str:
		return f"{self.char}: {self.frequency}"

	def __lt__(self, other):
		return self.frequency < other.frequency