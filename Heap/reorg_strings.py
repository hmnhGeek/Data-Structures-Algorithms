# Problem link - https://leetcode.com/problems/reorganize-string/description/

from collections import Counter

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
        # Overall time complexity is O(m + n) and space is O(m).

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
        # independent of this check. So overall time complexity of this while loop is
        # O(m) and space is also O(m).
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


without_heap()