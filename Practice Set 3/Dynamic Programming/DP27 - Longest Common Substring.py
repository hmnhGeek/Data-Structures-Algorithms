class Solution:
    @staticmethod
    def longest_common_substring(s1, s2):
        n1, n2 = len(s1), len(s2)
        dp = {i: {j: 0 for j in range(n2 + 1)} for i in range(n1 + 1)}
        ans = 0
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = 0
        return ans


print(Solution.longest_common_substring("abcd", "abzd"))
print(Solution.longest_common_substring("abcjklp", "acjkp"))
print(Solution.longest_common_substring("wasdijkl", "wsdjkl"))
print(Solution.longest_common_substring("tyfg", "cvbnuty"))
print(Solution.longest_common_substring("GeeksforGeeks", "GeeksQuiz"))
print(Solution.longest_common_substring("abcdxyz", "xyzabcd"))
print(Solution.longest_common_substring("abc", ""))
