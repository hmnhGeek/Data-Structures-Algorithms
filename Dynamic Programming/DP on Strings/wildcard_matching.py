def recursive():
    def solve_wildcard(s1, i, s2, j):
        # Time complexity is exponential and space complexity is O(m + n).

        # if we have exhausted 1st string (the one with wildcards), then second string must also get exhausted
        # in order to find a match.
        if i < 0:
            return j < 0

        # if string 2 got exhausted but not string 1, check now if string 1 has all "*"s because only *s can
        # be matched with a blank string.
        if j < 0:
            return all(i == "*" for i in s1)

        # if s1[i] matches with s2[j] or s1[i] is a "?", then we have found a match, move both i and j below.
        if s1[i] == s2[j] or s1[i] == "?":
            return solve_wildcard(s1, i - 1, s2, j - 1)

        # if s1[i] is a "*", then we can have 2 cases to solve for.
        elif s1[i] == "*":
            # we consider the jth character from s2 to match with *. Stay on * but in s2, move one index below.
            match_with_star = solve_wildcard(s1, i, s2, j - 1)

            # we don't match `j` with *. In that case, we have now introduced a discontinuity. We must not use
            # * now. Reduce i but stay on j as j is still not matched.
            dont_match_with_star = solve_wildcard(s1, i - 1, s2, j)

            # return `or` between them.
            return match_with_star or dont_match_with_star
        else:
            # if there is no wildcard character and also i and j don't match, return False, because we have found
            # a character where both strings don't have a match, so overall they are different.
            return False

    def wildcard(s1, s2):
        n = len(s1)
        m = len(s2)

        return solve_wildcard(s1, n - 1, s2, m - 1)

    print(wildcard("?ay", "ray"))
    print(wildcard("ab*cd", "abdefcd"))
    print(wildcard("ab?d", "abcc"))
    print(wildcard("ba*a?", "baaabab"))
    print(wildcard("a*ab", "baaabab"))
    print(wildcard("aa", "a"))
    print(wildcard("*", "aa"))
    print(wildcard("?a", "cb"))


recursive()