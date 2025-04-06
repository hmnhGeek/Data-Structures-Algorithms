from collections import Counter


class Solution:
    @staticmethod
    def transform(s1, s2):
        d1, d2 = dict(Counter(s1)), dict(Counter(s2))
        if d1 != d2:
            return -1
        count_of_swaps = 0
        i, j = len(s1) - 1, len(s2) - 1
        while i >= 0:
            if s1[i] != s2[j]:
                count_of_swaps += 1
            else:
                j -= 1
            i -= 1
        return count_of_swaps


print(Solution.transform("ABD", "BAD"))
print(Solution.transform("EACBD", "EABCD"))
