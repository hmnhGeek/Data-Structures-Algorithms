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
    # This will take O(n*m) time and O(m) space.
    lcs = get_lcs(str1, str2)

    # initialize the resultant string
    shortest_common_supersequence = ""

    # start from the 0th indices of both the strings.
    i = 0
    j = 0

    # while you're still within the limits of both the strings
    while i < len(str1) and j < len(str2):
        # if the current characters of both the strings are not in lcs, then add both the characters
        # in the final string and increment both i and j together.
        if str1[i] not in lcs and str2[j] not in lcs:
            shortest_common_supersequence += str1[i] + str2[j]
            i += 1
            j += 1
        else:
            # otherwise, if string 1's character is in lcs, then first add string 2's characters till we
            # don't get to the index j at which both s1[i] and s2[j] are same, i.e., both are in lcs. It
            # is possible that at the start only both are same, and that's fine; we would not add any
            # character from s2 then.
            if str1[i] in lcs:
                while j < len(str2) and str2[j] != str1[i]:
                    shortest_common_supersequence += str2[j]
                    j += 1

                # at this point j is at an index such that s2[j] = s1[i] and they are in lcs. So we will
                # add this character only once (either from s1 or s2, your choice), but then increment
                # both i and j.
                shortest_common_supersequence += str1[i]
                i += 1
                j += 1
            else:
                # else case would surely be that s1[i] is not in lcs but s2[j] is in lcs. In that case,
                # continuously add from s1 until s1[i] = s2[j] which are both in lcs.
                while i < len(str1) and str1[i] != str2[j]:
                    shortest_common_supersequence += str1[i]
                    i += 1

                # at this point i is at an index such that s2[j] = s1[i] and they are in lcs. So we will
                # add this character only once (either from s1 or s2, your choice), but then increment
                # both i and j.
                shortest_common_supersequence += str2[j]
                j += 1
                i += 1

    # once you're out of bounds in any of the string, check if characters are left from s1 or not, if yes,
    # then add them.
    while i < len(str1):
        shortest_common_supersequence += str1[i]
        i += 1

    # similar check for s2 is needed as well.
    while j < len(str2):
        shortest_common_supersequence += str2[j]
        j += 1

    # finally return the shortest common subsequence.
    return shortest_common_supersequence


print(get_shortest_common_subsequence("brute", "groot"))
print(get_shortest_common_subsequence("bleed", "blue"))
print(get_shortest_common_subsequence("coding", "ninjas"))
print(get_shortest_common_subsequence("blinding", "lights"))
print(get_shortest_common_subsequence("abac", "cab"))
print(get_shortest_common_subsequence("aaaaaaaa", "aaaaaaaa"))
print(get_shortest_common_subsequence("abcd", "xycd"))
print(get_shortest_common_subsequence("efgh", "jghi"))


