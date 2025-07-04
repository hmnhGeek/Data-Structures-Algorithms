# Problem link - https://leetcode.com/problems/longest-repeating-character-replacement/description/
# Solution - https://www.youtube.com/watch?v=_eNhaDCr6P0&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=8


class Solution:
    @staticmethod
    def longest_repeating_character_replacement(string, k):
        """
            Time complexity is O(n) and space complexity is O(26).
        """

        # define window variables
        n = len(string)
        left = right = 0

        # define tracking variables
        d = {i: 0 for i in string}

        # define result variables
        longest_length = 0
        start_index = -1

        # while there is ground to cover...
        while right < n:
            # increment the right index value
            d[string[right]] += 1

            # if more than k character replacement is required, shrink one unit from left.
            if sum(d.values()) - max(d.values()) > k:
                d[string[left]] -= 1
                left += 1

            # else update the result variables.
            if sum(d.values()) - max(d.values()) <= k:
                longest_length = max(longest_length, right - left + 1)
                start_index = left

            # increment the right index
            right += 1

        # return the substring.
        return string[start_index:start_index+longest_length] if start_index != -1 else ""


print(Solution.longest_repeating_character_replacement("AABABBA", 2))
print(Solution.longest_repeating_character_replacement("AABABBA", 1))
print(Solution.longest_repeating_character_replacement("ABAB", 2))
print(Solution.longest_repeating_character_replacement("ADBD", 1))
print(Solution.longest_repeating_character_replacement("ABBA", 2))
print(Solution.longest_repeating_character_replacement("AAABBCCD", 2))
print(Solution.longest_repeating_character_replacement("ABABA", 2))
print(Solution.longest_repeating_character_replacement("HHHHHH", 4))
