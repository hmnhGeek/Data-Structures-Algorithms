'''
    Time complexity is O(log(n)) and space complexity is O(1).
'''

def get_lower_bound_of(arr, k):
    # Function to return first occurrence of index i from arr | arr[i] <= k

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = int(low + (high - low)/2)

        if arr[mid] >= k:
            high = mid - 1
        else:
            low = mid + 1

    return low if low < len(arr) else None


def _get_upper_bound_of(arr, k, low, high):
    if low > high:
        return low

    mid = int(low + (high - low)/2)

    if arr[mid] <= k:
        return _get_upper_bound_of(arr, k, mid + 1, high)
    return _get_upper_bound_of(arr, k, low, mid - 1)


def get_upper_bound_of(arr, k):
    # Function to return first occurrence of index i from arr | arr[i] > k
    return _get_upper_bound_of(arr, k, 0, len(arr) - 1)


arr = [1, 2, 3, 3, 5, 8, 8, 10, 10, 11]
arr2 = [2, 3, 6, 7, 8, 8, 11, 11, 11, 12]
print(f"Upper bound of 6 in the array {arr2}: {get_upper_bound_of(arr2, 6)}")
print(f"Upper bound of 11 in the array {arr2}: {get_upper_bound_of(arr2, 11)}")
print(f"Upper bound of 12 in the array {arr2}: {get_upper_bound_of(arr2, 12)}")
print(f"Upper bound of 13 in the array {arr2}: {get_upper_bound_of(arr2, 13)}")
print(f"Upper bound of 0 in the array {arr2}: {get_upper_bound_of(arr2, 0)}")
print(f"Lower bound of 9 in the array {arr}: {get_lower_bound_of(arr, 9)}")

print(get_lower_bound_of([10, 20, 30, 40, 50], 47))