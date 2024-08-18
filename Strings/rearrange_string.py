# Problem link - https://www.geeksforgeeks.org/rearrange-characters-string-no-two-adjacent/


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
    """
        Overall time complexity is O(n * log(m)) and space is O(m).
    """

    # create an empty max heap which will be used to rearrange the string
    max_heap = MaxHeap()

    # get the count of each character of the string into a dictionary. Assume that the number of distinct characters
    # in the string are m.
    frequencies = dict()
    for character in string:
        if character not in frequencies:
            frequencies[character] = 1
        else:
            frequencies[character] += 1

    # push the character, and it's frequency into the max heap as Node data type. This will take O(log(m)) time. In the
    # worst case, the heap will have all the characters and so, the space it will occupy will be O(m).
    for character in frequencies:
        max_heap.insert(Node(character, frequencies[character]))

    # we will also use a variable to store previously used character, as we don't want it to be added again in to the
    # result if it again has the highest frequency.
    previous_used_character = None

    # create a resultant string with its length
    rearranged_string = ""
    length_of_rearranged_string = 0

    # while the heap is not empty; this will run `n` times, i.e., until all the characters of the strings are not
    # utilized. Hence, the time taken by this loop will be O(n * log(m)).
    while not max_heap.is_empty():
        # get the most frequent character (except previously used one, which would be None in first iteration). This
        # will take O(log(m)) time.
        character_node = max_heap.pop()

        # add this character to the resultant string and decrement its frequency. Also, increase the length of resultant
        # string.
        rearranged_string += character_node.char
        length_of_rearranged_string += 1
        character_node.count -= 1

        # now, we are about to update the previous variable, but before that, we must ensure that previous is not None.
        # if it is not None, and the count of previous character has not become 0, we must add it back to the max heap.
        # This will take O(log(m)) time.
        if previous_used_character is not None and previous_used_character.count > 0:
            max_heap.insert(previous_used_character)

        # update the previous used character with the current node.
        previous_used_character = character_node

    # if the length of original and resultant string is same, return the resultant string; this means we were able to
    # rearrange all the characters such that no one of them is adjacent, otherwise return None as the characters cannot
    # be rearranged.
    return rearranged_string if length_of_rearranged_string == len(string) else None


print(rearrange_string("aaabc"))
print(rearrange_string("aaabb"))
print(rearrange_string("aa"))
print(rearrange_string("aaaabc"))
print(rearrange_string("geeksforgeeks"))
print(rearrange_string("bbbb"))
print(rearrange_string("mississippi"))
print(rearrange_string("committee"))