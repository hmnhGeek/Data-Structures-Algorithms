# Problem link - https://www.geeksforgeeks.org/move-negative-numbers-beginning-positive-end-constant-extra-space/


def move(arr):
    """
        Time complexity is O(n) and space complexity is O(1).
    """

    # define two pointers pointing to start and end of the list.
    i, j = 0, len(arr) - 1

    # while i < j, i.e., we don't even want them to be equal.
    while i < j:
        # if both of them are positive, decrement j, we want to find a negative element
        # on the right which we can swap with the positive element on left.
        if arr[i] >= 0 and arr[j] >= 0:
            j -= 1

        # if left element is positive and right element is negative, swap, and move ahead.
        elif arr[i] >= 0 and arr[j] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

        # if left element is negative but right element is positive, its the correct format.
        # move ahead.
        elif arr[i] < 0 and arr[j] >= 0:
            i += 1
            j -= 1

        # if both are negative, increment left part, until we find a positive element which we
        # can swap with the right negative element.
        else:
            i += 1

    # once swapping is finished, print the array.
    print(arr)


move([-12, 11, -13, -5, 6, -7, 5, -3, -6])
move([-1, 2, -3, 4, 5, 6, -7, 8, 9])
move([-12, 11, -13, -5, 6, -7, 5, -3, 11])
move([1, 2,  -4, -5, 2, -7, 3, 2, -6, -8, -9, 3, 2,  1])