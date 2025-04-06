# Problem link - https://www.geeksforgeeks.org/transform-one-string-to-another-using-minimum-number-of-given-operation/
# Solution - https://www.youtube.com/watch?v=mv5eeYHOYiI


from collections import Counter


class Solution:
    @staticmethod
    def transform(s1, s2):
        """
            Time complexity is O(n) and space complexity is O(26).
        """

        # check if both the strings are permutations of each other or not.
        d1, d2 = dict(Counter(s1)), dict(Counter(s2))
        if d1 != d2:
            return -1

        # store the count of swaps in a variable.
        count_of_swaps = 0

        # start looping in the string from the last indices of both the strings.
        i, j = len(s1) - 1, len(s2) - 1

        # while string1 is still left...
        while i >= 0:
            # if the characters don't match, increment the count but keep `j` at its place.
            if s1[i] != s2[j]:
                count_of_swaps += 1
            else:
                j -= 1
            i -= 1

        # return the count of swaps needed.
        return count_of_swaps


print(Solution.transform("ABD", "BAD"))
print(Solution.transform("EACBD", "EABCD"))
