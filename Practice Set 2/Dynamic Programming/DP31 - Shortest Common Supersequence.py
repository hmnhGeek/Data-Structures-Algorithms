def recursive():
    """
        Time complexity is O(2^{m + n}) and space complexity is O(m + n).
    """
    def solve(s1, i, s2, j):
        if i < 0 or j < 0:
            return 0
        if s1[i] == s2[j]:
            return 1 + solve(s1, i - 1, s2, j - 1)
        else:
            return max(solve(s1, i - 1, s2, j), solve(s1, i, s2, j - 1))

    def lcs_length(s1, s2):
        n, m = len(s1), len(s2)
        return solve(s1, n - 1, s2, m - 1)

    print(lcs_length("abcd", "abzd"))


recursive()