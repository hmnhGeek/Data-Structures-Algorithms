# Problem link - https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1


class Solution:
    @staticmethod
    def _binary_search(arr, low, high):
        while low <= high:
            mid = int(low + (high - low) / 2)
            if arr[mid] == 1:
                high = mid - 1
            else:
                low = mid + 1
        return len(arr) - low

    @staticmethod
    def max1s_row(mtx):
        """
            Time complexity is O(n * log(m)) and space complexity is O(1).
        """
        n, m = len(mtx), len(mtx[0])
        max1s = 0
        row_idx = -1
        # iterate from the last row till the 0th row, so that we get the first row from top with max 1s, in n times.
        for i in range(n - 1, -1, -1):
            # get the count of 1s in the current row in O(log(m)) time.
            count_of_1s = Solution._binary_search(mtx[i], 0, m - 1)
            # if the count is greater than or equal to current max, update the result variables.
            if count_of_1s >= max1s:
                max1s = count_of_1s
                row_idx = i
        # return the row index with max 1s if max 1s are not 0, else there is no row having 1, return -1.
        return row_idx if max1s != 0 else -1


print(Solution.max1s_row([[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]))
print(Solution.max1s_row([[0, 0], [1, 1]]))
print(Solution.max1s_row([[0, 0], [0, 0]]))
print(Solution.max1s_row([[1, 1, 1], [0, 0, 1], [0, 0, 0]]))
print(Solution.max1s_row([[1, 1], [1, 1]]))