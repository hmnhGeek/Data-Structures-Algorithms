# Problem link - https://www.geeksforgeeks.org/a-program-to-check-if-strings-are-rotations-of-each-other/#naive-approach-by-generating-all-rotations-on2-time-and-o1-space
# Solution - https://www.youtube.com/watch?v=JoF0Z7nVSrA (Using KMP Algorithm)


"""
    The only way to figure out about KMP algorithm is to watch the video. The algorithm is rather complex.
"""

def get_lps_array(pattern):
    prev_lps = 0
    i = 1
    lps = [0] * len(pattern)
    while i < len(pattern):
        if pattern[prev_lps] == pattern[i]:
            lps[i] = prev_lps + 1
            i += 1
            prev_lps += 1
        elif prev_lps == 0:
            lps[i] = 0
            i += 1
        else:
            prev_lps = lps[prev_lps - 1]
    return lps


def does_pattern_exist(string, pattern):
    """
        Overall time complexity is O(m + n) and overall space complexity is O(m).
    """

    # Takes O(m) time and O(m) space.
    lps = get_lps_array(pattern)
    i, j = 0, 0

    # Takes O(n) time.
    while i < len(string):
        if string[i] == pattern[j]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = lps[j - 1]

        if j == len(pattern):
            return i - j
    return -1


def are_strings_rotation_of_each_other(str1, str2):
    temp = str1 + str1
    return does_pattern_exist(temp, str2) > 0


print(are_strings_rotation_of_each_other("abcd", "cdab"))
print(are_strings_rotation_of_each_other("aab", "aba"))
print(are_strings_rotation_of_each_other("abcd", "acbd"))