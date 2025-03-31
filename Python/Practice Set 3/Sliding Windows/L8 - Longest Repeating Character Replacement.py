# Problem link - https://www.geeksforgeeks.org/problems/longest-repeating-character-replacement/1
# Solution - https://www.youtube.com/watch?v=_eNhaDCr6P0&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=8


class Solution:
    @staticmethod
    def solve(string, k):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # define window variables
        left = right = 0
        n = len(string)

        # define result variables
        longest_length = 0
        start_index = -1

        # define tracking dictionary
        d = {i: 0 for i in string}

        # while there is ground to cover
        while right < n:
            # increment the right indexed value
            d[string[right]] += 1
            # if the replacement count is greater than k
            if (right - left + 1) - max(d.values()) > k:
                # decrement only one unit from left
                d[string[left]] -= 1
                left += 1
            # if the replacement count is within k, update the result variables
            if (right - left + 1) - max(d.values()) <= k:
                longest_length = max(longest_length, right - left + 1)
                start_index = left
            # increment the right index
            right += 1
        # return the substring
        return string[start_index:start_index+longest_length] if start_index != -1 else ""


print(Solution.solve("AABABBA", 2))
print(Solution.solve("ABAB", 2))
print(Solution.solve("AABABBA", 1))
print(Solution.solve("ADBD", 1))
print(Solution.solve("AAABBCCD", 2))
print(Solution.solve("ABABA", 2))
print(Solution.solve("HHHHHH", 4))
