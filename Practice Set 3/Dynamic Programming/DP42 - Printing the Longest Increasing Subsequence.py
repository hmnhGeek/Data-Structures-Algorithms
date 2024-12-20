def print_lis(arr):
    n = len(arr)
    dp, parents = {i: 1 for i in range(n)}, {i: i for i in range(n)}
    for i in range(n):
        for prev in range(i):
            if arr[i] > arr[prev] and dp[i] < 1 + dp[prev]:
                dp[i] = 1 + dp[prev]
                parents[i] = prev

    start_index = max(dp, key=dp.get)
    result = []
    while parents[start_index] != start_index:
        result.append(arr[start_index])
        start_index = parents[start_index]
    result.append(arr[start_index])
    return result[-1:-len(result)-1:-1]


print(print_lis([5, 4, 11, 1, 16, 8]))
