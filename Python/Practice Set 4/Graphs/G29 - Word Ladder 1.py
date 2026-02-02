# Problem link - https://www.geeksforgeeks.org/problems/word-ladder/1
# Solution - https://www.youtube.com/watch?v=tRPda0rcf8E&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=29


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
        """
            Time complexity is O(n * word_length * 26) and space complexity is O(n).
        """
        word_list_set = set(word_list)
        queue = Queue()
        queue.push((start_word, 1))
        if start_word in word_list_set:
            word_list_set.remove(start_word)
        while not queue.is_empty():
            word, level = queue.pop()
            if word == end_word:
                return level
            new_word = [i for i in word]
            for i in range(len(new_word)):
                for character in "abcdefghijklmnopqrstuvwxyz":
                    new_word[i] = character
                    if "".join(new_word) in word_list_set:
                        queue.push(("".join(new_word), level + 1))
                        if "".join(new_word) in word_list_set:
                            word_list_set.remove("".join(new_word))
                new_word = [i for i in word]
        return -1


print(Solution.word_ladder(["des","der","dfr","dgt","dfs"], "der", "dfs"))
print(Solution.word_ladder(["geek", "gefk"], "gedk", "geek"))
print(Solution.word_ladder(["poon", "plee", "same", "poie","plea","plie","poin"], "toon", "plea"))
print(Solution.word_ladder(["hot","dot","dog","lot","log","cog"], "hit", "cog"))
print(Solution.word_ladder(["hot","dot","dog","lot","log"], "hit", "cog"))
