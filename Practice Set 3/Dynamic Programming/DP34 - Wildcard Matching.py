def recursive():
    """
        Time complexity is exponential and space complexity is O(m + n).
    """

    def solve(s1, i, s2, j):
        if i == 0 and j == 0:
            return True
        if i == 0:
            return False
        if j == 0:
            for k in range(i):
                if s1[k] != "*":
                    return False
            return True
        if s1[i - 1] == s2[j - 1] or s1[i - 1] == "?":
            return solve(s1, i - 1, s2, j - 1)
        elif s1[i - 1] == "*":
            return solve(s1, i - 1, s2, j) or solve(s1, i, s2, j - 1)
        return False

    def wildcard_matching(s1, s2):
        n1, n2 = len(s1), len(s2)
        return solve(s1, n1, s2, n2)

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

    def solve(s1, i, s2, j, dp):
        if i == 0 and j == 0:
            return True
        if i == 0:
            return False
        if j == 0:
            for k in range(i):
                if s1[k] != "*":
                    return False
            return True
        if dp[i][j] is not None:
            return dp[i][j]
        if s1[i - 1] == s2[j - 1] or s1[i - 1] == "?":
            dp[i][j] = solve(s1, i - 1, s2, j - 1, dp)
        elif s1[i - 1] == "*":
            dp[i][j] = solve(s1, i - 1, s2, j, dp) or solve(s1, i, s2, j - 1, dp)
        else:
            dp[i][j] = False
        return dp[i][j]

    def wildcard_matching(s1, s2):
        n1, n2 = len(s1), len(s2)
        dp = {i: {j: None for j in range(n2 + 1)} for i in range(n1 + 1)}
        return solve(s1, n1, s2, n2, dp)

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
