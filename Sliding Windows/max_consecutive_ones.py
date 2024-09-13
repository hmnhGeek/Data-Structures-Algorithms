def get_max_consecutive_ones_with_k_zeros(array, k):
    # Time complexity would be O(n) and space would be O(1).

    # assuming that we have a window of element at index 0 only
    left = right = 0

    # the window size will be 1 for 0th index.
    max_size_recorded = 1

    # assuming that number of zeroes used is 0 (although the 0th element itself
    # can be a 0, but we will capture it in the while loop).
    num_zeroes_used = 0

    # store the length of the array
    num_elements = len(array)
    # while the right pointer is within the array
    while right < num_elements:
        # if the `right` element is 0, increment the zero count and ...
        if array[right] == 0:
            num_zeroes_used += 1

            # if by any chance the count of zeroes has exceeded k, shrink the window from left
            # unless the count of zeroes <= k
            while num_zeroes_used > k:
                left += 1
                if array[left - 1] == 0:
                    num_zeroes_used -= 1

        # since you have a perfect window now, update the max window size.
        max_size_recorded = max(max_size_recorded, right - left + 1)

        # increment the right pointer by expanding the window for taking in the next element.
        right += 1

    # return the max sized window size.
    return max_size_recorded


print(get_max_consecutive_ones_with_k_zeros([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(get_max_consecutive_ones_with_k_zeros([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
print(get_max_consecutive_ones_with_k_zeros([0, 1, 1, 0, 1, 0, 1, 1], 2))
print(get_max_consecutive_ones_with_k_zeros([1, 1, 1, 0, 0, 1, 1, 1, 0, 1], 1))