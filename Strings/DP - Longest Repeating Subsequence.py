def recursive():
    def solve(string, i, j):
        """
            Time complexity is exponential and space complexity is O(n). The code is exactly same as LCS, but the only
            difference is the explicit check for index i = j.
        """

        if i < 0 or j < 0:
            return 0
        # if the characters match at indices i and j and i != j, then we can consume these indices in the subsequence.
        if string[i] == string[j] and i != j:
            return 1 + solve(string, i - 1, j - 1)
        else:
            return max(solve(string, i - 1, j), solve(string, i, j - 1))

    def get_longest_repeating_subsequence(string: str):
        n = len(string)
        return solve(string, n - 1, n - 1)

    print(get_longest_repeating_subsequence("axxxy"))
    print(get_longest_repeating_subsequence("axxzxy"))
    print(get_longest_repeating_subsequence("abc"))
    print(get_longest_repeating_subsequence("aab"))
    print(get_longest_repeating_subsequence("abcab"))
    print(get_longest_repeating_subsequence("ABCBDCD"))
    print(get_longest_repeating_subsequence("BCCB"))


def memoized():
    def solve(string, i, j, dp):
        """
            Time complexity is O(n^2) and space complexity is O(n + n^2). The code is exactly same as LCS, but the only
            difference is the explicit check for index i = j.
        """

        if i == 0 or j == 0:
            return 0

        if dp[i][j] is not None:
            return dp[i][j]

        # if the characters match at indices i and j and i != j, then we can consume these indices in the subsequence.
        if string[i - 1] == string[j - 1] and i != j:
            dp[i][j] = 1 + solve(string, i - 1, j - 1, dp)
        else:
            dp[i][j] = max(solve(string, i - 1, j, dp), solve(string, i, j - 1, dp))
        return dp[i][j]

    def get_longest_repeating_subsequence(string: str):
        n = len(string)
        dp = {i: {j: None for j in range(n + 1)} for i in range(n + 1)}
        return solve(string, n, n, dp)

    print(get_longest_repeating_subsequence("axxxy"))
    print(get_longest_repeating_subsequence("axxzxy"))
    print(get_longest_repeating_subsequence("abc"))
    print(get_longest_repeating_subsequence("aab"))
    print(get_longest_repeating_subsequence("abcab"))
    print(get_longest_repeating_subsequence("ABCBDCD"))
    print(get_longest_repeating_subsequence("BCCB"))


recursive()
print()
memoized()