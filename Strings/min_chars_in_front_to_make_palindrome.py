def find_min_chars_to_make_palindrome(string):
    # Time complexity is O(N) and space complexity is O(1)

    i, j = 0, len(string) - 1
    temp = j
    result = 0

    while i < j:
        # if the characters at front and at end match, reduce the window size
        if string[i] == string[j]:
            i += 1
            j -= 1
        else:
            # if they don't match, then increase the count of the characters that need to be added.
            result += 1

            # start searching again from front and move j back to the position of temp - 1.
            i = 0
            j = temp - 1

            # update temp value to j
            temp = j
    return result


print(find_min_chars_to_make_palindrome("aaa"))
print(find_min_chars_to_make_palindrome("abc"))
print(find_min_chars_to_make_palindrome("AACECAAAA"))
print(find_min_chars_to_make_palindrome("abcd"))
print(find_min_chars_to_make_palindrome("dad"))
print(find_min_chars_to_make_palindrome("xxaxxa"))