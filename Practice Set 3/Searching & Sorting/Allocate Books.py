class Solution:
    @staticmethod
    def allocate_books(arr, k):
        """
            Time complexity is O(n * log(sum - max)) and space complexity is O(1).
        """

        if k > len(arr):
            return -1

        # define the search space.
        low, high = max(arr), sum(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            students_allocated = Solution._allocate(arr, mid)

            # if more students could be allocated, then increase the page count so that we lower down to k.
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