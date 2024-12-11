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

        # same as word ladder 1 code.
        hash_set = set(word_list)
        queue = Queue()
        queue.push([start_word])

        # create an array to store the words used on a level
        used_on_level = [start_word]

        # take initial level as 0
        level = 0

        # take a result variable to store all the answers.
        result = []

        # standard BFS...
        while not queue.is_empty():
            # pop the vector
            vector = queue.pop()

            # if length of vector is greater than level, it means we have crossed to the next level.
            if len(vector) > level:
                # increment the level
                level += 1

                # remove all the used words from the set.
                for used in used_on_level:
                    if used in hash_set:
                        hash_set.remove(used)

            # get the last word from the sequence
            word = vector[-1]

            # if the last word is the end word
            if word == end_word:
                # and this is the first time we are seeing an answer, push it to result.
                if len(result) == 0:
                    result.append(vector)
                # or if this vector length is same as the length of first vector, we have another answer, push it also.
                elif len(result[0]) == len(vector):
                    result.append(vector)

            # now loop on the index of the word
            for i in range(len(word)):
                # create a temp array to modify the word
                temp = [w for w in word]

                # replace ith character from all the alphabets.
                for char in "abcdefghijklmnopqrstuvwxyz":
                    temp[i] = char

                    # form the new word
                    new_word = "".join(temp)

                    # check if new word is present in hash set
                    if new_word in hash_set:
                        # add the new word into a new vector
                        new_sq = [s for s in vector]
                        new_sq += [new_word]

                        # push the new vector into the queue
                        queue.push(new_sq)

                        # add the new word in used_on_level.
                        used_on_level.append(new_word)

        # return the result.
        return result


print(Solution.word_ladder(["des","der","dfr","dgt","dfs"], "der", "dfs"))
print(Solution.word_ladder(["geek", "gefk"], "gedk", "geek"))
print(Solution.word_ladder(["hot","dot","dog","lot","log","cog"], "hit", "cog"))
print(Solution.word_ladder(["hot","dot","dog","lot","log"], "hit", "cog"))