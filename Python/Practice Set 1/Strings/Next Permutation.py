# Problem link - https://leetcode.com/problems/next-permutation/description/
# Solution - https://www.youtube.com/watch?v=JDOXKqF60RQ&t=976s


class Solution:
    @staticmethod
    def breakpoint_index(arr):
        n = len(arr)
        for i in range(n - 1, 0, -1):
            if arr[i - 1] < arr[i]:
                return i - 1
        return -1

    @staticmethod
    def reverse_part(arr, index):
        n = len(arr)
        i, j = index + 1, n - 1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    @staticmethod
    def just_greater(arr, bp_index):
        n = len(arr)
        for i in range(n - 1, bp_index, -1):
            if arr[i] > arr[bp_index]:
                return i
        return -1

    @staticmethod
    def get_next_permutation(arr):
        """
            Overall time complexity is O(n) and space complexity is O(1).
        """
        if len(arr) == 0 or len(arr) == 1:
            return
        bp_index = Solution.breakpoint_index(arr)
        if bp_index == -1:
            return arr[-1:-len(arr)-1:-1]
        swap_index = Solution.just_greater(arr, bp_index)
        arr[bp_index], arr[swap_index] = arr[swap_index], arr[bp_index]
        Solution.reverse_part(arr, bp_index)
        return arr


print(Solution.get_next_permutation([1, 2, 3]))
print(Solution.get_next_permutation([1, 1, 5]))
print(Solution.get_next_permutation([3, 2, 1]))
print(Solution.get_next_permutation([2, 4, 1, 7, 5, 0]))
print(Solution.get_next_permutation([3, 4, 2, 5, 1]))
print(Solution.get_next_permutation([2, 3, 1, 5, 4]))
print()
