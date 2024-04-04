from collections import Counter
from queue import PriorityQueue

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_tree(frequencies):
    pq = PriorityQueue()
    for char, freq in frequencies.items():
        pq.put(Node(char, freq))

    while pq.qsize() > 1:
        left = pq.get()
        right = pq.get()
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        pq.put(merged)

    return pq.get()

def generate_codes(node, prefix="", code_map={}):
    if node is not None:
        if node.char is not None:
            code_map[node.char] = prefix
        generate_codes(node.left, prefix + "0", code_map)
        generate_codes(node.right, prefix + "1", code_map)
    return code_map

def encode(data, code_map):
    encoded_data = ""
    for char in data:
        encoded_data += code_map[char]
    return encoded_data

def decode(data, root):
    decoded_data = ""
    current_node = root
    for bit in data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.char is not None:
            decoded_data += current_node.char
            current_node = root
    return decoded_data

# Example usage
if __name__ == "__main__":
    text = "ABRACADABRA"
    frequencies = Counter(text)
    
    huffman_tree = build_tree(frequencies)
    huffman_codes = generate_codes(huffman_tree)
    
    encoded_text = encode(text, huffman_codes)
    decoded_text = decode(encoded_text, huffman_tree)
    
    print(f"Original: {text}")
    print(f"Encoded: {encoded_text}")
    print(f"Decoded: {decoded_text}")
    print(f"Codes: {huffman_codes}")
