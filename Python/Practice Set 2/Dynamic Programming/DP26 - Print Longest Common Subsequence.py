# Problem link - https://www.naukri.com/code360/problems/longest-common-subsequence_624879?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=-zI4mrF2Pb4&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=27


def recursive():
    """
        Time complexity is O(2^{n1 + n2}) and space complexity is O(n1 + n2).
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
        Time complexity is O(n1 * n2) and space complexity is O(n1 + n2 + n1*n2).
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
        Time complexity is O(n1 * n2) and space complexity is O(n1 * n2).
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


def space_optimized():
    """
        Time complexity is O(n1 * n2) and space complexity is O(n2).
    """
    def lcs(s1, s2):
        n1, n2 = len(s1), len(s2)
        prev = {j: 0 for j in range(n2 + 1)}
        for i in range(1, n1 + 1):
            curr = {j: 0 for j in range(n2 + 1)}
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr
        return prev[n2]

    print(lcs("adebc", "dcadb"))
    print(lcs("ab", "defg"))
    print(lcs("abcde", "ace"))
    print(lcs("abc", "abc"))
    print(lcs("abc", "acd"))
    print(lcs("AGGTAB", "GXTXAYB"))
    print(lcs("ABC", "CBA"))


class Solution:
    @staticmethod
    def lcs(s1, s2):
        """
            Overall time complexity is O(n1 * n2) and space complexity is O(n1 * n2).
        """

        # construct the correct DP matrix in O(n1 * n2) time and O(n1 * n2) space.
        n1, n2 = len(s1), len(s2)
        dp = {i: {j: 0 for j in range(n2 + 1)} for i in range(n1 + 1)}
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # store the result variable and pointers i and j from the end of the matrix.
        result = ""
        i, j = n1, n2

        # while both pointers have strings to traverse. This will take O(n1 + n2) time.
        while i > 0 and j > 0:
            # if there's a match in characters, add it to the result
            if s1[i - 1] == s2[j - 1]:
                result += s1[i - 1]
                i -= 1
                j -= 1
            # if previous row has greater value than previous column, go to previous row.
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                # else go to previous column.
                j -= 1

        # return the reverse of result as actual answer.
        return result[-1:-len(result)-1:-1]


print(Solution.lcs("adebc", "dcadb"))
print(Solution.lcs("ab", "defg"))
print(Solution.lcs("abcde", "ace"))
print(Solution.lcs("abc", "abc"))
print(Solution.lcs("abc", "acd"))
print(Solution.lcs("AGGTAB", "GXTXAYB"))
print(Solution.lcs("ABC", "CBA"))
