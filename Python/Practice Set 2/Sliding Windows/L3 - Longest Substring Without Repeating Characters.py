# Problem link - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Solution - https://www.youtube.com/watch?v=-zSxTJkcdAo&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=3


class Solution:
    @staticmethod
    def longest_substring(string: str) -> str:
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # define window variables
        left = right = 0
        n = len(string)

        # store result variables.
        longest_length = 0
        start_index = -1

        # define a map to track character counts.
        d = {i: 0 for i in string}

        # while there is ground to cover.
        while right < n:
            # increment the count of right indexed character.
            d[string[right]] += 1

            # if there is any character whose freq > 1, shrink 1 unit from left.
            if any(v > 1 for v in d.values()):
                d[string[left]] -= 1
                left += 1
            else:
                # else update the results.
                longest_length = max(longest_length, right - left + 1)
                start_index = left

            # increment right
            right += 1

        # return the result if start index is not -1.
        return string[start_index:start_index+longest_length] if start_index != -1 else ""


print(Solution.longest_substring("cadbzabcd"))
print(Solution.longest_substring("abcabcbb"))
print(Solution.longest_substring("bbbbb"))
print(Solution.longest_substring("pwwkew"))
print(Solution.longest_substring("ABCBC"))
print(Solution.longest_substring("GEEKSFORGEEKS"))
print(Solution.longest_substring("mississippi"))
