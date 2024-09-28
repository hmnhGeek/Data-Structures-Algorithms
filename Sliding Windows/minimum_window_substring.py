# Problme link - https://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/
# Solution - https://www.youtube.com/watch?v=WJaij9ffOIY&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=12


from collections import Counter


def window_satisfied(temp_map, required_map):
    # This will take O(26) time and O(26*2) space, i.e, O(1) time and space each.

    for i in temp_map:
        # if at any point the character count of temp_map is less than the character count in required map,
        # return False.
        if temp_map[i] < required_map[i]:
            return False
    # else return True
    return True


def minimum_window_substring(string, sub):
    # This will take O(26n) time and O(26) space.

    # get the dictionary representation of `sub` string.
    required_map = dict(Counter(sub))
    # get a copy of the required_map, but initialize every character as 0.
    temp_map = {i: 0 for i in required_map}

    # create window variables
    i, j = 0, 0
    n = len(string)
    result = ""

    # until the right pointer is within string bounds.
    while j < n:
        # if the jth character is in the temp_map
        if string[j] in temp_map:
            # increment its count
            temp_map[string[j]] += 1

            # until each character in temp_map has a count >= the same character in required map
            while window_satisfied(temp_map, required_map):
                # first update the result string.
                result = string[i:j+1]
                # start shrinking the window from the left side.
                if string[i] in temp_map:
                    temp_map[string[i]] -= 1
                # increment i
                i += 1
        # increment j
        j += 1

    # finally return the result
    return result


print(minimum_window_substring("ddaaabbca", "abbc"))
print(minimum_window_substring("ADOBECODEBANC", "ABC"))
print(minimum_window_substring("a", "a"))
print(minimum_window_substring("a", "aa"))
print(minimum_window_substring("timetopractice", "toc"))
print(minimum_window_substring("zoomlazapzo", "oza"))