# Problem link - https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/
# Solution - https://www.youtube.com/watch?v=-zSxTJkcdAo&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=3


class Solution:
    @staticmethod
    def longest_substring(string):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # define a window
        left = right = 0
        n = len(string)

        # define a character tracking dictionary
        d = {i: 0 for i in string}

        # define result variables
        longest_length = 0
        start_index = -1

        # while there is ground to cover.
        while right < n:
            # increment the right index character
            d[string[right]] += 1

            # if there is any character having freq > 1, then shrink only one unit from left.
            if any(v > 1 for v in d.values()):
                d[string[left]] -= 1
                left += 1

            # if all the characters are unique, i.e., there is either 0 freq or 1 freq, update the result variables.
            if all(v <= 1 for v in d.values()):
                longest_length = max(longest_length, right - left + 1)
                start_index = left

            # increment right index.
            right += 1

        # return the longest substring.
        return string[start_index:start_index+longest_length] if start_index != -1 else ""


print(Solution.longest_substring("cadbzabcd"))
print(Solution.longest_substring("abcabcbb"))
print(Solution.longest_substring("bbbbb"))
print(Solution.longest_substring("pwwkew"))
print(Solution.longest_substring("ABCBC"))
print(Solution.longest_substring("GEEKSFORGEEKS"))
