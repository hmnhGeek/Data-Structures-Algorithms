class Solution:
    @staticmethod
    def get_rotation_index(arr):
        # define a search space.
        low, high = 0, len(arr) - 1

        # define the index to be found
        ans, index = 1e6, -1

        # typical binary search
        while low <= high:
            mid = int(low + (high - low)/2)

            # if all the indices are same
            if arr[low] == arr[mid] == arr[high]:
                # update the ans and index if required.
                if ans > arr[mid]:
                    ans = arr[mid]
                    index = low

                # shrink the search space and continue.
                low += 1
                high -= 1
                continue

            # if the left part is sorted
            if arr[low] <= arr[mid]:
                if ans > arr[low]:
                    ans = arr[low]
                    index = low
                low = mid + 1

            # else, when the right part is sorted
            else:
                if ans > arr[mid]:
                    ans = arr[mid]
                    index = mid
                high = mid - 1

        # return the index
        return index


print(Solution.get_rotation_index([3, 4, 5, 1, 2]))
print(Solution.get_rotation_index([1, 2, 4, 5, 7]))
print(Solution.get_rotation_index([3, 3, 3, 3, 2, 3, 3]))
print(Solution.get_rotation_index([1, 2, 3]))
print(Solution.get_rotation_index([2, 3, 4, 1]))
