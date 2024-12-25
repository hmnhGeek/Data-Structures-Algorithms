class Solution:
    @staticmethod
    def _allocation_possible(arr, mid, k):
        students = 0
        pages = 0
        for i in range(len(arr)):
            if pages + arr[i] <= mid:
                pages += arr[i]
            else:
                students += 1
                pages = arr[i]
        if pages > 0:
            students += 1
            pages = 0
        if students <= k:
            return 0
        return 1

    @staticmethod
    def allocate(arr, k):
        if k <= 0:
            return
        low, high = max(arr), sum(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            is_possible = Solution._allocation_possible(arr, mid, k)
            if is_possible == 0:
                high = mid - 1
            else:
                low = mid + 1
        return low


print(Solution.allocate([25, 46, 28, 49, 24], 4))