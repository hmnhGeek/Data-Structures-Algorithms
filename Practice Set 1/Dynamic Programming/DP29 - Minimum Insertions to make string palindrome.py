def recursive():
    def solve(s1, i, s2, j):
        if i == 0 or j == 0:
            return ""

        if s1[i - 1] == s2[j - 1]:
            return solve(s1, i - 1, s2, j - 1) + s1[i - 1]
        else:
            return max(
                solve(s1, i - 1, s2, j),
                solve(s1, i, s2, j - 1),
                key=len
            )

    def lcs(s1, s2):
        n1 = len(s1)
        n2 = len(s2)
        return solve(s1, n1, s2, n2)

    print(lcs("abcd", "abzde"))


recursive()