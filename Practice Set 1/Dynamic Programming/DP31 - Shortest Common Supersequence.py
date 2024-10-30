# Problem link - https://www.naukri.com/code360/problems/shortest-supersequence_4244493?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=xElxAuBcvsU&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=32


def scs(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = {i: {j: 0 for j in range(n2 + 1)} for i in range(n1 + 1)}

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    result = ""
    i, j = n1, n2
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            result += s1[i - 1]
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] >= dp[i][j - 1]:
                result += s1[i - 1]
                i -= 1
            else:
                result += s2[j - 1]
                j -= 1

    while i > 0:
        result += s1[i - 1]
        i -= 1

    while j > 0:
        result += s2[j - 1]
        j -= 1

    return result[-1:-len(result)-1:-1]


print(scs("brute", "groot"))
print(scs("bleed", "blue"))
print(scs("coding", "ninjas"))
print(scs("blinding", "lights"))