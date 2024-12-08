class Solution:
    @staticmethod
    def reverse_parts(arr, low, high):
        while low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1

    @staticmethod
    def find_next_permutation(arr):
        n = len(arr)
        # find the breakpoint
        bp_indx = -1
        for i in range(n - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                bp_indx = i
                break
        if bp_indx == -1:
            return arr[-1:-n-1:-1]
        for i in range(n - 1, bp_indx, -1):
            if arr[i] > arr[bp_indx]:
                arr[i], arr[bp_indx] = arr[bp_indx], arr[i]
                break
        Solution.reverse_parts(arr, bp_indx + 1, n - 1)
        return arr


print(Solution.find_next_permutation([2, 4, 1, 7, 5, 0]))
print(Solution.find_next_permutation([3, 2, 1]))
print(Solution.find_next_permutation([3, 4, 2, 5, 1]))