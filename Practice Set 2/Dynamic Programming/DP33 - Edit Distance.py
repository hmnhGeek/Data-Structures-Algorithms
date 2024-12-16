def recursive():
    """
        Time complexity is O(3^{n + m}) and space complexity is O(n + m).
    """

    def solve(s1, i, s2, j):
        if i == 0:
            return j
        if j == 0:
            return i
        if s1[i - 1] == s2[j - 1]:
            return solve(s1, i - 1, s2, j - 1)
        else:
            delete = 1 + solve(s1, i - 1, s2, j)
            replace = 1 + solve(s1, i - 1, s2, j - 1)
            insert = 1 + solve(s1, i, s2, j - 1)
            return min(delete, replace, insert)

    def edit_distance(s1, s2):
        n, m = len(s1), len(s2)
        return solve(s1, n, s2, m)

    print(edit_distance("horse", "ros"))
    print(edit_distance("abc", "dc"))
    print(edit_distance("whgtdwhgtdg", "aswcfg"))
    print(edit_distance("intention", "execution"))
    print(edit_distance("geek", "gesek"))
    print(edit_distance("cat", "cut"))
    print(edit_distance("sunday", "saturday"))


def memoized():
    """
        Time complexity is O(n * m) and space complexity is O(n + m + n * m).
    """

    def solve(s1, i, s2, j, dp):
        if i == 0:
            return j
        if j == 0:
            return i
        if dp[i][j] is not None:
            return dp[i][j]
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = solve(s1, i - 1, s2, j - 1, dp)
        else:
            delete = 1 + solve(s1, i - 1, s2, j, dp)
            replace = 1 + solve(s1, i - 1, s2, j - 1, dp)
            insert = 1 + solve(s1, i, s2, j - 1, dp)
            dp[i][j] = min(delete, replace, insert)
        return dp[i][j]

    def edit_distance(s1, s2):
        n, m = len(s1), len(s2)
        dp = {i: {j: None for j in range(m + 1)} for i in range(n + 1)}
        return solve(s1, n, s2, m, dp)

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