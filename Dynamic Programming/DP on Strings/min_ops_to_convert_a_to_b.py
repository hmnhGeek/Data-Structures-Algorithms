# Problem link - https://www.naukri.com/code360/problems/can-you-make_4244510?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=yMnH0jrir0Q&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=32

def get_lcs_length(str1, str2):
    n, m = len(str1), len(str2)
    prev = {j: 0 for j in range(m)}
    prev[0] = 1 if str1[0] == str2[0] else 0

    for j in range(1, m):
        if str1[0] == str2[j]:
            prev[j] = 1
        else:
            prev[j] = prev[j - 1]

    for i in range(1, n):
        curr = {j: 0 for j in range(m)}
        curr[0] = 1 if str1[i] == str2[0] else prev[0]
        for j in range(1, m):
            if str1[i] == str2[j]:
                curr[j] = 1 + prev[j - 1]
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev = curr
    return prev[m - 1]


def convert(str1, str2):
    """
        The idea is that we do not touch the common characters in the string. We can get the count of such non-touchable
        characters from the longest common subsequence length. The minimum operations required now are as follows:
        1. string 1 -> lcs
        2. lcs -> string 2

        Converting string 1 to lcs will take len(string 1) - len(lcs) operations.
        Converting lcs to string 2 will take len(string 2) - len(lcs) operations.
        Total number of operations thus comes out to be len(string 1) + len(string 2) - 2*len(lcs).

        Overall time complexity is same as that of get_lcs_length() function which is O(n*m) time and O(m) space.
    """
    lcs_length = get_lcs_length(str1, str2)
    n, m = len(str1), len(str2)
    return n + m - 2*lcs_length


print(convert("abcd", "anc"))
print(convert("aaa", "aa"))
print(convert("edl", "xcqja"))
print(convert("book", "bookshelf"))

