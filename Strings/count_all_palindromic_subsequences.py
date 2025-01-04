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


recursive()