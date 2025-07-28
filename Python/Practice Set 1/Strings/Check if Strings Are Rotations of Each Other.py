# Problem link - https://www.geeksforgeeks.org/dsa/a-program-to-check-if-strings-are-rotations-of-each-other/

class Solution:
    @staticmethod
    def check_if_rotation(s1, s2):
        """
            Time complexity is O(n) and space complexity is O(n).
        """
        temp = s1 + s1
        return s2 in temp


print(Solution.check_if_rotation("abcd", "cdab"))
print(Solution.check_if_rotation("aab", "aba"))
print(Solution.check_if_rotation("abcd", "acbd"))
