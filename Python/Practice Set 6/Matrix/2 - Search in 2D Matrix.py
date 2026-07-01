# Problem link - https://www.naukri.com/code360/problems/search-in-a-2d-matrix_980531


class Solution:
    @staticmethod
    def search(mtx, x):
        """
            Time complexity is O(log(mn)) and space complexity is O(1).
        """
        n, m = len(mtx), len(mtx[0])
        low, high = 0, n*m - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            i, j = mid//m, mid%m
            if mtx[i][j] == x:
                return i, j
            if mtx[i][j] > x:
                high = mid - 1
            else:
                low = mid + 1
        return -1, -1


print(Solution.search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
print(Solution.search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(Solution.search([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 8))