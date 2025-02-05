# Problem link - https://leetcode.com/problems/search-a-2d-matrix/
# Solution - https://www.youtube.com/watch?v=JXU4Akft7yk&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=26


class Solution:
    @staticmethod
    def search(mtx, x):
        """
            Time complexity is O(log(nm)) and space complexity is O(1).
        """
        n, m = len(mtx), len(mtx[0])
        low, high = 0, n*m - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            i, j = mid // m, mid % m
            if mtx[i][j] == x:
                return i, j
            if mtx[i][j] < x:
                low = mid + 1
            else:
                high = mid - 1
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
