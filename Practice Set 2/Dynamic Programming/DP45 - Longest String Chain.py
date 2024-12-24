def chain_possible(x, y):
    if len(x) != len(y) + 1:
        return False
    i, j = 0, 0
    while i < len(x):
        if 0 <= j < len(y) and x[i] == y[j]:
            j += 1
        i += 1
    return i == len(x) and j == len(y)


def longest_string_chain(strings):
    strings.sort(key=len)
    dp = {i: 1 for i in range(len(strings))}
    parents = {i: i for i in range(len(strings))}
    for i in range(len(strings)):
        for j in range(i):
            if chain_possible(strings[i], strings[j]) and dp[i] < 1 + dp[j]:
                dp[i] = 1 + dp[j]
                parents[i] = j
    start_index = max(dp, key=dp.get)
    result = []
    while start_index != parents[start_index]:
        result.append(strings[start_index])
        start_index = parents[start_index]
    result.append(strings[start_index])
    return result[-1:-len(result)-1:-1]


print(longest_string_chain(["x", "xx", "y", "xyx"]))