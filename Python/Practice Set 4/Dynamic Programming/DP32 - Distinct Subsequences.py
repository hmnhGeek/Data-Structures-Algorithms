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


recursive()
print()
memoized()
print()
