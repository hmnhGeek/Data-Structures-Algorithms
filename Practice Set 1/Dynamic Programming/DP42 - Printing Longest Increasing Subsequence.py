# Problem link - https://www.naukri.com/code360/problems/longest-increasing-subsequence_630459?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=IFfYfonAFGc


def print_lis(arr):
    dp = {i: 1 for i in range(len(arr))}
    parents = {i: i for i in range(len(arr))}

    for i in range(1, len(arr)):
        for prev in range(i):
            if arr[prev] < arr[i]:
                if 1 + dp[prev] > dp[i]:
                    parents[i] = prev
                    dp[i] = 1 + dp[prev]

    last_index_of_lis = max(dp, key=dp.get)
    lis_length = max(dp.values())
    result = [0]*lis_length
    start_node = last_index_of_lis
    i = lis_length - 1

    while parents[start_node] != start_node:
        result[i] = arr[start_node]
        i -= 1
        start_node = parents[start_node]
    result[i] = arr[start_node]
    print(result)


print_lis([5, 4, 11, 1, 16, 8])
print_lis([1, 2, 2])
print_lis([3, 10, 2, 1, 20])
print_lis([30, 20, 10])
print_lis([2, 2, 2])
print_lis([10, 20, 35, 80])