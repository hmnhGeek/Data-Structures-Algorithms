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


recursive()
print()
memoized()
print()
