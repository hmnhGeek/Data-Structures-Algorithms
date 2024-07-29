# Problem link - https://www.naukri.com/code360/problems/rose-garden_2248080

def is_possible(arr, mid, m, k):
    '''This function takes O(n) time and O(1) space.'''

    num_formed = 0
    counter = 0

    for i in range(len(arr)):
        # if blooming is possible on ith day, increase the counter
        if arr[i] <= mid:
            counter += 1
        else:
            # if blooming is not possible on ith day, add to num_formed
            # the value counter // k which represents how many adjacent
            # k flowers can be used to form a bouquet. Reset counter
            # back to 0.
            num_formed += (counter // k)
            counter = 0

    # at the end also, do make a check for counter // k.
    num_formed += (counter // k)

    # if you can form at least m bouquets, return True, else False.
    return num_formed >= m


def get_min_days(arr, m, k):
    '''
        Overall time complexity is O(n*log(max(arr) - min(arr))) and space is O(1).
    '''

    # if the required number of flowers used is more than available, return -1.
    if m*k > len(arr):
        return -1

    # to bloom at least one flower we need days = min(arr)
    # to bloom all the flowers we need days = max(arr)
    low, high = min(arr), max(arr)

    while low <= high:
        mid = int(low + (high - low)/2)

        if is_possible(arr, mid, m, k):
            # if m bouquets can be formed, let's check if lesser number of
            # days can also help us.
            high = mid - 1
        else:
            # if not possible, then we need more flowers to bloom and therefore
            # need more days to make it possible.
            low = mid + 1

    # low will now be at the least day at which scenario is possible.
    return low


print(get_min_days([7, 7, 7, 7, 13, 11, 12, 7], 2, 3))
print(get_min_days([1, 2, 1, 2, 7, 2, 2, 3, 1], 2, 3))
print(get_min_days([1, 2, 1, 2, 7, 2, 2, 3, 1], 2, 3))
print(get_min_days([1, 1, 1, 1], 1, 1))
