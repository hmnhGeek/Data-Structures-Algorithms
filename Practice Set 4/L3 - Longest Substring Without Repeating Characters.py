class Solution:
    @staticmethod
    def longest_substring(string):
        left = right = 0
        n = len(string)
        d = {i: 0 for i in string}
        longest_length = 0
        start_index = -1
        while right < n:
            d[string[right]] += 1
            if any(v > 1 for v in d.values()):
                d[string[left]] -= 1
                left += 1
            if all(v <= 1 for v in d.values()):
                longest_length = max(longest_length, right - left + 1)
                start_index = left
            right += 1
        return string[start_index:start_index+longest_length] if start_index != -1 else ""


print(Solution.longest_substring("cadbzabcd"))
print(Solution.longest_substring("abcabcbb"))
print(Solution.longest_substring("bbbbb"))
print(Solution.longest_substring("pwwkew"))
print(Solution.longest_substring("ABCBC"))
print(Solution.longest_substring("GEEKSFORGEEKS"))
