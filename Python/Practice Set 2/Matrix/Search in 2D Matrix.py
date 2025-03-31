# Problem link - https://www.naukri.com/code360/problems/search-in-a-2d-matrix_980531


class Solution:
    @staticmethod
    def search(mtx, x):
        """
            Time complexity is O(log(nm)) and space complexity is O(1).
        """
        n, m = len(mtx), len(mtx[0])

        # since the entire matrix is sorted in a way that if you flatten it you'll get a sorted array, we can perform a
        # simple binary search.
        low = 0
        high = n * m - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            element = mtx[mid // m][mid % m]
            if element == x:
                return mid // m, mid % m
            if element > x:
                high = mid - 1
            else:
                low = mid + 1
        return -1


print(Solution.search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
print(Solution.search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(Solution.search([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 8))
