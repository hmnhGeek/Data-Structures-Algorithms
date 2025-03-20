# Problem link - https://leetcode.com/problems/minimum-window-substring/
# Solution - https://www.youtube.com/watch?v=WJaij9ffOIY&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=12


from collections import Counter


class Solution:
    @staticmethod
    def _condition_satisfied(d, req):
        for i in req:
            if d[i] < req[i]:
                return False
        return True

    @staticmethod
    def min_window_substring(s, t):
        """
            Time complexity is O(26n) and space complexity is O(26).
        """

        # define window variables
        n = len(s)
        left = right = 0

        # define tracking variables
        d = {i: 0 for i in s}
        req = dict(Counter(t))

        # define result variables
        length = 1e6
        start_index = -1

        # while there is ground to cover...
        while right < n:
            # increment the right indexed value.
            d[s[right]] += 1

            # while the condition is satisfied, i.e., all elements of t are present in s, continuously shrink from left.
            while Solution._condition_satisfied(d, req):
                if length > right - left + 1:
                    length = right - left + 1
                    start_index = left
                d[s[left]] -= 1
                left += 1

            # increment right index
            right += 1

        # return the substring.
        return s[start_index:start_index+length] if start_index != -1 else ""


print(Solution.min_window_substring("ddaaabbca", "abc"))
print(Solution.min_window_substring("ADOBECODEBANC", "ABC"))
print(Solution.min_window_substring("a", "a"))
print(Solution.min_window_substring("a", "aa"))
print(Solution.min_window_substring("timetopractice", "toc"))
print(Solution.min_window_substring("zoomlazapzo", "oza"))
print(Solution.min_window_substring("ABBXC", "BXC"))
