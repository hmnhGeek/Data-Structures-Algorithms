# Problem link - https://www.naukri.com/code360/problems/longest-common-substring_1235207?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=_wP9mWNPL5w&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=28


def tabulation():
    def lcs(s1, s2):
        """
            Overall time complexity is O(nm) and space complexity is O(nm).
        """

        n, m = len(s1), len(s2)
        dp = {i: {j: 0 for j in range(m + 1)} for i in range(n + 1)}
        longest_length = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # if there's a match in the characters, set dp[i][j] = 1 + dp[i - 1[j - 1] to maintain the continuity
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    # also ensure to always keep the maximum length
                    longest_length = max(longest_length, dp[i][j])
                else:
                    # if the characters don't match, break the continuity and assign 0.
                    dp[i][j] = 0
        return longest_length

    print(lcs("abcd", "abzd"))
    print(lcs("abcjklp", "acjkp"))
    print(lcs("wasdijkl", "wsdjkl"))
    print(lcs("tyfg", "cvbnuty"))
    print(lcs("GeeksforGeeks", "GeeksQuiz"))
    print(lcs("abcdxyz", "xyzabcd"))
    print(lcs("abc", ""))


def space_optimized():
    def lcs(s1, s2):
        """
            Overall time complexity is O(nm) and space complexity is O(m).
        """

        n, m = len(s1), len(s2)
        prev = {j: 0 for j in range(m + 1)}
        longest_length = 0
        for i in range(1, n + 1):
            curr = {j: 0 for j in range(m + 1)}
            for j in range(1, m + 1):
                # if there's a match in the characters, set dp[i][j] = 1 + dp[i - 1[j - 1] to maintain the continuity
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                    # also ensure to always keep the maximum length
                    longest_length = max(longest_length, curr[j])
                else:
                    # if the characters don't match, break the continuity and assign 0.
                    curr[j] = 0
            prev = curr
        return longest_length

    print(lcs("abcd", "abzd"))
    print(lcs("abcjklp", "acjkp"))
    print(lcs("wasdijkl", "wsdjkl"))
    print(lcs("tyfg", "cvbnuty"))
    print(lcs("GeeksforGeeks", "GeeksQuiz"))
    print(lcs("abcdxyz", "xyzabcd"))
    print(lcs("abc", ""))


tabulation()
print()
space_optimized()
