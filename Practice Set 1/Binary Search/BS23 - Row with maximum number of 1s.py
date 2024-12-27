class Solution:
    @staticmethod
    def _count_1s(arr, low, high):
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[mid] == 1:
                high = mid - 1
            else:
                low = mid + 1
        return len(arr) - low

    @staticmethod
    def max_1_row(mtx):
        n, m = len(mtx), len(mtx[0])
        max_1s_till_now = 0
        row = -1
        for i in range(n - 1, -1, -1):
            count_of_1s = Solution._count_1s(mtx[i], 0, m - 1)
            if max_1s_till_now <= count_of_1s:
                max_1s_till_now = count_of_1s
                row = i
        return row


print(Solution.max_1_row([[1, 1, 1], [0, 0, 1], [0, 0, 0]]))
print(Solution.max_1_row([[1, 1], [1, 1]]))
print(Solution.max_1_row([[0, 0, 0], [0, 1, 1]]))
print(Solution.max_1_row([[0, 0], [1, 1], [0, 0]]))
print(Solution.max_1_row([[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]))
print(Solution.max_1_row([[0, 0, 1, 1], [0, 1, 1, 1], [0, 0, 1, 1], [0, 0, 0, 0]]))
