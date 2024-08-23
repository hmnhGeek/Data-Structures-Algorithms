def recursive():
    def solve_lcs(str1, i, str2, j):
        if i < 0 or j < 0:
            return ""

        if str1[i] == str2[j]:
            return solve_lcs(str1, i - 1, str2, j - 1) + str1[i]
        else:
            left = solve_lcs(str1, i - 1, str2, j)
            right = solve_lcs(str1, i, str2, j - 1)
            return max(left, right, key=len)

    def get_lcs(str1, str2):
        n = len(str1)
        m = len(str2)
        return solve_lcs(str1, n - 1, str2, m - 1)


def memoized():
    def solve_lcs(str1, i, str2, j, dp):
        if i < 0 or j < 0:
            return ""

        if dp[i][j] is not None:
            return dp[i][j]

        if str1[i] == str2[j]:
            dp[i][j] = solve_lcs(str1, i - 1, str2, j - 1, dp) + str1[i]
        else:
            left = solve_lcs(str1, i - 1, str2, j, dp)
            right = solve_lcs(str1, i, str2, j - 1, dp)
            dp[i][j] = max(left, right, key=len)
        return dp[i][j]

    def get_lcs(str1, str2):
        n = len(str1)
        m = len(str2)
        dp = {i: {j: None for j in range(m)} for i in range(n)}
        return solve_lcs(str1, n - 1, str2, m - 1, dp)


def tabulation():
    def get_lcs(str1, str2):
        n = len(str1)
        m = len(str2)
        dp = {i: {j: "" for j in range(m)} for i in range(n)}

        prev[0] = str1[0] if str1[0] == str2[0] else ""
        for j in range(1, m):
            if str1[0] == str2[j]:
                prev[j] = str1[0]
            else:
                prev[j] = prev[j - 1]
        for i in range(1, m):
            if str1[i] == str2[0]:
                dp[i][0] = str2[0]
            else:
                dp[i][0] = prev[0]

        for i in range(1, n):
            for j in range(1, m):
                if str1[i] == str2[j]:
                    dp[i][j] = prev[j - 1] + str1[i]
                else:
                    left = prev[j]
                    right = dp[i][j - 1]
                    dp[i][j] = max(left, right, key=len)

        return dp[n - 1][m - 1]


def get_lcs(str1, str2):
    n = len(str1)
    m = len(str2)
    prev = {j: "" for j in range(m)}

    prev[0] = str1[0] if str1[0] == str2[0] else ""
    for j in range(1, m):
        if str1[0] == str2[j]:
            prev[j] = str1[0]
        else:
            prev[j] = prev[j - 1]

    for i in range(1, n):
        curr = {j: "" for j in range(m)}
        curr[0] = str1[i] if str1[i] == str2[0] else prev[0]
        for j in range(1, m):
            if str1[i] == str2[j]:
                curr[j] = prev[j - 1] + str1[i]
            else:
                left = prev[j]
                right = curr[j - 1]
                curr[j] = max(left, right, key=len)
        prev = curr

    return prev[m - 1]


def get_shortest_common_subsequence(str1, str2):
    lcs = get_lcs(str1, str2)
    scs = ""
    i = 0
    j = 0

    while i < len(str1) and j < len(str2):
        if str1[i] not in lcs and str2[j] not in lcs:
            scs += str1[i] + str2[j]
            i += 1
            j += 1
        else:
            if str1[i] in lcs:
                while j < len(str2) and str2[j] != str1[i]:
                    scs += str2[j]
                    j += 1
                scs += str1[i]
                i += 1
                j += 1
            else:
                while i < len(str1) and str1[i] != str2[j]:
                    scs += str1[i]
                    i += 1
                scs += str2[j]
                j += 1
                i += 1

    while i < len(str1):
        scs += str1[i]
        i += 1

    while j < len(str2):
        scs += str2[j]
        j += 1

    return scs


print(get_shortest_common_subsequence("brute", "groot"))
print(get_shortest_common_subsequence("bleed", "blue"))
print(get_shortest_common_subsequence("coding", "ninjas"))
print(get_shortest_common_subsequence("blinding", "lights"))
print(get_shortest_common_subsequence("abac", "cab"))
print(get_shortest_common_subsequence("aaaaaaaa", "aaaaaaaa"))
print(get_shortest_common_subsequence("abcd", "xycd"))
print(get_shortest_common_subsequence("efgh", "jghi"))


