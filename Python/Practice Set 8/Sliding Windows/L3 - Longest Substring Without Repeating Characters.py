# Problem link - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Solution - https://www.youtube.com/watch?v=-zSxTJkcdAo&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=3


class Solution:
    @staticmethod
    def get_longest(string):
        """
            Time complexity is O(26n) and space complexity is O(26).
        """
        n = len(string)
        left = right = 0
        length = 0
        start_index = -1
        d = {i: 0 for i in string}
        while right < n:
            d[string[right]] += 1
            if any(v > 1 for v in d.values()):
                d[string[left]] -= 1
                left += 1
            if length < right - left + 1:
                length = right - left + 1
                start_index = left
            right += 1
        if start_index != -1:
            return string[start_index : start_index + length]
        return ""


print(Solution.get_longest("cadbzabcd"))
print(Solution.get_longest("abcabcbb"))
print(Solution.get_longest("bbbbb"))
print(Solution.get_longest("pwwkew"))
print(Solution.get_longest("ABCBC"))
print(Solution.get_longest("GEEKSFORGEEKS"))
print(Solution.get_longest("mississippi"))