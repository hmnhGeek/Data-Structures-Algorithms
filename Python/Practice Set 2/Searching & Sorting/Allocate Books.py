# Problem link - https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1
# Solution - https://www.youtube.com/watch?v=Z0hwjftStI4&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=19


class Solution:
    @staticmethod
    def _find_num_allocated(arr, mid, k, n):
        # initially, 0 students allocated and 0 pages assigned.
        students = 0
        pages = 0

        # loop on the array
        for i in range(n):
            # if adding ith page is still within limits, add the pages
            if pages + arr[i] <= mid:
                pages += arr[i]
            else:
                # else increment the student count
                students += 1
                pages = arr[i]

        # at end, if there are some pages left, assign it to another student.
        if pages != 0:
            students += 1
            pages = 0
        return students

    @staticmethod
    def allocate_books(arr, k):
        """
            Time complexity is O(n * log(sum - max)) and space complexity is O(1).
        """

        # if students count is negative, 0 or more than the books, return -1.
        if k <= 0 or k > len(arr):
            return -1
        n = len(arr)

        # min max pages must be used to allocate > k and sum(arr) to allocate to 1 student.
        low, high = max(arr), sum(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            # in O(n) find the number of students who will get the books if mid-pages are max allowed.
            students_allocated = Solution._find_num_allocated(arr, mid, k, n)

            # if more than k students were allocated, that means page limit was low, hence increase it.
            if students_allocated > k:
                low = mid + 1

            # if exactly k students were allocated, then pages were enough, lets try to reduce the max limit.
            elif students_allocated == k:
                high = mid - 1
            else:
                # else if < k students were allocated, that means limit is too high, decrease it.
                high = mid - 1
        return low


print(Solution.allocate_books([25, 46, 28, 49, 24], 4))
print(Solution.allocate_books([12, 34, 67, 90], 2))
print(Solution.allocate_books([15, 17, 20], 2))
print(Solution.allocate_books([22, 23, 67], 1))
print(Solution.allocate_books([15, 17, 20], 5))
