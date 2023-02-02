"""
Followed instruction on page, but created a huffman code class to handle all processes
1. Creating frequency table
2. Creating heap nodes and using Min heap as priority queue
3. Merging nodes and assigning them to left or right nodes and moving up and finally storing root note in self.heap
4. Using traverse and creating Huffman code for each letter  with 0 as left and 1 as right for movement
5. Storing a reverse char to code and code to char which can be used for decoding
6. Perform 3 different test also

"""

import sys
import heapq


# Node Class which stores character and frequency, have left and right arm
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # We need to compare nodes when we merge them
    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCode:

    # initiator of huffman code which collects all relevant data
    def __init__(self, data):
        self.data = data
        self.frequency = {}

        # Save final codes as dict, which will have letter has key and huffman code as value
        self.codes = {}
        self.heap = []
        self.code_to_char = {}
        self.encoded_string = ""

    """
    Take input string and creates a Frequency table, returns table with character and frequency
    """

    def create_frequency_table(self):
        # Handling Null and Empty data
        if self.data is None or self.data == '':
            return None

        for character in self.data:
            if character in self.frequency:
                self.frequency[character] += 1
            else:
                self.frequency[character] = 1

    """ 
    Creating a Heap function where i need:
    1. 
    2. Using heap creates that heapnode
    """

    # Make a Priority Queue using Min Heap
    def priority_heap(self):

        for key in self.frequency:
            heap_node = Node(key, self.frequency[key])
            heapq.heappush(self.heap, heap_node)

    """
    Building huffman tree from priority heap
    1. Pop 2 nodes from Heap
    2. merge them
    3. Recreate priority heap and repeat that process
    """

    def build_huffman_tree(self):

        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            merge_node = Node(None, node1.freq + node2.freq)

            # Assigning low value towards left and high towards right
            merge_node.left = node1
            merge_node.right = node2
            heapq.heappush(self.heap, merge_node)

        return self.heap

    # Recursive function to traverse LEFT and right to find the leaf node and store the value

    def create_huffman_code(self, node, huff_code):
        if node is None:
            return ""

        # All our leaf nodes are letters, when our last letter is leaf
        if node.char is not None:
            self.codes[node.char] = huff_code
            # This to do lookup when decoding
            self.code_to_char[huff_code] = node.char

        self.create_huffman_code(node.left, huff_code + '0')
        self.create_huffman_code(node.right, huff_code + '1')

    def encoding(self):
        # This brings in data to be encoded which is string
        root = heapq.heappop(self.heap)
        huff_code = ""

        return self.create_huffman_code(root, huff_code)
        # Create frequency table using data

    # Creating full string in huffman code
    def encoded_output_string(self):

        for char in self.data:
            self.encoded_string += self.codes[char]

        return self.encoded_string, self.code_to_char

    def __repr__(self):
        output = f'Frequency table is {self.frequency}\n'
        output += f'HuffmanCodes are {self.codes}\n'
        output += f'Huffman Encoded String is {self.encoded_string}\n'
        output += f'Decoded String is {self.decoded_out_string}'
        output += f"Original Heap is {self.heap} and heap for decode is {self.decode_heap}"
        return output


def huffman_encoding(data):
    # Creating Huffman Object
    if data is None or data == '':
        return None

    h = HuffmanCode(data)

    # Create a Frequency Table
    h.create_frequency_table()

    # Building Priority Queue using min heap
    h.priority_heap()

    # Merging Nodes and Building Huffman Tree,
    h.build_huffman_tree()

    # Crating Huffman Code
    h.encoding()

    # Creating encoded string of input string as per huffman coding
    encoded_data_out, tree_out = h.encoded_output_string()
    # print(h)
    return encoded_data_out, tree_out


def huffman_decoding(data, inp_tree):
    part_code = ""
    decoded_out_string = ''
    for char in data:
        part_code += char
        if part_code in inp_tree:
            decoded_out_string += inp_tree[part_code]
            part_code = ''
    return decoded_out_string


if __name__ == '__main__':
    # Test for None or Empty Input

    a_great_sentence = ""
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    if huffman_encoding(a_great_sentence) is None:
        encoded_data, tree = '', []
    else:
        encoded_data, tree = huffman_encoding(a_great_sentence)
        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # Test for very large value, size reduced from 1118 to 324

    a_great_sentence = "The concept of loops is available in almost all programming languages. Python loops help to iterate over a list, tuple, string, dictionary, and a set. There are two types of loop supported in Python “for” and “while”. The block of code is executed multiple times inside the loop until the condition fails. The loop control statements break the flow of execution and terminate/skip the iteration as per our need. Python break and continue are used inside the loop to change the flow of the loop from its standard procedure."
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    if huffman_encoding(a_great_sentence) is None:
        encoded_data, tree = '', []
    else:
        encoded_data, tree = huffman_encoding(a_great_sentence)
        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # Test for MATH FORMULA

    a_great_sentence = "=INDEX(list,MATCH(TRUE,ISNUMBER(SEARCH(list,[@[Cell]])),0))"
    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    if huffman_encoding(a_great_sentence) is None:
        encoded_data, tree = '', []
    else:
        encoded_data, tree = huffman_encoding(a_great_sentence)
        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)
    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
