# Problem link - https://www.naukri.com/code360/problems/search-in-a-2d-matrix_980531


class Solution:
    @staticmethod
    def search(mtx, element):
        """
            Time complexity is O(log(nm)) and space complexity is O(1).
        """

        n, m = len(mtx), len(mtx[0])

        # since the matrix is sorted in raster fashion, define low and high accordingly.
        low, high = 0, n*m - 1
        while low <= high:
            mid = int(low + (high - low)/2)

            # get mid-row and col
            i, j = mid//m, mid%m

            # if target is found, return the coordinate
            if mtx[i][j] == element:
                return i, j

            # if target is lower than mid, search in left half, else search in right half.
            elif mtx[i][j] > element:
                high = mid - 1
            else:
                low = mid + 1
        return None


print(Solution.search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
print(Solution.search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(Solution.search([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 8))
