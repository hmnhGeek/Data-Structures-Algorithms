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
    lcs_length = get_lcs_length(str1, str2)
    n, m = len(str1), len(str2)
    return n + m - 2*lcs_length


print(convert("abcd", "anc"))
print(convert("aaa", "aa"))
print(convert("edl", "xcqja"))
print(convert("book", "bookshelf"))

