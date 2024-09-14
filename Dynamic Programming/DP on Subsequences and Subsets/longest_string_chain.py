from collections import Counter


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


print("Recursive Solution")
recursive()

print("Memoized Solution")
memoized()