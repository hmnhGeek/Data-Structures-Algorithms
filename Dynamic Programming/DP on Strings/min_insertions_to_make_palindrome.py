def recursive():
    def solve_lcs(str1, i, str2, j):
        if i < 0 or j < 0:
            return 0

        if str1[i] == str2[j]:
            return 1 + solve_lcs(str1, i - 1, str2, j - 1)
        else:
            return max(
                solve_lcs(str1, i - 1, str2, j),
                solve_lcs(str1, i, str2, j - 1)
            )

    def lcs(str1, str2):
        n = len(str1)
        m = len(str2)
        return solve_lcs(str1, n - 1, str2, m - 1)


def memoized():
    def solve_lcs(str1, i, str2, j, dp):
        if i < 0 or j < 0:
            return 0

        if dp[i][j] is not None:
            return dp[i][j]

        if str1[i] == str2[j]:
            dp[i][j] = 1 + solve_lcs(str1, i - 1, str2, j - 1, dp)
        else:
            dp[i][j] = max(
                solve_lcs(str1, i - 1, str2, j, dp),
                solve_lcs(str1, i, str2, j - 1, dp)
            )
        return dp[i][j]

    def lcs(str1, str2):
        n = len(str1)
        m = len(str2)
        dp = {i: {j: None for j in range(m)} for i in range(n)}
        return solve_lcs(str1, n - 1, str2, m - 1, dp)

    print(lcs("abcde", "ace"))


def tabulation():
    def lcs(str1, str2):
        n = len(str1)
        m = len(str2)
        dp = {i: {j: float('-inf') for j in range(m)} for i in range(n)}

        dp[0][0] = 1 if str1[0] == str2[0] else 0

        for j in range(1, m):
            if str1[0] == str2[j]:
                dp[0][j] = 1
            else:
                dp[0][j] = dp[0][j - 1]

        for i in range(1, n):
            if str1[i] == str2[0]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i - 1][0]

        for i in range(1, n):
            for j in range(1, m):
                if str1[i] == str2[j]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i][j - 1]
                    )

        return dp[n - 1][m - 1]


def longest_common_subsequence(str1, str2):
    n = len(str1)
    m = len(str2)
    prev = {j: 0 for j in range(m)}

    prev[0] = 1 if str1[0] == str2[0] else 0

    for j in range(1, m):
        if str1[0] == str2[j]:
            prev[j] = 1
        else:
            prev[j] = prev[j - 1]

    for i in range(1, n):
        curr = {j: 0 for j in range(m)}
        curr[0] = 1 if str1[i] == str2[0] else prev[0]
        for j in range(1, m):
            if str1[i] == str2[j]:
                curr[j] = 1 + prev[j - 1]
            else:
                curr[j] = max(
                    prev[j],
                    curr[j - 1]
                )
        prev = curr

    return prev[m - 1]


def longest_common_palindromic_subsequence(string):
    return longest_common_subsequence(string, string[-1:-len(string)-1:-1])


def min_insertions_to_make_palindrome(string):
    n = len(string)
    lcp = longest_common_palindromic_subsequence(string)
    return n - lcp


print(min_insertions_to_make_palindrome("abca"))
print(min_insertions_to_make_palindrome("abcdefg"))
print(min_insertions_to_make_palindrome("aaaaa"))
print(min_insertions_to_make_palindrome("zzazz"))
print(min_insertions_to_make_palindrome("mbadm"))
print(min_insertions_to_make_palindrome("leetcode"))