class Solution:
    @staticmethod
    def get_longest_length(string: str):
        left, right = 0, 0
        longest_length = 0
        d = {i: 0 for i in string}
        start_index = 0
        n = len(string)
        while right < n:
            d[string[right]] += 1
            if any(v > 1 for v in d.values()):
                d[string[left]] -= 1
                left += 1
            else:
                longest_length = max(longest_length, right - left + 1)
                start_index = left
            right += 1
        return longest_length, string[start_index:start_index+longest_length]


print(Solution.get_longest_length("cadbzabcd"))
print(Solution.get_longest_length("abcabcbb"))
print(Solution.get_longest_length("bbbbb"))
print(Solution.get_longest_length("pwwkew"))