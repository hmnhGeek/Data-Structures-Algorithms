class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
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
            self.tail = node
        self.length += 1

    def pop(self):
        if self.is_empty():
            return
        item = self.head.data
        node = self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item


class Solution:
    @staticmethod
    def word_ladder(word_list, start_word, end_word):
        hash_set = set(word_list)
        queue = Queue()
        queue.push((start_word, 1))
        while not queue.is_empty():
            word, level = queue.pop()
            if word == end_word:
                return level

            for i in range(len(word)):
                temp = [w for w in word]
                for char in "abcdefghijklmnopqrstuvwxyz":
                    temp[i] = char
                    if "".join(temp) in hash_set:
                        queue.push(("".join(temp), level + 1))
                        hash_set.remove("".join(temp))
        return 0


print(Solution.word_ladder(["des","der","dfr","dgt","dfs"], "der", "dfs"))
print(Solution.word_ladder(["geek", "gefk"], "gedk", "geek"))
print(Solution.word_ladder(["poon", "plee", "same", "poie","plea","plie","poin"], "toon", "plea"))