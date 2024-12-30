class Solution:
    @staticmethod
    def _find_how_many_students_allocated(arr, mid):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # assume no pages and students have been assigned yet
        students = 0
        pages = 0

        # loop on the books now
        for i in range(len(arr)):
            # if adding the pages from this book does not breach the limit, add it.
            if pages + arr[i] <= mid:
                pages += arr[i]
            else:
                # else, increment the number of students and reset pages to this book's pages.
                students += 1
                pages = arr[i]

        # at the end, if there are still books to be allocated, then increment the number of students and set pages
        # to 0.
        if pages > 0:
            students += 1
            pages = 0

        # return the number of students to whom books have been allocated.
        return students

    @staticmethod
    def allocate_books(arr, k):
        """
            Time complexity is O(n * log(sum - max)) and space complexity is O(1).
        """

        n = len(arr)

        # if there are more students than the number of books, return -1.
        if k > n or k <= 0:
            return -1

        # define a search space.
        low, high = max(arr), sum(arr)
        while low <= high:
            mid = int(low + (high - low)/2)
            # check how many students have been allocated with mid-number of pages to the maximum pages a student can
            # hold.
            allocated_students = Solution._find_how_many_students_allocated(arr, mid)

            # if more than k students have been allocated, then we must increase the maximum number of pages a student
            # can hold so that we bring allocated students under control.
            if allocated_students > k:
                low = mid + 1
            else:
                # else we must try to reduce the max allowed pages
                high = mid - 1

        # finally, low will point to the correct answer.
        return low


print(Solution.allocate_books([25, 46, 28, 49, 24], 4))
print(Solution.allocate_books([12, 34, 67, 90], 2))
print(Solution.allocate_books([15, 17, 20], 2))
print(Solution.allocate_books([22, 23, 67], 1))
print(Solution.allocate_books([15, 17, 20], 5))
