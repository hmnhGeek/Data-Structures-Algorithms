from collections import Counter


class Solution:
    @staticmethod
    def _check(d, req):
        for i in req:
            if d[i] < req[i]:
                return False
        return True

    @staticmethod
    def min_window_substring(string, substring):
        n = len(string)
        left = right = 0

        d = {i: 0 for i in string}
        req = dict(Counter(substring))

        min_length = 1e6
        start_index = -1

        while right < n:
            d[string[right]] += 1
            while Solution._check(d, req):
                if min_length > right - left + 1:
                    min_length = min(min_length, right - left + 1)
                    start_index = left
                d[string[left]] -= 1
                left += 1
            right += 1
        while Solution._check(d, req):
            if min_length > right - left + 1:
                min_length = min(min_length, right - left + 1)
                start_index = left
            d[string[left]] -= 1
            left += 1
        return string[start_index:start_index+min_length] if start_index != -1 else ""


print(Solution.min_window_substring("ddaaabbca", "abc"))
print(Solution.min_window_substring("ADOBECODEBANC", "ABC"))
print(Solution.min_window_substring("a", "a"))
print(Solution.min_window_substring("a", "aa"))
print(Solution.min_window_substring("timetopractice", "toc"))
print(Solution.min_window_substring("zoomlazapzo", "oza"))
print(Solution.min_window_substring("ABBXC", "BXC"))