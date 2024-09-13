def get_longest_substring_with_k_distinct_characters(string, k):
    # Time complexity O(n) and space complexity is O(h + k) where h is the number of unique
    # characters.

    # store the length of the string for traversal
    n = len(string)

    # initialize a window of size 1 starting from index 0.
    left = right = 0
    max_length = 1

    # store the last indices of every character encountered in a dictionary.
    last_indices = dict()

    # a set to store the unique characters that have been used.
    characters_used = set()

    # in O(n) populate the last found indices to None
    for character in string:
        last_indices[character] = None

    # while right is within array bounds.
    while right < n:
        # get the current character
        character = string[right]

        # update the last index of this character in the dictionary with `right` index.
        last_indices[character] = right

        # add the character into `characters_used`.
        characters_used.add(character)

        # if more than k characters have been used, let's start removing from left
        if len(characters_used) > k:
            # pick the character that needs to be removed.
            character_to_remove = string[left]
            # update left to the index next to the last index of "character to remove".
            left = last_indices[character_to_remove] + 1
            # also, remove the character from the `characters_used`.
            characters_used.remove(character_to_remove)

        # update the max length
        max_length = max(max_length, right - left + 1)
        # expand the window to the right for next character
        right += 1

    # return max length
    return max_length


print(get_longest_substring_with_k_distinct_characters("aaabbccd", 2))
print(get_longest_substring_with_k_distinct_characters("abbbbbbc", 2))
print(get_longest_substring_with_k_distinct_characters("abcddefg", 3))
print(get_longest_substring_with_k_distinct_characters("aaaaaaaa", 3))
print(get_longest_substring_with_k_distinct_characters("abcefg", 1))
print(get_longest_substring_with_k_distinct_characters("aabbcc", 1))
print(get_longest_substring_with_k_distinct_characters("aabbcc", 3))
print(get_longest_substring_with_k_distinct_characters("aaabbb", 3))
