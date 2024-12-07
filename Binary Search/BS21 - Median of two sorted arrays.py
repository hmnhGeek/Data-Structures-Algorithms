# Problem link - https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# Solution - https://www.youtube.com/watch?v=F9c7LpRZWVQ&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=23


class Solution:
    @staticmethod
    def find_median(arr1, arr2):
        """
            Overall time complexity is O(n) and space complexity is O(1).
        """

        # define length variables.
        n1 = len(arr1)
        n2 = len(arr2)
        n = n1 + n2

        # define median variables as Nones
        elem1, elem2 = None, None

        # define pointers and a counter variable
        i, j = 0, 0
        counter = 0

        # merging from the two sorted arrays
        while i < len(arr1) and j < len(arr2):
            # increment the counter first
            counter += 1

            # if the counter has reached n/2, its elem1 turn
            if counter == n // 2:
                elem1 = min(arr1[i], arr2[j])
            # if the counter has reached n/2 + 1, its elem2 turn
            if counter == (n // 2) + 1:
                elem2 = min(arr1[i], arr2[j])

            # typical merge() function code
            if arr1[i] <= arr2[j]:
                i += 1
            else:
                j += 1

        while i < len(arr1):
            # same logic as above for counter, but this time just use arr1 instead of taking a min.
            counter += 1
            if counter == n // 2:
                elem1 = arr1[i]
            if counter == (n // 2) + 1:
                elem2 = arr1[i]
            i += 1

        while j < len(arr2):
            # same logic as above for counter, but this time just use arr2 instead of taking a min.
            counter += 1
            if counter == n // 2:
                elem1 = arr2[j]
            if counter == (n // 2) + 1:
                elem2 = arr2[j]
            j += 1

        # return the median
        if n % 2 == 0:
            return (elem1 + elem2) / 2
        return elem2

    @staticmethod
    def find_median_optimal(arr1, arr2):
        """
            Overall time complexity is O(log(n1)) and space complexity is O(1).
        """

        n1 = len(arr1)
        n2 = len(arr2)
        # always perform optimal approach on the shorter array.
        if n2 < n1:
            return Solution.find_median_optimal(arr2, arr1)

        # find the number of elements required on the left part of median.
        left = (n1 + n2 + 1)//2
        n = n1 + n2

        # define search space and perform Binary Search
        low = 0
        high = n1
        while low <= high:
            # find the number of elements to be picked from arr1.
            mid1 = int(low + (high - low)/2)
            # the number of elements to be picked from arr2 will be left - mid1.
            mid2 = left - mid1
            # define l1, l2, r1 and r2.
            l1 = arr1[mid1 - 1] if mid1 - 1 >= 0 else -1e6
            l2 = arr2[mid2 - 1] if mid2 - 1 >= 0 else -1e6
            r1 = arr1[mid1] if mid1 < n1 else 1e6
            r2 = arr2[mid2] if mid2 < n2 else 1e6
            # if the symmetry is valid, return the median
            if l1 <= r2 and l2 <= r1:
                if n % 2 == 1:
                    return max(l1, l2)
                return (max(l1, l2) + min(r1, r2))/2
            # else reduce the search space
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        return -1


print(Solution.find_median([1, 3, 4, 7, 10, 12], [2, 3, 6, 15]))
print(Solution.find_median([1, 3, 4], [2, 6]))
print(Solution.find_median([1, 3], [2]))
print(Solution.find_median([1, 2], [3, 4]))
print()
print(Solution.find_median_optimal([1, 3, 4, 7, 10, 12], [2, 3, 6, 15]))
print(Solution.find_median_optimal([1, 3, 4], [2, 6]))
print(Solution.find_median_optimal([1, 3], [2]))
print(Solution.find_median_optimal([1, 2], [3, 4]))
