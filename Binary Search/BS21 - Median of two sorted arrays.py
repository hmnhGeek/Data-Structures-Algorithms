class Solution:
    @staticmethod
    def find_median(arr1, arr2):
        n1 = len(arr1)
        n2 = len(arr2)
        n = n1 + n2
        elem1, elem2 = None, None
        i, j = 0, 0
        counter = 0

        while i < len(arr1) and j < len(arr2):
            counter += 1
            if counter == n // 2:
                elem1 = min(arr1[i], arr2[j])
            if counter == (n // 2) + 1:
                elem2 = min(arr1[i], arr2[j])
            if arr1[i] <= arr2[j]:
                i += 1
            else:
                j += 1

        while i < len(arr1):
            counter += 1
            if counter == n // 2:
                elem1 = arr1[i]
            if counter == (n // 2) + 1:
                elem2 = arr1[i]
            i += 1

        while j < len(arr2):
            counter += 1
            if counter == n // 2:
                elem1 = arr2[j]
            if counter == (n // 2) + 1:
                elem2 = arr2[j]
            j += 1

        if n % 2 == 0:
            return (elem1 + elem2) / 2
        return elem2


print(Solution.find_median([1, 3, 4, 7, 10, 12], [2, 3, 6, 15]))
print(Solution.find_median([1, 3, 4], [2, 6]))
print(Solution.find_median([1, 3], [2]))
print(Solution.find_median([1, 2], [3, 4]))