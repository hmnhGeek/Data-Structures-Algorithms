class Solution:
    @staticmethod
    def _is_possible(pages, mid):
        students_considered = 1
        pages_used = pages[0]
        for i in range(1, len(pages)):
            if pages[i] + pages_used <= mid:
                pages_used += pages[i]
            else:
                students_considered += 1
                pages_used = pages[i]
        return students_considered


    @staticmethod
    def allocate(pages, num_students):
        if len(pages) < num_students:
            return -1
        low, high = min(pages), sum(pages)
        while low <= high:
            mid = int(low + (high - low)/2)
            students_used = Solution._is_possible(pages, mid)
            if students_used <= num_students:
                high = mid - 1
            else:
                low = mid + 1
        return low


print(Solution.allocate([25, 46, 28, 49, 24], 4))
print(Solution.allocate([12, 34, 67, 90], 2))
print(Solution.allocate([15, 17, 20], 2))
print(Solution.allocate([22, 23, 67], 1))
print(Solution.allocate([15, 17, 20], 5))