# Problem link - https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1
# Solution - https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1


class Solution:
    @staticmethod
    def no_space(arr):
        """
            Total time complexity is O(n^2) and space complexity is O(1).
        """

        count = 0
        n = len(arr)
        # loop on the array
        for i in range(n):
            # take `j` from `i + 1` --> `n - 1`
            for j in range(i + 1, n):
                # if at any point, a_i > a_j, increment the inversion count.
                if arr[i] > arr[j]:
                    count += 1
        return count

    @staticmethod
    def _merge(arr, low, high):
        # typical merge method of a merge sort algorithm.

        mid = int(low + (high - low)/2)
        left, right = arr[low:mid+1], arr[mid+1:high+1]
        merged = []
        i, j = 0, 0
        inversion_count = 0

        while i < len(left) and j < len(right):
            # if the left element is greater than right element, then the elements from `i` in `left` to elements (n-1)
            # indexed elements in left will make count inverted pairs with current `j` element in `right`. The other
            # things will remain as is in merge method.
            if left[i] > right[j]:
                inversion_count += (len(left) - i)
                merged.append(right[j])
                j += 1
            else:
                merged.append(left[i])
                i += 1

        while i < len(left):
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged, inversion_count

    @staticmethod
    def _count_inversions(arr, low, high, inv_count):
        # typical merge sort base condition and code below.
        if low >= high:
            return

        mid = int(low + (high - low)/2)
        Solution._count_inversions(arr, low, mid, inv_count)
        Solution._count_inversions(arr, mid + 1, high, inv_count)
        arr[low:high+1], inversion_count = Solution._merge(arr, low, high)

        # just ensure to increase the global inversion count by the value given out by the _merge method.
        inv_count[0] += inversion_count

    @staticmethod
    def count_inversions(arr):
        """
            Time complexity is O(nlog(n)) and space complexity is O(n).
        """

        # store the reference to the global count of inversions.
        inversion_count = [0]
        # make a recursive call to merge sort method.
        Solution._count_inversions(arr, 0, len(arr) - 1, inversion_count)
        # return inversion count
        return inversion_count[0]


print(Solution.no_space([2, 4, 1, 3, 5]))
print(Solution.no_space([2, 3, 4, 5, 6]))
print(Solution.no_space([10, 10, 10]))
print(Solution.no_space([4, 3, 2, 1]))
print(Solution.no_space([5, 4, 3, 2, 1]))
print()
print(Solution.count_inversions([5, 4, 3, 2, 1]))
print(Solution.count_inversions([4, 3, 2, 1]))
print(Solution.count_inversions([10, 10, 10]))
print(Solution.count_inversions([2, 3, 4, 5, 6]))
print(Solution.count_inversions([2, 4, 1, 3, 5]))
