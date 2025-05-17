# Problem link - https://leetcode.com/problems/reverse-string/description/

class Solution:
    @staticmethod
    def reverse(string: str):
        """
            Time complexity is O(n) and space complexity is O(n).
        """
        return string[-1:-len(string)-1:-1]


print(Solution.reverse("hello"))