from collections import Counter


class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def get_lci(self, pi):
        lci = 2*pi + 1
        return lci if lci in range(len(self.heap)) else None

    def get_rci(self, pi):
        rci = 2*pi + 2
        return rci if rci in range(len(self.heap)) else None

    def get_pi(self, ci):
        if ci == 0:
            return
        pi = int((ci - 1)/2)
        return pi if pi in range(len(self.heap)) else None

    def get_min_child_index(self, lci, rci):
        if lci is None and rci is None:
            return
        if lci is None:
            return rci
        if rci is None:
            return lci
        min_child_index = lci
        if self.heap[rci].data < self.heap[min_child_index].data:
            min_child_index = rci
        return min_child_index

    def min_heapify_up(self, start_index):
        if start_index == 0:
            return
        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi].data > self.heap[min_child_index].data:
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.min_heapify_up(pi)

    def min_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        min_child_index = self.get_min_child_index(lci, rci)
        if min_child_index is not None:
            if self.heap[pi].data > self.heap[min_child_index].data:
                self.heap[pi], self.heap[min_child_index] = self.heap[min_child_index], self.heap[pi]
            self.min_heapify_down(min_child_index)

    def insert(self, x):
        self.heap.append(x)
        self.min_heapify_up(len(self.heap) - 1)

    def pop(self):
        if self.is_empty():
            return
        item = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        del self.heap[-1]
        self.min_heapify_down(0)
        return item


class Node:
    def __init__(self, character, data):
        self.character = character
        self.data = data
        self.left = self.right = None


class Solution:
    @staticmethod
    def _get_inorder(root, huffman_encodings, encoding):
        if root.left is None and root.right is None:
            huffman_encodings.append((root.character, encoding))
            return
        Solution._get_inorder(root.left, huffman_encodings, encoding + "0")
        Solution._get_inorder(root.right, huffman_encodings, encoding + "1")

    @staticmethod
    def get_huffman_encoding_of(string):
        # get the frequencies of the characters from the string in a list of tuples.
        mapping = Counter(string)
        frequencies = list(mapping.items())

        # declare a priority queue
        pq = MinHeap()

        # loop on the character and its frequency push them one by one into pq.
        for char, frequency in frequencies:
            pq.insert(Node(char, frequency))

        # while we don't reach to the root node...
        while len(pq.heap) != 1:
            # get the lowest two nodes by frequencies
            left_node, right_node = pq.pop(), pq.pop()

            # create their parent node (character can be sent as "")
            parent_node = Node("", left_node.data + right_node.data)

            # make the linkages between parent and its children
            parent_node.left = left_node
            parent_node.right = right_node

            # push the parent node back to the pq.
            pq.insert(parent_node)

        # once the pq has only one node (root node) of the huffman tree, perform an inorder traversal of this tree.
        huffman_encodings = []
        Solution._get_inorder(pq.heap[0], huffman_encodings, "")

        # return the huffman encodings of each character.
        return huffman_encodings


print(Solution.get_huffman_encoding_of("aaaaabbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeeeee"+"f"*45))
print(Solution.get_huffman_encoding_of("bcaadddccacacac"))
print(Solution.get_huffman_encoding_of("eeeeaaaaddcccbbbbbbb"))
print(Solution.get_huffman_encoding_of("abcd"))
print(Solution.get_huffman_encoding_of("AAAAAABCCCCCCDDEEEEE"))
print(Solution.get_huffman_encoding_of("geeksforgeeks"))
