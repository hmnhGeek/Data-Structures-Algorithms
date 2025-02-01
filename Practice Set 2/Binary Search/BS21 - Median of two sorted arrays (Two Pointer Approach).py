class Solution:
    @staticmethod
    def _even_sized_median(arr1, arr2, n1, n2, m):
        elem1, elem2 = None, None
        i, j = 0, 0
        counter = 0
        last_used = None
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                last_used = arr1[i]
                i += 1
            else:
                last_used = arr2[j]
                j += 1
            counter += 1
            if counter == m:
                elem1 = last_used
            elif counter == m + 1:
                elem2 = last_used
        while i < len(arr1):
            last_used = arr1[i]
            i += 1
            counter += 1
            if counter == m:
                elem1 = last_used
            elif counter == m + 1:
                elem2 = last_used
        while j < len(arr2):
            last_used = arr2[j]
            j += 1
            counter += 1
            if counter == m:
                elem1 = last_used
            elif counter == m + 1:
                elem2 = last_used
        return (elem1 + elem2)/2

    @staticmethod
    def _odd_sized_median(arr1, arr2, n1, n2, m):
        elem = None
        i, j = 0, 0
        counter = 0
        last_used = None
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                last_used = arr1[i]
                i += 1
            else:
                last_used = arr2[j]
                j += 1
            counter += 1
            if counter == m:
                elem = last_used

        while i < len(arr1):
            last_used = arr1[i]
            i += 1
            counter += 1
            if counter == m:
                elem = last_used

        while j < len(arr2):
            last_used = arr2[j]
            j += 1
            counter += 1
            if counter == m:
                elem = last_used

        return elem

    @staticmethod
    def get_median(arr1, arr2):
        n1, n2 = len(arr1), len(arr2)
        n = n1 + n2
        if n % 2 == 0:
            return Solution._even_sized_median(arr1, arr2, n1, n2, n//2)
        return Solution._odd_sized_median(arr1, arr2, n1, n2, (n + 1)//2)


print(Solution.get_median([1, 3, 4, 7, 10, 12], [2, 3, 6, 15]))
print(Solution.get_median([2, 3, 4], [1, 3]))
print(Solution.get_median([-5, 3, 6, 12, 15], [-12, -10, -6, -3, 4, 10]))
print(Solution.get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45, 60]))
print(Solution.get_median([], [2, 4, 5, 6]))
print(Solution.get_median([1, 3], [2]))
print(Solution.get_median([1, 2], [3, 4]))
print(Solution.get_median([2, 4, 6], [1, 3, 5]))
