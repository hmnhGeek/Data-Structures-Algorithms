def recursive():
    def solve_edit_distance(s1, i, s2, j):
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1

        if s1[i] == s2[j]:
            return solve_edit_distance(s1, i - 1, s2, j - 1)
        else:
            # insert post `i` index in s1; thus an insert operation in s1 and so, i remains the same
            # but `j` will reduce because we have made a match. `i` is still on the non-matched character.
            insert = 1 + solve_edit_distance(s1, i, s2, j - 1)

            # we can also delete the index `i` and move to `i - 1` and try to match it with `j`
            delete = 1 + solve_edit_distance(s1, i - 1, s2, j)

            # we can replace character at index `i` to match it with `j` and then reduce both.
            replace = 1 + solve_edit_distance(s1, i - 1, s2, j - 1)

            # out of all three done above, we will return minimum operations count.
            return min(insert, delete, replace)

    def edit_distance(s1, s2):
        n1 = len(s1)
        n2 = len(s2)
        return solve_edit_distance(s1, n1 - 1, s2, n2 - 1)

    print(edit_distance("horse", "ros"))
    print(edit_distance("abc", "dc"))
    print(edit_distance("whgtdwhgtdg", "aswcfg"))


recursive()
