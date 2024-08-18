class Node:
    def __init__(self, character, count):
        self.char = character
        self.count = count


class MaxHeap:
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

    def get_max_child_index(self, lci, rci):
        if lci is None and rci is None:
            return None
        if lci is None:
            return rci
        if rci is None:
            return lci

        max_child_index = lci
        if self.heap[rci].count > self.heap[max_child_index].count:
            max_child_index = rci
        return max_child_index

    def max_heapify_up(self, start_index):
        if start_index == 0:
            return

        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        max_child_index = self.get_max_child_index(lci, rci)

        if max_child_index is not None:
            if self.heap[pi].count < self.heap[max_child_index].count:
                self.heap[pi], self.heap[max_child_index] = self.heap[max_child_index], self.heap[pi]
            self.max_heapify_up(pi)

    def max_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        max_child_index = self.get_max_child_index(lci, rci)

        if max_child_index is not None:
            if self.heap[pi].count < self.heap[max_child_index].count:
                self.heap[pi], self.heap[max_child_index] = self.heap[max_child_index], self.heap[pi]
            self.max_heapify_down(max_child_index)

    def insert(self, node: Node):
        self.heap.append(node)
        self.max_heapify_up(len(self.heap) - 1)

    def pop(self):
        if self.is_empty():
            return
        item = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        del self.heap[-1]
        self.max_heapify_down(0)
        return item


def rearrange_string(string: str) -> str:
    max_heap = MaxHeap()
    frequencies = dict()

    for character in string:
        if character not in frequencies:
            frequencies[character] = 1
        else:
            frequencies[character] += 1

    for character in frequencies:
        max_heap.insert(Node(character, frequencies[character]))

    previous_used_character = None
    rearranged_string = ""
    length_of_rearranged_string = 0
    while not max_heap.is_empty():
        character_node = max_heap.pop()
        rearranged_string += character_node.char
        length_of_rearranged_string += 1
        character_node.count -= 1

        if previous_used_character is not None and previous_used_character.count > 0:
            max_heap.insert(previous_used_character)

        previous_used_character = character_node

    return rearranged_string if length_of_rearranged_string == len(string) else None


print(rearrange_string("aaabc"))
print(rearrange_string("aaabb"))
print(rearrange_string("aa"))
print(rearrange_string("aaaabc"))
print(rearrange_string("geeksforgeeks"))
print(rearrange_string("bbbb"))
print(rearrange_string("mississippi"))
print(rearrange_string("committee"))