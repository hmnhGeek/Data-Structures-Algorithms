def get_longest_substring_with_k_distinct_characters(string, k):
    n = len(string)
    left = right = 0
    max_length = 1
    last_indices = dict()
    characters_used = set()

    for character in string:
        last_indices[character] = None

    while right < n:
        character = string[right]
        last_indices[character] = right
        characters_used.add(character)

        if len(characters_used) > k:
            character_to_remove = string[left]
            left = last_indices[character_to_remove] + 1
            characters_used.remove(character_to_remove)

        max_length = max(max_length, right - left + 1)
        right += 1

    return max_length


print(get_longest_substring_with_k_distinct_characters("aaabbccd", 2))
print(get_longest_substring_with_k_distinct_characters("abbbbbbc", 2))
print(get_longest_substring_with_k_distinct_characters("abcddefg", 3))
print(get_longest_substring_with_k_distinct_characters("aaaaaaaa", 3))
print(get_longest_substring_with_k_distinct_characters("abcefg", 1))
print(get_longest_substring_with_k_distinct_characters("aabbcc", 1))
print(get_longest_substring_with_k_distinct_characters("aabbcc", 3))
print(get_longest_substring_with_k_distinct_characters("aaabbb", 3))
