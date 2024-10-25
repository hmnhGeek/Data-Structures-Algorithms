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
        char_list = [i for i in word]
        for i in range(len(char_list)):
            for j in WordLadder.alphabets:
                char_list[i] = j
                joined_word = "".join(char_list)
                if joined_word in word_list:
                    queue.push((joined_word, level + 1))
                    word_list.remove(joined_word)
            char_list = [i for i in word]

    @staticmethod
    def find_steps(word_list, start_word, end_word):
        word_list_set = set(word_list)
        queue = Queue()
        queue.push((start_word, 1))
        if start_word in word_list_set:
            word_list_set.remove(start_word)
        while not queue.is_empty():
            word, level = queue.pop()
            if word == end_word:
                return level
            original_word = word
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