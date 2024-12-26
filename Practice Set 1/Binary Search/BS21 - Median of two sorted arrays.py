class Solution:
    @staticmethod
    def get_median(arr1, arr2):
        n1, n2 = len(arr1), len(arr2)
        if n1 > n2:
            # always perform binary search on shorter array.
            return Solution.get_median(arr2, arr1)

        # define the search space by using shorter array.
        low, high = 0, n1

        # number elements on the left side.
        left = (n1 + n2 + 1)//2

        # binary search...
        while low <= high:
            # take mid1 number of elements from shorter array
            mid1 = int(low + (high - low)/2)
            # take left - mid1 number of elements from the longer array.
            mid2 = left - mid1

            # define l1, l2, r1 and r2.
            l1 = arr1[mid1 - 1] if 0 <= mid1 - 1 < n1 else -1e6
            l2 = arr2[mid2 - 1] if 0 <= mid2 - 1 < n2 else -1e6
            r1 = arr1[mid1] if 0 <= mid1 < n1 else 1e6
            r2 = arr2[mid2] if 0 <= mid2 < n2 else 1e6

            # if the condition is valid, return the median
            if l1 <= r2 and l2 <= r1:
                if (n1 + n2) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2))/2
                return max(l1, l2)
            # if l1 > r2, that means we have taken more from shorter array, reduce.
            elif l1 > r2:
                high = mid1 - 1
            else:
                # else, it means we have taken less from shorter array, increase.
                low = mid1 + 1

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
