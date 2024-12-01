def recursive():
    """
        Time complexity is exponential and space complexity is O(n1 + n2).
    """
    def solve(s1, i, s2, j):
        # if s1 is exhausted, we need to insert j + 1 characters from s2 to make s1 = s2.
        if i < 0:
            return j + 1

        # if s2 is exhausted, we need to delete i + 1 characters from s1 to make s1 = s2.
        if j < 0:
            return i + 1

        if s1[i] == s2[j]:
            # if both characters match, simply move to next characters without adding any cost.
            return solve(s1, i - 1, s2, j - 1)
        else:
            # assume that we replaced ith character in s1 to jth character in s2, thus they both now have same
            # characters. Add 1 cost and move to next indices.
            replace = 1 + solve(s1, i - 1, s2, j - 1)

            # maybe ith character is not needed, delete it and check for next character in s1, if it matches with
            # jth character in s2. Add 1 cost.
            deletion = 1 + solve(s1, i - 1, s2, j)

            # insert jth character at ith index. Now the previous ith character will still remain at `i`. So, stay at i
            # only, but decrement j for next character check. Add 1 cost.
            insertion = 1 + solve(s1, i, s2, j - 1)

            # return the minimum cost.
            return min(replace, insertion, deletion)

    def edit_distance(s1: str, s2: str) -> int:
        n1, n2 = len(s1), len(s2)
        return solve(s1, n1 - 1, s2, n2 - 1)

    print(edit_distance("geek", "gesek"))
    print(edit_distance("gfg", "gfg"))
    print(edit_distance("abc", "def"))
    print(edit_distance("horse", "ros"))
    print(edit_distance("intention", "execution"))
    print(edit_distance("abc", "dc"))
    print(edit_distance("whgtdwhgtdg", "aswcfg"))


def memoized():
    """
        Time complexity is O(n1 * n2) and space complexity is O(n1 + n2 + n1*n2).
    """
    def solve(s1, i, s2, j, dp):
        # if s1 is exhausted, we need to insert j + 1 characters from s2 to make s1 = s2.
        if i < 0:
            return j + 1

        # if s2 is exhausted, we need to delete i + 1 characters from s1 to make s1 = s2.
        if j < 0:
            return i + 1

        if dp[i][j] is not None:
            return dp[i][j]

        if s1[i] == s2[j]:
            # if both characters match, simply move to next characters without adding any cost.
            dp[i][j] = solve(s1, i - 1, s2, j - 1, dp)
        else:
            # assume that we replaced ith character in s1 to jth character in s2, thus they both now have same
            # characters. Add 1 cost and move to next indices.
            replace = 1 + solve(s1, i - 1, s2, j - 1, dp)

            # maybe ith character is not needed, delete it and check for next character in s1, if it matches with
            # jth character in s2. Add 1 cost.
            deletion = 1 + solve(s1, i - 1, s2, j, dp)

            # insert jth character at ith index. Now the previous ith character will still remain at `i`. So, stay at i
            # only, but decrement j for next character check. Add 1 cost.
            insertion = 1 + solve(s1, i, s2, j - 1, dp)

            # return the minimum cost.
            dp[i][j] = min(replace, insertion, deletion)
        return dp[i][j]

    def edit_distance(s1: str, s2: str) -> int:
        n1, n2 = len(s1), len(s2)
        dp = {i: {j: None for j in range(n2)} for i in range(n1)}
        return solve(s1, n1 - 1, s2, n2 - 1, dp)

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
