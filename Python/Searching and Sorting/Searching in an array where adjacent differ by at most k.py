# Problem link - https://www.geeksforgeeks.org/searching-array-adjacent-differ-k/


"""The idea is to start comparing from the leftmost element and find the difference between the current array element
and x. Let this difference be ‘diff’. From the given property of the array, we always know that x must be at least
‘diff/k’ away, so instead of searching one by one, we jump ‘diff/k’."""


def search_with_diff(arr, k, x):
    """
        This function takes O(n) time and O(1) space.
    """
    i = 0
    while i < len(arr):
        # if the ith element is x, return i
        if arr[i] == x:
            return i

        # Jump the difference between current array element and x divided by k.
        # We use max here to make sure that `i` moves at-least one step ahead.
        # Because it could be possible that abs() // k would return a 0.
        i += max(1, abs(arr[i] - x)//k)
    return -1


print(search_with_diff([4, 5, 6, 7, 6], 1, 6))
print(search_with_diff([20, 40, 50, 70, 70, 60], 20, 60))