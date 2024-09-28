# Problem link - https://leetcode.com/problems/partition-array-for-maximum-sum/description/
# Solution - https://www.youtube.com/watch?v=PhWWJmaKfMc&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=55


def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """

    def solve(arr, i, k, n):
        # if you've reached end, return 0
        if i == n:
            return 0

        # store a global max value for sum.
        max_ans = float('-inf')

        # store variables for local checks.
        length = 0
        local_max = float('-inf')

        # loop on the partitions till `kth` partition or `n` whichever is minimum.
        for j in range(i, min(i + k, n)):
            # increment the length of the partition and update the local maxima
            length += 1
            local_max = max(local_max, arr[j])

            # update the local sum and solve for right part.
            local_sum = (length * local_max) + solve(arr, j + 1, k, n)

            # update the global max
            max_ans = max(max_ans, local_sum)

        # return the global max
        return max_ans

    def partition_for_max_sum(arr, k):
        n = len(arr)
        return solve(arr, 0, k, n)

    print(partition_for_max_sum([1, 15, 7, 9, 2, 5, 10], 3))
    print(partition_for_max_sum([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4))
    print(partition_for_max_sum([1], 1))


recursive()
