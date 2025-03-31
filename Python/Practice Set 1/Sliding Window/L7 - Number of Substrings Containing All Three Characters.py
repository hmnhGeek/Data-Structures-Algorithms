# Problem link - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
# Solution - https://www.youtube.com/watch?v=xtqN4qlgr8s&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=7


class Solution:
    @staticmethod
    def contains_all_3(string):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # initialize `n` for the length of the array.
        n = len(string)

        # create window pointers
        left, right = 0, 0

        # create a map to store the counts of each character. This will take O(1) space.
        d = {"a": 0, "b": 0, "c": 0}

        # initialize a count variable to count the substrings.
        count = 0

        # while there is ground to cover.
        while right < n:
            # increment the count of `right` value.
            d[string[right]] += 1

            # if all 3 characters are present from left to right.
            while not any(v == 0 for v in d.values()):
                # the number of such substrings starting at left will be `n - right`.
                count += (n - right)
                # remove one character from front and check the while condition again for the next left.
                d[string[left]] -= 1
                left += 1

            # finally increment right.
            right += 1
        return count


print(Solution.contains_all_3("bbacba"))
print(Solution.contains_all_3("abcabc"))
print(Solution.contains_all_3("aaacb"))
print(Solution.contains_all_3("abc"))
print(Solution.contains_all_3("aabbabab"))