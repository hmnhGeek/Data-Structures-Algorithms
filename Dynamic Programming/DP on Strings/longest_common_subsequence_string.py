# Problem link - https://www.naukri.com/code360/problems/longest-common-subsequence_624879?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=-zI4mrF2Pb4&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=28

# The code remains exactly the same as counting the length of the longest common subsequence
# (longest_common_subsequence.py). The differences are these:
# 1. In case of returning 0, return "".
# 2. In case of character match, instead of adding 1, add the character after the recursive call.
#
# Otherwise, everything else remains the same.

def recursive():
    def solve_for_lcs(string1, index1, string2, index2):
        if index1 < 0 or index2 < 0:
            return ""

        if string1[index1] == string2[index2]:
            return solve_for_lcs(string1, index1 - 1, string2, index2 - 1) + string1[index1]

        left = solve_for_lcs(string1, index1 - 1, string2, index2)
        right = solve_for_lcs(string1, index1, string2, index2 - 1)
        return max(left, right, key=len)

    def get_lcs_string(string1, string2):
        if len(string1) == 0 or len(string2) == 0:
            return ""

        n, m = len(string1), len(string2)
        return solve_for_lcs(string1, n - 1, string2, m - 1)

    print(
        get_lcs_string("abcde", "bdgek")
    )

    print(
        get_lcs_string(
            "adebc",
            "dcadb"
        )
    )

    print(
        get_lcs_string(
            "ab",
            "defg"
        )
    )

    print(
        get_lcs_string(
            "abcde",
            "ace"
        )
    )

    print(
        get_lcs_string(
            "abc",
            "abc"
        )
    )

    print(
        get_lcs_string(
            "abc",
            "acd"
        )
    )

    print(
        get_lcs_string(
            "aggtab",
            "gxtxayb"
        )
    )

    print(
        get_lcs_string(
            "abc",
            "cba"
        )
    )


def memoized():
    def solve_for_lcs(string1, index1, string2, index2, dp):
        if index1 < 0 or index2 < 0:
            return ""

        if dp[index1][index2] is not None:
            return dp[index1][index2]

        if string1[index1] == string2[index2]:
            dp[index1][index2] = solve_for_lcs(string1, index1 - 1, string2, index2 - 1, dp) + string1[index1]
        else:
            left = solve_for_lcs(string1, index1 - 1, string2, index2, dp)
            right = solve_for_lcs(string1, index1, string2, index2 - 1, dp)
            dp[index1][index2] = max(left, right, key=len)
        return dp[index1][index2]

    def get_lcs_string(string1, string2):
        if len(string1) == 0 or len(string2) == 0:
            return ""

        n, m = len(string1), len(string2)
        dp = {i: {j: None for j in range(m)} for i in range(n)}
        return solve_for_lcs(string1, n - 1, string2, m - 1, dp)

    print(
        get_lcs_string("abcde", "bdgek")
    )

    print(
        get_lcs_string(
            "adebc",
            "dcadb"
        )
    )

    print(
        get_lcs_string(
            "ab",
            "defg"
        )
    )

    print(
        get_lcs_string(
            "abcde",
            "ace"
        )
    )

    print(
        get_lcs_string(
            "abc",
            "abc"
        )
    )

    print(
        get_lcs_string(
            "abc",
            "acd"
        )
    )

    print(
        get_lcs_string(
            "aggtab",
            "gxtxayb"
        )
    )

    print(
        get_lcs_string(
            "abc",
            "cba"
        )
    )


def tabulation():
    def get_lcs_string(string1, string2):
        if len(string1) == 0 or len(string2) == 0:
            return ""

        n, m = len(string1), len(string2)
        dp = {i: {j: "" for j in range(m)} for i in range(n)}

        dp[0][0] = string1[0] if string1[0] == string2[0] else ""

        for index2 in range(1, m):
            dp[0][index2] = string1[0] if string1[0] == string2[index2] else dp[0][index2 - 1]

        for index1 in range(1, n):
            dp[index1][0] = string2[0] if string1[index1] == string2[0] else dp[index1 - 1][0]

        for index1 in range(1, n):
            for index2 in range(1, m):
                if string1[index1] == string2[index2]:
                    dp[index1][index2] = dp[index1 - 1][index2 - 1] + string1[index1]
                else:
                    left = dp[index1 - 1][index2]
                    right = dp[index1][index2 - 1]
                    dp[index1][index2] = max(left, right, key=len)

        return dp[n - 1][m - 1]

    print(
        get_lcs_string("abcde", "bdgek")
    )

    print(
        get_lcs_string(
            "adebc",
            "dcadb"
        )
    )

    print(
        get_lcs_string(
            "ab",
            "defg"
        )
    )

    print(
        get_lcs_string(
            "abcde",
            "ace"
        )
    )

    print(
        get_lcs_string(
            "abc",
            "abc"
        )
    )

    print(
        get_lcs_string(
            "abc",
            "acd"
        )
    )

    print(
        get_lcs_string(
            "aggtab",
            "gxtxayb"
        )
    )

    print(
        get_lcs_string(
            "abc",
            "cba"
        )
    )


def space_optimized():
    def get_lcs_string(string1, string2):
        if len(string1) == 0 or len(string2) == 0:
            return ""

        n, m = len(string1), len(string2)
        prev = {j: "" for j in range(m)}

        prev[0] = string1[0] if string1[0] == string2[0] else ""
        for index2 in range(1, m):
            prev[index2] = string1[0] if string1[0] == string2[index2] else prev[index2 - 1]

        for index1 in range(1, n):
            curr = {j: "" for j in range(m)}
            curr[0] = string2[0] if string1[index1] == string2[0] else prev[0]
            for index2 in range(1, m):
                if string1[index1] == string2[index2]:
                    curr[index2] = prev[index2 - 1] + string1[index1]
                else:
                    left = prev[index2]
                    right = curr[index2 - 1]
                    curr[index2] = max(left, right, key=len)
            prev = curr
        return prev[m - 1]

    print(
        get_lcs_string("abcde", "bdgek")
    )

    print(
        get_lcs_string(
            "adebc",
            "dcadb"
        )
    )

    print(
        get_lcs_string(
            "ab",
            "defg"
        )
    )

    print(
        get_lcs_string(
            "abcde",
            "ace"
        )
    )

    print(
        get_lcs_string(
            "abc",
            "abc"
        )
    )

    print(
        get_lcs_string(
            "abc",
            "acd"
        )
    )

    print(
        get_lcs_string(
            "aggtab",
            "gxtxayb"
        )
    )

    print(
        get_lcs_string(
            "abc",
            "cba"
        )
    )


print("Recursion Solution")
recursive()

print()
print("Memoized Solution")
memoized()

print()
print("Tabulation Solution")
tabulation()

print()
print("Space Optimized Solution")
space_optimized()