class Solution:
    @staticmethod
    def longest_repeating_character_replacement(string, k):
        n = len(string)
        left = right = 0
        d = {i: 0 for i in string}
        longest_length = 0
        start_index = -1
        while right < n:
            d[string[right]] += 1
            if sum(d.values()) - max(d.values()) > k:
                d[string[left]] -= 1
                left += 1
            if sum(d.values()) - max(d.values()) <= k:
                longest_length = max(longest_length, right - left + 1)
                start_index = left
            right += 1
        return string[start_index:start_index+longest_length] if start_index != -1 else ""


print(Solution.longest_repeating_character_replacement("AABABBA", 2))
print(Solution.longest_repeating_character_replacement("AABABBA", 1))
print(Solution.longest_repeating_character_replacement("ABAB", 2))
print(Solution.longest_repeating_character_replacement("ADBD", 1))
print(Solution.longest_repeating_character_replacement("ABBA", 2))
print(Solution.longest_repeating_character_replacement("AAABBCCD", 2))
print(Solution.longest_repeating_character_replacement("ABABA", 2))
print(Solution.longest_repeating_character_replacement("HHHHHH", 4))