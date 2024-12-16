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


recursive()