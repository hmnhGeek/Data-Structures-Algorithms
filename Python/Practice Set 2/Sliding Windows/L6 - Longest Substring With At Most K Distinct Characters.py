# Problem link - https://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/
# Solution - https://www.youtube.com/watch?v=teM9ZsVRQyc&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=6


class Solution:
    @staticmethod
    def get_longest(string, k):
        """
            Time complexity is O(n) and space complexity is O(1). The explanation is exactly same as L5's explanation.
        """

        if k <= 0:
            return
        left = right = 0
        n = len(string)
        longest_length = 0
        start_index = -1
        d = {i: 0 for i in string}
        while right < n:
            d[string[right]] += 1
            if sum(1 for v in d.values() if v != 0) > k:
                d[string[left]] -= 1
                left += 1
            if sum(1 for v in d.values() if v != 0) <= k:
                longest_length = max(longest_length, right - left + 1)
                start_index = left
            right += 1
        return string[start_index:start_index+longest_length]


print(Solution.get_longest("aaabbccd", 2))
print(Solution.get_longest("abbbbbbc", 2))
print(Solution.get_longest("abcddefg", 3))
print(Solution.get_longest("aaaaaaaa", 3))
print(Solution.get_longest("abcefg", 1))
print(Solution.get_longest("aabbcc", 1))
print(Solution.get_longest("aabbcc", 2))
print(Solution.get_longest("aabbcc", 3))
print(Solution.get_longest("aaabbb", 3))