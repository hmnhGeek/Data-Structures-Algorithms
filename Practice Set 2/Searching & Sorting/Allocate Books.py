class Solution:
    @staticmethod
    def _find_num_allocated(arr, mid, k, n):
        students = 0
        pages = 0
        for i in range(n):
            if pages + arr[i] <= mid:
                pages += arr[i]
            else:
                students += 1
                pages = arr[i]
        if pages != 0:
            students += 1
            pages = 0
        return students

    @staticmethod
    def allocate_books(arr, k):
        if k <= 0 or k > len(arr):
            return -1
        n = len(arr)
        low, high = max(arr), sum(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            students_allocated = Solution._find_num_allocated(arr, mid, k, n)
            if students_allocated > k:
                low = mid + 1
            elif students_allocated == k:
                high = mid - 1
            else:
                high = mid - 1
        return low


print(Solution.allocate_books([25, 46, 28, 49, 24], 4))
print(Solution.allocate_books([12, 34, 67, 90], 2))
print(Solution.allocate_books([15, 17, 20], 2))
print(Solution.allocate_books([22, 23, 67], 1))
print(Solution.allocate_books([15, 17, 20], 5))