def recursive():
    """
        Time complexity is exponential and space is O(n1 + n2)
    """
    def solve(s1, i, s2, j):
        if i < 0 or j < 0:
            return 0

        if s1[i] == s2[j]:
            return 1 + solve(s1, i - 1, s2, j - 1)
        else:
            return max(
                solve(s1, i, s2, j - 1),
                solve(s1, i - 1, s2, j)
            )

    def lcs_length(s1, s2):
        n1, n2 = len(s1), len(s2)
        return solve(s1, n1 - 1, s2, n2 - 1)

    print(lcs_length("adebc", "dcadb"))
    print(lcs_length("ab", "defg"))
    print(lcs_length("AGGTAB", "GXTXAYB"))
    print(lcs_length("ABC", "CBA"))


recursive()