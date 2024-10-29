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


class WordLadder:
    alphabets = "abcdefghijklmnopqrstuvwxyz"

    @staticmethod
    def modify(word, word_list_set: set, traversal, queue: Queue, used_on_level):
        _list = [i for i in word]

        # traverse on each character of the word.
        for i in range(len(_list)):
            for alphabet in WordLadder.alphabets:
                # create a copy of the traversal array because in python lists are passed by reference.
                new_traversal = [i for i in traversal]

                # modify the character at index i, and form the new word.
                _list[i] = alphabet
                new_word = "".join(_list)

                # if the new word exists in the word list
                if new_word in word_list_set:
                    # then append it to the new traversal.
                    new_traversal.append(new_word)

                    # push the new traversal to the queue.
                    queue.push(new_traversal)

                    # add this new word on the current level
                    used_on_level.append(new_word)

            # restore the original word
            _list = [i for i in word]

    @staticmethod
    def get(word_list, start_word, end_word):
        word_list_set = set(word_list)

        # push the start word into a queue.
        queue = Queue()
        queue.push([start_word])

        # store the starting word at the current level 1.
        used_on_level = [start_word]

        # make the last level as 0
        last_level = 0
        result = []

        while not queue.is_empty():
            # pop a traversal list
            traversal = queue.pop()

            # if the traversal is on next level
            if len(traversal) > last_level:
                # increase the last level count
                last_level += 1

                # start popping the words from `used_on_level` from the word list set.
                for word in used_on_level:
                    if word in word_list_set:
                        word_list_set.remove(word)

            # get the last word from the traversal because that is what we are going to modify.
            last_word = traversal[-1]

            # if the last word is the end word.
            if last_word == end_word:
                # and this is the first result that we are appending, then simply append it to the result set.
                if len(result) == 0:
                    result.append(traversal)
                # else if the traversal that is being added, if it's on the same level as previously stored traversals
                # in the list, then append it as well. We don't want to add any traversal which takes a longer route.
                elif len(result[0]) == len(traversal):
                    result.append(traversal)

            # modify the queue
            WordLadder.modify(last_word, word_list_set, traversal, queue, used_on_level)

        # finally return the result.
        return result


print(WordLadder.get(["des","der","dfr","dgt","dfs"], "der", "dfs"))
print(WordLadder.get(["geek", "gefk"], "gedk", "geek"))
print(WordLadder.get(["hot","dot","dog","lot","log","cog"], "hit", "cog"))
print(WordLadder.get(["hot","dot","dog","lot","log"], "hit", "cog"))
