# Problem link - https://www.geeksforgeeks.org/problems/word-ladder/1
# Solution - https://www.youtube.com/watch?v=tRPda0rcf8E&list=PLgUwDviBIf0oE3gA41TKO2H5bHpPd7fzn&index=29

# first define a queue data structure
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

        item, node = self.head.data, self.head
        self.head = self.head.next
        del node
        self.length -= 1
        return item


def get_alphabets():
    return 'abcdefghijklmnopqrstuvwxyz'


def replace_char(word, index, character):
    # we cannot directly change a character in an immutable string
    # so, we first convert the string to list, change the character
    # and return by joining the list as a string. This takes O(len(word))
    # time and O(1) space.
    word = [w for w in word]
    word[index] = character
    return ''.join(word)


def word_ladder(start_word, end_word, word_list):
    # Overall time complexity is O(n * word_length).
    # Overall space complexity is O(n) for a queue and a set data structure.

    # initialize a queue to solve this problem using BFS technique.
    q = Queue()

    # convert the word_list into a set because we will be doing many find and remove
    # operations which are not feasible on a list data type. This set will act as a
    # visited array for the BFS traversal.
    not_visited = set(word_list)

    # push the start word into queue with step count of 1.
    q.push((start_word, 1))

    # remove the start word if it exists in the set as this word has been visited and
    # pushed to the queue.
    if start_word in not_visited:
        not_visited.remove(start_word)

    # get 26 characters from English alphabets.
    alphabets = get_alphabets()

    # typical BFS algorithm. The queue will run for all the words in the word list. Thus, the
    # following block will run for n*word_length*26.
    while not q.is_empty():
        word, steps = q.pop()

        # if the popped word is in fact the target end word, return the steps taken to reach it.
        if word == end_word:
            return steps

        # otherwise, start iterating on each character of the popped word.
        # This step runs 26*len(word) times.
        for i in range(len(word)):
            # store the ith character for future reference to reset the string.
            char = word[i]

            # replace the ith character from the popped word with each character from the alphabets
            # and check if the word is in the set or not. If it is in the set, it means that it has
            # not been visited yet. Remove it from the set, and push it to the queue with steps =
            # steps + 1.
            for j in alphabets:
                # assuming it takes O(1) time, but it does not.
                word = replace_char(word, i, j)
                if word in not_visited:
                    not_visited.remove(word)
                    q.push((word, steps + 1))

            # once all the alphabets on the character ith are done with, restore the original popped
            # word back.
            word = replace_char(word, i, char)

    return 0


print(
    word_ladder(
        'hit',
        'cog',
        ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
    )
)

print(
    word_ladder(
        'der',
        'dfs',
        ["des","der","dfr","dgt","dfs"]
    )
)

print(
    word_ladder(
        'gedk',
        'geek',
        ["geek", "gefk"]
    )
)

print(
    word_ladder(
        'toon',
        'plea',
        ["poon", "plee", "same", "poie","plea","plie","poin"]
    )
)