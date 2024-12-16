def recursive():
    """
        Time complexity is exponential and space complexity is O(n + m).
    """
    def solve(s1, i, s2, j):
        if i == 0 and j == 0:
            return True
        if i == 0 and j > 0:
            return False
        if i > 0 and j == 0:
            match_possible = True
            for k in range(i + 1):
                if s1[k - 1] != "*":
                    match_possible = False
                    break
            return match_possible
        if s1[i - 1] == s2[j - 1] or s1[i - 1] == "?":
            return solve(s1, i - 1, s2, j - 1)
        elif s1[i - 1] == "*":
            return solve(s1, i - 1, s2, j) or solve(s1, i, s2, j - 1)
        else:
            return False

    def match(s1, s2):
        n, m = len(s1), len(s2)
        return solve(s1, n, s2, m)

    print(match("ab*cd", "abdefcd"))
    print(match("ab?d", "abcc"))
    print(match("?ay", "ray"))
    print(match("ba*a?", "baaabab"))
    print(match("*", "abc"))
    print(match("a*ab", "baaabab"))
    print(match("a?c*", "abcde"))
    print(match("?a", "cb"))


def memoized():
    """
        Time complexity is O(m*n) and space complexity is O(n + m + mn).
    """
    def solve(s1, i, s2, j, dp):
        if i == 0 and j == 0:
            return True
        if i == 0 and j > 0:
            return False
        if i > 0 and j == 0:
            match_possible = True
            for k in range(i + 1):
                if s1[k - 1] != "*":
                    match_possible = False
                    break
            return match_possible
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
        n, m = len(s1), len(s2)
        dp = {i: {j: None for j in range(m + 1)} for i in range(n + 1)}
        return solve(s1, n, s2, m, dp)

    print(match("ab*cd", "abdefcd"))
    print(match("ab?d", "abcc"))
    print(match("?ay", "ray"))
    print(match("ba*a?", "baaabab"))
    print(match("*", "abc"))
    print(match("a*ab", "baaabab"))
    print(match("a?c*", "abcde"))
    print(match("?a", "cb"))


def tabulation():
    """
        Time complexity is O(m*n) and space complexity is O(mn).
    """
    def match(s1, s2):
        n, m = len(s1), len(s2)
        dp = {i: {j: False for j in range(m + 1)} for i in range(n + 1)}
        for i in range(1, n + 1):
            match_possible = True
            for k in range(i + 1):
                if s1[k - 1] != "*":
                    match_possible = False
                    break
            dp[i][0] = match_possible
        for j in range(1, m + 1):
            dp[0][j] = False
        dp[0][0] = True
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1] or s1[i - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                elif s1[i - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = False
        return dp[n][m]

    print(match("ab*cd", "abdefcd"))
    print(match("ab?d", "abcc"))
    print(match("?ay", "ray"))
    print(match("ba*a?", "baaabab"))
    print(match("*", "abc"))
    print(match("a*ab", "baaabab"))
    print(match("a?c*", "abcde"))
    print(match("?a", "cb"))


def space_optimized():
    """
        Time complexity is O(m*n) and space complexity is O(m).
    """
    def match(s1, s2):
        n, m = len(s1), len(s2)
        prev = {j: False for j in range(m + 1)}
        for j in range(1, m + 1):
            prev[j] = False
        prev[0] = True
        for i in range(1, n + 1):
            curr = {j: False for j in range(m + 1)}
            match_possible = True
            for k in range(i + 1):
                if s1[k - 1] != "*":
                    match_possible = False
                    break
            curr[0] = match_possible
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1] or s1[i - 1] == "?":
                    curr[j] = prev[j - 1]
                elif s1[i - 1] == "*":
                    curr[j] = prev[j] or curr[j - 1]
                else:
                    curr[j] = False
            prev = curr
        return prev[m]

    print(match("ab*cd", "abdefcd"))
    print(match("ab?d", "abcc"))
    print(match("?ay", "ray"))
    print(match("ba*a?", "baaabab"))
    print(match("*", "abc"))
    print(match("a*ab", "baaabab"))
    print(match("a?c*", "abcde"))
    print(match("?a", "cb"))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
