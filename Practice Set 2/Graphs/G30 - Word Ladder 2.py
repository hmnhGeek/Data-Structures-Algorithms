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
        queue.push([start_word])
        used_on_level = [start_word]
        level = 0
        result = []
        while not queue.is_empty():
            vector = queue.pop()
            if len(vector) > level:
                level += 1
                for used in used_on_level:
                    if used in hash_set:
                        hash_set.remove(used)
            word = vector[-1]

            if word == end_word:
                if len(result) == 0:
                    result.append(vector)
                elif len(result[0]) == len(vector):
                    result.append(vector)

            for i in range(len(word)):
                temp = [w for w in word]
                for char in "abcdefghijklmnopqrstuvwxyz":
                    temp[i] = char
                    new_word = "".join(temp)
                    if new_word in hash_set:
                        new_sq = [s for s in vector]
                        new_sq += [new_word]
                        queue.push(new_sq)
                        used_on_level.append(new_word)
        return result


print(Solution.word_ladder(["des","der","dfr","dgt","dfs"], "der", "dfs"))
print(Solution.word_ladder(["geek", "gefk"], "gedk", "geek"))
print(Solution.word_ladder(["hot","dot","dog","lot","log","cog"], "hit", "cog"))
print(Solution.word_ladder(["hot","dot","dog","lot","log"], "hit", "cog"))