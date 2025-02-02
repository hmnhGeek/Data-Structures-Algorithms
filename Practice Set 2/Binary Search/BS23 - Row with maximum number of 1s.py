class Solution:
    @staticmethod
    def _count_of_one(arr, low, high):
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
        max_1s, index = 0, -1
        for i in range(n):
            one_count = Solution._count_of_one(mtx[i], 0, m - 1)
            if one_count > max_1s:
                max_1s = one_count
                index = i
        return index


print(Solution.max_1_row([[1, 1, 1], [0, 0, 1], [0, 0, 0]]))
print(Solution.max_1_row([[1, 1], [1, 1]]))
print(Solution.max_1_row([[0, 0, 0], [0, 1, 1]]))
print(Solution.max_1_row([[0, 0], [1, 1], [0, 0]]))
print(Solution.max_1_row([[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]))
print(Solution.max_1_row([[0, 0, 1, 1], [0, 1, 1, 1], [0, 0, 1, 1], [0, 0, 0, 0]]))
