# Problem link - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Solution - https://www.youtube.com/watch?v=-zSxTJkcdAo&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=3


class Solution:
    @staticmethod
    def get_longest(string):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # define window variables
        n = len(string)
        left = right = 0

        # define tracking dictionary
        d = {i: 0 for i in string}

        # define result variables
        longest_length = 0
        start_index = -1

        # while there is ground to cover.
        while right < n:
            # increment right indexed value count.
            d[string[right]] += 1

            # if any character has freq > 1, there's duplicate; shrink from left.
            if any(v > 1 for v in d.values()):
                d[string[left]] -= 1
                left += 1

            # if all the characters in the window are unique, then update the result variables.
            if all(v <= 1 for v in d.values()):
                longest_length = max(longest_length, right - left + 1)
                start_index = left

            # increment right index.
            right += 1

        # return the substring.
        return string[start_index:start_index+longest_length] if start_index != -1 else ""


print(Solution.get_longest("cadbzabcd"))
print(Solution.get_longest("abcabcbb"))
print(Solution.get_longest("bbbbb"))
print(Solution.get_longest("pwwkew"))
print(Solution.get_longest("ABCBC"))
print(Solution.get_longest("GEEKSFORGEEKS"))
print(Solution.get_longest("mississippi"))
