# Problem link - https://www.geeksforgeeks.org/problems/next-permutation5226/1
# Solution - https://www.youtube.com/watch?v=JDOXKqF60RQ&t=1490s


class Solution:
    @staticmethod
    def reverse_parts(arr, low, high):
        while low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1

    @staticmethod
    def find_next_permutation(arr):
        """
            Overall time complexity is O(3n) and space complexity is O(1).
        """

        n = len(arr)
        # find the breakpoint index, i.e., the first index which breaks the linearly increasing order.
        bp_indx = -1
        for i in range(n - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                bp_indx = i
                break

        # if the array was sorted in decreasing order, bp_index will be -1, in that case, simply return the reverse.
        if bp_indx == -1:
            return arr[-1:-n-1:-1]

        # find the first greater element than bp_index element and swap with it.
        for i in range(n - 1, bp_indx, -1):
            if arr[i] > arr[bp_indx]:
                arr[i], arr[bp_indx] = arr[bp_indx], arr[i]
                break

        # then reverse the part after bp_index.
        Solution.reverse_parts(arr, bp_indx + 1, n - 1)
        return arr


print(Solution.find_next_permutation([2, 4, 1, 7, 5, 0]))
print(Solution.find_next_permutation([3, 2, 1]))
print(Solution.find_next_permutation([3, 4, 2, 5, 1]))