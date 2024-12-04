# Problem link - https://www.naukri.com/code360/problems/kth-missing-element_893215
# Solution - https://www.youtube.com/watch?v=uZ0N_hZpyps&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=17


class Solution:
    @staticmethod
    def find_missing(arr, k):
        """
            Overall time complexity is O(log(n)) and space complexity is O(1).
        """

        # added a check for an edge case.
        if k <= 0:
            return -1

        # define search space.
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = int(low + (high - low) / 2)

            # let's get the actual position of arr[mid] in case everyone was present, i.e., (arr[mid] - 1) in a 0 based
            # indexing. Now the offset is this number ` - mid`. These many numbers have been missed till now.
            diff = (arr[mid] - 1) - mid

            # if this difference is still less than k, we must check higher.
            if diff < k:
                low = mid + 1
            else:
                # else we must check lower.
                high = mid - 1

        # finally, high will point to a number which will be before kth missing number. To find that missing number now,
        # we must find how much high is behind k and then add that number to arr[high].
        # return k - {(arr[high] - 1) - high} + arr[high] = k + 1 + high = k + low.
        return k + low


print(Solution.find_missing([2, 3, 4, 7, 11], 5))
print(Solution.find_missing([5, 7, 10, 12], 4))
print(Solution.find_missing([2, 4, 5, 7], 3))
print(Solution.find_missing([4, 7, 9, 10], 1))
print(Solution.find_missing([4, 7, 9, 10], 4))
print(Solution.find_missing([1, 2, 3, 4], 2))
print(Solution.find_missing([2, 3, 5, 9, 10], 1))
print(Solution.find_missing([1, 2, 3], 2))
print(Solution.find_missing([2, 3, 5, 9, 10, 11, 12], 4))
