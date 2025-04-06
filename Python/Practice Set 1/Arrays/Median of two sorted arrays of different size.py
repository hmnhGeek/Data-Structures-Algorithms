# Problem link - https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/
# Solution - https://www.youtube.com/watch?v=F9c7LpRZWVQ&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=23


class Solution:
    @staticmethod
    def get_median(arr1, arr2):
        """
            Time complexity is O(min(log(n1, n2))) and space complexity is O(1).
        """

        n1, n2 = len(arr1), len(arr2)
        if n2 < n1:
            # always perform binary search on shorter array.
            return Solution.get_median(arr2, arr1)

        # number elements on the left side.
        n = n1 + n2
        median_term = (n + 1)//2

        # define the search space by using shorter array.
        low, high = 0, n1
        while low <= high:
            # take mid1 number of elements from shorter array
            mid1 = int(low + (high - low)/2)

            # take left - mid1 number of elements from the longer array.
            mid2 = median_term - mid1

            # define l1, l2, r1 and r2.
            l1 = arr1[mid1 - 1] if 0 <= mid1 - 1 < n1 else -1e6
            l2 = arr2[mid2 - 1] if 0 <= mid2 - 1 < n2 else -1e6
            r1 = arr1[mid1] if 0 <= mid1 < n1 else 1e6
            r2 = arr2[mid2] if 0 <= mid2 < n2 else 1e6

            # if l1 > r2, that means we have taken more from shorter array, reduce.
            if l1 > r2:
                high = mid1 - 1
            elif l2 > r1:
                # else, it means we have taken less from shorter array, increase.
                low = mid1 + 1
            else:
                # if the condition is valid, return the median
                if n % 2 == 0:
                    return (max(l1, l2) + min(r1, r2))/2
                return max(l1, l2)

        # return dummy value.
        return -1


print(Solution.get_median([1, 3, 4, 7, 10, 12], [2, 3, 6, 15]))
print(Solution.get_median([2, 3, 4], [1, 3]))
print(Solution.get_median([-5, 3, 6, 12, 15], [-12, -10, -6, -3, 4, 10]))
print(Solution.get_median([1, 12, 15, 26, 38], [2, 13, 17, 30, 45, 60]))
print(Solution.get_median([], [2, 4, 5, 6]))
print(Solution.get_median([1, 3], [2]))
print(Solution.get_median([1, 2], [3, 4]))
print(Solution.get_median([2, 4, 6], [1, 3, 5]))
