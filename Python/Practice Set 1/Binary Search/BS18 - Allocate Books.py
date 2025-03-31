# Problem link - https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1
# Solution - https://www.youtube.com/watch?v=Z0hwjftStI4&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=19


class Solution:
    @staticmethod
    def _allocation_possible(arr, mid, k):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        students = 0
        pages = 0
        for i in range(len(arr)):
            if pages + arr[i] <= mid:
                pages += arr[i]
            else:
                students += 1
                pages = arr[i]

        # at end, if pages are still pending, assign them to one more student.
        if pages > 0:
            students += 1
            pages = 0

        # if less than or equal to k students have been assigned books, we must lower down the number of pages.
        if students <= k:
            return 0
        # else we can increase the number of pages so that exactly k students get the books.
        return 1

    @staticmethod
    def allocate(arr, k):
        """
            Time complexity is O(n * log(sum - max)) and space complexity is O(1).
        """

        # if k is <= 0 or number of students is more than the number of books, return -1.
        if k <= 0 or k > len(arr):
            return -1
        low, high = max(arr), sum(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            # check if allocation to all k students is possible if each student gets at max mid-number of pages.
            is_possible = Solution._allocation_possible(arr, mid, k)
            if is_possible == 0:
                high = mid - 1
            else:
                low = mid + 1
        return low


print(Solution.allocate([25, 46, 28, 49, 24], 4))
print(Solution.allocate([12, 34, 67, 90], 2))
print(Solution.allocate([15, 17, 20], 5))
print(Solution.allocate([22, 23, 67], 1))
print(Solution.allocate([15, 17, 20], 2))
