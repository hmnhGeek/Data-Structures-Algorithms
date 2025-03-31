# Problem link - https://www.naukri.com/code360/problems/longest-substring-without-repeating-characters_758894
# Solution - https://www.youtube.com/watch?v=-zSxTJkcdAo&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=3


def get_longest_substring_with_unique_characters(string):
    """
        The time complexity is O(n) and space complexity is O(n) for the dictionary.
    """

    # create a dictionary to store the last index where a character was found.
    last_character_sighting = dict()

    # store left and right pointers for maintaining the sliding window.
    left, right = 0, 0

    # store the max length of the window. To start with, make it 1 because left = right = 0.
    max_length_obtained = 1

    # store the substring indices of the longest substring
    longest_substring_start_index = 0
    longest_substring_end_index = 0

    # store the length of the string
    string_length = len(string)

    # while the right pointer is within the array bounds
    while right < string_length:
        # if the `right` character is not yet encountered
        if string[right] not in last_character_sighting:
            # assign its last index in the dictionary and move right by one index;
            # i.e., expand the window size.
            last_character_sighting[string[right]] = right
            right += 1
        else:
            # else if the `right` character was encountered previously, get the
            # last index at which it was found.
            last_sighting_index = last_character_sighting[string[right]]

            # if the last index is outside the window (before the left boundary),
            # we need not worry, i.e., we can simply update the last index in the
            # dictionary to `right` and move right by one index, basically, consider
            # this character in our substring.
            if last_sighting_index < left:
                last_character_sighting[string[right]] = right
                right += 1
            else:
                # however, if the `right` character is already in the window previously,
                # that is, it's last index >= left boundary, we must shrink the window
                # from left by moving left to just-next index of the last sighting index.
                left = last_sighting_index + 1

        # now, if the new window size is larger than the current window size stored globally,
        # update the max window size and also update the indices of the window as the longest
        # substring indices. Also, note that `right` pointer is 1 index ahead of actual substring
        # last index. Why? Because whenever a character is placed in the window, right moves by
        # 1 to the right, therefore, the actual substring is string[left:right] and not
        # string[left:right+1].
        if right - left + 1 > max_length_obtained:
            max_length_obtained = right - left + 1
            longest_substring_start_index = left
            longest_substring_end_index = right

    # return the longest substring.
    return string[longest_substring_start_index:longest_substring_end_index]


print(get_longest_substring_with_unique_characters("abcabcbb"))
print(get_longest_substring_with_unique_characters("bbbbb"))
print(get_longest_substring_with_unique_characters("pwwkew"))
print(get_longest_substring_with_unique_characters("GEEKSFORGEEKS"))
print(get_longest_substring_with_unique_characters("xyxyz"))
print(get_longest_substring_with_unique_characters("mississippi"))