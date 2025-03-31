# Problem link - https://www.naukri.com/code360/problems/longest-increasing-subsequence_630459?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=IFfYfonAFGc&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=43

def print_lis(arr):
    n = len(arr)
    dp = {i: 1 for i in range(n)}
    parents = {i: i for i in range(n)}

    for index in range(n):
        for prev in range(index):
            if arr[index] > arr[prev]:
                if 1 + dp[prev] > dp[index]:
                    dp[index] = 1 + dp[prev]
                    parents[index] = prev

    last_index_of_lis = max(dp, key=dp.get)
    nodes = []
    start_node = last_index_of_lis
    while parents[start_node] != start_node:
        nodes.append(start_node)
        start_node = parents[start_node]
    nodes.append(start_node)

    for i in range(len(nodes)):
        nodes[i] = arr[nodes[i]]
    return nodes[-1:-len(nodes)-1:-1]


print(print_lis([10, 9, 2, 5, 3, 7, 101, 18]))
print(print_lis([5, 4, 11, 1, 16, 8]))
print(print_lis([1, 2, 2]))
print(print_lis([3, 10, 2, 1, 20]))
print(print_lis([30, 20, 10]))
print(print_lis([2, 2, 2]))
print(print_lis([10, 20, 35, 80]))