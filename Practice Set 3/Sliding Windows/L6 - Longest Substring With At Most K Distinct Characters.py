# Problem link - https://www.naukri.com/code360/problems/distinct-characters_2221410
# Solution - https://www.youtube.com/watch?v=teM9ZsVRQyc&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=6


class Solution:
    @staticmethod
    def get_longest(string, k):
        """
            Time complexity is O(26n) and space complexity is O(26).
        """

        # define pointers
        left = right = 0

        # define tracking dictionary
        d = {i: 0 for i in string}

        # define result variables
        n = len(string)
        longest_length = 0
        start_index = -1

        # while there is ground to cover.
        while right < n:
            # increment right indexed value
            d[string[right]] += 1
            # check if more than k distinct characters have been used or not, if yes...
            if sum(1 for v in d.values() if v > 0) > k:
                # shrink just 1 unit from left
                d[string[left]] -= 1
                left += 1
            # if no, then update the result variables.
            if sum(1 for v in d.values() if v > 0) <= k:
                if longest_length <= right - left + 1:
                    longest_length = right - left + 1
                    start_index = left
            # increment right
            right += 1

        # although not needed, but complete left pointer also.
        while left < n:
            if sum(1 for v in d.values() if v > 0) <= k:
                if longest_length <= n - left:
                    longest_length = n - left
                    start_index = left
            d[string[left]] -= 1
            left += 1

        # return the longest substring.
        return string[start_index:start_index+longest_length] if start_index != -1 else ""


print(Solution.get_longest("aaabbccd", 2))
print(Solution.get_longest("abbbbbbc", 2))
print(Solution.get_longest("abcddefg", 3))
print(Solution.get_longest("aaaaaaaa", 3))
print(Solution.get_longest("abcefg", 1))
print(Solution.get_longest("aabbcc", 1))
print(Solution.get_longest("aabbcc", 2))
print(Solution.get_longest("aabbcc", 3))
print(Solution.get_longest("aaabbb", 3))