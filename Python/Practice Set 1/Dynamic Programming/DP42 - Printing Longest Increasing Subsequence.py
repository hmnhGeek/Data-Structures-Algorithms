# Problem link - https://www.naukri.com/code360/problems/longest-increasing-subsequence_630459?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=IFfYfonAFGc


def print_lis(arr):
    dp = {i: 1 for i in range(len(arr))}
    parents = {i: i for i in range(len(arr))}

    for i in range(1, len(arr)):
        for prev in range(i):
            # if the prev value is less than current value...
            if arr[prev] < arr[i]:
                # then it can be considered in increasing sequence. But will including it
                # in the increasing sequence give us even a longer increasing sequence?
                if 1 + dp[prev] > dp[i]:
                    # if yes, then update the dp and parents dictionary.
                    parents[i] = prev
                    dp[i] = 1 + dp[prev]

    # get the index of the LIS from the dp array.
    last_index_of_lis = max(dp, key=dp.get)
    # get the length of LIS as the max increasing sequence length from dp array.
    lis_length = max(dp.values())

    # create a result array which would be of the size of LIS.
    result = [0]*lis_length

    # create a starting node (just like disjoint set, we will traverse the parents).
    start_node = last_index_of_lis
    # we will fill the array from back side.
    i = lis_length - 1

    # until the start node is a self parent
    while parents[start_node] != start_node:
        # update the ith index of the result
        result[i] = arr[start_node]
        # move to next lower index
        i -= 1
        # update start node.
        start_node = parents[start_node]

    # at last, update for self parent start node as well.
    result[i] = arr[start_node]
    print(result)


print_lis([5, 4, 11, 1, 16, 8])
print_lis([1, 2, 2])
print_lis([3, 10, 2, 1, 20])
print_lis([30, 20, 10])
print_lis([2, 2, 2])
print_lis([10, 20, 35, 80])