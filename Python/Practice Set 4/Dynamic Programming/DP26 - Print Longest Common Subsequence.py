def recursive():
    def get_lcs(s1, s2):
        n1, n2 = len(s1), len(s2)
        return solve(s1, n1, s2, n2)

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

    print(get_lcs("adebc", "dcadb"))
    print(get_lcs("ab", "defg"))
    print(get_lcs("abcde", "ace"))
    print(get_lcs("abc", "abc"))
    print(get_lcs("abc", "acd"))
    print(get_lcs("AGGTAB", "GXTXAYB"))
    print(get_lcs("ABC", "CBA"))


def memoized():
    def get_lcs(s1, s2):
        n1, n2 = len(s1), len(s2)
        dp = {i: {j: None for j in range(n2 + 1)} for i in range(n1 + 1)}
        return solve(s1, n1, s2, n2, dp)

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

    print(get_lcs("adebc", "dcadb"))
    print(get_lcs("ab", "defg"))
    print(get_lcs("abcde", "ace"))
    print(get_lcs("abc", "abc"))
    print(get_lcs("abc", "acd"))
    print(get_lcs("AGGTAB", "GXTXAYB"))
    print(get_lcs("ABC", "CBA"))


def tabulation():
    def get_lcs(s1, s2):
        n1, n2 = len(s1), len(s2)
        dp = {i: {j: 0 for j in range(n2 + 1)} for i in range(n1 + 1)}
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n1][n2]

    print(get_lcs("adebc", "dcadb"))
    print(get_lcs("ab", "defg"))
    print(get_lcs("abcde", "ace"))
    print(get_lcs("abc", "abc"))
    print(get_lcs("abc", "acd"))
    print(get_lcs("AGGTAB", "GXTXAYB"))
    print(get_lcs("ABC", "CBA"))

