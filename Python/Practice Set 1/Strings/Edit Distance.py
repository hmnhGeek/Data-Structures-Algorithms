def recursive():
    """
        Time complexity is exponential and space complexity is O(n1 + n2).
    """

    def edit_distance(s, t):
        n, m = len(s), len(t)
        return solve(s, n - 1, t, m - 1)

    def solve(s, i, t, j):
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1
        if s[i] == t[j]:
            return solve(s, i - 1, t, j - 1)
        else:
            return min(
                1 + solve(s, i - 1, t, j),
                1 + solve(s, i, t, j - 1),
                1 + solve(s, i - 1, t, j - 1)
            )

    print(edit_distance("geek", "gesek"))
    print(edit_distance("gfg", "gfg"))
    print(edit_distance("abc", "def"))
    print(edit_distance("horse", "ros"))
    print(edit_distance("intention", "execution"))
    print(edit_distance("abc", "dc"))
    print(edit_distance("whgtdwhgtdg", "aswcfg"))


def memoized():
    """
        Time complexity is O(nm) and space complexity is O(n + m + nm).
    """

    def edit_distance(s, t):
        n, m = len(s), len(t)
        dp = {i: {j: None for j in range(m + 1)} for i in range(n + 1)}
        return solve(s, n, t, m, dp)

    def solve(s, i, t, j, dp):
        if i == 0:
            return j
        if j == 0:
            return i
        if dp[i][j] is not None:
            return dp[i][j]
        if s[i - 1] == t[j - 1]:
            dp[i][j] = solve(s, i - 1, t, j - 1, dp)
        else:
            dp[i][j] = min(
                1 + solve(s, i - 1, t, j, dp),
                1 + solve(s, i, t, j - 1, dp),
                1 + solve(s, i - 1, t, j - 1, dp)
            )
        return dp[i][j]

    print(edit_distance("geek", "gesek"))
    print(edit_distance("gfg", "gfg"))
    print(edit_distance("abc", "def"))
    print(edit_distance("horse", "ros"))
    print(edit_distance("intention", "execution"))
    print(edit_distance("abc", "dc"))
    print(edit_distance("whgtdwhgtdg", "aswcfg"))


recursive()
print()
memoized()
print()