def bruteforce(arr, k):
    # Time complexity is O({n - k + 1}*k) and space complexity is O(n - k + 1)
    result = []
    n = len(arr)
    for i in range(n - k + 1):
        negative_found = False
        for j in range(i, i + k):
            if arr[j] < 0:
                result.append(arr[j])
                negative_found = True
                break
        if not negative_found:
            result.append(0)
    return result


print(bruteforce([-8, 2, 3, -6, 10], 2))
print(bruteforce([12, -1, -7, 8, -15, 30, 16, 28], 3))