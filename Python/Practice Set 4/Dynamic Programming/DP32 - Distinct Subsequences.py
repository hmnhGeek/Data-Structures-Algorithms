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


recursive()
print()