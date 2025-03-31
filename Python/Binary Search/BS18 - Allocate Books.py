# Problem link - https://www.naukri.com/code360/problems/allocate-books_1090540
# Solution - https://www.youtube.com/watch?v=Z0hwjftStI4&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=19


class Solution:
    @staticmethod
    def _is_possible(pages, mid):
        """
            Time complexity is O(n) and space complexity is O(1).
        """

        # start with first student, allocating him 0th book
        students_considered = 1
        pages_used = pages[0]

        # check from 1st book now.
        for i in range(1, len(pages)):
            # if adding this book does not cross the mid limit, add it.
            if pages[i] + pages_used <= mid:
                pages_used += pages[i]
            else:
                # else increment the count of students and set the pages_used to this index book because we will start
                # next allocation from this book.
                students_considered += 1
                pages_used = pages[i]

        # return the students used.
        return students_considered

    @staticmethod
    def allocate(pages, num_students):
        """
            Time complexity is O(nlog(sum(pages))) and space complexity is O(1).
        """

        if len(pages) < num_students:
            return -1
        low, high = min(pages), sum(pages)
        while low <= high:
            mid = int(low + (high - low)/2)
            students_used = Solution._is_possible(pages, mid)
            # if the number of students who were allocated books were less than required or equal to required, we must
            # decrease `high`. Why on ==? Because, we can try even lower pages for this case.
            if students_used <= num_students:
                high = mid - 1
            else:
                # else this would mean we have some books left to allocate, we must increase low.
                low = mid + 1
        # low points to correct answer.
        return low


print(Solution.allocate([25, 46, 28, 49, 24], 4))
print(Solution.allocate([12, 34, 67, 90], 2))
print(Solution.allocate([15, 17, 20], 2))
print(Solution.allocate([22, 23, 67], 1))
print(Solution.allocate([15, 17, 20], 5))