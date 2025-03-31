def house_robber(arr):
    n = len(arr)
    prev_prev = {True: -1e6, False: -1e6}
    prev = {True: arr[0], False: 0}

    for index in range(1, n):
        curr = {True: -1e6, False: -1e6}
        if index - 2 >= 0:
            curr[True] = arr[index] + max(prev_prev[True], prev_prev[False])
        curr[False] = max(prev[True], prev[False])
        prev_prev = prev
        prev = curr

    return max(prev[True], prev[False])


def house_robber2(arr):
    n = len(arr)
    return max(house_robber(arr[:n - 1]), house_robber(arr[1:]))


print(house_robber2([2, 3, 2]))
print(house_robber2([1, 3, 2, 1]))
print(house_robber2([1, 5, 1, 2, 6]))
print(house_robber2([1, 3, 2, 0]))