# Problem link - https://www.geeksforgeeks.org/problems/longest-palindrome-in-a-string3411/1
# Solution - https://www.youtube.com/watch?v=XYQecbcd6_c


class Solution:
    @staticmethod
    def get_longest_substring(string):
        """
            Time complexity is O(n^2) and space complexity is O(n).
        """

        result = ""
        length = 0

        for i in range(len(string)):
            l, r = i, i
            while 0 <= l < len(string) and 0 <= r < len(string) and string[l] == string[r]:
                if length < r - l + 1:
                    length = r - l + 1
                    result = string[l:r+1]
                l -= 1
                r += 1

            l, r = i, i + 1
            while 0 <= l < len(string) and 0 <= r < len(string) and string[l] == string[r]:
                if length < r - l + 1:
                    length = r - l + 1
                    result = string[l:r+1]
                l -= 1
                r += 1

        return result


print(Solution.get_longest_substring("forgeeksskeegfor"))
print(Solution.get_longest_substring("Geeks"))
print(Solution.get_longest_substring("abc"))
