def find_min_chars_to_make_palindrome(string):
    i, j = 0, len(string) - 1
    temp = j
    result = 0

    while i < j:
        if string[i] == string[j]:
            i += 1
            j -= 1
        else:
            result += 1
            i = 0
            j = temp - 1
            temp = j
    return result


print(find_min_chars_to_make_palindrome("aaa"))
print(find_min_chars_to_make_palindrome("abc"))
print(find_min_chars_to_make_palindrome("AACECAAAA"))
print(find_min_chars_to_make_palindrome("abcd"))
print(find_min_chars_to_make_palindrome("dad"))
print(find_min_chars_to_make_palindrome("xxaxxa"))