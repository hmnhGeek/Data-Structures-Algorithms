def recursive():
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


recursive()
print()
memoized()