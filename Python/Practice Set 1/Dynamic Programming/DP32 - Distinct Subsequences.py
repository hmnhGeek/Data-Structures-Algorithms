# Problem link - https://www.naukri.com/code360/problems/distinct-subsequences_981277
# Solution - https://www.youtube.com/watch?v=nVG7eTiD2bY&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=33


def recursive():
    """
        Time complexity is exponential and space complexity is O(n + m).
    """
    def solve(string, i, search_term, j):
        if j < 0:
            return 1
        if i < 0:
            return 0

        left = 0
        if string[i] == search_term[j]:
            left = solve(string, i - 1, search_term, j - 1)
        right = solve(string, i - 1, search_term, j)
        return left + right

    def distinct_subsequences(string, search_term):
        n = len(string)
        m = len(search_term)
        return solve(string, n - 1, search_term, m - 1)

    print(distinct_subsequences("babgbag", "bag"))
    print(distinct_subsequences("brootgroot", "brt"))
    print(distinct_subsequences("dingdingdingding", "ing"))
    print(distinct_subsequences("aaaaa", "a"))
    print(distinct_subsequences("rabbbit", "rabbit"))
    print(distinct_subsequences("banana", "ban"))
    print(distinct_subsequences("abcd", "abe"))


def memoized():
    """
        Time complexity is O(n*m) and space complexity is O(n + m + nm).
    """
    def solve(string, i, search_term, j, dp):
        if j == 0:
            return 1
        if i == 0:
            return 0

        if dp[i][j] is not None:
            return dp[i][j]

        left = 0
        if string[i - 1] == search_term[j - 1]:
            left = solve(string, i - 1, search_term, j - 1, dp)
        right = solve(string, i - 1, search_term, j, dp)
        dp[i][j] = left + right
        return dp[i][j]

    def distinct_subsequences(string, search_term):
        n = len(string)
        m = len(search_term)
        dp = {i: {j: None for j in range(m + 1)} for i in range(n + 1)}
        return solve(string, n, search_term, m, dp)

    print(distinct_subsequences("babgbag", "bag"))
    print(distinct_subsequences("brootgroot", "brt"))
    print(distinct_subsequences("dingdingdingding", "ing"))
    print(distinct_subsequences("aaaaa", "a"))
    print(distinct_subsequences("rabbbit", "rabbit"))
    print(distinct_subsequences("banana", "ban"))
    print(distinct_subsequences("abcd", "abe"))


def tabulation():
    """
        Time complexity is O(nm) and space complexity is O(nm).
    """
    def distinct_subsequences(string, search_term):
        n = len(string)
        m = len(search_term)
        dp = {i: {j: 0 for j in range(m + 1)} for i in range(n + 1)}
        for i in dp:
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = 0
                if string[i - 1] == search_term[j - 1]:
                    left = dp[i - 1][j - 1]
                right = dp[i - 1][j]
                dp[i][j] = left + right

        return dp[n][m]

    print(distinct_subsequences("babgbag", "bag"))
    print(distinct_subsequences("brootgroot", "brt"))
    print(distinct_subsequences("dingdingdingding", "ing"))
    print(distinct_subsequences("aaaaa", "a"))
    print(distinct_subsequences("rabbbit", "rabbit"))
    print(distinct_subsequences("banana", "ban"))
    print(distinct_subsequences("abcd", "abe"))


def space_optimized():
    """
        Time complexity is O(nm) and space complexity is O(m).
    """
    def distinct_subsequences(string, search_term):
        n = len(string)
        m = len(search_term)
        prev = {j: 0 for j in range(m + 1)}
        prev[0] = 1

        for i in range(1, n + 1):
            curr = {j: 0 for j in range(m + 1)}
            curr[0] = 1
            for j in range(1, m + 1):
                left = 0
                if string[i - 1] == search_term[j - 1]:
                    left = prev[j - 1]
                right = prev[j]
                curr[j] = left + right
            prev = curr

        return prev[m]

    print(distinct_subsequences("babgbag", "bag"))
    print(distinct_subsequences("brootgroot", "brt"))
    print(distinct_subsequences("dingdingdingding", "ing"))
    print(distinct_subsequences("aaaaa", "a"))
    print(distinct_subsequences("rabbbit", "rabbit"))
    print(distinct_subsequences("banana", "ban"))
    print(distinct_subsequences("abcd", "abe"))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()