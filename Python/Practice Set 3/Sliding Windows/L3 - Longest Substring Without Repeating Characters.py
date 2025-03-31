# Problem link - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Solution - https://www.youtube.com/watch?v=-zSxTJkcdAo&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=3


class Solution:
    @staticmethod
    def longest_all(string):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # define window variables
        n = len(string)
        left = right = 0

        # define a tracker dictionary
        d = {i: 0 for i in string}

        # define result variables
        longest_length, start_index = 0, -1

        # while there is ground to cover
        while right < n:
            # increment the count of right indexed character
            d[string[right]] += 1

            # if there are any duplicates in the window, keep the max window and decrement a unit size from left side.
            if any(v > 1 for v in d.values()):
                d[string[left]] -= 1
                left += 1

            # if all characters either don't appear or appear only once, update the max length
            if all(v <= 1 for v in d.values()):
                longest_length = max(longest_length, right - left + 1)
                start_index = left

            # increment the right pointer
            right += 1

        # return the valid substring.
        return string[start_index:start_index+longest_length] if start_index != -1 else ""


print(Solution.longest_all("cadbzabcd"))
print(Solution.longest_all("abcabcbb"))
print(Solution.longest_all("bbbbb"))
print(Solution.longest_all("pwwkew"))
print(Solution.longest_all("ABCBC"))
print(Solution.longest_all("GEEKSFORGEEKS"))
print(Solution.longest_all("xyxyz"))
