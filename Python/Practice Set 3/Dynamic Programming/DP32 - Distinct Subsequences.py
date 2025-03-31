# Problem link - https://www.naukri.com/code360/problems/subsequence-counting_3755256?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=nVG7eTiD2bY&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=33


def recursive():
    """
        Time complexity is exponential and space complexity is O(n1 + n2).
    """
    def solve(s1, i, s2, j):
        if j == 0:
            return 1
        if i == 0:
            return 0
        if s1[i - 1] == s2[j - 1]:
            return solve(s1, i - 1, s2, j - 1) + solve(s1, i - 1, s2, j)
        else:
            return solve(s1, i - 1, s2, j)

    def distinct_subsequences(s1, s2):
        n1, n2 = len(s1), len(s2)
        return solve(s1, n1, s2, n2)

    print(distinct_subsequences("babgbag", "bag"))
    print(distinct_subsequences("brootgroot", "brt"))
    print(distinct_subsequences("dingdingdingding", "ing"))
    print(distinct_subsequences("aaaaa", "a"))
    print(distinct_subsequences("rabbbit", "rabbit"))
    print(distinct_subsequences("banana", "ban"))
    print(distinct_subsequences("geeksforgeeks", "ge"))


def memoized():
    """
        Time complexity is O(n1 * n2) and space complexity is O(n1 + n2 + n1 * n2).
    """
    def solve(s1, i, s2, j, dp):
        if j == 0:
            return 1
        if i == 0:
            return 0
        if dp[i][j] is not None:
            return dp[i][j]
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = solve(s1, i - 1, s2, j - 1, dp) + solve(s1, i - 1, s2, j, dp)
        else:
            dp[i][j] = solve(s1, i - 1, s2, j, dp)
        return dp[i][j]

    def distinct_subsequences(s1, s2):
        n1, n2 = len(s1), len(s2)
        dp = {i: {j: None for j in range(n2 + 1)} for i in range(n1 + 1)}
        return solve(s1, n1, s2, n2, dp)

    print(distinct_subsequences("babgbag", "bag"))
    print(distinct_subsequences("brootgroot", "brt"))
    print(distinct_subsequences("dingdingdingding", "ing"))
    print(distinct_subsequences("aaaaa", "a"))
    print(distinct_subsequences("rabbbit", "rabbit"))
    print(distinct_subsequences("banana", "ban"))
    print(distinct_subsequences("geeksforgeeks", "ge"))


def tabulation():
    """
        Time complexity is O(n1 * n2) and space complexity is O(n1 * n2).
    """
    def distinct_subsequences(s1, s2):
        n1, n2 = len(s1), len(s2)
        dp = {i: {j: 0 for j in range(n2 + 1)} for i in range(n1 + 1)}
        for i in dp:
            dp[i][0] = 1
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n1][n2]

    print(distinct_subsequences("babgbag", "bag"))
    print(distinct_subsequences("brootgroot", "brt"))
    print(distinct_subsequences("dingdingdingding", "ing"))
    print(distinct_subsequences("aaaaa", "a"))
    print(distinct_subsequences("rabbbit", "rabbit"))
    print(distinct_subsequences("banana", "ban"))
    print(distinct_subsequences("geeksforgeeks", "ge"))


def space_optimized():
    """
        Time complexity is O(n1 * n2) and space complexity is O(n2).
    """
    def distinct_subsequences(s1, s2):
        n1, n2 = len(s1), len(s2)
        prev = {j: 0 for j in range(n2 + 1)}
        prev[0] = 1
        for i in range(1, n1 + 1):
            curr = {j: 0 for j in range(n2 + 1)}
            curr[0] = 1
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = prev[j - 1] + prev[j]
                else:
                    curr[j] = prev[j]
            prev = curr
        return prev[n2]

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
