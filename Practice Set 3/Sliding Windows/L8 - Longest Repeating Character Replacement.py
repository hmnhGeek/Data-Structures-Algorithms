class Solution:
    @staticmethod
    def solve(string, k):
        left = right = 0
        n = len(string)
        longest_length = 0
        start_index = -1
        d = {i: 0 for i in string}
        while right < n:
            d[string[right]] += 1
            if (right - left + 1) - max(d.values()) > k:
                d[string[left]] -= 1
                left += 1
            if (right - left + 1) - max(d.values()) <= k:
                longest_length = max(longest_length, right - left + 1)
                start_index = left
            right += 1
        return string[start_index:start_index+longest_length] if start_index != -1 else ""


print(Solution.solve("AABABBA", 2))
print(Solution.solve("ABAB", 2))
print(Solution.solve("AABABBA", 1))
print(Solution.solve("ADBD", 1))
print(Solution.solve("AAABBCCD", 2))
print(Solution.solve("ABABA", 2))
print(Solution.solve("HHHHHH", 4))
