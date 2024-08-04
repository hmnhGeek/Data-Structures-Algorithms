# Problem link - https://leetcode.com/problems/reorganize-string/description/

from collections import Counter


class MaxHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def get_lci(self, pi):
        lci = 2*pi + 1
        return lci if lci in range(len(self.heap)) else None

    def get_rci(self, pi):
        rci = 2*pi + 2
        return rci if rci in range(len(self.heap)) else None

    def get_pi(self, ci):
        if ci == 0:
            return None
        pi = int((ci - 1)/2)
        return pi if pi in range(len(self.heap)) else None

    def get_max_child_index(self, lci, rci):
        if lci is None and rci is None:
            return None
        if lci is None:
            return rci
        if rci is None:
            return lci

        max_child_index = lci
        if self.heap[rci][1] > self.heap[max_child_index][1]:
            max_child_index = rci

        return max_child_index

    def max_heapify_up(self, start_index):
        if start_index == 0:
            return

        pi = self.get_pi(start_index)
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        max_child_index = self.get_max_child_index(lci, rci)

        if max_child_index is not None:
            if self.heap[pi][1] < self.heap[max_child_index][1]:
                self.heap[pi], self.heap[max_child_index] = self.heap[max_child_index], self.heap[pi]
            self.max_heapify_up(pi)

    def max_heapify_down(self, pi):
        lci, rci = self.get_lci(pi), self.get_rci(pi)
        max_child_index = self.get_max_child_index(lci, rci)

        if max_child_index is not None:
            if self.heap[pi][1] < self.heap[max_child_index][1]:
                self.heap[pi], self.heap[max_child_index] = self.heap[max_child_index], self.heap[pi]
            self.max_heapify_down(max_child_index)

    def insert(self, x):
        self.heap.append(x)
        self.max_heapify_up(len(self.heap) - 1)

    def pop(self):
        if self.is_empty():
            return

        item = self.heap[0]
        self.heap[0], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[0]
        del self.heap[len(self.heap) - 1]
        self.max_heapify_down(0)
        return item


def with_heap():
    # Assuming string s has length n and unique characters m.
    def reorg(s):
        # Overall time complexity is O(n*log(m)) and space is O(m).

        # will take O(m) space in worst case.
        max_heap = MaxHeap()

        # takes O(n) time to create mp and mp itself takes O(m) space.
        mp = dict(Counter(s))

        # runs for m times insert operation takes O(log(m)) time. Overall time is O(m*log(m))
        # basically populate max heap to retrieve most freq characters in logarithmic time.
        for i in mp.items():
            max_heap.insert(i)

        prev = None
        result = ""

        # this will run till all the characters are exhausted, i.e., n times. Thus, overall time taken
        # by this loop is O(n*log(m)).
        # Hence, this will take O(n*log(m)) time. Also note that `is_empty()` takes O(1) time
        while not max_heap.is_empty():
            # will take O(log(m)) to pop. pop the next frequent character
            next_char = max_heap.pop()
            character, freq = next_char

            # if there is a prev character which was just used in the last iteration, check if its
            # frequency is still non-zero. If yes, insert it back into max heap before updating prev.
            if prev is not None and prev[1] > 0:
                # will take O(log(m)) to insert prev
                max_heap.insert(prev)

            # add the current character into the result & reduce its frequency.
            result += character
            freq -= 1

            # update this character as prev for the next iteration.
            prev = (character, freq)

        # if the max heap got empty before utilizing all the characters, that means adjacent characters
        # will be present, return -1.
        if prev is not None and prev[1] > 0:
            return -1

        # return result if heap is empty and if prev[1] == 0 (all characters from original string have
        # been utilized).
        return result

    print(reorg("mississippi"))
    print(reorg("aab"))
    print(reorg("aaab"))
    print(reorg("aaabbcc"))
    print(reorg("aa"))
    print(reorg("aaabb"))
    print(reorg("apple"))
    print(reorg("beekeeper"))
    print(reorg("address"))


def without_heap():
    def get_most_freq_except(d, exc):
        # if exc or `except` (prev) character is not available, simply return
        # the most frequent character from dictionary d. If d is empty, return
        # None. This takes O(m) time and O(m) space (for filtered).
        if exc is None:
            return max(d, key=d.get) if d != {} else None

        # filter out all the characters apart from exc.
        filtered = {k: v for k, v in d.items() if k != exc}

        # if filtered result is not empty, return the key with max count, else return None.
        return max(filtered, key=filtered.get) if filtered != {} else None

    def reorg(s):
        # Let len(s) = n and the number of unique characters in s be m.
        # Overall time complexity is O(m*n) and space is O(m).

        # initialize a dictionary which holds the count of each character in the string.
        # This takes O(m) size. Time to generate this mp dictionary is O(n).
        mp = dict(Counter(s))

        # initialize a prev variable which will store the currently used character that
        # needs to be added into the result but should not be considered in the next
        # iteration to avoid adjacent placement of the same characters.
        prev = None
        result = ""

        # until and unless all the characters have been utilized from the given string.
        # This `all` check also takes O(m) time but `get_most_freq_except`'s O(m) is
        # independent of this check. However, the while loop runs for all the characters,
        # thus giving it a time complexity of O(n*m). Space consumed by get_most_freq_except
        # is O(m).
        while not all(v == 0 for v in mp.values()):
            # get the next frequent character apart from prev, because prev was already
            # utilized just before. Takes O(m) time and space.
            next_char = get_most_freq_except(mp, prev)

            # if next_char is not there or all the characters apart from prev have been
            # utilized, then it means that we will have to use prev in result now. But
            # this would mean same adjacent character in the final string. Hence, desired
            # result is not possible, return -1.
            if next_char is None or mp[next_char] == 0:
                return -1

            # if next_char is present with a frequency > 0, reduce its frequency by 1 unit.
            mp[next_char] -= 1

            # update the prev to this character so that it is not utilized in the next
            # iteration.
            prev = next_char

            # append this character to result
            result += next_char

        # finally return the desired result.
        return result

    print(reorg("mississippi"))
    print(reorg("aab"))
    print(reorg("aaab"))
    print(reorg("aaabbcc"))
    print(reorg("aa"))
    print(reorg("aaabb"))
    print(reorg("apple"))
    print(reorg("beekeeper"))
    print(reorg("address"))

without_heap()
print()
with_heap()