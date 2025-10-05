# Problem link - https://leetcode.com/problems/minimum-window-substring/
# Solution - https://www.youtube.com/watch?v=WJaij9ffOIY&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=12


from collections import Counter


class Solution:
    @staticmethod
    def valid_condition(ds, dt):
        for i in dt:
            if ds[i] < dt[i]:
                return False
        return True

    @staticmethod
    def min_window_substring(s, t):
        """
            Time complexity is O(26n) and space complexity is O(26).
        """
        ds, dt = {i: 0 for i in s}, dict(Counter(t))
        n = len(s)
        left = right = 0
        length = n
        start_index = -1
        while right < n:
            ds[s[right]] += 1
            while Solution.valid_condition(ds, dt):
                length = right - left + 1
                start_index = left
                ds[s[left]] -= 1
                left += 1
            right += 1
        return s[start_index:start_index+length] if start_index != -1 else ""


print(Solution.min_window_substring("ddaaabbca", "abc"))
print(Solution.min_window_substring("ADOBECODEBANC", "ABC"))
print(Solution.min_window_substring("a", "a"))
print(Solution.min_window_substring("a", "aa"))
print(Solution.min_window_substring("timetopractice", "toc"))
print(Solution.min_window_substring("zoomlazapzo", "oza"))
print(Solution.min_window_substring("ABBXC", "BXC"))
