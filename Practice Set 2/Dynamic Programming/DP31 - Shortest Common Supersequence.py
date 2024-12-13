def recursive():
    """
        Time complexity is O(2^{m + n}) and space complexity is O(m + n).
    """
    def solve(s1, i, s2, j):
        if i < 0 or j < 0:
            return 0
        if s1[i] == s2[j]:
            return 1 + solve(s1, i - 1, s2, j - 1)
        else:
            return max(solve(s1, i - 1, s2, j), solve(s1, i, s2, j - 1))

    def lcs_length(s1, s2):
        n, m = len(s1), len(s2)
        return solve(s1, n - 1, s2, m - 1)

    print(lcs_length("abcd", "abzd"))


def memoized():
    """
        Time complexity is O(2^{m + n}) and space complexity is O(m + n).
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

    def lcs_length(s1, s2):
        n, m = len(s1), len(s2)
        dp = {i: {j: None for j in range(m + 1)} for i in range(n + 1)}
        return solve(s1, n, s2, m, dp)

    print(lcs_length("abcd", "abzd"))


recursive()
print()
memoized()