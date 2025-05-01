# Problem link - https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/


class Solution:
    @staticmethod
    def get_min_max(arr):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        mini, maxi = 1e6, -1e6
        for i in range(len(arr)):
            if arr[i] > maxi:
                maxi = arr[i]
            if arr[i] < mini:
                mini = arr[i]
        return mini, maxi


print(Solution.get_min_max([3, 5, 4, 1, 9]))
print(Solution.get_min_max([22, 14, 8, 17, 35, 3]))
print(Solution.get_min_max([2, 1, 4, 6, 8, 8, 6]))
