class Solution:
    @staticmethod
    def get_longest_substring(string, k):
        n = len(string)
        left = right = 0
        d = {i: 0 for i in string}
        longest_length = 0
        start_index = -1
        while right < n:
            d[string[right]] += 1
            if sum(1 for v in d.values() if v > 0) > k:
                d[string[left]] -= 1
                left += 1
            if sum(1 for v in d.values() if v > 0) <= k:
                longest_length = max(longest_length, right - left + 1)
                start_index = left
            right += 1
        return string[start_index:start_index+longest_length] if start_index != -1 else ""


print(Solution.get_longest_substring("aaabbccd", 2))