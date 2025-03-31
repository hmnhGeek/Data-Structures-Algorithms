# Problem link - https://www.naukri.com/code360/problems/longest-common-subsequence_624879?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=6i_T5kkfv4A&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=29


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


def get_lcs(s1: str, s2: str) -> str:
    n1 = len(s1)
    n2 = len(s2)
    dp = {i: {j: 0 for j in range(n2 + 1)} for i in range(n1 + 1)}
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    result = ""
    i, j = n1, n2
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            result += s1[i - 1]
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
    return result[-1:-len(result) - 1:-1]


def get_longest_palindromic_subsequence(string: str) -> str:
    reversed = string[-1:-len(string)-1:-1]
    return get_lcs(string, reversed)


print(get_longest_palindromic_subsequence("bbbab"))
print(get_longest_palindromic_subsequence("bbabcbcab"))