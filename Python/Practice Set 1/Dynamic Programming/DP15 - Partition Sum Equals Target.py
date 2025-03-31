# Problem link - https://www.naukri.com/code360/problems/partition-equal-subset-sum_892980?source=youtube&campaign=striver_dp_videos


class Solution:
    @staticmethod
    def subset_sum(arr, k):
        n = len(arr)
        prev = {j: False for j in range(k + 1)}
        prev[0] = True
        prev[arr[0]] = True

        for i in range(1, n):
            curr = {j: False for j in range(k + 1)}
            for target in range(k + 1):
                left = False
                if target >= arr[i]:
                    left = prev[target - arr[i]]
                right = prev[target]
                curr[target] = left or right
            prev = curr
        return prev[k]

    @staticmethod
    def get_partition_sum(arr):
        # Time complexity is O(n*target) and space is O(target).
        arr_sum = sum(arr)
        if arr_sum % 2 != 0:
            return False
        target = arr_sum//2
        return Solution.subset_sum(arr, target)


print(Solution.get_partition_sum([3, 1, 1, 2, 2, 1]))
print(Solution.get_partition_sum([5, 6, 5, 11, 6]))
print(Solution.get_partition_sum([2, 2, 1, 1, 1, 1, 1, 3, 3]))
print(Solution.get_partition_sum([8, 7, 6, 12, 4, 5]))