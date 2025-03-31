# Problem link - https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/
# Solution - https://www.youtube.com/watch?v=teM9ZsVRQyc&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=6


class Solution:
    @staticmethod
    def get_longest(s, k):
        """
            Time complexity is O(26n) and space complexity is O(26).
        """

        # define window variables
        n = len(s)
        left = right = 0

        # define result variables
        longest_length = 0
        start_index = -1

        # define a tracking dictionary
        d = {i: 0 for i in s}

        # while there is ground to cover...
        while right < n:
            # increment right index count
            d[s[right]] += 1

            # if more than k distinct characters are present, shrink one unit from left.
            if sum(1 for v in d.values() if v > 0) > k:
                d[s[left]] -= 1
                left += 1

            # else update the result variables
            if sum(1 for v in d.values() if v > 0) <= k:
                longest_length = max(longest_length, right - left + 1)
                start_index = left

            # increment right index
            right += 1

        # return the substring.
        return s[start_index:start_index+longest_length] if start_index != -1 else ""


print(Solution.get_longest("aaabbccd", 2))
print(Solution.get_longest("abbbbbbc", 2))
print(Solution.get_longest("abcddefg", 3))
print(Solution.get_longest("aaaaaaaa", 3))
print(Solution.get_longest("abcefg", 1))
print(Solution.get_longest("aabbcc", 1))
print(Solution.get_longest("aabbcc", 2))
print(Solution.get_longest("aabbcc", 3))
print(Solution.get_longest("aaabbb", 3))
