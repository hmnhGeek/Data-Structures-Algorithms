def recursive():
    def solve(s1, i, s2, j):
        if i < 0 and j < 0:
            return 0
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1

        if s1[i] == s2[j]:
            return solve(s1, i - 1, s2, j - 1)
        else:
            return min(
                1 + solve(s1, i - 1, s2, j),
                1 + solve(s1, i, s2, j - 1),
                1 + solve(s1, i - 1, s2, j - 1)
            )

    def edit_distance(s1, s2):
        n1 = len(s1)
        n2 = len(s2)
        return solve(s1, n1 - 1, s2, n2 - 1)

    print(edit_distance("abc", "dc"))
    print(edit_distance("whgtdwhgtdg", "aswcfg"))


recursive()