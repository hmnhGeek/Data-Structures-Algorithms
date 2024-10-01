def remove_adjacent_duplicates(string, index, result):
    if index < 0:
        return result

    if len(result) == 0:
        return remove_adjacent_duplicates(string, index - 1, string[index] + result)

    if string[index] != result[0]:
        return remove_adjacent_duplicates(string, index - 1, string[index] + result)
    return remove_adjacent_duplicates(string, index - 1, result)


def remove_adjacent_duplicate_characters(string):
    n = len(string)
    result = ""
    return remove_adjacent_duplicates(string, n - 1, result)


print(remove_adjacent_duplicate_characters("aabb"))
print(remove_adjacent_duplicate_characters("aabaa"))
print(remove_adjacent_duplicate_characters("aaaaabbbbbb"))
print(remove_adjacent_duplicate_characters("geeksforgeeks"))
print(remove_adjacent_duplicate_characters("aabccba"))