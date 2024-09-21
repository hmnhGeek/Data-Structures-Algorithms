def get_freq(string):
    # function to give the frequencies of each character in a string.
    d = {i: 0 for i in string}
    for i in string:
        d[i] += 1
    return d


def get_smallest_window(main_string, substring):
    # get the frequency of substring characters in O(n) time and O(n) space in worst case.
    freq = get_freq(substring)

    # store the answer's length as same as the length of the main string.
    min_length = len(main_string)

    # assign indices for the window
    i, j = 0, 0
    n = len(main_string)

    # create a local tracker which will count the same characters that are in substring from the main string.
    substring_count_tracker = {i: 0 for i in substring}

    # store the result in a variable. For now make it same as main string. Here, we are implying that the result
    # or the smallest substring from main string which contains all the characters from second string is actually
    # the main string itself.
    result = main_string

    # while the j index does not overflow from the right boundary.
    while j < n:
        # check if all the characters from the second string have been found or not. If yes, then until any one
        # character is exhausted, do the following.
        while all(v != 0 for v in substring_count_tracker.values()):
            # if at any point, the substring count tracker has the exact same frequencies as that of the second string,
            # we must update the window size and result string.
            if freq == substring_count_tracker:
                window_size = (j - i)
                # if the window size is less than the min_length obtained till now, update min_length and result
                if min_length > window_size:
                    min_length = window_size
                    result = main_string[i:j]

            # also, start shrinking the window from the left side, but while shrinking, if the character at index i
            # is in freq (or substring_count_tracker {read `keys()`}), then reduce its count.
            if main_string[i] in freq:
                substring_count_tracker[main_string[i]] -= 1
            i += 1

        # finally, start expanding the window from the right side, but while expanding, if the character at index j
        # is in freq (or substring_count_tracker {read `keys()`}), then increase its count.
        if main_string[j] in freq:
            substring_count_tracker[main_string[j]] += 1
        j += 1

    # once `j` has overflown from the right side, shrink the window from the left side if there are all the characters
    # in the window from the second string. Basically, follow the same logic as above for shrinking.
    while all(v != 0 for v in substring_count_tracker.values()):
        if freq == substring_count_tracker:
            window_size = (j - i)
            if min_length > window_size:
                min_length = window_size
                result = main_string[i:j]

        if main_string[i] in freq:
            substring_count_tracker[main_string[i]] -= 1
        i += 1

    # return the resultant string.
    return result


print(get_smallest_window("timetopractice", "toc"))
print(get_smallest_window("zoomlazapzo", "oza"))
print(get_smallest_window("ADOBECODEBANC", "ABC"))
print(get_smallest_window("ABBXC", "BXC"))
print(get_smallest_window("ABCKCPCPAAC", "CCP"))