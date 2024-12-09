# Problem link - https://leetcode.com/problems/minimum-window-substring/
# Solution - https://www.youtube.com/watch?v=WJaij9ffOIY&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=12


from collections import Counter


class Solution:
    @staticmethod
    def _satisfied(d, r):
        """
            T: O(26) and S: O(26).
        """
        for i in r:
            # if at any point count of characters in string < required count, return false
            if d[i] < r[i]:
                return False
        # return true if everything is fine.
        return True

    @staticmethod
    def min_window_substring(string, req):
        """
            T: O(26n) and S: O(26).
        """

        # define dictionaries for string and required string.
        d = {i: 0 for i in string}
        r = dict(Counter(req))

        # define window variables
        left = right = 0
        n = len(string)

        # define result variables
        start_index = -1
        min_length = 1e6

        # while there is ground to cover.
        while right < n:
            # increment the count of the right.
            d[string[right]] += 1

            # and while the window contains all the characters from required string, update min length and continuously
            # shrink from the left side.
            while Solution._satisfied(d, r):
                min_length = min(min_length, right - left + 1)
                start_index = left
                d[string[left]] -= 1
                left += 1

            # finally increment from the right side.
            right += 1

        # at the end also, it is possible that we can achieve even shorter length window.
        while Solution._satisfied(d, r):
            min_length = min(min_length, right - left + 1)
            start_index = left
            d[string[left]] -= 1
            left += 1

        # return the min window substring.
        return string[start_index:start_index+min_length] if start_index != -1 else ""


print(Solution.min_window_substring("ddaaabbca", "abc"))
print(Solution.min_window_substring("ADOBECODEBANC", "ABC"))
print(Solution.min_window_substring("a", "a"))
print(Solution.min_window_substring("a", "aa"))
print(Solution.min_window_substring("timetopractice", "toc"))
print(Solution.min_window_substring("zoomlazapzo", "oza"))
print(Solution.min_window_substring("ABBXC", "BXC"))
