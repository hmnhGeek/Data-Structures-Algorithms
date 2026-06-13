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


recursive()
print()
