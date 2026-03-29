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

    @staticmethod
    def optimized_lcs(s1, s2):
        """
            Time complexity is O(n1 * n2) and space complexity is O(n2).
        """
        n = len(s1)
        m = len(s2)
        prev = {j: 0 for j in range(m + 1)}
        result = 0
        for i in range(1, n + 1):
            curr = {j: 0 for j in range(m + 1)}
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                    result = max(result, curr[j])
                else:
                    curr[j] = 0
            prev = curr
        return result

    @staticmethod
    def print_lcs(s1, s2):
        """
            Time complexity is O(n1 * n2) and space complexity is O(n1 * n2).
        """
        n = len(s1)
        m = len(s2)
        dp = {i: {j: 0 for j in range(m + 1)} for i in range(n + 1)}
        result = 0
        index = [None, None]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    if result < dp[i][j]:
                        result = dp[i][j]
                        index[0] = i
                        index[1] = j
                else:
                    dp[i][j] = 0
        lcs = ""
        i, j = index[0], index[1]
        while i is not None and j is not None and dp[i][j] != 0:
            lcs += s1[i - 1]
            i -= 1
            j -= 1
        return lcs[-1:-len(lcs)-1:-1]


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
print()
print(Solution.print_lcs("abcd", "abzd"))
print(Solution.print_lcs("abcjklp", "acjkp"))
print(Solution.print_lcs("wasdijkl", "wsdjkl"))
print(Solution.print_lcs("tyfg", "cvbnuty"))
print(Solution.print_lcs("GeeksforGeeks", "GeeksQuiz"))
print(Solution.print_lcs("abcdxyz", "xyzabcd"))
print(Solution.print_lcs("abc", ""))
