class Solution:
    @staticmethod
    def longest_repeating_character_replacement(string: str, k: int) -> str:
        if k < 0:
            return ""
        left = right = length = 0
        start_index = -1
        n = len(string)
        d = Solution._get_empty_dict(string)
        while right < n:
            curr = string[right]
            d[curr] += 1
            if (right - left + 1) - max(d.values()) > k:
                d[string[left]] -= 1
                left += 1
            if right - left + 1 > length:
                length = right - left + 1
                start_index = left
            right += 1
        if start_index == -1:
            return ""
        return string[start_index: start_index + length]

    @staticmethod
    def _get_empty_dict(string):
        d = {}
        for i in string:
            d[i] = 0
        return d


print(Solution.longest_repeating_character_replacement("AABABBA", 2))
print(Solution.longest_repeating_character_replacement("AABABBA", 1))
print(Solution.longest_repeating_character_replacement("ABAB", 2))
print(Solution.longest_repeating_character_replacement("ADBD", 1))
print(Solution.longest_repeating_character_replacement("ABBA", 2))
print(Solution.longest_repeating_character_replacement("AAABBCCD", 2))
print(Solution.longest_repeating_character_replacement("ABABA", 2))
print(Solution.longest_repeating_character_replacement("HHHHHH", 4))
