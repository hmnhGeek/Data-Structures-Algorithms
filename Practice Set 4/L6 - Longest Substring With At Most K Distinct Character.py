# Problem link - https://www.naukri.com/code360/problems/distinct-characters_2221410
# Solution - https://www.youtube.com/watch?v=teM9ZsVRQyc&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=6


class Solution:
    @staticmethod
    def get_longest(arr, k):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # edge case
        if k < 0:
            return -1

        # define window variables
        left = right = 0
        n = len(arr)

        # define a tracking dictionary
        d = {i: 0 for i in arr}

        # define result variables
        longest_length = 0
        start_index = -1

        # while there is ground to cover.
        while right < n:
            # increment the right indexed value count.
            d[arr[right]] += 1

            # if there are more than k distinct characters in the window, shrink one unit from left.
            if sum(1 for v in d.values() if v != 0) > k:
                d[arr[left]] -= 1
                left += 1

            # if there are <= k distinct characters in the window, update the result variables.
            if sum(1 for v in d.values() if v != 0) <= k:
                longest_length = max(longest_length, right - left + 1)
                start_index = left

            # increment right index.
            right += 1

        # return the substring with k distinct characters and longest length.
        return arr[start_index:start_index+longest_length] if start_index != -1 else ""


print(Solution.get_longest("aaabbccd", 2))
print(Solution.get_longest("abbbbbbc", 2))
print(Solution.get_longest("abcddefg", 3))
print(Solution.get_longest("aaaaaaaa", 3))
print(Solution.get_longest("abcefg", 1))
print(Solution.get_longest("aabbcc", 1))
print(Solution.get_longest("aabbcc", 2))
print(Solution.get_longest("aabbcc", 3))
print(Solution.get_longest("aaabbb", 3))
