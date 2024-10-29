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


def memoized():
    """
        Time complexity is O(n1*n2) and space complexity is O(n1 + n2 + n1*n2)
    """
    def solve(s1: str, i: int, s2: str, j: int, dp) -> str:
        if i == 0 or j == 0:
            return ""

        if dp[i][j] is not None:
            return dp[i][j]

        if s1[i - 1] == s2[j - 1]:
            return solve(s1, i - 1, s2, j - 1, dp) + s1[i - 1]

        left = solve(s1, i - 1, s2, j, dp)
        right = solve(s1, i, s2, j - 1, dp)
        dp[i][j] = max(left, right, key=len)
        return dp[i][j]

    def get_lcs(s1: str, s2: str) -> str:
        n1 = len(s1)
        n2 = len(s2)
        dp = {i: {j: None for j in range(n2 + 1)} for i in range(n1 + 1)}
        return solve(s1, n1, s2, n2, dp)

    print(get_lcs("abcde", "bdgek"))
    print(get_lcs("adebc", "dcadb"))
    print(get_lcs("ab", "defg"))


def tabulation():
    """
        Time complexity is O(n1*n2) and space complexity is O(n1*n2)
    """
    def get_lcs(s1: str, s2: str) -> str:
        n1 = len(s1)
        n2 = len(s2)
        dp = {i: {j: "" for j in range(n2 + 1)} for i in range(n1 + 1)}

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + s1[i - 1]
                else:
                    left = dp[i - 1][j]
                    right = dp[i][j - 1]
                    dp[i][j] = max(left, right, key=len)
        return dp[n1][n2]

    print(get_lcs("abcde", "bdgek"))
    print(get_lcs("adebc", "dcadb"))
    print(get_lcs("ab", "defg"))


def space_optimized():
    """
        Time complexity is O(n1*n2) and space complexity is O(n2)
    """
    def get_lcs(s1: str, s2: str) -> str:
        n1 = len(s1)
        n2 = len(s2)
        prev = {j: "" for j in range(n2 + 1)}

        for i in range(1, n1 + 1):
            curr = {j: "" for j in range(n2 + 1)}
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = prev[j - 1] + s1[i - 1]
                else:
                    left = prev[j]
                    right = curr[j - 1]
                    curr[j] = max(left, right, key=len)
            prev = curr
        return prev[n2]

    print(get_lcs("abcde", "bdgek"))
    print(get_lcs("adebc", "dcadb"))
    print(get_lcs("ab", "defg"))


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()