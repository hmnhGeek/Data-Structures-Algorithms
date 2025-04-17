class Solution:
    @staticmethod
    def search(mtx, element):
        n, m = len(mtx), len(mtx[0])
        low, high = 0, n*m - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            i, j = mid//m, mid%m
            if mtx[i][j] == element:
                return i, j
            elif mtx[i][j] > element:
                high = mid - 1
            else:
                low = mid + 1
        return None


print(Solution.search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
print(Solution.search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(Solution.search([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 8))
