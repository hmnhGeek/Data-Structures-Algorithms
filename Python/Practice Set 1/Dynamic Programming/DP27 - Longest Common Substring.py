# Problem link - https://www.naukri.com/code360/problems/longest-common-substring_1235207?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=_wP9mWNPL5w&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=28


def longest_common_substring(s1, s2):
    """
        Time complexity is O(n1*n2) and space complexity is O(n1*n2).
    """
    n1 = len(s1)
    n2 = len(s2)
    dp = {i: {j: "" for j in range(n2 + 1)} for i in range(n1 + 1)}

    # initialize a variable for storing the answer.
    ans = ""

    # loop on the strings just like you do in LCSubsequence.
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            # if the characters at i and j matched, add the current character.
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + s1[i - 1]
                # update the answer with the longest substring
                ans = max(ans, dp[i][j], key=len)
            else:
                # if there is a mismatch, break the substring.
                dp[i][j] = ""
    # return the longest substring which was derived from DP matrix.
    return ans


print(longest_common_substring("abcd", "abzd"))
print(longest_common_substring("abcjklp", "acjkp"))
print(longest_common_substring("wasdijkl", "wsdjkl"))
print(longest_common_substring("tyfg", "cvbnuty"))