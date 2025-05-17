class Solution:
    @staticmethod
    def allocate_books(arr, k):
        if k <= 0 or k > len(arr):
            return -1

        low = max(arr)
        high = sum(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            students_allocated = Solution._allocate(arr, mid)
            if students_allocated == k:
                high = mid - 1
            elif students_allocated > k:
                low = mid + 1
            else:
                high = mid - 1
        return low

    @staticmethod
    def _allocate(arr, mid):
        pages = 0
        num_students = 0
        for i in range(len(arr)):
            if pages + arr[i] <= mid:
                pages += arr[i]
            else:
                pages = arr[i]
                num_students += 1
        if pages > 0:
            num_students += 1
            pages = 0
        return num_students


print(Solution.allocate_books([25, 46, 28, 49, 24], 4))
print(Solution.allocate_books([12, 34, 67, 90], 2))
print(Solution.allocate_books([15, 17, 20], 2))
print(Solution.allocate_books([22, 23, 67], 1))
print(Solution.allocate_books([15, 17, 20], 5))
