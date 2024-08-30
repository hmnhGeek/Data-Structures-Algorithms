def recursive():
    def solve_edit_distance(s1, i, s2, j):
        # Time complexity is exponential and space complexity is O(n + m).

        # if s1 is exhausted, then we simply need insert operations `left over characters of s2` times,
        # which is `j + 1`.
        if i < 0:
            return j + 1

        # if s2 is exhausted, we need to simply delete from s1 to come to s2 and that would be `leftover
        # characters from s1`, i.e., i + 1.
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
    print(edit_distance("geek", "gesek"))
    print(edit_distance("cat", "cut"))
    print(edit_distance("sunday", "saturday"))


def memoized():
    def solve_edit_distance(s1, i, s2, j, dp):
        # Time complexity is O(m + n) and space complexity is O(n + m + m*n).

        # if s1 is exhausted, then we simply need insert operations `left over characters of s2` times,
        # which is `j + 1`.
        if i < 0:
            return j + 1

        # if s2 is exhausted, we need to simply delete from s1 to come to s2 and that would be `leftover
        # characters from s1`, i.e., i + 1.
        if j < 0:
            return i + 1

        if dp[i][j] is not None:
            return dp[i][j]

        if s1[i] == s2[j]:
            dp[i][j] = solve_edit_distance(s1, i - 1, s2, j - 1, dp)
        else:
            # insert post `i` index in s1; thus an insert operation in s1 and so, i remains the same
            # but `j` will reduce because we have made a match. `i` is still on the non-matched character.
            insert = 1 + solve_edit_distance(s1, i, s2, j - 1, dp)

            # we can also delete the index `i` and move to `i - 1` and try to match it with `j`
            delete = 1 + solve_edit_distance(s1, i - 1, s2, j, dp)

            # we can replace character at index `i` to match it with `j` and then reduce both.
            replace = 1 + solve_edit_distance(s1, i - 1, s2, j - 1, dp)

            # out of all three done above, we will return minimum operations count.
            dp[i][j] = min(insert, delete, replace)
        return dp[i][j]

    def edit_distance(s1, s2):
        n = len(s1)
        m = len(s2)
        dp = {i: {j: None for j in range(m)} for i in range(n)}
        return solve_edit_distance(s1, n - 1, s2, m - 1, dp)

    print(edit_distance("horse", "ros"))
    print(edit_distance("abc", "dc"))
    print(edit_distance("whgtdwhgtdg", "aswcfg"))
    print(edit_distance("geek", "gesek"))
    print(edit_distance("cat", "cut"))
    print(edit_distance("sunday", "saturday"))


def tabulation():
    def solve_edit_distance(s1, i, s2, j, dp):
        # Time complexity is O(m*n) and space complexity is O(n + m + m*n).

        # if s1 is exhausted, then we simply need insert operations `left over characters of s2` times,
        # which is `j + 1`.
        if i == 0:
            return j + 1

        # if s2 is exhausted, we need to simply delete from s1 to come to s2 and that would be `leftover
        # characters from s1`, i.e., i + 1.
        if j == 0:
            return i + 1

        if dp[i][j] is not None:
            return dp[i][j]

        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = solve_edit_distance(s1, i - 1, s2, j - 1, dp)
        else:
            # insert post `i` index in s1; thus an insert operation in s1 and so, i remains the same
            # but `j` will reduce because we have made a match. `i` is still on the non-matched character.
            insert = 1 + solve_edit_distance(s1, i, s2, j - 1, dp)

            # we can also delete the index `i` and move to `i - 1` and try to match it with `j`
            delete = 1 + solve_edit_distance(s1, i - 1, s2, j, dp)

            # we can replace character at index `i` to match it with `j` and then reduce both.
            replace = 1 + solve_edit_distance(s1, i - 1, s2, j - 1, dp)

            # out of all three done above, we will return minimum operations count.
            dp[i][j] = min(insert, delete, replace)
        return dp[i][j]

    def edit_distance(s1, s2):
        """
            Time complexity will be O(m*n) and space would be O(m*n).
        """

        # whenever we have i < 0 or j < 0 kind of base conditions in recursion, try to bring indexing scheme to 1-based
        # indexing scheme. We don't need the recursive solution above, but just for reference, you can consider the
        # code above to be utilized here. In this recursion, we have taken 1-based indexing. Just ensure that when you
        # refer to any index in strings s1 or s2, subtract 1 from it to bring back to 0-based indexing scheme.

        n = len(s1)
        m = len(s2)

        # note that i and j will now run till n and m.
        dp = {i: {j: 0 for j in range(m + 1)} for i in range(n + 1)}

        # index 0 of s1 (refer recursive solution in tabulation)
        for j in dp[0]:
            dp[0][j] = j

        # index 0 of s2 (refer recursive solution in tabulation)
        for i in dp:
            dp[i][0] = i

        # note that i and j will now run till n and m.
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # insert post `i` index in s1; thus an insert operation in s1 and so, i remains the same
                    # but `j` will reduce because we have made a match. `i` is still on the non-matched character.
                    insert = 1 + dp[i][j - 1]

                    # we can also delete the index `i` and move to `i - 1` and try to match it with `j`
                    delete = 1 + dp[i - 1][j]

                    # we can replace character at index `i` to match it with `j` and then reduce both.
                    replace = 1 + dp[i - 1][j - 1]

                    # out of all three done above, we will return minimum operations count.
                    dp[i][j] = min(insert, delete, replace)

        # answer always lie on the last index of the dp array
        return dp[n][m]

    print(edit_distance("horse", "ros"))
    print(edit_distance("abc", "dc"))
    print(edit_distance("whgtdwhgtdg", "aswcfg"))
    print(edit_distance("geek", "gesek"))
    print(edit_distance("cat", "cut"))
    print(edit_distance("sunday", "saturday"))


recursive()
print()
memoized()
print()
tabulation()
