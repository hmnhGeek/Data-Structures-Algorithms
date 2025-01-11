class Solution:
    @staticmethod
    def search(mtx, target):
        n, m = len(mtx), len(mtx[0])
        low, high = 0, n*m - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            r, c = mid//m, mid%m
            if mtx[r][c] == target:
                return r, c
            if target > mtx[r][c]:
                low = mid + 1
            else:
                high = mid - 1
        return -1, -1


print(Solution.search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
print(Solution.search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(Solution.search([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], 8))
