def get_distincts(mp):
    count = 0
    for i in mp:
        if mp[i] > 0:
            count += 1
    return count


def get_less_than_equal_to(arr, k):
    if k < 0:
        return 0
    i, j, count = 0, 0, 0
    n = len(arr)
    distinct_count = 0
    mp = {i: 0 for i in arr}

    while j < n:
        mp[arr[j]] += 1

        while get_distincts(mp) > k:
            mp[arr[i]] -= 1
            i += 1

        distinct_count += (j - i + 1)
        j += 1

    return distinct_count


def get_k_distinct(arr, k):
    return get_less_than_equal_to(arr, k) - get_less_than_equal_to(arr, k - 1)


print(get_k_distinct([1, 2, 1, 2, 3], 2))
print(get_k_distinct([1, 2, 1, 3, 4], 3))
print(get_k_distinct([2, 1, 2, 1, 6], 2))
print(get_k_distinct([1, 2, 3, 4, 5], 1))