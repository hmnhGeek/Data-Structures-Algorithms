class Solution:
    @staticmethod
    def solution(string, k):
        n = len(string)
        left = right = 0
        max_freq = 0
        start_index = -1
        longest_length = 0
        d = {i: 0 for i in string}
        while right < n:
            d[string[right]] += 1
            max_freq = max(d.values())
            if (right - left + 1) - max_freq > k:
                d[string[left]] -= 1
                left += 1
                max_freq = max(d.values())
            if (right - left + 1) - max_freq <= k:
                longest_length = max(longest_length, right - left + 1)
                start_index = left
            right += 1
        return string[start_index:start_index+longest_length] if start_index != -1 else ""


print(Solution.solution("AABABBA", 1))
print(Solution.solution("ABAB", 2))
print(Solution.solution("ADBD", 1))
print(Solution.solution("ABBA", 2))
print(Solution.solution("AAABBCCD", 2))
print(Solution.solution("ABABA", 2))
print(Solution.solution("HHHHHH", 4))