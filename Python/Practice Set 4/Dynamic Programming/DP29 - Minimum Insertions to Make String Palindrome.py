# Problem link - https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/description/
# Solution - https://www.youtube.com/watch?v=xPBLEj41rFU&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=30


class Solution:
    @staticmethod
    def lcs2(s1, s2):
        n = len(s1)
        m = len(s2)
        dp = {i: {j: 0 for j in range(m + 1)} for i in range(n + 1)}
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i][j - 1]
                    )
        return dp

    @staticmethod
    def min_insertions(string):
        """
            Time complexity is O(n^2) and space complexity is O(n).
        """
        reversed = string[-1:-len(string)-1:-1]
        dp = Solution.lcs2(string, reversed)
        i, j = len(string), len(string)
        result = ""
        while i > 0 and j > 0:
            if string[i - 1] == reversed[j - 1]:
                result += string[i - 1]
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
        return len(string) - len(result)


print(Solution.min_insertions("abca"))
print(Solution.min_insertions("abcdefg"))
print(Solution.min_insertions("aaaaa"))
print(Solution.min_insertions("zzazz"))
print(Solution.min_insertions("mbadm"))
print(Solution.min_insertions("leetcode"))
