# Problem link - https://leetcode.com/problems/longest-repeating-character-replacement/description/
# Solution - https://www.youtube.com/watch?v=_eNhaDCr6P0&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=9


class AlphabetsMap:
    def __init__(self):
        self.mp = {i: 0 for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

    def increment(self, key):
        self.mp[key] += 1

    def decrement(self, key):
        self.mp[key] -= 1

    def max_freq(self):
        return max(self.mp.values())


def longest_repeating_character_replacement(string, k):
    """
        Time complexity is O(N) and space complexity is O(26) = O(1).
    """

    map = AlphabetsMap()
    i, j = 0, 0
    max_length = 1
    n = len(string)

    # run the loop till j does not breach out of the window
    while j < n:
        # increment the map[string[j]]
        map.increment(string[j])

        # get the max frequency
        max_freq = map.max_freq()

        # if window size - max frequency is more than k, then considering window size is not possible.
        # decrement from the ith side, i.e. shrink the window.
        if (j - i + 1) - max_freq > k:
            map.decrement(string[i])
            i += 1

        # irrespective of the window getting shrunk or not, check if updating the max_length is possible or not.
        if (j - i + 1) - max_freq <= k:
            max_length = max(max_length, j - i + 1)

        # expand the window from right side.
        j += 1

    # return the max length.
    return max_length


print(longest_repeating_character_replacement("AAABBCCD", 2))
print(longest_repeating_character_replacement("ABAB", 2))
print(longest_repeating_character_replacement("AABABBA", 1))