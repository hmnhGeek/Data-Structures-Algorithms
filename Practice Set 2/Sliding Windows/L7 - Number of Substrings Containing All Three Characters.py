# Problem link - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
# Solution - https://www.youtube.com/watch?v=xtqN4qlgr8s&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=8


class Solution:
    @staticmethod
    def contains_all_three(string):
        """
            Overall time complexity is O(n) and space complexity is O(1).
        """

        # define window variables
        n = len(string)
        left = right = 0

        # define a map to hold character count
        d = {"a": 0, "b": 0, "c": 0}

        # store the number of substrings in count variable.
        count = 0

        # while there is ground to cover.
        while right < n:
            # increment right indexed value count.
            d[string[right]] += 1
            # if all characters are present, update the count
            while all(v > 0 for v in d.values()):
                count += (n - right)
                # continuously shrink from left till every character is present
                d[string[left]] -= 1
                left += 1
            # increment right
            right += 1
        # return count
        return count


print(Solution.contains_all_three("bbacba"))
print(Solution.contains_all_three("abcabc"))
print(Solution.contains_all_three("aaacb"))
print(Solution.contains_all_three("abc"))
print(Solution.contains_all_three("aabbabab"))