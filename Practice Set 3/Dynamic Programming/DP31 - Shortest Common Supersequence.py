def recursive():
    """
        Time complexity is exponential and space complexity is O(n + m).
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


def memoized():
    """
        Time complexity is O(nm) and space complexity is O(n + m + nm).
    """

    def solve(s1, i, s2, j, dp):
        if i == 0 or j == 0:
            return 0
        if dp[i][j] is not None:
            return dp[i][j]
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = 1 + solve(s1, i - 1, s2, j - 1, dp)
        else:
            dp[i][j] = max(solve(s1, i - 1, s2, j, dp), solve(s1, i, s2, j - 1, dp))
        return dp[i][j]

    def lcs(s1, s2):
        n1, n2 = len(s1), len(s2)
        dp = {i: {j: None for j in range(n2 + 1)} for i in range(n1 + 1)}
        return solve(s1, n1, s2, n2, dp)

    print(lcs("adebc", "dcadb"))
    print(lcs("ab", "defg"))
    print(lcs("abcde", "ace"))
    print(lcs("abc", "abc"))
    print(lcs("abc", "acd"))
    print(lcs("AGGTAB", "GXTXAYB"))
    print(lcs("ABC", "CBA"))


def tabulation():
    """
        Time complexity is O(nm) and space complexity is O(nm).
    """
    def lcs(s1, s2):
        n1, n2 = len(s1), len(s2)
        dp = {i: {j: 0 for j in range(n2 + 1)} for i in range(n1 + 1)}
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n1][n2]

    print(lcs("adebc", "dcadb"))
    print(lcs("ab", "defg"))
    print(lcs("abcde", "ace"))
    print(lcs("abc", "abc"))
    print(lcs("abc", "acd"))
    print(lcs("AGGTAB", "GXTXAYB"))
    print(lcs("ABC", "CBA"))


class Solution:
    @staticmethod
    def print_shortest_common_supersequence(s1, s2):
        """
            Time complexity is O(nm + n + m) and space complexity is O(nm).
        """

        n1, n2 = len(s1), len(s2)
        dp = {i: {j: 0 for j in range(n2 + 1)} for i in range(n1 + 1)}
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        result = ""
        i, j = n1, n2
        while i > 0 and j > 0:
            if s1[i - 1] == s2[j - 1]:
                result += s1[i - 1]
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                result += s1[i - 1]
                i -= 1
            else:
                result += s2[j - 1]
                j -= 1
        while i > 0:
            result += s1[i - 1]
            i -= 1
        while j > 0:
            result += s2[j - 1]
            j -= 1
        return result[-1:-len(result)-1:-1]


print(Solution.print_shortest_common_supersequence("brute", "groot"))
print(Solution.print_shortest_common_supersequence("bleed", "blue"))
print(Solution.print_shortest_common_supersequence("coding", "ninjas"))
print(Solution.print_shortest_common_supersequence("blinding", "lights"))
