class Solution:
    @staticmethod
    def allocate_books(arr, k):
        low, high = max(arr), sum(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            students_allocated = Solution._allocate(arr, mid)
            if students_allocated > k:
                low = mid + 1
            elif students_allocated == k:
                high = mid - 1
            else:
                high = mid - 1
        return low

    @staticmethod
    def _allocate(arr, mid):
        students_allocated = 0
        pages = 0
        n = len(arr)
        for i in range(n):
            if pages + arr[i] > mid:
                students_allocated += 1
                pages = arr[i]
                continue
            pages += arr[i]
        if pages > 0:
            students_allocated += 1
            pages = 0
        return students_allocated


print(Solution.allocate_books([25, 46, 28, 49, 24], 4))
print(Solution.allocate_books([12, 34, 67, 90], 2))
print(Solution.allocate_books([15, 17, 20], 2))
print(Solution.allocate_books([22, 23, 67], 1))
print(Solution.allocate_books([15, 17, 20], 5))