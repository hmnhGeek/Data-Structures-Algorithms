class Solution:
    @staticmethod
    def longest_substring(string: str) -> str:
        left = right = 0
        n = len(string)
        longest_length = 0
        start_index = -1
        d = {i: 0 for i in string}
        while right < n:
            d[string[right]] += 1
            if any(v > 1 for v in d.values()):
                d[string[left]] -= 1
                left += 1
            else:
                longest_length = max(longest_length, right - left + 1)
                start_index = left
            right += 1
        return string[start_index:start_index+longest_length] if start_index != -1 else ""


print(Solution.longest_substring("cadbzabcd"))
print(Solution.longest_substring("abcabcbb"))
print(Solution.longest_substring("bbbbb"))
print(Solution.longest_substring("pwwkew"))