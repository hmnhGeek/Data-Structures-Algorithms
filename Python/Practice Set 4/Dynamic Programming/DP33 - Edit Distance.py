def recursive():
    """
        Time complexity is exponential and space complexity is O(n + m).
    """
    def edit_distance(s, p):
        n, m = len(s), len(p)
        return solve(s, n, p, m)

    def solve(s, i, p, j):
        if j == 0:
            return i
        if i == 0:
            return j
        if s[i - 1] == p[j - 1]:
            return solve(s, i - 1, p, j - 1)
        else:
            return 1 + min(solve(s, i, p, j - 1), solve(s, i - 1, p, j), solve(s, i - 1, p, j - 1))

    print(edit_distance("horse", "ros"))
    print(edit_distance("abc", "dc"))
    print(edit_distance("whgtdwhgtdg", "aswcfg"))
    print(edit_distance("intention", "execution"))
    print(edit_distance("geek", "gesek"))
    print(edit_distance("cat", "cut"))
    print(edit_distance("sunday", "saturday"))


def memoized():
    """
        Time complexity is O(nm) and space complexity is O(n + m + nm).
    """

    def edit_distance(s, p):
        n, m = len(s), len(p)
        dp = {i: {j: None for j in range(m + 1)} for i in range(n + 1)}
        return solve(s, n, p, m, dp)

    def solve(s, i, p, j, dp):
        if j == 0:
            return i
        if i == 0:
            return j
        if dp[i][j] is not None:
            return dp[i][j]
        if s[i - 1] == p[j - 1]:
            dp[i][j] = solve(s, i - 1, p, j - 1, dp)
        else:
            dp[i][j] = 1 + min(solve(s, i, p, j - 1, dp), solve(s, i - 1, p, j, dp), solve(s, i - 1, p, j - 1, dp))
        return dp[i][j]

    print(edit_distance("horse", "ros"))
    print(edit_distance("abc", "dc"))
    print(edit_distance("whgtdwhgtdg", "aswcfg"))
    print(edit_distance("intention", "execution"))
    print(edit_distance("geek", "gesek"))
    print(edit_distance("cat", "cut"))
    print(edit_distance("sunday", "saturday"))


def tabulation():
    """
        Time complexity is O(nm) and space complexity is O(nm).
    """

    def edit_distance(s, p):
        n, m = len(s), len(p)
        dp = {i: {j: 1e6 for j in range(m + 1)} for i in range(n + 1)}
        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
        return dp[n][m]

    print(edit_distance("horse", "ros"))
    print(edit_distance("abc", "dc"))
    print(edit_distance("whgtdwhgtdg", "aswcfg"))
    print(edit_distance("intention", "execution"))
    print(edit_distance("geek", "gesek"))
    print(edit_distance("cat", "cut"))
    print(edit_distance("sunday", "saturday"))


recursive()
print()
memoized()
print()
tabulation()
print()
