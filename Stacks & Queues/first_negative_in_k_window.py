def bruteforce(arr, k):
    # Time complexity is O({n - k + 1}*k) and space complexity is O(n - k + 1) for storing result.
    result = []
    n = len(arr)

    # iterate on each window
    for i in range(n - k + 1):
        # assume that no negative value is found
        negative_found = False
        # iterate on each element in the window
        for j in range(i, i + k):
            if arr[j] < 0:
                # if the element is negative, add it to result, set negative_found to True and
                # break out of this nested loop.
                result.append(arr[j])
                negative_found = True
                break

        # if no negative value was found in this window, add a 0.
        if not negative_found:
            result.append(0)

    # return result list
    return result


print(bruteforce([-8, 2, 3, -6, 10], 2))
print(bruteforce([12, -1, -7, 8, -15, 30, 16, 28], 3))