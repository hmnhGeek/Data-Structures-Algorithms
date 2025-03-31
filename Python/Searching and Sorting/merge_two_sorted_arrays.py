# Problem link - https://www.geeksforgeeks.org/merge-two-sorted-arrays/


class Solution:
    @staticmethod
    def merge(l1, l2):
        i, j = 0, 0
        merged = []
        while i < len(l1) and j < len(l2):
            if l1[i] <= l2[j]:
                merged.append(l1[i])
                i += 1
            else:
                merged.append(l2[j])
                j += 1
        while i < len(l1):
            merged.append(l1[i])
            i += 1
        while j < len(l2):
            merged.append(l2[j])
            j += 1
        return merged


print(Solution.merge([1, 2, 3, 4], [2, 2, 3, 5, 6]))
print(Solution.merge([1, 3, 4, 5], [2, 4, 6, 8]))
print(Solution.merge([5, 8, 9], [4, 7, 8]))