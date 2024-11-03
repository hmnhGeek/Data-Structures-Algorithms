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
    lps = get_lps_array(pattern)
    i, j = 0, 0
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