# Problem link - https://www.naukri.com/code360/problems/printing-longest-increasing-subsequence_8360670
# Solution - https://www.youtube.com/watch?v=IFfYfonAFGc&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=43


def print_lis(arr):
    """
        Time complexity is O(n^2) and space complexity is O(2n).
    """

    n = len(arr)
    # define a DP array and a parents array
    dp, parents = {i: 1 for i in range(n)}, {i: i for i in range(n)}

    # loop on all the indices and its previous indices
    for i in range(n):
        for prev in range(i):
            # if the current element in the array is greater than prev, and if LIS ending at `i` is of smaller length
            # than the LIS formed after adding this element to the LIS ending at `prev` index, then update the variables
            if arr[i] > arr[prev] and dp[i] < 1 + dp[prev]:
                # update LIS length ending at `i`
                dp[i] = 1 + dp[prev]
                # update parent of `i` to `prev`
                parents[i] = prev

    # get the last index of LIS as we will use it to backtrack.
    start_index = max(dp, key=dp.get)
    # create a result list
    result = []

    # backtracking until ultimate parent is found.
    while parents[start_index] != start_index:
        result.append(arr[start_index])
        start_index = parents[start_index]
    # add the element at ultimate parent as well.
    result.append(arr[start_index])

    # return the reverse of the result for the correct LIS.
    return result[-1:-len(result) - 1:-1]


print(print_lis([5, 4, 11, 1, 16, 8]))
print(print_lis([1, 2, 2]))
print(print_lis([10, 20, 3, 40]))
print(print_lis([10, 22, 9, 33, 21, 50, 41, 60, 80]))
print(print_lis([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
print(print_lis([1]))
print(print_lis([5, 6, 3, 4, 7, 6]))
print(print_lis([1, 2, 3, 4, 5]))
