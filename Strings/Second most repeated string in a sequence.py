from collections import Counter


class Solution:
    @staticmethod
    def get_second_most(arr):
        d = dict(Counter(arr))
        max_val = max(d.values())
        second_max = 0
        second_max_key = -1
        for k, v in d.items():
            if second_max < v < max_val:
                second_max = v
                second_max_key = k
        return second_max_key


print(Solution.get_second_most(
    [
        "aaa",
        "bbb",
        "ccc",
        "bbb",
        "aaa",
        "aaa"
    ]
))

print(Solution.get_second_most(["geek", "for", "geek", "for", "geek", "aaa"]))
