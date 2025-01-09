class Solution:
    @staticmethod
    def get_num_rotations(arr):
        low = 0
        high = len(arr) - 1
        ans = 1e6
        index = None
        while low <= high:
            mid = int(low + (high - low)/2)
            if arr[low] == arr[mid] == arr[high]:
                low += 1
                high -= 1
                continue
            if arr[low] <= arr[mid]:
                if arr[low] < ans:
                    ans = arr[low]
                    index = low
                low = mid + 1
            else:
                if arr[mid] < ans:
                    ans = arr[mid]
                    index = mid
                high = mid - 1
        return index


print(Solution.get_num_rotations([3, 4, 5, 1, 2]))
print(Solution.get_num_rotations([1, 2, 4, 5, 7]))
