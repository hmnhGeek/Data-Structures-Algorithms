def get_lower_than_equal_to_in_row(row, val):
    # if the first element itself is greater than value, no need to
    # initiate a binary search, return 0
    if row[0] > val:
        return 0

    # start binary search
    low, high = 0, len(row) - 1

    while low <= high:
        mid = (low + high) // 2

        # if the mid-value is <= value, then there could be more
        # elements to the right which satisfy <= value condition.
        # Increment the low to (mid + 1).
        if row[mid] <= val:
            low = mid + 1

        # else we must have included elements, some of which (including the mid-one)
        # have a higher value than `val`. Therefore, decrement high to mid - 1.
        else:
            high = mid - 1

    # as soon as low > high, low would indicate the number of elements
    # having values <= val, return low.
    return low


def get_number_of_elements_smaller_than(mtx, mid):
    '''
        This function takes O(log(n)) time.
    '''
    nums = 0

    # for each row in the matrix, find how many numbers in the row
    # have elements <= mid-value. Add them up in nums and return it.
    # This way, we get all the numbers in the matrix which are less
    # than or equal to mid-value.
    for row in mtx:
        nums += get_lower_than_equal_to_in_row(row, mid)

    return nums


def get_kth(mtx, k):
    '''
        The binary search over the value range has a time complexity of O(log(n))
        Each iteration of the binary search calls a function with time complexity O(n log(n))
        Overall time complexity is thus O(n (log(n))^2)
        Overall space complexity is O(1).
    '''
    n = len(mtx)
    low = mtx[0][0]
    high = mtx[n - 1][n - 1]

    while low <= high:
        mid = (low + high) // 2
        num_smaller = get_number_of_elements_smaller_than(mtx, mid)

        # we are trying to find the kth largest element right?
        # so, if mid is the correct answer, then num_smaller should be k - 1,
        # that is, number of elements smaller than mid would be k - 1.

        # if number of smaller values in matrix than mid is less than k - 1,
        # we should increase our low value to accommodate more elements
        if num_smaller <= k - 1:
            low = mid + 1

        # else if number of smaller values is more than k - 1, we should
        # decrease our high value to trim down some values.
        else:
            high = mid - 1

    # as soon as low > high, then low will be the answer.
    return low


def example1():
    mtx = [
        [16, 28, 60, 64],
        [22, 41, 63, 91],
        [27, 50, 87, 93],
        [36, 78, 87, 94]
    ]

    print(get_kth(mtx, 3))


def example2():
    mtx = [[10, 20, 30, 40],
           [15, 25, 35, 45],
           [24, 29, 37, 48],
           [32, 33, 39, 50]]

    print(get_kth(mtx, 7))


example1()
example2()