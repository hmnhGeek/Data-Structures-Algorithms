def recursive():
    """
        Time complexity is exponential and space complexity O(n + m).
    """
    def solve(s1, i, s2, j):
        if i < 0 and j < 0:
            return True
        if i < 0 and j >= 0:
            return False
        if j < 0:
            all_stars = True
            for k in range(i):
                if s1[i] != "*":
                    all_stars = False
            return all_stars

        if s1[i] == s2[j] or s1[i] == "?":
            return solve(s1, i - 1, s2, j - 1)
        elif s1[i] == "*":
            return solve(s1, i - 1, s2, j) or solve(s1, i, s2, j - 1)
        else:
            return False

    def match(s1, s2):
        n = len(s1)
        m = len(s2)
        return solve(s1, n - 1, s2, m - 1)

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
        Time complexity is exponential and space complexity O(n + m).
    """
    def solve(s1, i, s2, j, dp):
        if i == 0 and j == 0:
            return True
        if i == 0 and j > 0:
            return False
        if j == 0 and i > 0:
            all_stars = True
            for k in range(1, i + 1):
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

    def match(s1, s2):
        n = len(s1)
        m = len(s2)
        dp = {i: {j: None for j in range(m + 1)} for i in range(n + 1)}
        return solve(s1, n, s2, m, dp)

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