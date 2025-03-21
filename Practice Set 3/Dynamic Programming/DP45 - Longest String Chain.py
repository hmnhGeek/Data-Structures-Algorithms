# Problem link - https://www.geeksforgeeks.org/find-the-length-of-the-longest-possible-word-chain/
# Solution - https://www.youtube.com/watch?v=YY8iBaYcc4g&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=46


def compare(x, y):
    if len(x) != len(y) + 1:
        return False
    i, j = 0, 0
    while i < len(x):
        if 0 <= j < len(y) and x[i] == y[j]:
            j += 1
        i += 1
    return i == len(x) and j == len(y)


class Solution:
    @staticmethod
    def longest_string_chain(strings):
        """
            Overall time complexity is O(n^2 * l) and space complexity is O(n).
        """

        # sort the strings array by length in O(n log(n)) time.
        strings.sort(key=len)

        n = len(strings)

        # store dp and parents dictionary in O(n) space.
        dp = {i: 1 for i in range(n)}
        parents = {i: i for i in range(n)}

        # loop on i and j in O(n^2) time
        for i in range(n):
            for prev in range(i):
                # assuming strings[i] to be larger, we are taking another O(l) time to check if chain is possible or
                # not, where l is the length of strings[i].
                if compare(strings[i], strings[prev]):
                    dp[i] = 1 + dp[prev]
                    parents[i] = prev

        # back track to get the longest chain.
        start_index = max(dp, key=dp.get)
        result = []
        while start_index != parents[start_index]:
            result.append(strings[start_index])
            start_index = parents[start_index]
        result.append(strings[start_index])
        return result[-1:-len(result)-1:-1]


print(Solution.longest_string_chain(["x", "xx", "y", "xyx"]))
print(Solution.longest_string_chain(["m", "nm", "mmm"]))
print(Solution.longest_string_chain(["a", "bc", "ad", "adc", "bcd"]))
print(Solution.longest_string_chain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))
print(Solution.longest_string_chain(["a", "b", "ba", "bca", "bda", "bdca"]))
print(Solution.longest_string_chain(["abcd", "dbqca"]))