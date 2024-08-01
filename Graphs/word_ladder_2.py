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


def get_alphanets():
    return 'abcdefghijklmnopqrstuvwxyz'


def replace(word, i, char):
    word = [w for w in word]
    word[i] = char
    return ''.join(word)


def word_ladder(start_word, end_word, word_list):
    # Overall time complexity is O(N*M*26) and space complexity is O(N*M).

    # In this version of the word ladder problem, we are asked to form the sequences and not
    # store the levels. Therefore, we will store the sequences in the queue and not simply
    # the word. Since the queue is storing sequences, each of size M (assuming) in the worst case,
    # and there are N words in the word list, the space complexity is O(N*M).
    q = Queue()
    q.push([start_word])

    # used_words will store all the new words that have been used on a particular level. Once
    # a BFS level has been completed from the queue, its only then that we remove that used word
    # from the set.
    used_words = [start_word]
    not_visited = set(word_list)

    # initialize the first level as level 0 and store other constants.
    level = 0
    alphabets = get_alphanets()
    result = []

    # typical BFS algorithm, with time complexity same as word ladder 1.
    while not q.is_empty():
        seq = q.pop()
        word = seq[-1]

        # if the last word in the sequence is the end word that we are targeting, then
        # append it to the result list.
        if word == end_word:
            if len(result) == 0:
                result.append(seq)
            elif len(result[0]) == len(seq):
                result.append(seq)

        # length of the sequence represents the level of the BFS. For example, if in a sequence
        # there are 2 words, then they must be in second level. Think like a binary tree. If the
        # popped sequence's length is greater than the level, increment the level and remove all
        # the used words from the previous level from not_visited set. At last clear used_words
        # to avoid unnecessary checks later on, as this level has been completed and the words
        # used in this level will never come again.
        if len(seq) > level:
            level += 1
            for word in used_words:
                if word in not_visited:
                    not_visited.remove(word)
            used_words = []

        # for the last word in the sequence, replace all of its characters one by one and check
        # if they are present in the set or not. If they are, then push them to queue, and also
        # push them to the used_words list for that level. Please note that we have not modified
        # the seq by appending because once you push to queue and then remove the word from seq,
        # it would also remove that last word from queue as well because in Python, lists are
        # passed by reference. Instead, create a new sequence and push it to queue. used_words is
        # common to the whole program, and thus no need to worry about references in it. Rest of
        # the logic remains the same as in word ladder 1 problem.
        for i in range(len(word)):
            char = word[i]

            for j in alphabets:
                word = replace(word, i, j)
                if word in not_visited:
                    new_seq = seq + [word]
                    q.push(new_seq)
                    used_words.append(word)

            word = replace(word, i, char)

    return result

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
        'gefk',
        ["geek", "gefk"]
    )
)