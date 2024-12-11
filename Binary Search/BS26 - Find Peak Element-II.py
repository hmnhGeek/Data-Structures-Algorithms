# Problem link - https://www.geeksforgeeks.org/find-peak-element-2d-array/
# Solution - https://www.youtube.com/watch?v=nGGp5XBzC4g&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=28


class Solution:
    @staticmethod
    def _get_max(mtx, mid, n, m):
        max_elem, idx = -1e6, -1
        for i in range(n):
            if mtx[i][mid] > max_elem:
                max_elem = mtx[i][mid]
                idx = i
        return idx

    @staticmethod
    def find_peak(mtx):
        """
            Overall time complexity is O(n * log(m)) and space complexity is O(1).
        """

        n, m = len(mtx), len(mtx[0])
        # define the search space as the columns.
        low, high = 0, m - 1
        while low <= high:
            # get the mid-column index
            mid = int(low + (high - low) / 2)
            # find the row index of the max element in the mid-column. This will take O(n) time.
            max_elem_row_idx = Solution._get_max(mtx, mid, n, m)

            # get the left and right element of the mid. No need to check for top and bottom because the element is max
            # in its column.
            left = mtx[max_elem_row_idx][mid - 1] if mid - 1 >= 0 else -1
            right = mtx[max_elem_row_idx][mid + 1] if mid + 1 < n else -1
            possible_peak = mtx[max_elem_row_idx][mid]

            # if it is a peak from left and right perspective also, then return this element's coordinates.
            if possible_peak > left and possible_peak > right:
                return max_elem_row_idx, mid

            # if left is greater, the peak might lie in the left half columns
            elif left > possible_peak:
                high = mid - 1
            else:
                # else peak must be in the right half columns
                low = mid + 1
        return None, None


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
