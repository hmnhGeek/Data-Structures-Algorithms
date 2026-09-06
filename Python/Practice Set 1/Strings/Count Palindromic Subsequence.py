def recursive():
    def count(string):
        n = len(string)
        return solve(string, 0, n - 1)

    def solve(string, i, j):
        if i > j:
            return 0
        if i == j:
            return 1
        if string[i] == string[j]:
            return 1 + solve(string, i + 1, j) + solve(string, i, j - 1)
        else:
            return solve(string, i + 1, j) + solve(string, i, j - 1) - solve(string, i + 1, j - 1)

    print(count("abcd"))
    print(count("aab"))
    print(count("geeksforgeeks"))
    print(count("103301"))
    print(count("bccb"))


def memoized():
    """
        Time complexity is O(n^2) and space complexity is O(n^2 + n).
    """
    def count(string):
        n = len(string)
        dp = {i: {j: None for j in range(n)} for i in range(n)}
        return solve(string, 0, n - 1, dp)

    def solve(string, i, j, dp):
        if i > j:
            return 0
        if i == j:
            return 1
        if dp[i][j] is not None:
            return dp[i][j]
        if string[i] == string[j]:
            dp[i][j] = 1 + solve(string, i + 1, j, dp) + solve(string, i, j - 1, dp)
        else:
            dp[i][j] = solve(string, i + 1, j, dp) + solve(string, i, j - 1, dp) - solve(string, i + 1, j - 1, dp)
        return dp[i][j]

    print(count("abcd"))
    print(count("aab"))
    print(count("geeksforgeeks"))
    print(count("103301"))
    print(count("bccb"))


def tabulation():
    """
        Time complexity is O(n^2) and space complexity is O(n^2).
    """
    def count(string):
        n = len(string)
        dp = {i: {j: 0 for j in range(n)} for i in range(n)}
        for i in dp:
            dp[i][i] = 1
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if string[i] == string[j]:
                    dp[i][j] = 1 + dp[i + 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
        return dp[0][n - 1]

    print(count("abcd"))
    print(count("aab"))
    print(count("geeksforgeeks"))
    print(count("103301"))
    print(count("bccb"))


recursive()
print()
memoized()
print()
tabulation()
print()
