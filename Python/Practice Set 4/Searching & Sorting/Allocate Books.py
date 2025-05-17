# Problem link - https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1
# Solution - https://www.youtube.com/watch?v=Z0hwjftStI4&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=19


class Solution:
    @staticmethod
    def allocate_books(arr, k):
        """
            Time complexity is O(n * log(sum - max)) and space complexity is O(1).
        """

        if k <= 0 or k > len(arr):
            return -1

        # define the search space.
        low = max(arr)
        high = sum(arr)

        while low <= high:
            mid = int(low + (high - low)/2)
            students_allocated = Solution._allocate(arr, mid)
            if students_allocated == k:
                high = mid - 1

            # if more students could be allocated, then increase the page count so that we lower down to k.
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
