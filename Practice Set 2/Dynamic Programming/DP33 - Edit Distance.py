# Problem link - https://www.naukri.com/code360/problems/edit-distance_630420?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=fJaKO8FbDdo&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=34


def recursive():
    """
        Time complexity is O(3^{n + m}) and space complexity is O(n + m).
    """

    def solve(s1, i, s2, j):
        if i == 0:
            return j
        if j == 0:
            return i
        if s1[i - 1] == s2[j - 1]:
            return solve(s1, i - 1, s2, j - 1)
        else:
            delete = 1 + solve(s1, i - 1, s2, j)
            replace = 1 + solve(s1, i - 1, s2, j - 1)
            insert = 1 + solve(s1, i, s2, j - 1)
            return min(delete, replace, insert)

    def edit_distance(s1, s2):
        n, m = len(s1), len(s2)
        return solve(s1, n, s2, m)

    print(edit_distance("horse", "ros"))
    print(edit_distance("abc", "dc"))
    print(edit_distance("whgtdwhgtdg", "aswcfg"))
    print(edit_distance("intention", "execution"))
    print(edit_distance("geek", "gesek"))
    print(edit_distance("cat", "cut"))
    print(edit_distance("sunday", "saturday"))


def memoized():
    """
        Time complexity is O(n * m) and space complexity is O(n + m + n * m).
    """

    def solve(s1, i, s2, j, dp):
        if i == 0:
            return j
        if j == 0:
            return i
        if dp[i][j] is not None:
            return dp[i][j]
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = solve(s1, i - 1, s2, j - 1, dp)
        else:
            delete = 1 + solve(s1, i - 1, s2, j, dp)
            replace = 1 + solve(s1, i - 1, s2, j - 1, dp)
            insert = 1 + solve(s1, i, s2, j - 1, dp)
            dp[i][j] = min(delete, replace, insert)
        return dp[i][j]

    def edit_distance(s1, s2):
        n, m = len(s1), len(s2)
        dp = {i: {j: None for j in range(m + 1)} for i in range(n + 1)}
        return solve(s1, n, s2, m, dp)

    print(edit_distance("horse", "ros"))
    print(edit_distance("abc", "dc"))
    print(edit_distance("whgtdwhgtdg", "aswcfg"))
    print(edit_distance("intention", "execution"))
    print(edit_distance("geek", "gesek"))
    print(edit_distance("cat", "cut"))
    print(edit_distance("sunday", "saturday"))


def tabulation():
    """
        Time complexity is O(n * m) and space complexity is O(n * m).
    """
    def edit_distance(s1, s2):
        n, m = len(s1), len(s2)
        dp = {i: {j: 1e6 for j in range(m + 1)} for i in range(n + 1)}
        for j in dp[0]:
            dp[0][j] = j
        for i in dp:
            dp[i][0] = i
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    delete = 1 + dp[i - 1][j]
                    replace = 1 + dp[i - 1][j - 1]
                    insert = 1 + dp[i][j - 1]
                    dp[i][j] = min(delete, replace, insert)
        return dp[n][m]

    print(edit_distance("horse", "ros"))
    print(edit_distance("abc", "dc"))
    print(edit_distance("whgtdwhgtdg", "aswcfg"))
    print(edit_distance("intention", "execution"))
    print(edit_distance("geek", "gesek"))
    print(edit_distance("cat", "cut"))
    print(edit_distance("sunday", "saturday"))


def space_optimized():
    """
        Time complexity is O(n * m) and space complexity is O(m).
    """
    def edit_distance(s1, s2):
        n, m = len(s1), len(s2)
        prev = {j: 1e6 for j in range(m + 1)}
        for j in prev:
            prev[j] = j
        prev[0] = 0 # for i = 0
        for i in range(1, n + 1):
            curr = {j: 1e6 for j in range(m + 1)}
            curr[0] = i
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    delete = 1 + prev[j]
                    replace = 1 + prev[j - 1]
                    insert = 1 + curr[j - 1]
                    curr[j] = min(delete, replace, insert)
            prev = curr
        return prev[m]

    print(edit_distance("horse", "ros"))
    print(edit_distance("abc", "dc"))
    print(edit_distance("whgtdwhgtdg", "aswcfg"))
    print(edit_distance("intention", "execution"))
    print(edit_distance("geek", "gesek"))
    print(edit_distance("cat", "cut"))
    print(edit_distance("sunday", "saturday"))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()
