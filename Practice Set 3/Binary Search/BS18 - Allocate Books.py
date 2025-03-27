# Problem link - https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1
# Solution - https://www.youtube.com/watch?v=Z0hwjftStI4&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=19


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
        """
            Time complexity is O(n * log(sum - max)) and space complexity is O(1).
        """

        n = len(arr)

        # if the number of books < required students, return -1
        if n < k:
            return -1

        # define a search space.
        low, high = max(arr), sum(arr)
        while low <= high:
            mid = int(low + (high - low)/2)

            # find the number of students whom the books have been allocated in O(n) time with mid number of pages.
            students = Solution._get_count(arr, mid)

            # if number of students allocated <= required students, let's try to decrease the number of pages.
            if students <= k:
                high = mid - 1
            else:
                # if number of students allocated > required students, let's try to increase the number of pages.
                low = mid + 1

        # low represents the correct number of minimum pages.
        return low


print(Solution.allocate([25, 46, 28, 49, 24], 4))
print(Solution.allocate([12, 34, 67, 90], 2))
print(Solution.allocate([15, 17, 20], 5))
print(Solution.allocate([22, 23, 67], 1))
print(Solution.allocate([15, 17, 20], 2))
