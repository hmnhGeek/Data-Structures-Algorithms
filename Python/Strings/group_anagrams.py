# Problem link - https://www.geeksforgeeks.org/problems/print-anagrams-together/1
# Solution - https://www.youtube.com/watch?v=vzdNOK2oB2E


def group_strings(strings):
    """
        Time complexity is O(m*n*26) = O(mn) and space would be O(m*n).
    """

    # create a dictionary which will have keys as counts of each character and the corresponding value
    # as the string with that count of characters.
    groups = dict()

    # loop on each string from the list.
    for string in strings:
        # create a blank count array
        counts = [0] * 26
        # loop on each character in the string, and increase the count of that character
        for char in string:
            counts[ord(char) - ord("a")] += 1

        # convert the counts list to tuple for dictionary key assignment
        counts = tuple(counts)

        # append the string if key exists, else create a new key-value pair
        if counts in groups:
            groups[counts].append(string)
        else:
            groups[counts] = [string]

    # return the groups
    return list(groups.values())


print(group_strings(["act", "god", "cat", "dog", "tac"]))
print(group_strings(["no", "on", "is"]))
print(group_strings(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(group_strings([""]))
print(group_strings(["a"]))
