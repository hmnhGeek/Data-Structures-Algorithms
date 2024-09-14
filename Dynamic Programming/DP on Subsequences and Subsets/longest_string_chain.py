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


def solve(strings, index, prev):
    if index == 0:
        if have_unit_diff(strings[0], prev):
            return 1
        return 0

    left = float('-inf')
    if have_unit_diff(strings[index], prev):
        left = 1 + solve(strings, index - 1, strings[index])

    right = solve(strings, index - 1, prev)
    return max(left, right)


def get_longest_string_chain(strings):
    n = len(strings)
    strings.sort()
    return solve(strings, n - 1, None)


print(get_longest_string_chain(["a", "b", "ba", "bca", "bda", "bdca"]))
print(get_longest_string_chain(["x", "xx", "y", "xyx"]))