def tabulation():
    def lcs(s1, s2):
        n, m = len(s1), len(s2)
        dp = {i: {j: 0 for j in range(m + 1)} for i in range(n + 1)}
        longest_length = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    longest_length = max(longest_length, dp[i][j])
                else:
                    dp[i][j] = 0
        return longest_length

    print(lcs("abcd", "abzd"))
    print(lcs("abcjklp", "acjkp"))
    print(lcs("wasdijkl", "wsdjkl"))
    print(lcs("tyfg", "cvbnuty"))
    print(lcs("GeeksforGeeks", "GeeksQuiz"))
    print(lcs("abcdxyz", "xyzabcd"))
    print(lcs("abc", ""))


tabulation()
