def recursive():
    """
        Time complexity is O(2^{n + m}) and space complexity is O(n + m).
    """

    def solve(s1, i, s2, j):
        if i == 0 or j == 0:
            return 0
        if s1[i - 1] == s2[j - 1]:
            return 1 + solve(s1, i - 1, s2, j - 1)
        else:
            return max(
                solve(s1, i - 1, s2, j),
                solve(s1, i, s2, j - 1)
            )

    def lcs(s1, s2):
        n, m = len(s1), len(s2)
        return solve(s1, n, s2, m)

    print(lcs("abcd", "abzd"))


recursive()