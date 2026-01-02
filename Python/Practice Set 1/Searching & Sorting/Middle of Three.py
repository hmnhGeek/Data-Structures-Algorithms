# Problem link - https://www.geeksforgeeks.org/problems/middle-of-three2926/1

class Solution:
    """
        Time complexity is O(1) and space complexity is O(1).
    """
    @staticmethod
    def get_middle_of_three(a, b, c):
        s = a + b + c
        return s - min(a, b, c) - max(a, b, c)


print(Solution.get_middle_of_three(978, 518, 300))
print(Solution.get_middle_of_three(162, 934, 200))
print(Solution.get_middle_of_three(246, 214, 450))
