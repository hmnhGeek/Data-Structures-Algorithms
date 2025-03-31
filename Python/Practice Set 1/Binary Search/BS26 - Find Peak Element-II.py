# Problem link - https://www.geeksforgeeks.org/find-peak-element-2d-array/
# Solution - https://www.youtube.com/watch?v=nGGp5XBzC4g&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=28


class Solution:
    @staticmethod
    def _get_max_cell_in_col(mtx, mid, n):
        x = 0
        for i in range(n):
            if mtx[i][mid] > mtx[x][mid]:
                x = i
        return x

    @staticmethod
    def find_peak(mtx):
        """
            Time complexity is O(n * log(m)) and space complexity is O(1).
        """

        n, m = len(mtx), len(mtx[0])
        # define search space as the column space.
        low, high = 0, m - 1
        while low <= high:
            mid = int(low + (high - low)/2)
            # get the max element row
            x = Solution._get_max_cell_in_col(mtx, mid, n)

            # get left and right values of this max element.
            left = mtx[x][mid - 1] if 0 <= mid - 1 < m else -1
            right = mtx[x][mid + 1] if 0 <= mid + 1 < m else -1

            # if (x, mid) is a peak, return it
            if mtx[x][mid] > left and mtx[x][mid] > right:
                return x, mid

            # else modify the search space based on the logic of Peak Element - I.
            elif mtx[x][mid] < right:
                low = mid + 1
            elif mtx[x][mid] < left:
                high = mid - 1
            else:
                high = mid - 1
        return -1, -1



print(
    Solution.find_peak(
        [[8, 6], [10, 1]]
    )
)

print(
    Solution.find_peak(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    )
)

print(Solution.find_peak([[1, 4], [3, 2]]))
print(Solution.find_peak([[10, 20, 15], [21, 30, 14], [7, 16, 32]]))
