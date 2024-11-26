class Solution:
    @staticmethod
    def longest_repeating_character_replacement(string, k):
        left = right = 0
        n = len(string)
        longest_length = 0
        start_index = 0
        d = {i: 0 for i in string}
        while right < n:
            d[string[right]] += 1
            if sum(1 for v in d.values() if v != 0) <= 1:
                longest_length = max(longest_length, right - left + 1)
                start_index = left
            elif k > 0:
                min_freq_character = min(d, key=d.get)
                d[min_freq_character] -= 1
                k -= 1
                longest_length = max(longest_length, right - left + 1)
                start_index = left
            else:
                d[string[left]] -= 1
                left += 1
            right += 1
        return longest_length, string[start_index:start_index+longest_length]


print(Solution.longest_repeating_character_replacement("AABABBA", 1))
print(Solution.longest_repeating_character_replacement("ABAB", 2))
print(Solution.longest_repeating_character_replacement("ADBD", 1))
print(Solution.longest_repeating_character_replacement("ABBA", 2))
print(Solution.longest_repeating_character_replacement("AAABBCCD", 2))