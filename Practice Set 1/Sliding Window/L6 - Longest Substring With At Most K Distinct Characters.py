class Solution:
    @staticmethod
    def get_longest_substring(string: str, k: int):
        d = {i: 0 for i in string}
        left, right = 0, 0
        n = len(string)
        longest_length = 0
        start_index = 0
        while right < n:
            d[string[right]] += 1
            if sum(1 for value in d.values() if value != 0) <= k:
                longest_length = max(longest_length, right - left + 1)
                start_index = left
            else:
                d[string[left]] -= 1
                left += 1
            right += 1
        return longest_length, string[start_index:start_index+longest_length]


print(Solution.get_longest_substring("aaabbccd", 2))
print(Solution.get_longest_substring("abbbbbbc", 2))
print(Solution.get_longest_substring("abcddefg", 3))
print(Solution.get_longest_substring("aaaaaaaa", 3))
print(Solution.get_longest_substring("abcefg", 1))
print(Solution.get_longest_substring("aabbcc", 1))
print(Solution.get_longest_substring("aabbcc", 2))
print(Solution.get_longest_substring("aabbcc", 3))
print(Solution.get_longest_substring("aaabbb", 3))