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

        # convert word list to a hash set so that removal of words is easy. Takes O(n) space.
        hash_set = set(word_list)

        # define a queue and push the start word with level 1 into it to perform BFS.
        queue = Queue()
        queue.push((start_word, 1))

        # while BFS is possible
        while not queue.is_empty():
            # pop the word from the queue
            word, level = queue.pop()

            # if the word is end word, return the level.
            if word == end_word:
                return level

            # loop on the index of word
            for i in range(len(word)):
                # create a temp list to modify the string
                temp = [w for w in word]
                # add uppercase letters also if needed.
                for char in "abcdefghijklmnopqrstuvwxyz":
                    # replace character at index i
                    temp[i] = char
                    # if the new word is in hash set, push it to queue and remove it from hash set to denote visited.
                    if "".join(temp) in hash_set:
                        queue.push(("".join(temp), level + 1))
                        hash_set.remove("".join(temp))

        # if end word was never found, return 0.
        return 0


print(Solution.word_ladder(["des","der","dfr","dgt","dfs"], "der", "dfs"))
print(Solution.word_ladder(["geek", "gefk"], "gedk", "geek"))
print(Solution.word_ladder(["poon", "plee", "same", "poie","plea","plie","poin"], "toon", "plea"))
print(Solution.word_ladder(["hot","dot","dog","lot","log","cog"], "hit", "cog"))
print(Solution.word_ladder(["hot","dot","dog","lot","log"], "hit", "cog"))