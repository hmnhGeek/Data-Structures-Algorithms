class Solution:
    @staticmethod
    def longest_common_substring(s1, s2):
        """
            Time complexity is O(n1 * n2) and space complexity is O(n1 * n2).
        """
        n = len(s1)
        m = len(s2)
        dp = {i: {j: 0 for j in range(m + 1)} for i in range(n + 1)}
        result = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    result = max(result, dp[i][j])
                else:
                    dp[i][j] = 0
        return result


print(Solution.longest_common_substring("abcd", "abzd"))
print(Solution.longest_common_substring("abcjklp", "acjkp"))
print(Solution.longest_common_substring("wasdijkl", "wsdjkl"))
print(Solution.longest_common_substring("tyfg", "cvbnuty"))
print(Solution.longest_common_substring("GeeksforGeeks", "GeeksQuiz"))
print(Solution.longest_common_substring("abcdxyz", "xyzabcd"))
print(Solution.longest_common_substring("abc", ""))