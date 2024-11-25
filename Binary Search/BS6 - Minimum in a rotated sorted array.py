class Solution:
    @staticmethod
    def min_in_uniques(arr):
        """
            Time complexity is O(log(n)) and space complexity is O(1).
        """
        n = len(arr)
        low, high = 0, n - 1
        while low <= high:
            mid = int(low + (high - low) / 2)

            # if the previous element to mid is greater than mid, then mid is minimum.
            if 0 <= mid - 1 < n and arr[mid - 1] > arr[mid]:
                return arr[mid]

            # if the next element to mid is smaller than mid, then the next element, i.e., mid + 1 is minimum.
            if 0 <= mid + 1 < n and arr[mid + 1] < arr[mid]:
                return arr[mid + 1]

            # if left part is unsorted, minimum must lie here.
            if arr[low] > arr[mid]:
                high = mid - 1

            # else if the right part is unsorted, minimum must lie in right part.
            elif arr[high] < arr[mid]:
                low = mid + 1

            # if however, the entire space is sorted, then return arr[low] as minimum
            elif arr[low] <= arr[mid] <= arr[high]:
                return arr[low]
        return arr[low] if low in range(n) else -1

    @staticmethod
    def min_in_uniques_v2(arr):
        """
            Time complexity is O(log(n)) and space complexity is O(1).
        """
        n = len(arr)
        low, high = 0, n - 1
        ans = 1e6
        while low <= high:
            mid = int(low + (high - low)/2)
            # if left part is sorted, take the minimum of left part and continue with the unsorted part
            if arr[low] <= arr[mid]:
                ans = min(ans, arr[low])
                low = mid + 1
            # else if the right part is sorted, take the minimum of right part and continue with the unsorted part
            else:
                ans = min(ans, arr[mid])
                high = mid - 1
        return ans


print(Solution.min_in_uniques([4, 5, 6, 7, 0, 1, 2]))
print(Solution.min_in_uniques([4, 1, 2, 3]))
print(Solution.min_in_uniques([3, 4, 5, 1, 2]))
print(Solution.min_in_uniques([3, 4, 1, 2]))
print(Solution.min_in_uniques([25, 30, 5, 10, 15, 20]))
print(Solution.min_in_uniques([11, 13, 15, 17]))
print(Solution.min_in_uniques([7, 8, 1, 2, 3, 4, 5, 6]))
print(Solution.min_in_uniques([1, 2]))
print(Solution.min_in_uniques([2, 1]))
print()
print(Solution.min_in_uniques_v2([4, 5, 6, 7, 0, 1, 2]))
print(Solution.min_in_uniques_v2([4, 1, 2, 3]))
print(Solution.min_in_uniques_v2([3, 4, 5, 1, 2]))
print(Solution.min_in_uniques_v2([3, 4, 1, 2]))
print(Solution.min_in_uniques_v2([25, 30, 5, 10, 15, 20]))
print(Solution.min_in_uniques_v2([11, 13, 15, 17]))
print(Solution.min_in_uniques_v2([7, 8, 1, 2, 3, 4, 5, 6]))
print(Solution.min_in_uniques_v2([1, 2]))
print(Solution.min_in_uniques_v2([2, 1]))
