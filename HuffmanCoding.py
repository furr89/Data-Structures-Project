import sys

# Node class storing the character and its frequency
class LeafNode:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.next = None

        self.right = None
        self.left = None

# Tree node to store sum of freeuncy from children nodes
class TreeNode:

    def __init__(self, left_child, right_child, frequency_sum):
        self.left = left_child
        self.right = right_child
        self.frequency = frequency_sum
        self.next = None

# Orders the nodes based on frequency
class PriorityQueue:
    def __init__(self):
        self.head = None
        self.size = 0

    # Adds to the front of the queue
    def push(self, new_node):

        if self.head == None:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head = new_node

        self.size += 1

    # Inserts a node in order of its frequency from low to high
    def priority_insert(self, new_node):
        
        # Insertion if queue is empty
        if self.head == None:
            new_node.next = self.head
            self.head = new_node

        # Insertion when head's frequency is greater
        elif self.head.frequency > new_node.frequency:
            new_node.next = self.head
            self.head = new_node

        # If it's at the middle
        else:
            current = self.head
            while current.next != None and current.next.frequency < new_node.frequency:
                current = current.next

            new_node.next = current.next
            current.next = new_node
        self.size += 1
                     
    # Removes the first item from the queue
    def pop(self):

        if self.get_size() == 0:
            return

        removed_node = self.head
        self.head = self.head.next
        self.size -= 1
        return removed_node

    def get_size(self):
        return self.size

# Returns dictionary with character-frequency pairs
def get_char_frequency(data):

    if data == None or type(data) == int:
        return None

    char_codes = {}

    # Loop through the string
    for char in data:

        # If the character is not present add it
        if char not in char_codes.keys():
            char_codes[char] = 1
        
        # Otherwise, increase the frequency
        else:
            char_codes[char] += 1

    # Returns the sorted dictionary based on frequency from high to low
    #sorted_data = dict(sorted(heap_data.items(), key = lambda f: f[1], reverse=True))
    #return sorted_data

    return char_codes

# From the dictionary, order the nodes by frequency from low to high. Returns an ordered queue
def build_queue(data):
    
    pqueue = PriorityQueue()
    dict_str = get_char_frequency(data)

    if not dict_str:
        return None

    for char, freq in dict_str.items():
        leaf = LeafNode(char, freq)
        pqueue.priority_insert(leaf)

    return pqueue

# Builds the Huffman tree
def build_tree(data):

    pqueue = build_queue(data)

    if not pqueue:
        return None

    # From the queue, build the tree until the tree is the only node left
    while pqueue.get_size() > 1:
        
        # Removes first and second node and saves it
        left_child = pqueue.pop()
        right_child = pqueue.pop()

        # Creates a TreeNode assiging the children and setting the frequency
        tree = TreeNode(left_child, right_child, left_child.frequency + right_child.frequency)
        pqueue.priority_insert(tree)

    # Returns the tree
    return pqueue.head

# Traverses the tree in a DFS pre-order manner and saves the codes in a dictionary
def get_char_codes(tree_root, node_char, code_dict):

    if tree_root == None:
        return

    # If the root is now leaf node
    if type(tree_root) == LeafNode:

        # If its been traversed already
        if len(node_char) > 0:
            code_dict[tree_root.character] = node_char
        
        # Otherwise set the code to 1
        else:
            code_dict[tree_root.character] = '1'

    # Traverses left and right, adds the corresponding digit to the code 
    get_char_codes(tree_root.left, node_char + '0', code_dict)
    get_char_codes(tree_root.right, node_char + '1', code_dict)

# Returns an encoded string 
def huffman_encoding(data):

    if data == None or type(data) == int:
        return None

    # Get the codes for the characters
    tree = build_tree(data)
    code_dict = {}
    get_char_codes(tree, '', code_dict)

    # Loop through the string, when a letter has been found, set its code in a new string
    encoded_str = ""
    for e in data:
        encoded_str += code_dict[e]

    #print(encoded_str)
    return encoded_str
  
# Returns a decoded string
def huffman_decoding(data, tree):

    decoded_str = ""
    current = tree

    # Loops through data 
    for c in data:
        
        # Checks if the digit in data matches and if the pointers are valid
        if c == '0' and current.left:
            current = current.left
        elif c == '1' and current.right:
            current = current.right

        # If the end is reached, it is a character
        if type(current) == LeafNode:
            decoded_str += current.character
            current = tree

    #print(decoded_str)
    return decoded_str
    
# Test function
def test_huffman(data):

    if data == "" or type(data) == int or data == None:
        return 

    tree_code = build_tree(data) # Build the tree

    # Original string info
    print ("The size of the data is:", format(sys.getsizeof(data)))
    print ("The content of the data is: {}\n".format(data))

    encoded_huff = huffman_encoding(data) # Encodes the string

    # Encoded string info
    print ("The size of the encoded data is:", format(sys.getsizeof(int(encoded_huff, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_huff))

    decoded_huff = huffman_decoding(encoded_huff, tree_code) # Decodes the string

    # Decoeded string info
    print ("The size of the decoded data is:", format(sys.getsizeof(decoded_huff)))
    print ("The content of the encoded data is: {}\n".format(decoded_huff))


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test cases from 1 to 3 are expected to produce regular outputs

# Test Case 1
test_huffman("AAAAAABBBCCCCCCDDEEEFFFFF")

# Test Case 2
test_huffman("This is a great sentence")

# Test Case 3
test_huffman("A sTrAnGe StRiNg!")

# Test cases 4 to 6 are expected to produce smaller codes

# Test Case 4
test_huffman("ab")

# Test Case 5
test_huffman("ccc")

# Test Case 6
test_huffman(" ")

# From test case 7 to 9, inputs are in incorrect formats, ouputs should not be processed

# Test Case 7
test_huffman("")

# Test Case 8
test_huffman(4)

# Test Case 9
test_huffman(None)


