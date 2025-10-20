def recursive():
    def lcs(s1, s2):
        n, m = len(s1), len(s2)
        return solve(s1, n, s2, m)

    def solve(s1, i, s2, j):
        if i == 0 or j == 0:
            return 0
        if s1[i - 1] == s2[j - 1]:
            return 1 + solve(s1, i - 1, s2, j - 1)
        else:
            return max(
                solve(s1, i, s2, j - 1),
                solve(s1, i - 1, s2, j)
            )

    print(lcs("adebc", "dcadb"))
    print(lcs("ab", "defg"))
    print(lcs("AGGTAB", "GXTXAYB"))
    print(lcs("ABC", "CBA"))


def memoized():
    def lcs(s1, s2):
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
            dp[i][j] = max(
                solve(s1, i, s2, j - 1, dp),
                solve(s1, i - 1, s2, j, dp)
            )
        return dp[i][j]

    print(lcs("adebc", "dcadb"))
    print(lcs("ab", "defg"))
    print(lcs("AGGTAB", "GXTXAYB"))
    print(lcs("ABC", "CBA"))


def tabulation():
    def lcs(s1, s2):
        n, m = len(s1), len(s2)
        dp = {i: {j: 0 for j in range(m + 1)} for i in range(n + 1)}
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[n][m]

    print(lcs("adebc", "dcadb"))
    print(lcs("ab", "defg"))
    print(lcs("AGGTAB", "GXTXAYB"))
    print(lcs("ABC", "CBA"))


def space_optimized():
    def lcs(s1, s2):
        n, m = len(s1), len(s2)
        prev = {j: 0 for j in range(m + 1)}
        for i in range(1, n + 1):
            curr = {j: 0 for j in range(m + 1)}
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(curr[j - 1], prev[j])
            prev = curr
        return prev[m]

    print(lcs("adebc", "dcadb"))
    print(lcs("ab", "defg"))
    print(lcs("AGGTAB", "GXTXAYB"))
    print(lcs("ABC", "CBA"))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
