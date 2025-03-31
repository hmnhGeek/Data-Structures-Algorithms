# Problem link - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
# Solution - https://www.youtube.com/watch?v=xtqN4qlgr8s&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=8


class Solution:
    @staticmethod
    def solve(string):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # define window variables
        n = len(string)
        left = right = 0

        # define a count variable to count valid substrings.
        count = 0

        # define a tracking dictionary
        d = {"a": 0, "b": 0, "c": 0}

        # while there is ground to cover.
        while right < n:
            # increment the right indexed character count.
            d[string[right]] += 1

            # while all 3 characters are present
            while sum(1 for v in d.values() if v != 0) == 3:
                # increment the count
                count += (n - right)
                # shrink one unit from left
                d[string[left]] -= 1
                left += 1

            # increment right index
            right += 1

        # return the count of the substrings
        return count


print(Solution.solve("bbacba"))
print(Solution.solve("abcabc"))
print(Solution.solve("aaacb"))
print(Solution.solve("abc"))
print(Solution.solve("aabbabab"))
