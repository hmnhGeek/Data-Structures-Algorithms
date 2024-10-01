# Problem link - https://www.geeksforgeeks.org/remove-consecutive-duplicates-string/


def remove_adjacent_duplicates(string, index, result):
    # if index becomes negative, return whatever result that has been formed till now.
    if index < 0:
        return result

    # if this is the first time, i.e., index == n - 1, simply prepend the last character to the result
    # as there is no character to compare with.
    if len(result) == 0:
        return remove_adjacent_duplicates(string, index - 1, string[index] + result)

    # if there is already some characters in result, compare the current index value with front of the result.
    # if they do not match, then we can prepend this character and move to next index.
    if string[index] != result[0]:
        return remove_adjacent_duplicates(string, index - 1, string[index] + result)

    # however, if they match, don't do anything to the result, and simply move to the next index.
    return remove_adjacent_duplicates(string, index - 1, result)


def remove_adjacent_duplicate_characters(string):
    # Time complexity is O(n) and space complexity is O(n).
    n = len(string)
    result = ""
    return remove_adjacent_duplicates(string, n - 1, result)


print(remove_adjacent_duplicate_characters("aabb"))
print(remove_adjacent_duplicate_characters("aabaa"))
print(remove_adjacent_duplicate_characters("aaaaabbbbbb"))
print(remove_adjacent_duplicate_characters("geeksforgeeks"))
print(remove_adjacent_duplicate_characters("aabccba"))