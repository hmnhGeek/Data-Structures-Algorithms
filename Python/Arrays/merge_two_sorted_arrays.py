# Problem link - https://www.geeksforgeeks.org/merge-two-sorted-arrays/#using-merge-of-mergesort


class Solution:
    @staticmethod
    def merge(arr1, arr2):
        """
            Overall time complexity is O(max(m, n)) and space complexity is O(m + n)
        """

        merged = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
        while i < len(arr1):
            merged.append(arr1[i])
            i += 1
        while j < len(arr2):
            merged.append(arr2[j])
            j += 1
        return merged


print(Solution.merge([1, 3, 4, 5], [2, 4, 6, 8]))
print(Solution.merge([5, 8, 9], [4, 7, 8]))