# Problem link - https://leetcode.com/problems/wildcard-matching/description/
# Solution - https://www.youtube.com/watch?v=ZmlQ3vgAOMo&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=35


def recursive():
    """
        Time complexity is exponential and space complexity is O(m + n).
    """

    def wildcard_matching(s1, s2):
        n, m = len(s1), len(s2)
        return solve(s1, n, s2, m)

    def solve(s1, i, s2, j):
        if i == 0 and j > 0:
            return False
        if i == 0 and j == 0:
            return True
        if i > 0 and j == 0:
            all_stars = True
            for k in range(i):
                if s1[k - 1] != "*":
                    all_stars = False
            return all_stars
        if s1[i - 1] == s2[j - 1] or s1[i - 1] == "?":
            return solve(s1, i - 1, s2, j - 1)
        elif s1[i - 1] == "*":
            return solve(s1, i - 1, s2, j) or solve(s1, i, s2, j - 1)
        else:
            return False

    print(wildcard_matching("ab*cd", "abdefcd"))
    print(wildcard_matching("ab?d", "abcc"))
    print(wildcard_matching("?ay", "ray"))
    print(wildcard_matching("ba*a?", "baaabab"))
    print(wildcard_matching("*", "abc"))
    print(wildcard_matching("a*ab", "baaabab"))
    print(wildcard_matching("a?c*", "abcde"))
    print(wildcard_matching("?a", "cb"))


def memoized():
    """
        Time complexity is O(nm) and space complexity is O(m + n + nm).
    """

    def wildcard_matching(s1, s2):
        n, m = len(s1), len(s2)
        dp = {i: {j: None for j in range(m + 1)} for i in range(n + 1)}
        return solve(s1, n, s2, m, dp)

    def solve(s1, i, s2, j, dp):
        if i == 0 and j > 0:
            return False
        if i == 0 and j == 0:
            return True
        if i > 0 and j == 0:
            all_stars = True
            for k in range(i):
                if s1[k - 1] != "*":
                    all_stars = False
            return all_stars
        if dp[i][j] is not None:
            return dp[i][j]
        if s1[i - 1] == s2[j - 1] or s1[i - 1] == "?":
            dp[i][j] = solve(s1, i - 1, s2, j - 1, dp)
        elif s1[i - 1] == "*":
            dp[i][j] = solve(s1, i - 1, s2, j, dp) or solve(s1, i, s2, j - 1, dp)
        else:
            dp[i][j] = False
        return dp[i][j]

    print(wildcard_matching("ab*cd", "abdefcd"))
    print(wildcard_matching("ab?d", "abcc"))
    print(wildcard_matching("?ay", "ray"))
    print(wildcard_matching("ba*a?", "baaabab"))
    print(wildcard_matching("*", "abc"))
    print(wildcard_matching("a*ab", "baaabab"))
    print(wildcard_matching("a?c*", "abcde"))
    print(wildcard_matching("?a", "cb"))


def tabulation():
    """
        Time complexity is O(nm) and space complexity is O(nm).
    """

    def wildcard_matching(s1, s2):
        n, m = len(s1), len(s2)
        dp = {i: {j: False for j in range(m + 1)} for i in range(n + 1)}
        dp[0][0] = True
        for i in range(1, n + 1):
            all_stars = True
            for k in range(i):
                if s1[k - 1] != "*":
                    all_stars = False
            dp[i][0] = all_stars
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1] or s1[i - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                elif s1[i - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = False
        return dp[n][m]

    print(wildcard_matching("ab*cd", "abdefcd"))
    print(wildcard_matching("ab?d", "abcc"))
    print(wildcard_matching("?ay", "ray"))
    print(wildcard_matching("ba*a?", "baaabab"))
    print(wildcard_matching("*", "abc"))
    print(wildcard_matching("a*ab", "baaabab"))
    print(wildcard_matching("a?c*", "abcde"))
    print(wildcard_matching("?a", "cb"))


def space_optimized():
    """
        Time complexity is O(nm) and space complexity is O(m).
    """

    def wildcard_matching(s1, s2):
        n, m = len(s1), len(s2)
        prev = {j: False for j in range(m + 1)}
        prev[0] = True
        for i in range(1, n + 1):
            curr = {j: False for j in range(m + 1)}
            all_stars = True
            for k in range(i):
                if s1[k - 1] != "*":
                    all_stars = False
            curr[0] = all_stars
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1] or s1[i - 1] == "?":
                    curr[j] = prev[j - 1]
                elif s1[i - 1] == "*":
                    curr[j] = prev[j] or curr[j - 1]
                else:
                    curr[j] = False
            prev = curr
        return prev[m]

    print(wildcard_matching("ab*cd", "abdefcd"))
    print(wildcard_matching("ab?d", "abcc"))
    print(wildcard_matching("?ay", "ray"))
    print(wildcard_matching("ba*a?", "baaabab"))
    print(wildcard_matching("*", "abc"))
    print(wildcard_matching("a*ab", "baaabab"))
    print(wildcard_matching("a?c*", "abcde"))
    print(wildcard_matching("?a", "cb"))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
print()
