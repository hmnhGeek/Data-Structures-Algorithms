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
        for i in range(len(_list)):
            for alphabet in WordLadder.alphabets:
                new_traversal = [i for i in traversal]
                _list[i] = alphabet
                new_word = "".join(_list)
                if new_word in word_list_set:
                    new_traversal.append(new_word)
                    queue.push(new_traversal)
                    used_on_level.append(new_word)
            _list = [i for i in word]

    @staticmethod
    def get(word_list, start_word, end_word):
        word_list_set = set(word_list)
        queue = Queue()
        used_on_level = [start_word]
        level = 0
        queue.push([start_word])
        result = []

        while not queue.is_empty():
            traversal = queue.pop()
            if len(traversal) > level:
                level += 1
                for word in used_on_level:
                    if word in word_list_set:
                        word_list_set.remove(word)

            last_word = traversal[-1]
            if last_word == end_word:
                if len(result) == 0:
                    result.append(traversal)
                elif len(result[0]) == len(traversal):
                    result.append(traversal)

            WordLadder.modify(last_word, word_list_set, traversal, queue, used_on_level)

        return result


print(WordLadder.get(["des","der","dfr","dgt","dfs"], "der", "dfs"))
print(WordLadder.get(["geek", "gefk"], "gedk", "geek"))
print(WordLadder.get(["hot","dot","dog","lot","log","cog"], "hit", "cog"))
print(WordLadder.get(["hot","dot","dog","lot","log"], "hit", "cog"))
