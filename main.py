from math import floor
from utils import contents
from huffman import Huffman
from burrows import couting_sort

def main():
    # text = contents('pg5097.txt')
    # huff = Huffman()
    # huff.build_tree(text[3:50])
    # huff.build_codemap()
    # encoded_text = huff.encode()
    # decoded_text = huff.decode(encoded_text)
    # print(decoded_text)

    print(couting_sort([7, 9, 13, 2, 8, 7, 2, 1, 0]))


if __name__ == '__main__':
    main()