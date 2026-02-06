class Solution:
    @staticmethod
    def get_longest_substring(string, k):
        if k <= 0:
            return -1
        left = right = 0
        n = len(string)
        start_index = -1
        length = 0
        d = {i: 0 for i in string}
        while right < n:
            d[string[right]] += 1
            if sum(1 for v in d.values() if v > 0) > k:
                d[string[left]] -= 1
                left += 1
            if right - left + 1 > length:
                length = right - left + 1
                start_index = left
            right += 1
        if start_index != -1:
            return string[start_index:start_index+length]
        return ""


print(Solution.get_longest_substring("aaabbccd", 2))
print(Solution.get_longest_substring("abbbbbbc", 2))
print(Solution.get_longest_substring("abcddefg", 3))
print(Solution.get_longest_substring("aaaaaaaa", 3))
print(Solution.get_longest_substring("abcefg", 1))
print(Solution.get_longest_substring("aabbcc", 1))
print(Solution.get_longest_substring("aabbcc", 2))
print(Solution.get_longest_substring("aabbcc", 3))
print(Solution.get_longest_substring("aaabbb", 3))
