# Problem link - https://www.geeksforgeeks.org/problems/second-most-repeated-string-in-a-sequence0534/1


from collections import Counter


class Solution:
    @staticmethod
    def get_second_most(arr):
        """
            Time complexity is O(n) and space complexity is O(n * |s|).
        """

        # This will take O(n) time and O(n*|s|) space.
        d = dict(Counter(arr))

        # This will take O(n) time.
        max_val = max(d.values())

        # store second max key and its value.
        second_max = 0
        second_max_key = -1

        # loop in O(n) time
        for k, v in d.items():
            # update second max value
            if second_max < v < max_val:
                second_max = v
                second_max_key = k

        # return second max key.
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
