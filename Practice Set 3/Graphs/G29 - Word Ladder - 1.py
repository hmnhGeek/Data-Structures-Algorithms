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
        h = set(word_list)
        queue = Queue()
        queue.push((start_word, 1))
        result = 0
        if start_word in h:
            h.remove(start_word)
        while not queue.is_empty():
            word, level = queue.pop()
            if word == end_word:
                return level
            for i in range(len(word)):
                word_split = [j for j in word]
                for char in "abcdefghijklmnopqrstuvwxyz":
                    word_split[i] = char
                    new_word = "".join(word_split)
                    if new_word in h:
                        queue.push((new_word, level + 1))
                        h.remove(new_word)
        return result


print(Solution.word_ladder(["des","der","dfr","dgt","dfs"], "der", "dfs"))
print(Solution.word_ladder(["geek", "gefk"], "gedk", "geek"))
print(Solution.word_ladder(["poon", "plee", "same", "poie","plea","plie","poin"], "toon", "plea"))
print(Solution.word_ladder(["hot","dot","dog","lot","log","cog"], "hit", "cog"))
print(Solution.word_ladder(["hot","dot","dog","lot","log"], "hit", "cog"))
