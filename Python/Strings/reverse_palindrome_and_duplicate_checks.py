# Problem link 1 - https://leetcode.com/problems/reverse-string/description/
# Problem link 2 - https://www.geeksforgeeks.org/problems/palindrome-string0817/1
# Problem link 3 - https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/


class StringUtility:
    @staticmethod
    def reverse(string: str) -> str:
        # Time complexity is O(n) and space complexity is O(n).
        result = ""
        for i in range(-1, -len(string) - 1, -1):
            result += string[i]
        return result

    @staticmethod
    def is_palindrome(string: str) -> bool:
        # Time complexity is O(n) and space complexity is O(1).
        i, j = 0, len(string) - 1
        while i < j:
            if string[i] == string[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    @staticmethod
    def find_duplicates(string: str) -> str:
        # Time complexity is O(n) and space complexity is O(k) where k is the count of distinct characters in string.
        hash_map = {i: 0 for i in string}
        for i in string:
            hash_map[i] += 1
        result = ""
        for i in hash_map:
            if hash_map[i] > 1:
                result += i
        return result


# Reverse
print(StringUtility.reverse("hello"))
print(StringUtility.reverse("Hannah"))

# Palindrome check
print(StringUtility.is_palindrome("abba"))
print(StringUtility.is_palindrome("abc"))

# Duplicates
print(StringUtility.find_duplicates("geeksforgeeks"))