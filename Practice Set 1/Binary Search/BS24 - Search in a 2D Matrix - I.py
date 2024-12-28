class Solution:
    @staticmethod
    def search(mtx, target):
        n, m = len(mtx), len(mtx[0])
        low = 0
        high = n * m - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            x, y = mid // m, mid % m
            if mtx[x][y] == target:
                return x, y
            if mtx[x][y] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1, -1


print(
    Solution.search(
        [
            [3, 4, 7, 9],
            [12, 13, 16, 18],
            [20, 21, 23, 29]
        ],
        23
    )
)

print(
    Solution.search(
        [
            [3, 4, 7, 9],
            [12, 13, 16, 18],
            [20, 21, 23, 29]
        ],
        28
    )
)

print(Solution.search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(Solution.search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
print(
    Solution.search(
        [[18, 21, 27],
         [38, 55, 67]],
        55
    )
)
