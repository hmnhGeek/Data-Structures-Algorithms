# Problem link - https://leetcode.com/problems/find-peak-element/description/
# Solution - https://www.youtube.com/watch?v=cXxmbemS6XM&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=10


class Solution:
    """
        Time complexity is O(log(n)) and space complexity is O(1).
    """
    @staticmethod
    def find_peak_element(arr):
        # handle edge cases separately.

        # if there is only one element, then that will be the peak itself, because out of bounds areas are -inf.
        if len(arr) == 1:
            return arr[0]

        # if arr[1] is same (i.e., plateau from -inf < arr[0] >= arr[1]), then also arr[0] is a peak.
        if arr[0] >= arr[1]:
            return arr[0]

        # same above logic from the right end
        if arr[-1] >= arr[-2]:
            return arr[-1]

        # define the search space now from 1 --> n - 2.
        low, high = 1, len(arr) - 2
        while low <= high:
            mid = int(low + (high - low) / 2)

            # cases for a peak.
            # if mid element is strictly greater than its neighbours, it's a peak.
            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return arr[mid]

            # if this is the case
            """
                 (mid)______(mid + 1)
                    /
                   /
                  /
                 (mid - 1)
            """
            # then also mid is a peak
            if arr[mid] > arr[mid - 1] and arr[mid] == arr[mid + 1]:
                return arr[mid]

            # finally, if this is the case
            """
                (mid - 1)_______(mid)
                                \
                                 \
                                  \
                                  (mid + 1)
            """
            # then also mid is a peak.
            if arr[mid] > arr[mid + 1] and arr[mid] == arr[mid - 1]:
                return arr[mid]

            #    (mid - 1) --------- (mid) ---------- (mid + 1)
            if arr[mid - 1] == arr[mid] == arr[mid + 1]:
                low = mid + 1

            #                (mid + 1)
            #                 /
            #                /
            #              (mid)
            #              /
            #             /
            #    (mid - 1)
            elif arr[mid - 1] < arr[mid] < arr[mid + 1]:
                low = mid + 1

            #   (mid - 1)
            #           \
            #            \
            #            (mid)
            #              \
            #               \
            #               (mid + 1)
            elif arr[mid - 1] > arr[mid] > arr[mid + 1]:
                high = mid - 1

            # invert of a peak; we can decide to go any side.
            elif arr[mid - 1] > arr[mid] and arr[mid] < arr[mid + 1]:
                low = mid + 1

            #                            (mid + 1)
            #                             /
            #                            /
            #    (mid - 1) -------- (mid)
            elif arr[mid] < arr[mid + 1]:
                low = mid + 1

            #   (mid - 1)
            #           \
            #            \
            #            (mid) --------- (mid + 1)
            else:
                high = mid - 1

        return -1


print(Solution.find_peak_element([3, 3, 3, 3]))
print(Solution.find_peak_element([1, 2, 3, 1]))
print(Solution.find_peak_element([1, 2, 1, 3, 5, 6, 4]))
print(Solution.find_peak_element([1, 8, 1, 5, 3]))
print(Solution.find_peak_element([1, 2, 1]))
print(Solution.find_peak_element([5, 10, 20, 15]))
print(Solution.find_peak_element([10, 20, 15, 2, 23, 90, 90]))
print(Solution.find_peak_element([1, 1, 1]))
print(Solution.find_peak_element([1, 2, 3, 4, 5]))
print(Solution.find_peak_element([5, 4, 3, 2, 1]))
print(Solution.find_peak_element([1, 10, 13, 7, 6, 5, 4, 2, 1, 0]))
