# Problem link - https://leetcode.com/problems/single-element-in-a-sorted-array/description/
# Solution - https://www.youtube.com/watch?v=AZOmHuHadxQ&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=9


class Solution:
    @staticmethod
    def get_single_element(arr):
        """
            Time complexity is O(log(n)) and space complexity is O(1).
        """

        n = len(arr)

        # handle the edge cases separately.
        if n == 1:
            return arr[0]
        if arr[0] != arr[1]:
            return arr[0]
        if arr[n - 1] != arr[n - 2]:
            return arr[n - 1]

        # maintain the same search space. Do not shrink to 1 --> n - 2 because in that case low and high elements will
        # become unique elements as well. By checking for edge cases above, we have ensured that mid will never come to
        # 0 or n - 1.
        low = 0
        high = n - 1
        while low <= high:
            mid = int(low + (high - low) / 2)

            # if mid is unique, return mid element.
            if arr[mid - 1] != arr[mid] and arr[mid + 1] != arr[mid]:
                return arr[mid]

            # if mid's twin is on left side, exclude it from left count.
            if arr[mid - 1] == arr[mid]:
                left_count = mid - low - 1
            else:
                # else, mid's twin must be on right side, thus include all elements in count from the left side.
                left_count = mid - low

            # same logic for the case when mid + 1 is same as mid.
            if arr[mid + 1] == arr[mid]:
                right_count = high - mid - 1
            else:
                right_count = high - mid

            # if there are odd number of elements on the left side, then the single element must be on the left side.
            if left_count % 2 == 1:
                high = mid - 1
            # if there are odd number of elements on the right side, then the single element must be on the right side.
            else:
                low = mid + 1

        # return -1 if such element is not found
        return -1


print(Solution.get_single_element([1, 2, 2, 3, 3, 4, 4]))
print(Solution.get_single_element([1, 1, 2, 3, 3, 4, 4]))
print(Solution.get_single_element([1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]))
print(Solution.get_single_element([1, 1, 2, 2, 3]))
print(Solution.get_single_element([1, 1, 2, 2, 4, 5, 5]))
print(Solution.get_single_element([1, 1, 3, 5, 5]))
print(Solution.get_single_element([1, 1, 4, 4, 15]))
print(Solution.get_single_element([1, 1, 2, 3, 3, 4, 4, 8, 8]))
print(Solution.get_single_element([3, 3, 7, 7, 10, 11, 11]))
