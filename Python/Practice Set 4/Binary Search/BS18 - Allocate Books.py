# Problem link - https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1
# Solution - https://www.youtube.com/watch?v=Z0hwjftStI4&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=19


class Solution:
    @staticmethod
    def allocate(arr, k):
        """
            Time complexity is O(n * log(sum - max)) and space complexity is O(1).
        """
        if k <= 0 or len(arr) < k:
            return
        low, high = max(arr), sum(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            allocated = Solution._find_allocation(arr, mid)
            if allocated <= k:
                high = mid - 1
            else:
                low = mid + 1
        return low

    @staticmethod
    def _find_allocation(arr, mid):
        allocated = 0
        pages = 0
        for i in range(len(arr)):
            if pages + arr[i] > mid:
                allocated += 1
                pages = arr[i]
            else:
                pages += arr[i]
        if pages > 0:
            allocated += 1
        return allocated


print(Solution.allocate([25, 46, 28, 49, 24], 4))
print(Solution.allocate([12, 34, 67, 90], 2))
print(Solution.allocate([15, 17, 20], 5))
print(Solution.allocate([22, 23, 67], 1))
print(Solution.allocate([15, 17, 20], 2))