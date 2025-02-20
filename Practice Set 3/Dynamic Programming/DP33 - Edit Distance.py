def recursive():
    """
        Time complexity is exponential and space complexity is O(n1 + n2).
    """
    def solve(s1, i, s2, j):
        if i == 0:
            return j
        if j == 0:
            return i
        if s1[i - 1] == s2[j - 1]:
            return solve(s1, i - 1, s2, j - 1)
        else:
            return min(
                1 + solve(s1, i - 1, s2, j),
                1 + solve(s1, i, s2, j - 1),
                1 + solve(s1, i - 1, s2, j - 1)
            )

    def edit_distance(s1, s2):
        n1, n2 = len(s1), len(s2)
        return solve(s1, n1, s2, n2)

    print(edit_distance("horse", "ros"))
    print(edit_distance("abc", "dc"))
    print(edit_distance("whgtdwhgtdg", "aswcfg"))
    print(edit_distance("intention", "execution"))
    print(edit_distance("geek", "gesek"))
    print(edit_distance("cat", "cut"))
    print(edit_distance("sunday", "saturday"))


def memoized():
    """
        Time complexity is O(n1 * n2) and space complexity is O(n1 + n2 + n1 * n2).
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
            dp[i][j] = min(
                1 + solve(s1, i - 1, s2, j, dp),
                1 + solve(s1, i, s2, j - 1, dp),
                1 + solve(s1, i - 1, s2, j - 1, dp)
            )
        return dp[i][j]

    def edit_distance(s1, s2):
        n1, n2 = len(s1), len(s2)
        dp = {i: {j: None for j in range(n2 + 1)} for i in range(n1 + 1)}
        return solve(s1, n1, s2, n2, dp)

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