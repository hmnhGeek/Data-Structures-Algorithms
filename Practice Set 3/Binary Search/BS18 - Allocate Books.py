class Solution:
    @staticmethod
    def _get_count(arr, mid):
        students = 0
        pages = 0
        n = len(arr)
        for i in range(n):
            if pages + arr[i] <= mid:
                pages += arr[i]
            else:
                students += 1
                pages = arr[i]
        if pages > 0:
            students += 1
            pages = 0
        return students

    @staticmethod
    def allocate(arr, k):
        n = len(arr)
        if n < k:
            return -1
        low, high = max(arr), sum(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            students = Solution._get_count(arr, mid)
            if students <= k:
                high = mid - 1
            else:
                low = mid + 1
        return low


print(Solution.allocate([25, 46, 28, 49, 24], 4))
print(Solution.allocate([12, 34, 67, 90], 2))
print(Solution.allocate([15, 17, 20], 5))
print(Solution.allocate([22, 23, 67], 1))
print(Solution.allocate([15, 17, 20], 2))
