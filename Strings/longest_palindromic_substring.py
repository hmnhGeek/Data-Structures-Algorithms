# Problem link - https://www.geeksforgeeks.org/problems/longest-palindrome-in-a-string3411/1
# Solution - https://www.youtube.com/watch?v=XYQecbcd6_c&t=348s
# Solution - https://www.youtube.com/watch?v=n_kL8BkURVA


def recursive():
    """
        Time complexity is exponential and space is O(n).
    """
    def solve(string, i, j):
        if i >= j:
            return True
        if string[i] == string[j]:
            return solve(string, i + 1, j - 1)
        else:
            return False

    def get_longest_palindromic_substring(string: str):
        start = 0
        length = 0
        n = len(string)
        for i in range(n):
            for j in range(i, n):
                if solve(string, i, j) and j - i + 1 > length:
                    start = i
                    length = j - i + 1
        return string[start:start+length]

    print(get_longest_palindromic_substring("aaaabbaa"))
    print(get_longest_palindromic_substring("abc"))
    print(get_longest_palindromic_substring("abacdfgdcaba"))


def memoized():
    """
        Time complexity is O(n^4) and space is O(n + n^2)
    """
    def solve(string, i, j, dp):
        if i >= j:
            return True

        if dp[i][j] is not None:
            return dp[i][j]

        if string[i] == string[j]:
            dp[i][j] = solve(string, i + 1, j - 1, dp)
        else:
            dp[i][j] = False
        return dp[i][j]

    def get_longest_palindromic_substring(string: str):
        start = 0
        length = 0
        n = len(string)
        dp = {i: {j: None for j in range(n)} for i in range(n)}
        for i in range(n):
            for j in range(i, n):
                if solve(string, i, j, dp) and j - i + 1 > length:
                    start = i
                    length = j - i + 1
        return string[start:start+length]

    print(get_longest_palindromic_substring("aaaabbaa"))
    print(get_longest_palindromic_substring("abc"))
    print(get_longest_palindromic_substring("abacdfgdcaba"))


recursive()
print()
memoized()
print()


class Solution:
    @staticmethod
    def longest_palindromic_substring(string):
        """
            Worst case time complexity is O(n^2) and space complexity is O(1).
        """
        result, length = "", 0
        n = len(string)

        # loop on each character of the string.
        for i in range(n):
            # assuming this character to be the center, expand outwards and search for the maximum possible palindromic
            # substring and update the results. Do this for both odd and even length strings.

            # ODD CASE
            left, right = i, i
            while left >= 0 and right < n and string[left] == string[right]:
                if right - left + 1 > length:
                    result = string[left:right+1]
                    length = right - left + 1
                left -= 1
                right += 1

            # EVEN CASE
            left, right = i, i + 1
            while left >= 0 and right < n and string[left] == string[right]:
                if right - left + 1 > length:
                    result = string[left:right+1]
                    length = right - left + 1
                left -= 1
                right += 1

        return result


print(Solution.longest_palindromic_substring("aaaabbaa"))
print(Solution.longest_palindromic_substring("abc"))
print(Solution.longest_palindromic_substring("abacdfgdcaba"))