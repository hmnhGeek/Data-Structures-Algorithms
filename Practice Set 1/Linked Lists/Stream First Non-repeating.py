class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None


class Deque:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def push(self, x):
        node = Node(x)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1

    def pop(self):
        if self.is_empty():
            return "#"
        item = self.head.data
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item

    def front(self):
        if self.is_empty():
            return "#"
        return self.head.data


class Solution:
    @staticmethod
    def first_non_repeating(string):
        freq = {i: 0 for i in string}
        deque = Deque()
        n = len(string)
        result = ""
        for i in range(n):
            freq[string[i]] += 1
            if freq[string[i]] == 1:
                deque.push(string[i])
            while deque.front() in freq and freq[deque.front()] > 1:
                deque.pop()
            result += deque.front()
        return result


print(Solution.first_non_repeating("abcbbac"))
print(Solution.first_non_repeating("zz"))
print(Solution.first_non_repeating("aabc"))
print(Solution.first_non_repeating("geeksforgeeksandgeeksquizfor"))
print(Solution.first_non_repeating("aabcbc"))
print(Solution.first_non_repeating("abadbc"))
print(Solution.first_non_repeating("abcabc"))
