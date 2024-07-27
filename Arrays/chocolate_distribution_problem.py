# Problem - https://www.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1
# Solution - https://www.youtube.com/watch?v=oYNU1TD9W5Y

def distribute(arr, m):
    '''
        Overall time complexity is O(n*log(n)).
        Overall space complexity is O(1). However, Python's sort might use some additional space.
    '''

    # sort the array, so that we can use sliding window technique.
    # sorting the array ensures that maximum and minimum numbers
    # are closest for any window. That way, we can reduce the
    # computation by not generating all the 2^n possibilities
    # using power set approach. This will take O(n*log(n)) time.
    arr.sort()
    n = len(arr)
    min_diff = float('inf')

    # loop through all the slides in the window. To not overflow
    # out of the list and maintain window size, ensure that i runs
    # from [0 to n - m]. This will take O(n - m) time.
    for i in range(n - m + 1):
        # the maximum value is at the right end of the window
        # the minimum value is at the left end of the window.
        # update the min_diff value.
        min_diff = min(min_diff, arr[i + m - 1] - arr[i])

    return min_diff

print(distribute([3, 4, 1, 9, 56, 7, 9, 12], 5))
print(distribute([7, 3, 2, 4, 9, 12, 56], 3))