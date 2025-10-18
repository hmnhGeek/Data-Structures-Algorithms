# Problem link - https://www.naukri.com/code360/problems/search-in-a-2d-matrix_980531


class Solution:
    @staticmethod
    def search(mtx, element):
        """
            Time complexity is O(log(mn)) and space complexity is O(1).
        """

        n, m = len(mtx), len(mtx[0])
        low = 0
        high = n*m - 1

        while low <= high:
            mid = int(low + (high - low)/2)
            row = mid // m
            col = mid % m
            x = mtx[row][col]
            if x == element:
                return True
            if x > element:
                high = mid - 1
            else:
                low = mid + 1
        return False


print(Solution.search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
print(Solution.search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(Solution.search([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 8))
