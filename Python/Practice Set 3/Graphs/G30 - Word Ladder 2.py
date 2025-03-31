# Problem link - https://www.geeksforgeeks.org/problems/word-ladder-ii/1
# Solution - https://www.youtube.com/watch?v=DREutrv2XD0&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=30


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

        hash_map = set(word_list)
        queue = Queue()
        used_on_level = set()
        level = 0
        used_on_level.add(start_word)
        queue.push([start_word, ])
        result = []

        for word in used_on_level:
            if word in hash_map:
                hash_map.remove(word)
        used_on_level.clear()

        while not queue.is_empty():
            vector = queue.pop()
            word = vector[-1]

            if len(vector) > level:
                level += 1
                for w in used_on_level:
                    if w in hash_map:
                        hash_map.remove(w)
                used_on_level.clear()

            if word == end_word:
                if len(result) == 0:
                    result.append(vector)
                elif len(result[0]) == len(vector):
                    result.append(vector)

            for c in range(len(word)):
                original = word
                temp = [i for i in original]
                for alp in "abcdefghijklmnopqrstuvwxyz":
                    temp[c] = alp
                    new_word = "".join(temp)
                    if new_word in hash_map:
                        next_vector = [j for j in vector] + [new_word, ]
                        queue.push(next_vector)
                    used_on_level.add(new_word)
                    temp = [i for i in original]

        return result


print(Solution.word_ladder(["des","der","dfr","dgt","dfs"], "der", "dfs"))
print(Solution.word_ladder(["geek", "gefk"], "gedk", "geek"))
print(Solution.word_ladder(["hot","dot","dog","lot","log","cog"], "hit", "cog"))
print(Solution.word_ladder(["hot","dot","dog","lot","log"], "hit", "cog"))
