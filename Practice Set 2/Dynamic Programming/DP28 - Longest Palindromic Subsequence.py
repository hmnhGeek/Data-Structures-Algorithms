def recursive():
    """
        Time complexity is O(2^{n + m}) and space complexity is O(n + m).
    """

    def solve(s1, i, s2, j):
        if i == 0 or j == 0:
            return 0
        if s1[i - 1] == s2[j - 1]:
            return 1 + solve(s1, i - 1, s2, j - 1)
        else:
            return max(
                solve(s1, i - 1, s2, j),
                solve(s1, i, s2, j - 1)
            )

    def lcs(s1, s2):
        n, m = len(s1), len(s2)
        return solve(s1, n, s2, m)

    print(lcs("abcd", "abzd"))


def memoized():
    """
        Time complexity is O(n * m) and space complexity is O(n + m + n*m).
    """

    def solve(s1, i, s2, j, dp):
        if i == 0 or j == 0:
            return 0
        if dp[i][j] is not None:
            return dp[i][j]
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = 1 + solve(s1, i - 1, s2, j - 1, dp)
        else:
            dp[i][j] = max(
                solve(s1, i - 1, s2, j, dp),
                solve(s1, i, s2, j - 1, dp)
            )
        return dp[i][j]

    def lcs(s1, s2):
        n, m = len(s1), len(s2)
        dp = {i: {j: None for j in range(m + 1)} for i in range(n + 1)}
        return solve(s1, n, s2, m, dp)

    print(lcs("abcd", "abzd"))


def tabulation():
    """
        Time complexity is O(n * m) and space complexity is O(n * m).
    """
    def lcs(s1, s2):
        n, m = len(s1), len(s2)
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
        return dp[n][m]

    print(lcs("abcd", "abzd"))


recursive()
print()
memoized()
print()
tabulation()