# Problem link - https://www.naukri.com/code360/problems/longest-common-subsequence_624879?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=NPZn9jBrX8U&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=26

def recursive():
    def solve_for_longest_common_subsequence(string1, index1, string2, index2):
        # Time complexity would be O(2^{n + m}) and space complexity would be O(n + m).

        # if at any point, any or both indices becomes negative, return zero, as a negative index would mean that one
        # of the string has been completely exhausted.
        if index1 < 0 or index2 < 0:
            return 0

        # if the characters from string 1 and string 2 match at their respective indices, this means we can add 1 to
        # the LCS solve for lower indices on both the strings.
        if string1[index1] == string2[index2]:
            return 1 + solve_for_longest_common_subsequence(string1, index1 - 1, string2, index2 - 1)

        # if they do not match, we will add a 0 to LCS and add maximum value obtained once by reducing index 1 and
        # keeping index 2 intact and vice versa.
        return 0 + max(
            solve_for_longest_common_subsequence(string1, index1 - 1, string2, index2),
            solve_for_longest_common_subsequence(string1, index1, string2, index2 - 1)
        )

    def longest_common_subsequence(string1, string2):
        # if either of the string is empty, return 0 as there will be no common subsequence at all
        if len(string1) == 0 or len(string2) == 0:
            return 0

        # recursively solve for LCS
        n, m = len(string1), len(string2)
        return solve_for_longest_common_subsequence(string1, n - 1, string2, m - 1)

    print(
        longest_common_subsequence(
            "adebc",
            "dcadb"
        )
    )

    print(
        longest_common_subsequence(
            "ab",
            "defg"
        )
    )

    print(
        longest_common_subsequence(
            "abcde",
            "ace"
        )
    )

    print(
        longest_common_subsequence(
            "abc",
            "abc"
        )
    )

    print(
        longest_common_subsequence(
            "abc",
            "acd"
        )
    )

    print(
        longest_common_subsequence(
            "aggtab",
            "gxtxayb"
        )
    )

    print(
        longest_common_subsequence(
            "abc",
            "cba"
        )
    )


def memoized():
    def solve_for_longest_common_subsequence(string1, index1, string2, index2, dp):
        # Time complexity would be O(n + m) and space complexity would be O(n + m + n*m) for the dp array.

        # if at any point, any or both indices becomes negative, return zero, as a negative index would mean that one
        # of the string has been completely exhausted.
        if index1 < 0 or index2 < 0:
            return 0

        if dp[index1][index2] is not None:
            return dp[index1][index2]

        # if the characters from string 1 and string 2 match at their respective indices, this means we can add 1 to
        # the LCS solve for lower indices on both the strings.
        if string1[index1] == string2[index2]:
            dp[index1][index2] = 1 + solve_for_longest_common_subsequence(string1, index1 - 1, string2, index2 - 1, dp)
        else:
            # if they do not match, we will add a 0 to LCS and add maximum value obtained once by reducing index 1 and
            # keeping index 2 intact and vice versa.
            dp[index1][index2] = 0 + max(
                solve_for_longest_common_subsequence(string1, index1 - 1, string2, index2, dp),
                solve_for_longest_common_subsequence(string1, index1, string2, index2 - 1, dp)
            )

        return dp[index1][index2]

    def longest_common_subsequence(string1, string2):
        # if either of the string is empty, return 0 as there will be no common subsequence at all
        if len(string1) == 0 or len(string2) == 0:
            return 0

        # recursively solve for LCS
        n, m = len(string1), len(string2)
        dp = {i: {j: None for j in range(m)} for i in range(n)}
        return solve_for_longest_common_subsequence(string1, n - 1, string2, m - 1, dp)

    print(
        longest_common_subsequence(
            "adebc",
            "dcadb"
        )
    )

    print(
        longest_common_subsequence(
            "ab",
            "defg"
        )
    )

    print(
        longest_common_subsequence(
            "abcde",
            "ace"
        )
    )

    print(
        longest_common_subsequence(
            "abc",
            "abc"
        )
    )

    print(
        longest_common_subsequence(
            "abc",
            "acd"
        )
    )

    print(
        longest_common_subsequence(
            "aggtab",
            "gxtxayb"
        )
    )

    print(
        longest_common_subsequence(
            "abc",
            "cba"
        )
    )


def tabulation():
    def longest_common_subsequence(string1, string2):
        # Time complexity would be O(n + m) and space complexity would be O(n*m) for the dp array.

        # if either of the string is empty, return 0 as there will be no common subsequence at all
        if len(string1) == 0 or len(string2) == 0:
            return 0

        n, m = len(string1), len(string2)
        dp = {i: {j: 0 for j in range(m)} for i in range(n)}

        # special base case for checking the first character of the strings
        dp[0][0] = 1 if string1[0] == string2[0] else 0

        # fill the first column of the dp matrix for index1 starting from 1 to n - 1.
        for index1 in range(1, n):
            # if there is a match, put 1, else put max(dp[index1 - 1][0], -inf) = dp[index1 - 1][0] as index2 cannot
            # go down from 0.
            dp[index1][0] = 1 if string1[index1] == string2[0] else dp[index1 - 1][0]

        # fill the first row of the dp matrix for index2 starting from 1 to m - 1.
        for index2 in range(1, m):
            # if there is a match, put 1, else put max(-inf, dp[0][index2 - 1]) = dp[0][index2 - 1] as index1 cannot
            # go down from 0.
            dp[0][index2] = 1 if string1[0] == string2[index2] else dp[0][index2 - 1]

        for index1 in range(1, n):
            for index2 in range(1, m):
                # if the characters from string 1 and string 2 match at their respective indices, this means we can
                # add 1 to the LCS solve for lower indices on both the strings.
                if string1[index1] == string2[index2]:
                    dp[index1][index2] = 1 + dp[index1 - 1][index2 - 1]
                else:
                    # if they do not match, we will add a 0 to LCS and add maximum value obtained once by reducing
                    # index 1 and keeping index 2 intact and vice versa.
                    dp[index1][index2] = 0 + max(dp[index1 - 1][index2], dp[index1][index2 - 1])

        return dp[n - 1][m - 1]

    print(
        longest_common_subsequence(
            "adebc",
            "dcadb"
        )
    )

    print(
        longest_common_subsequence(
            "ab",
            "defg"
        )
    )

    print(
        longest_common_subsequence(
            "abcde",
            "ace"
        )
    )

    print(
        longest_common_subsequence(
            "abc",
            "abc"
        )
    )

    print(
        longest_common_subsequence(
            "abc",
            "acd"
        )
    )

    print(
        longest_common_subsequence(
            "aggtab",
            "gxtxayb"
        )
    )

    print(
        longest_common_subsequence(
            "abc",
            "cba"
        )
    )


recursive()
print()
tabulation()