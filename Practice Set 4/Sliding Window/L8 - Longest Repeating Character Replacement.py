# Problem link - https://leetcode.com/problems/longest-repeating-character-replacement/
# Solution - https://www.youtube.com/watch?v=_eNhaDCr6P0&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=8


class Solution:
    @staticmethod
    def longest_repeating_character_replacement(string, k):
        """
            Time complexity is O(n) and space complexity is O(26).
        """

        # if k is negative, return a blank string.
        if k < 0:
            return ""

        # define window variables
        left = right = 0
        n = len(string)

        # define a tracking dictionary
        d = {i: 0 for i in string}

        # define result variables.
        longest_length = 0
        start_index = -1

        # while there is ground to cover.
        while right < n:
            # increment the right indexed character count
            d[string[right]] += 1

            # if the replacement count is more than k, shrink one unit from left.
            if (right - left + 1) - max(d.values()) > k:
                d[string[left]] -= 1
                left += 1

            # if replacement count is within k, update the result variables.
            if (right - left + 1) - max(d.values()) <= k:
                longest_length = max(longest_length, right - left + 1)
                start_index = left

            # increment right index.
            right += 1

        # return the longest substring.
        return string[start_index:start_index+longest_length] if start_index != -1 else ""


print(Solution.longest_repeating_character_replacement("AABABBA", 1))
print(Solution.longest_repeating_character_replacement("ABAB", 2))
print(Solution.longest_repeating_character_replacement("ADBD", 1))
print(Solution.longest_repeating_character_replacement("ABBA", 2))
print(Solution.longest_repeating_character_replacement("AAABBCCD", 2))
print(Solution.longest_repeating_character_replacement("ABABA", 2))
print(Solution.longest_repeating_character_replacement("HHHHHH", 4))