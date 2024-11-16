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


recursive()