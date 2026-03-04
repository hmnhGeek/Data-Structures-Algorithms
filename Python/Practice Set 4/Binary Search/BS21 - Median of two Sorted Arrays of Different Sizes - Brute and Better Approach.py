class Solution:
    @staticmethod
    def get_median(arr1, arr2):
        n, m = len(arr1), len(arr2)
        elem1, elem2 = None, None
        counter = 0
        k = (n + m + 1)//2
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2) and counter < k:
            if arr1[i] <= arr2[j]:
                elem1 = arr1[i]
                i += 1
            else:
                elem1 = arr2[j]
                j += 1
            counter += 1
        while i < len(arr1) and counter < k:
            elem1 = arr1[i]
            i += 1
            counter += 1
        while j < len(arr2) and counter < k:
            elem1 = arr2[j]
            j += 1
            counter += 1

        if i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                elem2 = arr1[i]
            else:
                elem2 = arr2[j]
        if i < len(arr1):
            elem2 = arr1[i]
        if j < len(arr2):
            elem2 = arr2[j]
        if (n + m) % 2 == 0:
            return (elem1 + elem2)/2.0
        return elem1


print(Solution.get_median([1, 3, 4, 7, 10, 12], [2, 3, 6, 15]))
print(Solution.get_median([2, 3, 4], [1, 3]))
print(Solution.get_median([-5, 3, 6, 12, 15], [-12, -10, -6, -3, 4, 10]))
print(Solution.get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45, 60]))
print(Solution.get_median([], [2, 4, 5, 6]))
print(Solution.get_median([1, 3], [2]))
print(Solution.get_median([1, 2], [3, 4]))
print(Solution.get_median([2, 4, 6], [1, 3, 5]))
