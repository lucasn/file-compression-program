from pqueue import PQueue

class Huffman:
    huffman_marker = 259
    HUFFMAX_MAX_SYMBOL = 260

    def __init__(self,):
        self.tree = None
        self.codes = None
        self.text = None

    def build_tree(self, text):
        text = [byte for byte in text]
        text.append(self.huffman_marker)
        self.text = text
        symbols_frequency = [0 for _ in range(self.HUFFMAX_MAX_SYMBOL)]

        self.symbols_frequency = symbols_frequency

        for symbol in text:
            symbols_frequency[symbol] += 1
        
        priority_queue = PQueue(HuffmanTreeNode.less)
        for symbol, frequency in enumerate(symbols_frequency):
            if frequency != 0:
                node = HuffmanTreeNode(symbol, frequency)
                priority_queue.insert(node)

        while priority_queue.size() > 1:
            n1 = priority_queue.minimum()
            n2 = priority_queue.minimum()
            merged_node = n1.merge(n2)
            priority_queue.insert(merged_node)
        
        self.tree = priority_queue.minimum()

    def build_codemap(self):
        symbols_code = ['-1' for _ in range(self.HUFFMAX_MAX_SYMBOL)]
        self.tree.build_codemap_rec(symbols_code, '')
        self.codes = symbols_code

    def encode(self):
        encoded_text = bytearray()
        actual_byte = 0
        n_inserted_bits = 0
        for char in self.text:
            for bit in self.codes[char]:
                if (n_inserted_bits == 8):
                    encoded_text.append(actual_byte)
                    actual_byte = 0
                    n_inserted_bits = 0

                if bit == '1':
                    actual_byte = actual_byte | (1 << (7 - n_inserted_bits))
                n_inserted_bits += 1
        if n_inserted_bits != 0:
            encoded_text.append(actual_byte)
        
        return encoded_text

    def decode(self, encoded_text):
        decoded_text = bytearray()
        actual_node = self.tree
        for byte in encoded_text:
            for shift in range(8):
                bit_on = byte & 1 << (7 - shift)
                if bit_on == 0:
                   actual_node = actual_node.left
                else:
                   actual_node = actual_node.right

                if actual_node.symbol == 259:
                    return decoded_text

                elif actual_node.symbol != None:
                    decoded_text.append(actual_node.symbol)
                    actual_node = self.tree
            
        raise Exception('Terminator Symbol not found')

class HuffmanTreeNode:
    def __init__(self, symbol, frequency=0, left=None, right=None):
        self.symbol = symbol
        self.left = left
        self.right = right
        self.frequency = frequency
    
    @classmethod
    def less(cls, node1, node2):
        return node1.frequency < node2.frequency

    def merge(self, node):
        merged_node = HuffmanTreeNode(
            symbol=None, 
            frequency=self.frequency + node.frequency,
            left=self,
            right=node)
        
        return merged_node
    
    def build_codemap_rec(self, symbols_code, code):
        if self.symbol == None:
            self.left.build_codemap_rec(symbols_code, code + '0')
            self.right.build_codemap_rec(symbols_code, code + '1')
        else:
            symbols_code[self.symbol] = code