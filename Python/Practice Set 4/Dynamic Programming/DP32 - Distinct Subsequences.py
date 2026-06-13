def recursive():
    """
        Time complexity is exponential and space complexity is O(n + m).
    """
    def distinct_subsequences(string, pattern):
        n, m = len(string), len(pattern)
        return solve(string, n, pattern, m)

    def solve(string, i, pattern, j):
        if j == 0:
            return 1
        if i == 0:
            return 0
        if string[i - 1] == pattern[j - 1]:
            return solve(string, i - 1, pattern, j - 1) + solve(string, i - 1, pattern, j)
        else:
            return solve(string, i - 1, pattern, j)

    print(distinct_subsequences("babgbag", "bag"))
    print(distinct_subsequences("brootgroot", "brt"))
    print(distinct_subsequences("dingdingdingding", "ing"))
    print(distinct_subsequences("aaaaa", "a"))
    print(distinct_subsequences("rabbbit", "rabbit"))
    print(distinct_subsequences("banana", "ban"))
    print(distinct_subsequences("geeksforgeeks", "ge"))


def memoized():
    """
        Time complexity is O(mn) and space complexity is O(n + m + mn).
    """
    def distinct_subsequences(string, pattern):
        n, m = len(string), len(pattern)
        dp = {i: {j: None for j in range(m + 1)} for i in range(n + 1)}
        return solve(string, n, pattern, m, dp)

    def solve(string, i, pattern, j, dp):
        if j == 0:
            return 1
        if i == 0:
            return 0
        if dp[i][j] is not None:
            return dp[i][j]
        if string[i - 1] == pattern[j - 1]:
            dp[i][j] = solve(string, i - 1, pattern, j - 1, dp) + solve(string, i - 1, pattern, j, dp)
        else:
            dp[i][j] = solve(string, i - 1, pattern, j, dp)
        return dp[i][j]

    print(distinct_subsequences("babgbag", "bag"))
    print(distinct_subsequences("brootgroot", "brt"))
    print(distinct_subsequences("dingdingdingding", "ing"))
    print(distinct_subsequences("aaaaa", "a"))
    print(distinct_subsequences("rabbbit", "rabbit"))
    print(distinct_subsequences("banana", "ban"))
    print(distinct_subsequences("geeksforgeeks", "ge"))


def tabulation():
    """
        Time complexity is O(mn) and space complexity is O(mn).
    """
    def distinct_subsequences(string, pattern):
        n, m = len(string), len(pattern)
        dp = {i: {j: 0 for j in range(m + 1)} for i in range(n + 1)}
        for i in range(n + 1):
            dp[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if string[i - 1] == pattern[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][m]

    print(distinct_subsequences("babgbag", "bag"))
    print(distinct_subsequences("brootgroot", "brt"))
    print(distinct_subsequences("dingdingdingding", "ing"))
    print(distinct_subsequences("aaaaa", "a"))
    print(distinct_subsequences("rabbbit", "rabbit"))
    print(distinct_subsequences("banana", "ban"))
    print(distinct_subsequences("geeksforgeeks", "ge"))


def space_optimized():
    """
        Time complexity is O(mn) and space complexity is O(m).
    """
    def distinct_subsequences(string, pattern):
        n, m = len(string), len(pattern)
        prev = {j: 0 for j in range(m + 1)}
        prev[0] = 1
        for i in range(1, n + 1):
            curr = {j: 0 for j in range(m + 1)}
            curr[0] = 1
            for j in range(1, m + 1):
                if string[i - 1] == pattern[j - 1]:
                    curr[j] = prev[j - 1] + prev[j]
                else:
                    curr[j] = prev[j]
            prev = curr
        return prev[m]

    print(distinct_subsequences("babgbag", "bag"))
    print(distinct_subsequences("brootgroot", "brt"))
    print(distinct_subsequences("dingdingdingding", "ing"))
    print(distinct_subsequences("aaaaa", "a"))
    print(distinct_subsequences("rabbbit", "rabbit"))
    print(distinct_subsequences("banana", "ban"))
    print(distinct_subsequences("geeksforgeeks", "ge"))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
print()
