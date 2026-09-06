class Solution:
    @staticmethod
    def merge_without_extra_space(a, b):
        i = len(a) - 1
        j = 0
        while i >= 0 and j < len(b):
            if a[i] > b[j]:
                a[i], b[j] = b[j], a[i]
                i -= 1
                j += 1
            else:
                break
        a.sort()
        b.sort()
        print(a, b)


Solution.merge_without_extra_space([2, 4, 7, 10], [2, 3])
Solution.merge_without_extra_space([1, 5, 9, 10, 15, 20], [2, 3, 8, 13])
Solution.merge_without_extra_space([0, 1], [2, 3])
