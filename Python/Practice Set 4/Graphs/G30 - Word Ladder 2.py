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
        queue = Queue()
        word_list_set = set(word_list)
        level = 0
        used_on_level = []
        result = []
        queue.push([start_word])
        used_on_level.append(start_word)
        while not queue.is_empty():
            vector = queue.pop()
            if len(vector) > level:
                level += 1
                for i in used_on_level:
                    if i in word_list_set:
                        word_list_set.remove(i)
                used_on_level.clear()
            word = vector[-1]
            if word == end_word:
                if len(result) == 0:
                    result.append(vector)
                elif len(vector) == len(result[0]):
                    result.append(vector)
            new_word = [i for i in word]
            for i in range(len(new_word)):
                for character in "abcdefghijklmnopqrstuvwxyz":
                    new_word[i] = character
                    possible_word = "".join(new_word)
                    if possible_word in word_list_set:
                        new_vector = vector + [possible_word]
                        queue.push(new_vector)
                        used_on_level.append(possible_word)
                new_word = [w for w in word]
        return result


print(Solution.word_ladder(["des","der","dfr","dgt","dfs"], "der", "dfs"))
print(Solution.word_ladder(["geek", "gefk"], "gedk", "geek"))
print(Solution.word_ladder(["hot","dot","dog","lot","log","cog"], "hit", "cog"))
print(Solution.word_ladder(["hot","dot","dog","lot","log"], "hit", "cog"))
