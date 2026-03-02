# Problem link - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
# Solution - https://www.youtube.com/watch?v=xtqN4qlgr8s&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=7


class Solution:
    @staticmethod
    def get_less_than_equal_to(string, k):
        if k < 0:
            return 0
        left = right = 0
        n = len(string)
        d = {"a": 0, "b": 0, "c": 0}
        count = 0
        while right < n:
            d[string[right]] += 1
            while sum(1 for v in d.values() if v > 0) > k:
                d[string[left]] -= 1
                left += 1
            count += (right - left + 1)
            right += 1
        return count

    @staticmethod
    def get_num_substrings(string):
        """
            Time complexity is O(2n) and space complexity is O(1).
        """
        return Solution.get_less_than_equal_to(string, 3) - Solution.get_less_than_equal_to(string, 2)


print(Solution.get_num_substrings("bbacba"))
print(Solution.get_num_substrings("abcabc"))
print(Solution.get_num_substrings("aaacb"))
print(Solution.get_num_substrings("abc"))
print(Solution.get_num_substrings("aabbabab"))
