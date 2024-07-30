# Problem link - https://www.naukri.com/code360/problems/largest-subarray-sum-minimized_7461751
# Solution - https://www.youtube.com/watch?v=thUd_WJn6wk&list=PLgUwDviBIf0pMFMWuuvDNMAkoQFi-h0ZF&index=20

# Exactly same problem - https://www.naukri.com/code360/problems/painter-s-partition-problem_1089557

# Exactly same as Book Allocation Problem - https://github.com/hmnhGeek/Data-Structures-Algorithms/blob/main/Searching%20and%20Sorting/allocate_books.py

def max_can_make_required_splits(arr, max_sum_allowed, num_subarrays_required):
    # This will take O(n) time and O(1) space.

    num_arrays_made = 1
    sum_acc = arr[0]

    for i in range(1, len(arr)):
        if arr[i] + sum_acc > max_sum_allowed:
            num_arrays_made += 1
            sum_acc = arr[i]
        else:
            sum_acc += arr[i]

    return num_arrays_made <= num_subarrays_required


def get_largest_subarray_sum(arr, k):
    # Overall time complexity is O(n*log(sum - max)) and O(1) space.

    if k > len(arr):
        return -1

    low = max(arr)
    high = sum(arr)

    # This will take O(n*log(sum - max)) and O(1) space.
    while low <= high:
        mid = int(low + (high - low)/2)

        if max_can_make_required_splits(arr, mid, k):
            high = mid - 1
        else:
            low = mid + 1

    return low


print(get_largest_subarray_sum([1, 2, 3, 4, 5], 3))
print(get_largest_subarray_sum([3, 5, 1], 3))
print(get_largest_subarray_sum([10, 4, 5, 10, 9, 10], 4))