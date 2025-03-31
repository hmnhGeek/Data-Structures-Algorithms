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


class WordLadder:
    alphabets = "abcdefghijklmnopqrstuvwxyz"

    @staticmethod
    def _check_and_update_queue(word, word_list, level, queue):
        # split the current word into a character list. We can't modify strings and therefore a list is needed.
        char_list = [i for i in word]

        # now loop on each character of the word.
        for i in range(len(char_list)):
            # for each character, loop on the 26 alphabets and replace the character at `i` with it.
            for j in WordLadder.alphabets:
                char_list[i] = j
                # join the word after replacing the ith character
                joined_word = "".join(char_list)

                # if the joined word is in the word list set, push it to the queue with level + 1.
                if joined_word in word_list:
                    queue.push((joined_word, level + 1))
                    # ensure to remove it from the set because we are using this set as a visited array.
                    word_list.remove(joined_word)

            # once the ith character is done with, restore the original word for next character index.
            char_list = [i for i in word]

    @staticmethod
    def find_steps(word_list, start_word, end_word):
        # convert the word list to a set so that get operations are amortized O(1). This will take O(n).
        word_list_set = set(word_list)

        # initiate a queue and push the start word into it with a level 1, in O(1).
        queue = Queue()
        queue.push((start_word, 1))

        # if the start word is in set, remove it as we have already pushed it to the queue. This will take O(1).
        if start_word in word_list_set:
            word_list_set.remove(start_word)

        # typical BFS algorithm...
        while not queue.is_empty():
            # pop the current node...
            word, level = queue.pop()

            # if the popped word is the target word, return the popped level.
            if word == end_word:
                return level

            # use the WordLadder class method to update the queue.
            WordLadder._check_and_update_queue(word, word_list_set, level, queue)
        return 0


print(
    WordLadder.find_steps(
        ["des", "der", "dfr", "dgt", "dfs"],
        "der",
        "dfs"
    )
)

print(
    WordLadder.find_steps(
        ["geek", "gefk"],
        "gedk",
        "geek"
    )
)

print(
    WordLadder.find_steps(
        ["poon", "plee", "same", "poie","plea","plie","poin"],
        "toon",
        "plea"
    )
)