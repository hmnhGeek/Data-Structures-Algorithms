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
        n = len(s)
        left = right = 0
        d = {i: 0 for i in s}
        req = dict(Counter(t))
        length = 1e6
        start_index = -1
        while right < n:
            d[s[right]] += 1
            while Solution._condition_satisfied(d, req):
                if length > right - left + 1:
                    length = right - left + 1
                    start_index = left
                d[s[left]] -= 1
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
