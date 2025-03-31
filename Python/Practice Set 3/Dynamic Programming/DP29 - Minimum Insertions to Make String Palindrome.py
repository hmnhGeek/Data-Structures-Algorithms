# Problem link - https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/description/
# Solution - https://www.youtube.com/watch?v=xPBLEj41rFU&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=30


def recursive():
    def solve(s1, i, s2, j):
        if i == 0 or j == 0:
            return 0
        if s1[i - 1] == s2[j - 1]:
            return 1 + solve(s1, i - 1, s2, j - 1)
        else:
            return max(solve(s1, i - 1, s2, j), solve(s1, i, s2, j - 1))

    def lcs(s1, s2):
        n1, n2 = len(s1), len(s2)
        return solve(s1, n1, s2, n2)

    print(lcs("adebc", "dcadb"))
    print(lcs("ab", "defg"))
    print(lcs("abcde", "ace"))
    print(lcs("abc", "abc"))
    print(lcs("abc", "acd"))
    print(lcs("AGGTAB", "GXTXAYB"))
    print(lcs("ABC", "CBA"))


def memoized():
    """
        Time complexity is O(n1 * n2) and space complexity is O(n1 + n2 + n1 * n2).
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

    def lcs(s1, s2):
        n1, n2 = len(s1), len(s2)
        dp = {i: {j: None for j in range(n2 + 1)} for i in range(n1 + 1)}
        return solve(s1, n1, s2, n2, dp)

    print(lcs("adebc", "dcadb"))
    print(lcs("ab", "defg"))
    print(lcs("abcde", "ace"))
    print(lcs("abc", "abc"))
    print(lcs("abc", "acd"))
    print(lcs("AGGTAB", "GXTXAYB"))
    print(lcs("ABC", "CBA"))


def tabulation():
    """
        Time complexity is O(n1 * n2) and space complexity is O(n1 * n2).
    """
    def lcs(s1, s2):
        n1, n2 = len(s1), len(s2)
        dp = {i: {j: 0 for j in range(n2 + 1)} for i in range(n1 + 1)}
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n1][n2]

    print(lcs("adebc", "dcadb"))
    print(lcs("ab", "defg"))
    print(lcs("abcde", "ace"))
    print(lcs("abc", "abc"))
    print(lcs("abc", "acd"))
    print(lcs("AGGTAB", "GXTXAYB"))
    print(lcs("ABC", "CBA"))


def space_optimized():
    """
        Time complexity is O(n1 * n2) and space complexity is O(n2).
    """
    def lcs(s1, s2):
        n1, n2 = len(s1), len(s2)
        prev = {j: 0 for j in range(n2 + 1)}
        for i in range(1, n1 + 1):
            curr = {j: 0 for j in range(n2 + 1)}
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr
        return prev[n2]

    print(lcs("adebc", "dcadb"))
    print(lcs("ab", "defg"))
    print(lcs("abcde", "ace"))
    print(lcs("abc", "abc"))
    print(lcs("abc", "acd"))
    print(lcs("AGGTAB", "GXTXAYB"))
    print(lcs("ABC", "CBA"))


class Solution:
    @staticmethod
    def _lcs(s1, s2):
        n1, n2 = len(s1), len(s2)
        prev = {j: 0 for j in range(n2 + 1)}
        for i in range(1, n1 + 1):
            curr = {j: 0 for j in range(n2 + 1)}
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr
        return prev[n2]

    @staticmethod
    def min_insertions(s):
        """
            Time complexity is O(n^2) and space complexity is O(n).
        """
        n = len(s)
        lps_length = Solution._lcs(s, s[-1:-len(s)-1:-1])
        return n - lps_length


print(Solution.min_insertions("abca"))
print(Solution.min_insertions("abcdefg"))
print(Solution.min_insertions("aaaaa"))
print(Solution.min_insertions("zzazz"))
print(Solution.min_insertions("mbadm"))
print(Solution.min_insertions("leetcode"))

