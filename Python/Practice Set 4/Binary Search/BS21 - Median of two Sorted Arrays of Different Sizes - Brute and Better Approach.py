# Problem link - https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/
# Solution - https://www.youtube.com/watch?v=F9c7LpRZWVQ&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=23


class Solution:
    @staticmethod
    def get_median(arr1, arr2):
        """
            Time complexity is O(n + m) and space complexity is O(1).
        """
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

    @staticmethod
    def best_method(arr1, arr2):
        """
            Time complexity is O(log(min(n1, n2))) and space complexity is O(1).
        """
        n1, n2 = len(arr1), len(arr2)
        if n1 > n2:
            return Solution.best_method(arr2, arr1)
        n = (n1 + n2 + 1)//2
        low, high = 0, n1
        while low <= high:
            mid1 = int(low + (high - low)/2)
            mid2 = n - mid1
            l1 = arr1[mid1 - 1] if 0 <= mid1 - 1 < n1 else -1e6
            l2 = arr2[mid2 - 1] if 0 <= mid2 - 1 < n2 else -1e6
            r1 = arr1[mid1] if 0 <= mid1 < n1 else 1e6
            r2 = arr2[mid2] if 0 <= mid2 < n2 else 1e6
            if l1 > r2:
                high = mid1 - 1
            elif l2 > r1:
                low = mid1 + 1
            else:
                if (n1 + n2) % 2 == 1:
                    return max(l1, l2)
                return (max(l1, l2) + min(r1, r2))/2.0
        return -1


print(Solution.get_median([1, 3, 4, 7, 10, 12], [2, 3, 6, 15]))
print(Solution.get_median([2, 3, 4], [1, 3]))
print(Solution.get_median([-5, 3, 6, 12, 15], [-12, -10, -6, -3, 4, 10]))
print(Solution.get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45, 60]))
print(Solution.get_median([], [2, 4, 5, 6]))
print(Solution.get_median([1, 3], [2]))
print(Solution.get_median([1, 2], [3, 4]))
print(Solution.get_median([2, 4, 6], [1, 3, 5]))
print()
print(Solution.best_method([1, 3, 4, 7, 10, 12], [2, 3, 6, 15]))
print(Solution.best_method([2, 3, 4], [1, 3]))
print(Solution.best_method([-5, 3, 6, 12, 15], [-12, -10, -6, -3, 4, 10]))
print(Solution.best_method([1, 12, 15, 26, 38], [2, 13, 17, 30, 45, 60]))
print(Solution.best_method([], [2, 4, 5, 6]))
print(Solution.best_method([1, 3], [2]))
print(Solution.best_method([1, 2], [3, 4]))
print(Solution.best_method([2, 4, 6], [1, 3, 5]))
print()