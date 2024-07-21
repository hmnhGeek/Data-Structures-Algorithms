def get_right_greater(arr):
    # The idea is to loop from right to left and updating the greatest value in maxi

    n = len(arr)
    result = [None for _ in range(n)]

    # initially, maxi will have the greatest value as last element from the array.
    maxi = arr[-1]

    # start from the second last element in the array and the right greatest of last
    # element will be None always as there are no elements to the right.
    for i in range(n - 2, -1, -1):

        # if the ith element is smaller than maxi, update result's ith value with maxi
        # as this would be the greatest element to the right of i index.
        if arr[i] <= maxi:
            result[i] = maxi

        # else, if ith index has a greater value than the greatest to the right,
        # then it means that we should update maxi to this array value. Also,
        # since now this value is greatest in the right section, it would have no
        # element as greatest to its right, and so we don't update result[i] and
        # it is kept as None only.
        else:
            maxi = arr[i]

    return result


def get_left_greater(arr):
    # The idea is to loop from left to right and updating the greatest value in maxi

    n = len(arr)
    result = [None for _ in range(n)]

    # initially, maxi will have the greatest value as the 0th element from the array.
    maxi = arr[0]

    # start from the second element in the array and the right greatest of 0th
    # element will be None always as there are no elements to it's left.
    for i in range(1, n):

        # if the ith element is smaller than maxi, update result's ith value with maxi
        # as this would be the greatest element to the left of i index.
        if arr[i] <= maxi:
            result[i] = maxi

        # else, if ith index has a greater value than the greatest to the left,
        # then it means that we should update maxi to this array value. Also,
        # since now this value is greatest in the left section, it would have no
        # element as greatest to its left, and so we don't update result[i] and
        # it is kept as None only.
        else:
            maxi = arr[i]

    return result


def intersector(x, y):
    if x is None or y is None: return None
    return min(x, y)


def trap_rainwater(arr):
    '''
        Overall time complexity is O(n)
        Overall space complexity is O(n)
    '''

    # compute the greatest value from array to the left of every index
    # it will take O(n) time and O(n) space to store these values.
    left_greater = get_left_greater(arr)

    # compute the greatest value from array to the right of every index
    # it will take O(n) time and O(n) space to store these values.
    right_greater = get_right_greater(arr)

    # intersect the left greater and the right greater values, if either of them is None,
    # return None, else return minimum of the two values
    # basically we want both left and right boundaries. If either of the boundary is null,
    # it means water can't be stored. It will take O(n) time.
    intersection = [intersector(left_greater[i], right_greater[i]) for i in range(len(arr))]

    # initialize water amount
    water = 0

    # loop in the original array, which will take O(n) time
    for i in range(len(arr)):
        if intersection[i] is not None:
            # add the amount of water by adding (intersection - arr) value at index i
            water += abs(intersection[i] - arr[i])

    return water

print(trap_rainwater([7, 4, 0, 9]))
print(trap_rainwater([6, 9, 9]))
print(trap_rainwater([7, 1, 1, 9, 9, 3, 5, 8]))
print(trap_rainwater([2,6,8,0,9,9,7]))
print(trap_rainwater([2,1,1,1,2,4,8,0,1,0,0,1,0,0,0,7,6,1]))
print(trap_rainwater([2, 1, 1, 2, 1, 1, 2, 1,1,1,2]))
