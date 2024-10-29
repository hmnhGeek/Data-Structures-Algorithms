def recursive():
    def solve(s1, i, s2, j):
        if i == 0 or j == 0:
            return ""

        if s1[i - 1] == s2[j - 1]:
            return solve(s1, i - 1, s2, j - 1) + s1[i - 1]
        else:
            return max(solve(s1, i - 1, s2, j), solve(s1, i, s2, j - 1))

    def get_lcs(s1: str, s2: str) -> str:
        n1 = len(s1)
        n2 = len(s2)
        return solve(s1, n1, s2, n2)


def memoized():
    def solve(s1, i, s2, j, dp):
        if i == 0 or j == 0:
            return ""

        if dp[i][j] is not None:
            return dp[i][j]

        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = solve(s1, i - 1, s2, j - 1, dp) + s1[i - 1]
        else:
            dp[i][j] = max(solve(s1, i - 1, s2, j, dp), solve(s1, i, s2, j - 1, dp))

        return dp[i][j]

    def get_lcs(s1: str, s2: str) -> str:
        n1 = len(s1)
        n2 = len(s2)
        dp = {i: {j: None for j in range(n2 + 1)} for i in range(n1 + 1)}
        return solve(s1, n1, s2, n2, dp)

    print(get_lcs("abcd", "abzde"))


def tabulation():
    def get_lcs(s1: str, s2: str) -> str:
        n1 = len(s1)
        n2 = len(s2)
        dp = {i: {j: "" for j in range(n2 + 1)} for i in range(n1 + 1)}
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + s1[i - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n1][n2]

    print(get_lcs("abcd", "abzde"))


def space_optimized():
    def get_lcs(s1: str, s2: str) -> str:
        n1 = len(s1)
        n2 = len(s2)
        dp = {i: {j: "" for j in range(n2 + 1)} for i in range(n1 + 1)}
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + s1[i - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n1][n2]

    print(get_lcs("abcd", "abzde"))