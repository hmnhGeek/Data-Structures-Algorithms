# Problem link - https://www.naukri.com/code360/problems/smallest-divisor-with-the-given-limit_1755882

def ceil(x):
    if int(x) < x:
        return int(x) + 1
    return x


def is_less_than_threshold(arr, threshold, mid):
    # This will take O(n) time and O(1) space.
    num = 0
    for i in arr:
        num += ceil(i/mid)

    return num <= threshold


def get_smallest_divisor(arr, threshold):
    # The minimum sum that we can get is `n = len(arr)`. This will happen only
    # when all the indices contribute 1 as ceil value. This will be possible
    # only when you divide by max of the array. So if threshold < n, then the
    # answer is not possible.
    if threshold < len(arr):
        return -1

    low, high = 1, max(arr)

    # this will take O(n*log(max(arr))) time and O(1) space.
    while low <= high:
        mid = int(low + (high - low)/2)

        if is_less_than_threshold(arr, threshold, mid):
            # if mid (denominator) as a divisor gives result <= threshold,
            # let's reduce mid further by reducing high to mid - 1 to check if
            # some lower divisor also yields result below threshold.
            high = mid - 1
        else:
            # if mid as a divisor gives result > threshold, we need to increase
            # the divisor so that ceil values reduces, and we come within
            # threshold limits. And so, let's increase low value.
            low = mid + 1

    return low


print(get_smallest_divisor([1, 2, 5, 9], 6))
print(get_smallest_divisor([1, 2, 3, 4, 5], 8))
print(get_smallest_divisor([8, 4, 2, 3], 10))
print(get_smallest_divisor([2, 3, 5, 7, 11], 11))
print(get_smallest_divisor([1, 2, 5, 9], 2))


