def recursive():
    def solve_lcs(string1, index1, string2, index2, lcs_length_till_now, max_obtained):
        # Time complexity would be exponential and space would be deepest of the recursion stack.

        # during the last part of any branch of the recursion tree, we might have got some common substring, at that
        # point, any or both indices might go negative. In this case, return the max of max_obtained till now and the
        # lcs length obtained from this last part, whichever is maximum; you can update max_obtained for code
        # readability and return it finally.
        if index1 < 0 or index2 < 0:
            return max(max_obtained, lcs_length_till_now)

        # if there is a character match, increment the value of lcs_length_till_now by 1 and proceed for lower indices
        if string1[index1] == string2[index2]:
            max_obtained = solve_lcs(string1, index1 - 1, string2, index2 - 1, lcs_length_till_now + 1, max_obtained)
        else:
            # if there is a mismatch, then first of all, update the max_obtained by checking if lcs length of the part
            # is greater than max_obtained till now or not.
            max_obtained = max(lcs_length_till_now, max_obtained)

            # reset lcs length because from next recursion, we will start finding fresh substring.
            lcs_length_till_now = 0

            # update the max_obtained that will be returned from the left recursion (reducing only index1).
            max_obtained = solve_lcs(string1, index1 - 1, string2, index2, lcs_length_till_now, max_obtained)

            # update the max_obtained that will be returned from the right recursion (reducing only index2). Please
            # note that any change in lcs_length_till_now from left recursion will have no impact here, because
            # lcs_length_till_now will be back-tracked to 0 at this point again, and so, in the right recursion,
            # we will be basically searching for a fresh substring.
            max_obtained = solve_lcs(string1, index1, string2, index2 - 1, lcs_length_till_now, max_obtained)

        # return the overall max.
        return max_obtained

    def get_longest_common_substring(string1, string2):
        # Edge case
        if len(string1) == 0 or len(string2) == 0:
            return 0

        n = len(string1)
        m = len(string2)

        # store these two variables:
        # lcs_length_obtained: during the recursion, we will continuously sum up length in this variable and will
        #                      reset it back to 0 once there is a mismatch; so basically, this is used as a window.
        # max_obtained: It will always store the max value of the sum that recursion must have fetched.
        lcs_length_obtained = 0
        max_obtained = 0

        # solve for this problem recursively.
        max_obtained = solve_lcs(string1, n - 1, string2, m - 1, lcs_length_obtained, max_obtained)
        return max_obtained

    print(
        get_longest_common_substring(
            "abcjklp",
            "acjkp"
        )
    )

    print(
        get_longest_common_substring(
            "ab",
            "defg"
        )
    )

    print(
        get_longest_common_substring(
            "adebc",
            "dcadb"
        )
    )

    print(
        get_longest_common_substring(
            "tyfg",
            "cvbnuty"
        )
    )

    print(
        get_longest_common_substring(
            "wasdijkl",
            "wsdjkl"
        )
    )

    print(
        get_longest_common_substring(
            "geeksforgeeks",
            "geeksquiz"
        )
    )

    print(
        get_longest_common_substring(
            "abcdxyz",
            "xyzabcd"
        )
    )

    print(
        get_longest_common_substring(
            "zxabcdezy",
            "yzabcdezx"
        )
    )


def tabulation_from_longest_common_subsequence():
    def get_longest_common_substring(string1, string2):
        # Time complexity would be O(n*m) and space complexity would be O(n*m) for the dp array.

        # if either of the string is empty, return 0 as there will be no common subsequence at all
        if len(string1) == 0 or len(string2) == 0:
            return 0

        n, m = len(string1), len(string2)
        dp = {i: {j: 0 for j in range(m)} for i in range(n)}

        # special base case for checking the first character of the strings
        dp[0][0] = 1 if string1[0] == string2[0] else 0

        # fill the first column of the dp matrix for index1 starting from 1 to n - 1.
        for index1 in range(1, n):
            # if there is a match, put 1, else put 0
            dp[index1][0] = 1 if string1[index1] == string2[0] else 0

        # fill the first row of the dp matrix for index2 starting from 1 to m - 1.
        for index2 in range(1, m):
            # if there is a match, put 1, else put 0
            dp[0][index2] = 1 if string1[0] == string2[index2] else 0

        # variable to store the maximum length obtained for the substring.
        max_length_obtained = 0

        for index1 in range(1, n):
            for index2 in range(1, m):
                # if the characters from string 1 and string 2 match at their respective indices, this means we can
                # add 1 to the LCS and solve for lower indices on both the strings. Also, update the variable
                # max_length_obtained.
                if string1[index1] == string2[index2]:
                    dp[index1][index2] = 1 + dp[index1 - 1][index2 - 1]
                    max_length_obtained = max(max_length_obtained, dp[index1][index2])
                else:
                    # if they do not match, simply put a 0 in the matrix to denote a discontinuity.
                    dp[index1][index2] = 0

        return max_length_obtained

    print(
        get_longest_common_substring(
            "abcjklp",
            "acjkp"
        )
    )

    print(
        get_longest_common_substring(
            "ab",
            "defg"
        )
    )

    print(
        get_longest_common_substring(
            "adebc",
            "dcadb"
        )
    )

    print(
        get_longest_common_substring(
            "tyfg",
            "cvbnuty"
        )
    )

    print(
        get_longest_common_substring(
            "wasdijkl",
            "wsdjkl"
        )
    )

    print(
        get_longest_common_substring(
            "geeksforgeeks",
            "geeksquiz"
        )
    )

    print(
        get_longest_common_substring(
            "abcdxyz",
            "xyzabcd"
        )
    )

    print(
        get_longest_common_substring(
            "zxabcdezy",
            "yzabcdezx"
        )
    )


def space_optimized():
    def get_longest_common_substring(string1, string2):
        # Time complexity would be O(n*m) and space complexity would be O(m) for the dp array.

        # if either of the string is empty, return 0 as there will be no common subsequence at all
        if len(string1) == 0 or len(string2) == 0:
            return 0

        n, m = len(string1), len(string2)
        prev = {j: 0 for j in range(m)}

        # special base case for checking the first character of the strings
        prev[0] = 1 if string1[0] == string2[0] else 0

        # fill the first row of the dp matrix for index2 starting from 1 to m - 1.
        for index2 in range(1, m):
            # if there is a match, put 1, else put 0
            prev[index2] = 1 if string1[0] == string2[index2] else 0

        # variable to store the maximum length obtained for the substring.
        max_length_obtained = 0

        for index1 in range(1, n):
            curr = {j: 0 for j in range(m)}

            # note this... compare with subsequence problem code.
            curr[0] = 1 if string1[index1] == string2[0] else 0

            for index2 in range(1, m):
                # if the characters from string 1 and string 2 match at their respective indices, this means we can
                # add 1 to the LCS and solve for lower indices on both the strings. Also, update the variable
                # max_length_obtained.
                if string1[index1] == string2[index2]:
                    curr[index2] = 1 + prev[index2 - 1]
                    max_length_obtained = max(max_length_obtained, curr[index2])
                else:
                    # if they do not match, simply put a 0 in the matrix to denote a discontinuity.
                    curr[index2] = 0
            prev = curr

        return max_length_obtained

    print(
        get_longest_common_substring(
            "abcjklp",
            "acjkp"
        )
    )

    print(
        get_longest_common_substring(
            "ab",
            "defg"
        )
    )

    print(
        get_longest_common_substring(
            "adebc",
            "dcadb"
        )
    )

    print(
        get_longest_common_substring(
            "tyfg",
            "cvbnuty"
        )
    )

    print(
        get_longest_common_substring(
            "wasdijkl",
            "wsdjkl"
        )
    )

    print(
        get_longest_common_substring(
            "geeksforgeeks",
            "geeksquiz"
        )
    )

    print(
        get_longest_common_substring(
            "abcdxyz",
            "xyzabcd"
        )
    )

    print(
        get_longest_common_substring(
            "zxabcdezy",
            "yzabcdezx"
        )
    )


print("Recursion Solution")
recursive()

print()
print("Tabulation Solution")
tabulation_from_longest_common_subsequence()

print()
print("Space Optimized Solution")
space_optimized()