# Problem link - https://www.geeksforgeeks.org/problems/palindrome-string0817/1


class Solution:
    @staticmethod
    def is_palindrome(string: str) -> bool:
        """
            Time complexity is O(n) and space complexity is O(1).
        """
        i, j = 0, len(string) - 1
        while i <= j:
            if string[i] == string[j]:
                i += 1
                j -= 1
            else:
                return False
        return True


print(Solution.is_palindrome("abba"))
print(Solution.is_palindrome("abc"))
print(Solution.is_palindrome("a"))
print(Solution.is_palindrome("acbca"))
