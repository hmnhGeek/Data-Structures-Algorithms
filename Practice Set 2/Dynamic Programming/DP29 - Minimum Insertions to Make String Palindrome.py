# Problem link - https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/description/
# Solution - https://www.youtube.com/watch?v=xPBLEj41rFU&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=30


def recursive():
    """
        Time complexity is O(2^{n + m}) and space complexity is O(m + n).
    """
    def solve(s1, i, s2, j):
        if i == 0 or j == 0:
            return 0
        if s1[i - 1] == s2[j - 1]:
            return 1 + solve(s1, i - 1, s2, j - 1)
        else:
            return max(solve(s1, i - 1, s2, j), solve(s1, i, s2, j - 1))

    def min_inserts_for_palindrome(s1, s2):
        n = len(s1)
        m = len(s2)
        return solve(s1, n, s2, m)

    print(min_inserts_for_palindrome("abcd", "abzd"))


def memoized():
    """
        Time complexity is O(m * n) and space complexity is O(m + n + m*n).
    """
    def solve(s1, i, s2, j, dp):
        if i == 0 or j == 0:
            return 0
        if dp[i][j] is not None:
            return dp[i][j]
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = 1 + solve(s1, i - 1, s2, j - 1, dp)
        else:
            dp[i][j] = max(solve(s1, i - 1, s2, j, dp), solve(s1, i, s2, j - 1, dp))
        return dp[i][j]

    def min_inserts_for_palindrome(s1, s2):
        n = len(s1)
        m = len(s2)
        dp = {i: {j: None for j in range(m + 1)} for i in range(n + 1)}
        return solve(s1, n, s2, m, dp)

    print(min_inserts_for_palindrome("abcd", "abzd"))


def tabulation():
    """
        Time complexity is O(m * n) and space complexity is O(m * n).
    """
    def min_inserts_for_palindrome(s1, s2):
        n = len(s1)
        m = len(s2)
        dp = {i: {j: 0 for j in range(m + 1)} for i in range(n + 1)}
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n][m]

    print(min_inserts_for_palindrome("abcd", "abzd"))


def space_optimized():
    """
        Time complexity is O(m * n) and space complexity is O(m).
    """
    def min_inserts_for_palindrome(s1, s2):
        n = len(s1)
        m = len(s2)
        prev = {j: 0 for j in range(m + 1)}
        for i in range(1, n + 1):
            curr = {j: 0 for j in range(m + 1)}
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr
        return prev[m]

    print(min_inserts_for_palindrome("abcd", "abzd"))


class Solution:
    @staticmethod
    def _lcs_length(s1, s2):
        n = len(s1)
        m = len(s2)
        prev = {j: 0 for j in range(m + 1)}
        for i in range(1, n + 1):
            curr = {j: 0 for j in range(m + 1)}
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr
        return prev[m]

    @staticmethod
    def min_insertions(string):
        """
            Overall time complexity is O(n^2) and space complexity is O(n).
        """
        reversed = string[-1:-len(string)-1:-1]
        lcs_length = Solution._lcs_length(string, reversed)
        return len(string) - lcs_length


print(Solution.min_insertions("abca"))
print(Solution.min_insertions("abcdefg"))
print(Solution.min_insertions("aaaaa"))
print(Solution.min_insertions("zzazz"))
print(Solution.min_insertions("mbadm"))
print(Solution.min_insertions("leetcode"))
