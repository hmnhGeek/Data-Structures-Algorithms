class Solution:
    @staticmethod
    def _get_1s_count(arr, low, high):
        while low <= high:
            mid = int(low + (high - low) / 2)
            if arr[mid] == 1:
                high = mid - 1
            else:
                low = mid + 1
        return len(arr) - low

    @staticmethod
    def get_max_1s(mtx):
        n, m = len(mtx), len(mtx[0])
        max_1s = 0
        max_1s_row = None
        for row in range(n - 1, -1, -1):
            ones_count = Solution._get_1s_count(mtx[row], 0, m - 1)
            if max_1s <= ones_count:
                max_1s = ones_count
                max_1s_row = row
        return max_1s_row


print(Solution.get_max_1s([[1, 1, 1], [0, 0, 1], [0, 0, 0]]))
print(Solution.get_max_1s([[1, 1], [1, 1]]))
print(Solution.get_max_1s([[0, 0, 0], [0, 1, 1]]))
print(Solution.get_max_1s([[0, 0], [1, 1], [0, 0]]))
