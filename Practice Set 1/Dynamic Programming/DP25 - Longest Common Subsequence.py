def recursive():
    """
        Time complexity is exponential and space is O(n1 + n2)
    """
    def solve(s1, i, s2, j):
        if i < 0 or j < 0:
            return 0

        if s1[i] == s2[j]:
            return 1 + solve(s1, i - 1, s2, j - 1)
        else:
            return max(
                solve(s1, i, s2, j - 1),
                solve(s1, i - 1, s2, j)
            )

    def lcs_length(s1, s2):
        n1, n2 = len(s1), len(s2)
        return solve(s1, n1 - 1, s2, n2 - 1)

    print(lcs_length("adebc", "dcadb"))
    print(lcs_length("ab", "defg"))
    print(lcs_length("AGGTAB", "GXTXAYB"))
    print(lcs_length("ABC", "CBA"))


def memoized():
    """
        Time complexity is O(n1*n2) and space is O(n1 + n2 + n1*n2)
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
                solve(s1, i, s2, j - 1, dp),
                solve(s1, i - 1, s2, j, dp)
            )
        return dp[i][j]

    def lcs_length(s1, s2):
        n1, n2 = len(s1), len(s2)
        dp = {i: {j: None for j in range(n2 + 1)} for i in range(n1 + 1)}
        return solve(s1, n1, s2, n2, dp)

    print(lcs_length("adebc", "dcadb"))
    print(lcs_length("ab", "defg"))
    print(lcs_length("AGGTAB", "GXTXAYB"))
    print(lcs_length("ABC", "CBA"))


recursive()
print()
memoized()