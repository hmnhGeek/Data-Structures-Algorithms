def recursive():
    """
        Time complexity is exponential and space complexity is O(n + m).
    """
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
        Time complexity is O(nm) and space complexity is O(n + m + nm).
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


recursive()
print()
memoized()