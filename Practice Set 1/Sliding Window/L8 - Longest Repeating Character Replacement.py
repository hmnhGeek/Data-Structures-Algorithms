# Problem link - https://leetcode.com/problems/longest-repeating-character-replacement/description/
# Solution - https://www.youtube.com/watch?v=_eNhaDCr6P0&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=8


class Solution:
    @staticmethod
    def longest_repeating_character_replacement(string, k):
        """
            Overall time complexity is O(26*n) and space complexity is O(26).
        """

        # define window variables.
        left = right = 0
        n = len(string)

        # define answer variables.
        longest_length = 0
        start_index = 0

        # define frequency tracking variables.
        max_freq = 0
        d = {i: 0 for i in string}

        # while there is ground to cover.
        while right < n:
            # increment the frequency of the right indexed character.
            d[string[right]] += 1
            # update the max frequency.
            max_freq = max(max_freq, d[string[right]])

            # if current substring length - max freq tells us to replace more than k characters, then we must shrink
            # one unit from the left side in order to maintain the longest length window.
            if right - left + 1 - max_freq > k:
                d[string[left]] -= 1
                left += 1
                # while decrementing, also ensure to update the max frequency in O(26) time. If we just need the length
                # there is no need to do this step. But if we want to print the substring, we must update the frequency.
                max_freq = max(d.values())

            # check again if we can now replace at-most k characters.
            if right - left + 1 - max_freq <= k:
                # if yes, then update the result variables.
                longest_length = max(longest_length, right - left + 1)
                start_index = left

            # ensure to increment `right`.
            right += 1

        # return result variables.
        return longest_length, string[start_index:start_index+longest_length]


print(Solution.longest_repeating_character_replacement("AABABBA", 1))
print(Solution.longest_repeating_character_replacement("ABAB", 2))
print(Solution.longest_repeating_character_replacement("ADBD", 1))
print(Solution.longest_repeating_character_replacement("ABBA", 2))
print(Solution.longest_repeating_character_replacement("AAABBCCD", 2))
print(Solution.longest_repeating_character_replacement("ABABA", 2))
print(Solution.longest_repeating_character_replacement("HHHHHH", 4))