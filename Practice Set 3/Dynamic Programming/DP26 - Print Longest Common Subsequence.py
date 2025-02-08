def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """
    def solve(s1, i, s2, j):
        if i == 0 or j == 0:
            return 0
        if s1[i - 1] == s2[j - 1]:
            return 1 + solve(s1, i - 1, s2, j - 1)
        else:
            return max(solve(s1, i - 1, s2, j), solve(s1, i, s2, j - 1))

    def lcs(s1, s2):
        n1, n2 = len(s1), len(s2)
        return solve(s1, n1, s2, n2)

    print(lcs("adebc", "dcadb"))
    print(lcs("ab", "defg"))
    print(lcs("abcde", "ace"))
    print(lcs("abc", "abc"))
    print(lcs("abc", "acd"))
    print(lcs("AGGTAB", "GXTXAYB"))
    print(lcs("ABC", "CBA"))


recursive()