# Problem link - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/
# Solution - https://www.youtube.com/watch?v=xtqN4qlgr8s&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=7


class Solution:
    @staticmethod
    def get_substrings(string):
        """
            Time complexity O(n) and space complexity is O(1).
        """

        # define window variables
        n = len(string)
        left = right = 0

        # make a dictionary to track character count
        d = {"a": 0, "b": 0, "c": 0}

        # count the number of substrings in `count`.
        count = 0

        # while there is ground to cover.
        while right < n:
            # increment d_right.
            d[string[right]] += 1
            # while all 3 characters are available in the window
            while sum(1 for v in d.values() if v > 0) == 3:
                # increment the count
                count += (n - right)
                # and shrink from the left
                d[string[left]] -= 1
                left += 1
            # increment right
            right += 1
        # return the count.
        return count


print(Solution.get_substrings("bbacba"))
print(Solution.get_substrings("abcabc"))
print(Solution.get_substrings("aaacb"))
print(Solution.get_substrings("abc"))