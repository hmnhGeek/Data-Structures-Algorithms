# Problem link - https://www.naukri.com/code360/problems/minimum-insertions-to-make-palindrome_985293?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=xPBLEj41rFU&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=30


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


def memoized():
    def solve(s1, i, s2, j, dp):
        if i == 0 or j == 0:
            return ""

        if dp[i][j] is not None:
            return dp[i][j]

        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = solve(s1, i - 1, s2, j - 1, dp) + s1[i - 1]
        else:
            dp[i][j] = max(
                solve(s1, i - 1, s2, j, dp),
                solve(s1, i, s2, j - 1, dp),
                key=len
            )
        return dp[i][j]

    def lcs(s1, s2):
        n1 = len(s1)
        n2 = len(s2)
        dp = {i: {j: None for j in range(n2 + 1)} for i in range(n1 + 1)}
        return solve(s1, n1, s2, n2, dp)

    print(lcs("abcd", "abzde"))


def tabulation():
    def lcs(s1, s2):
        n1 = len(s1)
        n2 = len(s2)
        dp = {i: {j: "" for j in range(n2 + 1)} for i in range(n1 + 1)}

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + s1[i - 1]
                else:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        key=len
                    )

        return dp[n1][n2]

    print(lcs("abcd", "abzde"))


def space_optimized():
    def lcs(s1, s2):
        n1 = len(s1)
        n2 = len(s2)
        prev = {j: "" for j in range(n2 + 1)}

        for i in range(1, n1 + 1):
            curr = {j: "" for j in range(n2 + 1)}
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = prev[j - 1] + s1[i - 1]
                else:
                    curr[j] = max(
                        prev[j],
                        curr[j - 1],
                        key=len
                    )
            prev = curr

        return prev[n2]

    print(lcs("abcd", "abzde"))


def lcs(s1, s2):
        n1 = len(s1)
        n2 = len(s2)
        dp = {i: {j: 0 for j in range(n2 + 1)} for i in range(n1 + 1)}

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i][j - 1]
                    )

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
        return result[-1:-len(result)-1:-1]


def get_min_chars_to_make_palindrome(string):
    reversed = string[-1:-len(string)-1:-1]
    longest_palindromic_subsequence = lcs(string, reversed)
    return len(string) - len(longest_palindromic_subsequence)


print(get_min_chars_to_make_palindrome("codingninjas"))
print(get_min_chars_to_make_palindrome("abcdefg"))
print(get_min_chars_to_make_palindrome("abca"))
print(get_min_chars_to_make_palindrome("aaaaa"))