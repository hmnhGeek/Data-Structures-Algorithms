class Solution:
    @staticmethod
    def get_longest(s, k):
        n = len(s)
        left = right = 0
        longest_length = 0
        start_index = -1
        d = {i: 0 for i in s}
        while right < n:
            d[s[right]] += 1
            if sum(1 for v in d.values() if v > 0) > k:
                d[s[left]] -= 1
                left += 1
            if sum(1 for v in d.values() if v > 0) <= k:
                longest_length = max(longest_length, right - left + 1)
                start_index = left
            right += 1
        return s[start_index:start_index+longest_length] if start_index != -1 else ""


print(Solution.get_longest("aaabbccd", 2))
print(Solution.get_longest("abbbbbbc", 2))
print(Solution.get_longest("abcddefg", 3))
print(Solution.get_longest("aaaaaaaa", 3))
print(Solution.get_longest("abcefg", 1))
print(Solution.get_longest("aabbcc", 1))
print(Solution.get_longest("aabbcc", 2))
print(Solution.get_longest("aabbcc", 3))
print(Solution.get_longest("aaabbb", 3))
