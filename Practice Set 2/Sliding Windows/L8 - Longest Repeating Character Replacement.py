# Problem link - https://www.geeksforgeeks.org/problems/longest-repeating-character-replacement/1
# Solution - https://www.youtube.com/watch?v=_eNhaDCr6P0&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=8


class Solution:
    @staticmethod
    def solution(string, k):
        """
            Overall time complexity is O(n) and space complexity is O(26).
        """

        # define window variables.
        n = len(string)
        left = right = 0
        max_freq = 0

        # define result variables
        start_index = -1
        longest_length = 0
        d = {i: 0 for i in string}

        # while there is ground to cover.
        while right < n:
            # increment the count of right indexed character and update the max freq in O(26) time.
            d[string[right]] += 1
            max_freq = max(d.values())

            # check if the replacement count > k, if it is...
            if (right - left + 1) - max_freq > k:
                # shrink window from left
                d[string[left]] -= 1
                left += 1
                # and update the max frequency.
                max_freq = max(d.values())
            # if replacement count <= k, then update result variables
            if (right - left + 1) - max_freq <= k:
                longest_length = max(longest_length, right - left + 1)
                start_index = left
            # increment right index
            right += 1
        # return the substring.
        return string[start_index:start_index+longest_length] if start_index != -1 else ""


print(Solution.solution("AABABBA", 1))
print(Solution.solution("ABAB", 2))
print(Solution.solution("ADBD", 1))
print(Solution.solution("ABBA", 2))
print(Solution.solution("AAABBCCD", 2))
print(Solution.solution("ABABA", 2))
print(Solution.solution("HHHHHH", 4))