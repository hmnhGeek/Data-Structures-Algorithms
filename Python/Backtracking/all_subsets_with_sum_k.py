def get_all_paths(arr, index, paths, path, k):
    # if target became 0, add the path till now to the paths set.
    if k == 0:
        paths.add(path[-1:-len(path)-1:-1])
        return

    # if you reached index 0 and the 0th element is exactly equal to target,
    # simply add 0th element into path and add that path to the paths set.
    if index == 0:
        if arr[0] == k:
            resultant = path + (arr[0],)
            paths.add(resultant[-1:-len(resultant)-1:-1])
        return

    # if the element at index can contribute to the formation of the target,
    # use it and move to lower index by adding this element to path and reducing
    # the target value.
    if arr[index] <= k:
        get_all_paths(arr, index - 1, paths, path + (arr[index],), k - arr[index])

    # if not consuming this index (whatever be the reason), move to lower index with
    # same target.
    get_all_paths(arr, index - 1, paths, path, k)


def all_paths_with_sum_k(arr, k):
    n = len(arr)
    paths = set()
    get_all_paths(arr, n - 1, paths, (), k)
    return paths


print(all_paths_with_sum_k([1, 2, 3, 1], 3))
print(all_paths_with_sum_k([1, 1, 1, 1, 1], 3))
print(all_paths_with_sum_k([3, 34, 4, 12, 5, 2], 9))
print(all_paths_with_sum_k([3, 34, 4, 12, 5, 2], 30))