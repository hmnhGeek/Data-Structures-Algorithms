def get_longest_substring_with_unique_characters(string):
    last_character_sighting = dict()
    left, right = 0, 0
    max_length_obtained = 0
    longest_substring_start_index = 0
    longest_substring_end_index = 0
    string_length = len(string)

    while right < string_length:
        if string[right] not in last_character_sighting:
            last_character_sighting[string[right]] = right
            right += 1
        else:
            last_sighting_index = last_character_sighting[string[right]]
            if last_sighting_index < left:
                last_character_sighting[string[right]] = right
                right += 1
            else:
                left += 1
        if right - left + 1 > max_length_obtained:
            max_length_obtained = right - left + 1
            longest_substring_start_index = left
            longest_substring_end_index = right

    return string[longest_substring_start_index:longest_substring_end_index]


print(get_longest_substring_with_unique_characters("abcabcbb"))
print(get_longest_substring_with_unique_characters("bbbbb"))
print(get_longest_substring_with_unique_characters("pwwkew"))
print(get_longest_substring_with_unique_characters("GEEKSFORGEEKS"))
print(get_longest_substring_with_unique_characters("xyxyz"))