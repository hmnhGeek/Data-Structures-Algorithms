# Problem link - https://www.naukri.com/code360/problems/search-in-a-2d-matrix_980531


class Solution:
    @staticmethod
    def search(mtx, target):
        """
            Time complexity is O(log(nm)) and space complexity is O(1).
        """

        n, m = len(mtx), len(mtx[0])

        # since the matrix is sorted in raster fashion, define low and high accordingly.
        low, high = 0, n*m - 1
        while low <= high:
            mid = int(low + (high - low)/2)

            # get mid-row and col
            r, c = mid//m, mid%m

            # if target is found, return the coordinate
            if mtx[r][c] == target:
                return r, c

            # if target is higher than mid, search in right half, else search in left half.
            if target > mtx[r][c]:
                low = mid + 1
            else:
                high = mid - 1

        # return -1 if not found.
        return -1, -1


print(Solution.search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
print(Solution.search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(Solution.search([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 8))
