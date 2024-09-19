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
    map = AlphabetsMap()
    i, j = 0, 0
    max_length = 1
    n = len(string)

    while j < n:
        map.increment(string[j])
        max_freq = map.max_freq()

        while (j - i + 1) - max_freq > k:
            map.decrement(string[i])
            max_freq = map.max_freq()
            i += 1

        if (j - i + 1) - max_freq <= k:
            max_length = max(max_length, j - i + 1)
        j += 1
    return max_length


print(longest_repeating_character_replacement("AAABBCCD", 2))
print(longest_repeating_character_replacement("ABAB", 2))
print(longest_repeating_character_replacement("AABABBA", 1))