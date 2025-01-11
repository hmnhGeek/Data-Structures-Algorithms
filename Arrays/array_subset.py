class Solution:
    @staticmethod
    def is_subset(a, b):
        if len(b) > len(a):
            return False
        m, n = len(a), len(b)
        found_status = {i: False for i in b}
        for i in range(m):
            if a[i] in found_status:
                found_status[a[i]] = True
        return all(v for v in found_status.values())


print(Solution.is_subset([11, 7, 1, 13, 21, 3, 7, 3], [11, 3, 7, 1, 7]))
print(Solution.is_subset([1, 2, 3, 4, 4, 5, 6], [1, 2, 4]))
print(Solution.is_subset([10, 5, 2, 23, 19], [19, 5, 3]))
