# Problem link - https://www.naukri.com/code360/problems/can-you-make_4244510?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=yMnH0jrir0Q&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=31


def recursive():
    """
        Time complexity is exponential and space complexity is O(n + m).
    """
    def get_lcs_length(s1, s2):
        n, m = len(s1), len(s2)
        return solve(s1, n, s2, m)

    def solve(s1, i, s2, j):
        if i == 0 or j == 0:
            return 0
        if s1[i - 1] == s2[j - 1]:
            return 1 + solve(s1, i - 1, s2, j - 1)
        else:
            return max(solve(s1, i - 1, s2, j), solve(s1, i, s2, j - 1))

    print(get_lcs_length("adebc", "dcadb"))
    print(get_lcs_length("ab", "defg"))
    print(get_lcs_length("abcde", "ace"))
    print(get_lcs_length("abc", "abc"))
    print(get_lcs_length("abc", "acd"))
    print(get_lcs_length("AGGTAB", "GXTXAYB"))
    print(get_lcs_length("ABC", "CBA"))


def memoized():
    """
        Time complexity is O(nm) and space complexity is O(n + m + nm).
    """
    def get_lcs_length(s1, s2):
        n, m = len(s1), len(s2)
        dp = {i: {j: None for j in range(m + 1)} for i in range(n + 1)}
        return solve(s1, n, s2, m, dp)

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

    print(get_lcs_length("adebc", "dcadb"))
    print(get_lcs_length("ab", "defg"))
    print(get_lcs_length("abcde", "ace"))
    print(get_lcs_length("abc", "abc"))
    print(get_lcs_length("abc", "acd"))
    print(get_lcs_length("AGGTAB", "GXTXAYB"))
    print(get_lcs_length("ABC", "CBA"))


def tabulation():
    """
        Time complexity is O(nm) and space complexity is O(nm).
    """
    def get_lcs_length(s1, s2):
        n, m = len(s1), len(s2)
        dp = {i: {j: 0 for j in range(m + 1)} for i in range(n + 1)}
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n][m]

    print(get_lcs_length("adebc", "dcadb"))
    print(get_lcs_length("ab", "defg"))
    print(get_lcs_length("abcde", "ace"))
    print(get_lcs_length("abc", "abc"))
    print(get_lcs_length("abc", "acd"))
    print(get_lcs_length("AGGTAB", "GXTXAYB"))
    print(get_lcs_length("ABC", "CBA"))


def space_optimized():
    """
        Time complexity is O(nm) and space complexity is O(m).
    """
    def get_lcs_length(s1, s2):
        n, m = len(s1), len(s2)
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

    print(get_lcs_length("adebc", "dcadb"))
    print(get_lcs_length("ab", "defg"))
    print(get_lcs_length("abcde", "ace"))
    print(get_lcs_length("abc", "abc"))
    print(get_lcs_length("abc", "acd"))
    print(get_lcs_length("AGGTAB", "GXTXAYB"))
    print(get_lcs_length("ABC", "CBA"))


class Solution:
    @staticmethod
    def _get_lcs_length(s1, s2):
        n, m = len(s1), len(s2)
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
    def get_min_ops(s1, s2):
        """
            Time complexity is O(nm) and space complexity is O(m).
        """
        lcs_length = Solution._get_lcs_length(s1, s2)
        return len(s1) + len(s2) - (2 * lcs_length)


print(Solution.get_min_ops("abcd", "anc"))
print(Solution.get_min_ops("aaa", "aa"))
print(Solution.get_min_ops("edl", "xcqja"))
print(Solution.get_min_ops("heap", "pea"))
print(Solution.get_min_ops("geeksforgeeks", "geeks"))
