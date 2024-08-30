# Problem link - https://www.naukri.com/code360/problems/wildcard-pattern-matching_701650?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=ZmlQ3vgAOMo&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=36


# function to check if a slice of string with 1-based indexing contains all *s or not.
def check_all_stars(string, index):
    for i in range(1, index + 1):
        if string[i - 1] != "*":
            return False
    return True


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
            return all(k == "*" for k in s1[:i+1])

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


def memoized():
    # use 1 based indexing because we observed that we have a base condition i < 0 and j < 0 in the recursive solution.
    def solve_wildcard(s1, i, s2, j, dp):
        # Time complexity is O(m*n) and space complexity is O(m + n + m*n).

        # if we have exhausted 1st string (the one with wildcards), then second string must also get exhausted
        # in order to find a match.
        if i == 0:
            return j == 0

        # if string 2 got exhausted but not string 1, check now if string 1 has all "*"s because only *s can
        # be matched with a blank string.
        if j == 0:
            return check_all_stars(s1, i)

        if dp[i][j] is not None:
            return dp[i][j]

        # if s1[i] matches with s2[j] or s1[i] is a "?", then we have found a match, move both i and j below.
        if s1[i - 1] == s2[j - 1] or s1[i - 1] == "?":
            dp[i][j] = solve_wildcard(s1, i - 1, s2, j - 1, dp)

        # if s1[i] is a "*", then we can have 2 cases to solve for.
        elif s1[i - 1] == "*":
            # we consider the jth character from s2 to match with *. Stay on * but in s2, move one index below.
            match_with_star = solve_wildcard(s1, i, s2, j - 1, dp)

            # we don't match `j` with *. In that case, we have now introduced a discontinuity. We must not use
            # * now. Reduce i but stay on j as j is still not matched.
            dont_match_with_star = solve_wildcard(s1, i - 1, s2, j, dp)

            # return `or` between them.
            dp[i][j] = match_with_star or dont_match_with_star
        else:
            # if there is no wildcard character and also i and j don't match, return False, because we have found
            # a character where both strings don't have a match, so overall they are different.
            dp[i][j] = False
        return dp[i][j]

    def wildcard(s1, s2):
        n = len(s1)
        m = len(s2)
        dp = {i: {j: None for j in range(m + 1)} for i in range(n + 1)}
        return solve_wildcard(s1, n, s2, m, dp)

    print(wildcard("?ay", "ray"))
    print(wildcard("ab*cd", "abdefcd"))
    print(wildcard("ab?d", "abcc"))
    print(wildcard("ba*a?", "baaabab"))
    print(wildcard("a*ab", "baaabab"))
    print(wildcard("aa", "a"))
    print(wildcard("*", "aa"))
    print(wildcard("?a", "cb"))


def tabulation():
    # use 1 based indexing because we observed that we have a base condition i < 0 and j < 0 in the recursive solution.
    def wildcard(s1, s2):
        """
            Time complexity is O(n*m) and space complexity is also O(m*n).
        """

        n = len(s1)
        m = len(s2)
        dp = {i: {j: False for j in range(m + 1)} for i in range(n + 1)}

        # only when i = 0 and j = 0 at the same time, we can say the string match
        dp[0][0] = True

        # for all the indices in string1 and blank string 2 (j = 0); check if the slices till :i in string 1 are all *s
        # or not. Refer base case in memoization and recursive solutions.
        for i in range(1, n + 1):
            dp[i][0] = check_all_stars(s1, i)

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # if s1[i] matches with s2[j] or s1[i] is a "?", then we have found a match, move both i and j below.
                if s1[i - 1] == s2[j - 1] or s1[i - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]

                # if s1[i] is a "*", then we can have 2 cases to solve for.
                elif s1[i - 1] == "*":
                    # we consider the jth character from s2 to match with *. Stay on * but in s2, move one index below.
                    match_with_star = dp[i][j - 1]

                    # we don't match `j` with *. In that case, we have now introduced a discontinuity. We must not use
                    # * now. Reduce i but stay on j as j is still not matched.
                    dont_match_with_star = dp[i - 1][j]

                    # return `or` between them.
                    dp[i][j] = match_with_star or dont_match_with_star
                else:
                    # if there is no wildcard character and also i and j don't match, return False, because we have
                    # found a character where both strings don't have a match, so overall they are different.
                    dp[i][j] = False

        return dp[n][m]

    print(wildcard("?ay", "ray"))
    print(wildcard("ab*cd", "abdefcd"))
    print(wildcard("ab?d", "abcc"))
    print(wildcard("ba*a?", "baaabab"))
    print(wildcard("a*ab", "baaabab"))
    print(wildcard("aa", "a"))
    print(wildcard("*", "aa"))
    print(wildcard("?a", "cb"))


def space_optimized():
    # use 1 based indexing because we observed that we have a base condition i < 0 and j < 0 in the recursive solution.
    def wildcard(s1, s2):
        """
            Time complexity is O(n*m) and space complexity is also O(m).
        """

        n = len(s1)
        m = len(s2)

        prev = {j: False for j in range(m + 1)}
        # prev represents i = 0; and for j = 0 at the same time, we can say the strings match
        prev[0] = True

        for i in range(1, n + 1):
            curr = {j: False for j in range(m + 1)}
            # for all the indices in string1 and blank string 2 (j = 0); check if the slices till :i in string 1 are
            # all *s or not. Refer base case in memoization and recursive solutions.
            curr[0] = check_all_stars(s1, i)

            for j in range(1, m + 1):
                # if s1[i] matches with s2[j] or s1[i] is a "?", then we have found a match, move both i and j below.
                if s1[i - 1] == s2[j - 1] or s1[i - 1] == "?":
                    curr[j] = prev[j - 1]

                # if s1[i] is a "*", then we can have 2 cases to solve for.
                elif s1[i - 1] == "*":
                    # we consider the jth character from s2 to match with *. Stay on * but in s2, move one index below.
                    match_with_star = curr[j - 1]

                    # we don't match `j` with *. In that case, we have now introduced a discontinuity. We must not use
                    # * now. Reduce i but stay on j as j is still not matched.
                    dont_match_with_star = prev[j]

                    # return `or` between them.
                    curr[j] = match_with_star or dont_match_with_star
                else:
                    # if there is no wildcard character and also i and j don't match, return False, because we have
                    # found a character where both strings don't have a match, so overall they are different.
                    curr[j] = False
            prev = curr

        return prev[m]

    print(wildcard("?ay", "ray"))
    print(wildcard("ab*cd", "abdefcd"))
    print(wildcard("ab?d", "abcc"))
    print(wildcard("ba*a?", "baaabab"))
    print(wildcard("a*ab", "baaabab"))
    print(wildcard("aa", "a"))
    print(wildcard("*", "aa"))
    print(wildcard("?a", "cb"))


print("Recursion Solution")
recursive()

print()
print("Memoized Solution")
memoized()

print()
print("Tabulation Solution")
tabulation()

print()
print("Space Optimized Solution")
space_optimized()