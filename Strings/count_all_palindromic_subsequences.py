def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """

    def solve(string, i, j):
        if i > j:
            return 0
        if i == j:
            return 1

        # if there's a match, add 1 to count and solve for f(i + 1, j) and f(i, j - 1)
        if string[i] == string[j]:
            return 1 + solve(string, i + 1, j) + solve(string, i, j - 1)
        else:
            # if there's no match, solve for f(i + 1, j) and f(i, j - 1) and subtract f(i + 1, j - 1).
            return solve(string, i + 1, j) + solve(string, i, j - 1) - solve(string, i + 1, j - 1)

    def count(string):
        n = len(string)
        return solve(string, 0, n - 1)

    print(count("abcd"))
    print(count("aab"))
    print(count("geeksforgeeks"))
    print(count("103301"))
    print(count("bccb"))


def memoized():
    """
        Time complexity is O(n^2) and space complexity is O(2n).
    """

    def solve(string, i, j, dp):
        if i > j:
            return 0
        if i == j:
            return 1
        if dp[i][j] is not None:
            return dp[i][j]
        # if there's a match, add 1 to count and solve for f(i + 1, j) and f(i, j - 1)
        if string[i] == string[j]:
            dp[i][j] = 1 + solve(string, i + 1, j, dp) + solve(string, i, j - 1, dp)
        else:
            # if there's no match, solve for f(i + 1, j) and f(i, j - 1) and subtract f(i + 1, j - 1).
            dp[i][j] = solve(string, i + 1, j, dp) + solve(string, i, j - 1, dp) - solve(string, i + 1, j - 1, dp)
        return dp[i][j]

    def count(string):
        n = len(string)
        dp = {i: {j: None for j in range(n)} for i in range(n)}
        return solve(string, 0, n - 1, dp)

    print(count("abcd"))
    print(count("aab"))
    print(count("geeksforgeeks"))
    print(count("103301"))
    print(count("bccb"))


recursive()
print()
memoized()