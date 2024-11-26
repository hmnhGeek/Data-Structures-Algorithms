class Solution:
    @staticmethod
    def longest_repeating_character_replacement(string, k):
        left = right = 0
        n = len(string)
        longest_length = 0
        start_index = 0
        max_freq = 0
        d = {i: 0 for i in string}
        while right < n:
            d[string[right]] += 1
            max_freq = max(max_freq, d[string[right]])
            if right - left + 1 - max_freq > k:
                d[string[left]] -= 1
                left += 1
                max_freq = max(d.values())
            if right - left + 1 - max_freq <= k:
                longest_length = max(longest_length, right - left + 1)
                start_index = left
            right += 1
        return longest_length, string[start_index:start_index+longest_length]


print(Solution.longest_repeating_character_replacement("AABABBA", 1))
print(Solution.longest_repeating_character_replacement("ABAB", 2))
print(Solution.longest_repeating_character_replacement("ADBD", 1))
print(Solution.longest_repeating_character_replacement("ABBA", 2))
print(Solution.longest_repeating_character_replacement("AAABBCCD", 2))
print(Solution.longest_repeating_character_replacement("ABABA", 2))
print(Solution.longest_repeating_character_replacement("HHHHHH", 4))