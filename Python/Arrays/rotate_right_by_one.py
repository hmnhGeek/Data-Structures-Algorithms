# Problem link - https://www.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1


def rotate(arr):
    """
        Time complexity is O(n) and space complexity is O(1).
    """
    prev, temp, n = arr[0], None, len(arr)

    # start from index = 1 as index = 0 is stored in prev.
    for i in range(1, n):
        # store the current index value in temp.
        temp = arr[i]
        # assign the current index with prev value.
        arr[i] = prev
        # update prev to temp.
        prev = temp

    # finally, prev would have the last element. Update arr[0] with prev.
    arr[0] = prev


# Example 1
a = [1, 2, 3, 4, 5]
rotate(a)
print(a)

# Example 2
b = [9, 8, 7, 6, 4, 2, 1, 3]
rotate(b)
print(b)