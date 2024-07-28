def _get_floor(arr, k, low, high):
    if low > high:
        return arr[low - 1] if 0 <= low - 1 < len(arr) else -1

    mid = int(low + (high - low)/2)

    if arr[mid] <= k:
        # move to right part, because there could be a bigger floor value <= k.
        return _get_floor(arr, k, mid + 1, high)
    else:
        # move to the left part
        return _get_floor(arr, k, low, mid - 1)

def floor(arr, k):
    return _get_floor(arr, k, 0, len(arr) - 1)

print(floor([10, 20, 24, 30, 40, 50], 34))