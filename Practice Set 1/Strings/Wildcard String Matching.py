def recursive():
    """
        Time complexity is exponential and space complexity is O(n1 + n2).
    """
    def solve(s1, i, s2, j):
        if i == 0 and j == 0:
            return True
        if i == 0:
            return False
        if j == 0:
            all_stars = True
            for k in range(i, 0, -1):
                if s1[k - 1] != "*":
                    all_stars = False
            return all_stars

        if s1[i - 1] == s2[j - 1] or s1[i - 1] == "?":
            return solve(s1, i - 1, s2, j - 1)
        elif s1[i - 1] == "*":
            return solve(s1, i - 1, s2, j) or solve(s1, i, s2, j - 1)
        return False

    def match(string, pattern):
        n1, n2 = len(string), len(pattern)
        return solve(string, n1, pattern, n2)

    print(match("?ay", "ray"))
    print(match("ab*cd", "abdefcd"))
    print(match("ab?d", "abcc"))
    print(match("ba*a?", "baaabab"))
    print(match("a", "aa"))
    print(match("*", "aa"))
    print(match("?a", "cb"))
    print(match("**", ""))


def memoized():
    """
        Time complexity is O(n1 * n2) and space complexity is O(n1 + n2 + n1 * n2).
    """
    def solve(s1, i, s2, j, dp):
        if i == 0 and j == 0:
            return True
        if i == 0:
            return False
        if j == 0:
            all_stars = True
            for k in range(i, 0, -1):
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

    def match(string, pattern):
        n1, n2 = len(string), len(pattern)
        dp = {i: {j: None for j in range(n2 + 1)} for i in range(n1 + 1)}
        return solve(string, n1, pattern, n2, dp)

    print(match("?ay", "ray"))
    print(match("ab*cd", "abdefcd"))
    print(match("ab?d", "abcc"))
    print(match("ba*a?", "baaabab"))
    print(match("a", "aa"))
    print(match("*", "aa"))
    print(match("?a", "cb"))
    print(match("**", ""))


recursive()
print()
memoized()
