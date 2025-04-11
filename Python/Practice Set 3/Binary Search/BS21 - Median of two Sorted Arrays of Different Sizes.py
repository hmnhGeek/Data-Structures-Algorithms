class Solution:
    @staticmethod
    def get_median(arr1, arr2):
        n1, n2 = len(arr1), len(arr2)

        # always perform binary search on the shorter array.
        if n1 > n2:
            return Solution.get_median(arr2, arr1)

        # find how many elements should be present on the left.
        n = n1 + n2
        left = (n + 1)//2

        # pick no one from a1 or pick all from a1.
        low, high = 0, n1
        while low <= high:
            mid1 = int(low + (high - low)/2)
            mid2 = left - mid1
            l1 = arr1[mid1 - 1] if 0 <= mid1 - 1 < n1 else -1e6
            l2 = arr2[mid2 - 1] if 0 <= mid2 - 1 < n2 else -1e6
            r1 = arr1[mid1] if 0 <= mid1 < n1 else 1e6
            r2 = arr2[mid2] if 0 <= mid2 < n2 else 1e6

            # if l1 > r2, we have picked more from a1, reduce!
            if l1 > r2:
                high = mid1 - 1

            # if l2 > r1, we have picked more from a2, increase from a1.
            elif l2 > r1:
                low = mid1 + 1

            # else if the condition is valid, return the median.
            else:
                if n % 2 == 0:
                    return (max(l1, l2) + min(r1, r2))/2
                return max(l1, l2)
        return -1


print(Solution.get_median([1, 3, 4, 7, 10, 12], [2, 3, 6, 15]))
print(Solution.get_median([2, 3, 4], [1, 3]))
print(Solution.get_median([-5, 3, 6, 12, 15], [-12, -10, -6, -3, 4, 10]))
print(Solution.get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45, 60]))
print(Solution.get_median([], [2, 4, 5, 6]))
print(Solution.get_median([1, 3], [2]))
print(Solution.get_median([1, 2], [3, 4]))
print(Solution.get_median([2, 4, 6], [1, 3, 5]))
