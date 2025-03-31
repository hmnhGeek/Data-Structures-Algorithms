# Problem link - https://www.naukri.com/code360/problems/minimum-rate-to-eat-bananas_7449064

def ceil(x):
    if x > int(x):
        return int(x) + 1

    return x


def is_rate_possible(arr, mid, hours):
    consumed_hours = 0
    for i in range(len(arr)):
        consumed_hours += ceil(arr[i]/mid)

    return consumed_hours <= hours


def get_min_rate(piles, hours):
    if hours < len(piles):
        return -1

    low, high = 1, max(piles)

    # Typical binary search which takes O(n*log(max(piles))) time
    # and O(1) space.
    while low <= high:
        mid = int(low + (high - low)/2)

        # this function takes O(n) time and O(1) space.
        if is_rate_possible(piles, mid, hours):
            # if rate = mid is possible, check for lower rates
            # if they are valid rates or not
            high = mid - 1
        else:
            # if the rate is slow, koko needs to increase her rate
            # of eating bananas to finish within given hours.
            low = mid + 1

    return low


print(get_min_rate([3, 6, 2, 8], 7))
print(get_min_rate([7, 15, 6, 3], 8))
print(get_min_rate([25, 12, 8, 14, 19], 5))

# koko cannot eat 5 piles within four hours.
print(get_min_rate([1, 1, 8, 6, 1], 4))

