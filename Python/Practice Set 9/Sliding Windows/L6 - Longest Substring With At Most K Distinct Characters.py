# Problem link - https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/
# Solution - https://www.youtube.com/watch?v=teM9ZsVRQyc&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=6


class Solution:
    @staticmethod
    def get_longest_substring(string, k):
        """
            Time complexity is O(26n) and space complexity is O(26).
        """
        if k <= 0:
            return
        d = {i: 0 for i in string}
        left = right = 0
        n = len(string)
        longest_length = 0
        start_index = -1
        while right < n:
            d[string[right]] += 1
            if sum(1 for v in d.values() if v > 0) > k:
                d[string[left]] -= 1
                left += 1
            if right - left + 1 > longest_length:
                longest_length = right - left + 1
                start_index = left
            right += 1
        if start_index == -1:
            return []
        return string[start_index:start_index+longest_length]


print(Solution.get_longest_substring("aaabbccd", 2))
print(Solution.get_longest_substring("abbbbbbc", 2))
print(Solution.get_longest_substring("abcddefg", 3))
print(Solution.get_longest_substring("aaaaaaaa", 3))
print(Solution.get_longest_substring("abcefg", 1))
print(Solution.get_longest_substring("aabbcc", 1))
print(Solution.get_longest_substring("aabbcc", 2))
print(Solution.get_longest_substring("aabbcc", 3))
print(Solution.get_longest_substring("aaabbb", 3))
