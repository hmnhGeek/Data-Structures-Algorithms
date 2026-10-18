# Problem link - https://www.geeksforgeeks.org/find-the-length-of-the-longest-possible-word-chain/
# Solution - https://www.youtube.com/watch?v=YY8iBaYcc4g&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=46


class Solution:
    @staticmethod
    def _unit_diff(curr, prev):
        if len(curr) != len(prev) + 1:
            return False
        i, j = 0, 0
        while i < len(curr):
            if j < len(prev) and curr[i] == prev[j]:
                i += 1
                j += 1
            else:
                i += 1
        return i >= len(curr) and j >= len(prev)

    @staticmethod
    def longest_string_chain(strings):
        """
            Overall time complexity is O(n^2 * l) and space complexity is O(n).
        """
        n = len(strings)
        strings.sort(key = len)
        dp = {i: 1 for i in range(n)}
        parent = {i: i for i in range(n)}
        for i in range(n):
            for prev in range(i):
                if Solution._unit_diff(strings[i], strings[prev]) and 1 + dp[prev] > dp[i]:
                    dp[i] = 1 + dp[prev]
                    parent[i] = prev
        start_index = max(dp, key=dp.get)
        result = []
        while start_index != parent[start_index]:
            result.append(strings[start_index])
            start_index = parent[start_index]
        result.append(strings[start_index])
        return result[-1:-len(result)-1:-1]


print(Solution.longest_string_chain(["x", "xx", "y", "xyx"]))
print(Solution.longest_string_chain(["m", "nm", "mmm"]))
print(Solution.longest_string_chain(["a", "bc", "ad", "adc", "bcd"]))
print(Solution.longest_string_chain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]))
print(Solution.longest_string_chain(["a", "b", "ba", "bca", "bda", "bdca"]))
print(Solution.longest_string_chain(["abcd", "dbqca"]))
