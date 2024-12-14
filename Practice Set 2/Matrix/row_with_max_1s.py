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
        n, m = len(mtx), len(mtx[0])
        max1s = 0
        row_idx = -1
        for i in range(n - 1, -1, -1):
            count_of_1s = Solution._binary_search(mtx[i], 0, m - 1)
            if count_of_1s >= max1s:
                max1s = count_of_1s
                row_idx = i
        return row_idx if max1s != 0 else -1


print(Solution.max1s_row([[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]))
print(Solution.max1s_row([[0, 0], [1, 1]]))
print(Solution.max1s_row([[0, 0], [0, 0]]))
