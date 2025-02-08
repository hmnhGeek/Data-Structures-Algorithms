# Problem link - https://www.naukri.com/code360/problems/longest-common-substring_1235207?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=_wP9mWNPL5w&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=28


class Solution:
    @staticmethod
    def longest_common_substring(s1, s2):
        """
            Time complexity is O(n1 * n2) and space complexity is O(n1 * n2).
        """
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

    @staticmethod
    def optimized_lcs(s1, s2):
        """
            Time complexity is O(n1 * n2) and space complexity is O(n2).
        """
        n1, n2 = len(s1), len(s2)
        prev = {j: 0 for j in range(n2 + 1)}
        ans = 0
        for i in range(1, n1 + 1):
            curr = {j: 0 for j in range(n2 + 1)}
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                    ans = max(ans, curr[j])
                else:
                    curr[j] = 0
            prev = curr
        return ans


print(Solution.longest_common_substring("abcd", "abzd"))
print(Solution.longest_common_substring("abcjklp", "acjkp"))
print(Solution.longest_common_substring("wasdijkl", "wsdjkl"))
print(Solution.longest_common_substring("tyfg", "cvbnuty"))
print(Solution.longest_common_substring("GeeksforGeeks", "GeeksQuiz"))
print(Solution.longest_common_substring("abcdxyz", "xyzabcd"))
print(Solution.longest_common_substring("abc", ""))
print()
print(Solution.optimized_lcs("abcd", "abzd"))
print(Solution.optimized_lcs("abcjklp", "acjkp"))
print(Solution.optimized_lcs("wasdijkl", "wsdjkl"))
print(Solution.optimized_lcs("tyfg", "cvbnuty"))
print(Solution.optimized_lcs("GeeksforGeeks", "GeeksQuiz"))
print(Solution.optimized_lcs("abcdxyz", "xyzabcd"))
print(Solution.optimized_lcs("abc", ""))
