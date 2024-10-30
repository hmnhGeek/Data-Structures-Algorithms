# Problem link - https://www.naukri.com/code360/problems/can-you-make_4244510?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=yMnH0jrir0Q&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=31


def lcs(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    dp = {i: {j: "" for j in range(n2 + 1)} for i in range(n1 + 1)}

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + s1[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)

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


def min_ops_to_convert(s1, s2):
    _lcs = lcs(s1, s2)
    return len(s1) + len(s2) - 2*len(_lcs)


print(min_ops_to_convert("abcd", "anc"))
print(min_ops_to_convert("aaa", "aa"))
print(min_ops_to_convert("edl", "xcqja"))
print(min_ops_to_convert("heap", "pea"))