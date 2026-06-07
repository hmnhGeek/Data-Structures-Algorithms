# Problem link - https://leetcode.com/problems/minimum-window-substring/
# Solution - https://www.youtube.com/watch?v=WJaij9ffOIY&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=12


from collections import Counter


class Solution:
    @staticmethod
    def min_window_substring(string, pattern):
        """
            Time complexity is O(26n) and space complexity is O(26).
        """
        t = dict(Counter(pattern))
        d = {i: 0 for i in string}
        left = right = 0
        n = len(string)
        length, start_index = n, -1
        while right < n:
            d[string[right]] += 1
            while Solution._all_chars_available(d, t):
                start_index = left
                length = min(length, right - left + 1)
                d[string[left]] -= 1
                left += 1
            right += 1
        if start_index != -1:
            return string[start_index:start_index+length]
        return ""

    @staticmethod
    def _all_chars_available(d, t):
        for character in t:
            if d[character] < t[character]:
                return False
        return True


print(Solution.min_window_substring("ddaaabbca", "abc"))
print(Solution.min_window_substring("ADOBECODEBANC", "ABC"))
print(Solution.min_window_substring("a", "a"))
print(Solution.min_window_substring("a", "aa"))
print(Solution.min_window_substring("timetopractice", "toc"))
print(Solution.min_window_substring("zoomlazapzo", "oza"))
print(Solution.min_window_substring("ABBXC", "BXC"))
