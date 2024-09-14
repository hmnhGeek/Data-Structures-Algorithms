# Problem link - https://www.naukri.com/code360/problems/longest-string-chain_3752111?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=YY8iBaYcc4g&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=47


def have_unit_diff(string1, string2):
    """
        To understand this code, please test for these cases:
        1. abc, ac --> True
        2. adc, ab --> False even though the difference between their lengths is a unit.

        # Time complexity is O(max(len(s1), len(s2))) and space complexity is O(1).
    """

    if string2 is None:
        return True

    # assuming string2 to be always of greater length and that too with only 1 unit difference
    if len(string2) != len(string1) + 1:
        return False

    # we will use a two pointer approach to find if all the characters match apart from the one because of which 1 unit
    # difference is coming.
    i, j = 0, 0

    # while the j pointer (of the larger array) is within bounds
    while j < len(string2):
        # if `i` is in bounds and both the string characters match, move both i and j to their next characters
        if i < len(string1) and string1[i] == string2[j]:
            i += 1
            j += 1
        else:
            # else only increment `j`.
            j += 1

    # if both were able to reach the ends after the while loop ends, we return True, else False.
    return i == len(string1) and j == len(string2)


def recursive():
    def solve(strings, index, prev):
        if index == 0:
            # if the 0th element and prev have a unit difference only, return 1 else return 0
            if have_unit_diff(strings[0], prev):
                return 1
            return 0

        left = float('-inf')
        # if the index element and prev have a unit difference only, then only perform left recursion
        if have_unit_diff(strings[index], prev):
            # perform left recursion by making prev = strings[index]
            left = 1 + solve(strings, index - 1, strings[index])

        # perform only the right recursion with same prev
        right = solve(strings, index - 1, prev)

        # return max out of left and right to get the longest chain.
        return max(left, right)

    def get_longest_string_chain(strings):
        # Overall time complexity is O(2^n) and space complexity is O(n).

        n = len(strings)
        # we need to sort in order to maintain the correct usage of `have_unit_diff()` function because in this function
        # string 1 is always assumed to be shorter than string 2. This will take O(n*log(n)) time.
        strings.sort()
        return solve(strings, n - 1, None)

    print(get_longest_string_chain(["a", "b", "ba", "bca", "bda", "bdca"]))
    print(get_longest_string_chain(["x", "xx", "y", "xyx"]))
    print(get_longest_string_chain(["m", "nm", "mmm"]))
    print(get_longest_string_chain(["a", "bc", "ad", "adc", "bcd"]))


def memoized():
    def solve(strings, index, prev, dp):
        if index == 0:
            # if the 0th element and prev have a unit difference only, return 1 else return 0
            if have_unit_diff(strings[0], prev):
                return 1
            return 0

        if dp[index][prev] is not None:
            return dp[index][prev]

        left = float('-inf')
        # if the index element and prev have a unit difference only, then only perform left recursion
        if have_unit_diff(strings[index], prev):
            # perform left recursion by making prev = strings[index]
            left = 1 + solve(strings, index - 1, strings[index], dp)

        # perform only the right recursion with same prev
        right = solve(strings, index - 1, prev, dp)

        # return max out of left and right to get the longest chain.
        dp[index][prev] = max(left, right)
        return dp[index][prev]

    def get_longest_string_chain(strings):
        # Overall time complexity is O(n^2) and space complexity is O(n + n^2).

        n = len(strings)
        # we need to sort in order to maintain the correct usage of `have_unit_diff()` function because in this function
        # string 1 is always assumed to be shorter than string 2. This will take O(n*log(n)) time.
        strings.sort()

        dp = {i: {j: None for j in strings} for i in range(n)}
        for i in dp:
            dp[i][None] = None

        return solve(strings, n - 1, None, dp)

    print(get_longest_string_chain(["a", "b", "ba", "bca", "bda", "bdca"]))
    print(get_longest_string_chain(["x", "xx", "y", "xyx"]))
    print(get_longest_string_chain(["m", "nm", "mmm"]))
    print(get_longest_string_chain(["a", "bc", "ad", "adc", "bcd"]))


def tabulation():
    def get_longest_string_chain(strings):
        # Overall time complexity is O(n^2) and space complexity is O(n^2).

        n = len(strings)
        # we need to sort in order to maintain the correct usage of `have_unit_diff()` function because in this function
        # string 1 is always assumed to be shorter than string 2. This will take O(n*log(n)) time.
        strings.sort()

        dp = {i: {j: 0 for j in strings} for i in range(n)}
        for i in dp:
            dp[i][None] = 0

        for prev in dp[0]:
            dp[0][prev] = 1 if have_unit_diff(strings[0], prev) else 0

        for index in range(1, n):
            for prev in dp[index]:
                left = float('-inf')
                # if the index element and prev have a unit difference only, then only perform left recursion
                if have_unit_diff(strings[index], prev):
                    # perform left recursion by making prev = strings[index]
                    left = 1 + dp[index - 1][strings[index]]

                # perform only the right recursion with same prev
                right = dp[index - 1][prev]

                # return max out of left and right to get the longest chain.
                dp[index][prev] = max(left, right)

        return dp[n - 1][None]

    print(get_longest_string_chain(["a", "b", "ba", "bca", "bda", "bdca"]))
    print(get_longest_string_chain(["x", "xx", "y", "xyx"]))
    print(get_longest_string_chain(["m", "nm", "mmm"]))
    print(get_longest_string_chain(["a", "bc", "ad", "adc", "bcd"]))


def space_optimized():
    def get_longest_string_chain(strings):
        # Overall time complexity is O(n^2) and space complexity is O(n).

        n = len(strings)
        # we need to sort in order to maintain the correct usage of `have_unit_diff()` function because in this function
        # string 1 is always assumed to be shorter than string 2. This will take O(n*log(n)) time.
        strings.sort()

        # add a previous array for the 0th index.
        previous = {j: 0 for j in strings}
        # add a None key for 0th index.
        previous[None] = 0

        # for all the string2 (i.e., prev), assume them to be 2nd in chain and set their base cases with 0th string.
        for prev in previous:
            previous[prev] = 1 if have_unit_diff(strings[0], prev) else 0

        # since we have set up 0th index, start from index = 1.
        for index in range(1, n):
            # create a curr dictionary
            curr = {j: 0 for j in strings}
            curr[None] = 0

            # for string2 as prev
            for prev in curr:
                left = float('-inf')
                # if the index element and prev have a unit difference only, then only perform left recursion
                if have_unit_diff(strings[index], prev):
                    # perform left recursion by making prev = strings[index]
                    left = 1 + previous[strings[index]]

                # perform only the right recursion with same prev
                right = previous[prev]

                # return max out of left and right to get the longest chain.
                curr[prev] = max(left, right)

            # update previous
            previous = curr

        return previous[None]

    print(get_longest_string_chain(["a", "b", "ba", "bca", "bda", "bdca"]))
    print(get_longest_string_chain(["x", "xx", "y", "xyx"]))
    print(get_longest_string_chain(["m", "nm", "mmm"]))
    print(get_longest_string_chain(["a", "bc", "ad", "adc", "bcd"]))


print("Recursive Solution")
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