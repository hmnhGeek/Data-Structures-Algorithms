from collections import Counter


class Solution:
    @staticmethod
    def _window_is_valid(required, given):
        for i in required:
            if given[i] < required[i]:
                return False
        return True


    @staticmethod
    def minimum_window(string: str, t: str) -> str:
        t_counter = dict(Counter(t))
        tracker = {i: 0 for i in string}
        left = right = 0
        n = len(string)
        min_length = 1e6
        start_index = 0
        while right < n:
            tracker[string[right]] += 1
            while Solution._window_is_valid(t_counter, tracker):
                min_length = min(min_length, right - left + 1)
                start_index = left
                tracker[string[left]] -= 1
                left += 1
            right += 1

        while Solution._window_is_valid(t_counter, tracker):
            min_length = min(min_length, right - left + 1)
            start_index = left
            tracker[string[left]] -= 1
            left += 1

        return string[start_index:start_index+min_length] if min_length != 1e6 else ""


print(Solution.minimum_window("ddaaabbca", "abc"))
print(Solution.minimum_window("timetopractice", "toc"))
print(Solution.minimum_window("zoomlazapzo", "oza"))
print(Solution.minimum_window("ADOBECODEBANC", "ABC"))
print(Solution.minimum_window("a", "a"))
print(Solution.minimum_window("a", "aa"))
print(Solution.minimum_window("ABBXC", "BXC"))
