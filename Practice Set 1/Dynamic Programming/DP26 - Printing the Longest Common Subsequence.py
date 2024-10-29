def recursive():
    """
        Time complexity is exponential and space complexity is O(n1 + n2)
    """
    def solve(s1: str, i: int, s2: str, j: int) -> str:
        if i < 0 or j < 0:
            return ""

        if s1[i] == s2[j]:
            return solve(s1, i - 1, s2, j - 1) + s1[i]

        left = solve(s1, i - 1, s2, j)
        right = solve(s1, i, s2, j - 1)
        return max(left, right, key=len)

    def get_lcs(s1: str, s2: str) -> str:
        n1 = len(s1)
        n2 = len(s2)
        return solve(s1, n1 - 1, s2, n2 - 1)

    print(get_lcs("abcde", "bdgek"))
    print(get_lcs("adebc", "dcadb"))
    print(get_lcs("ab", "defg"))

recursive()