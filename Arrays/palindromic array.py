class Solution:
    @staticmethod
    def _is_palindrome(s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    @staticmethod
    def solve(arr):
        for i in arr:
            if not Solution._is_palindrome(str(i)):
                return False
        return True


print(Solution.solve([111, 222, 333, 444, 555]))
print(Solution.solve([121, 131, 20]))
