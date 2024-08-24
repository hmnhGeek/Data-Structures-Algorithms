# Problem link - https://www.geeksforgeeks.org/problems/minimum-swaps-required-to-bring-all-elements-less-than-or-equal-to-k-together4847/1
# Solution - https://www.youtube.com/watch?v=0Hkh1cjnBNA


def min_swaps_for_k_together(arr, k):
    """
        Overall time complexity is O(n) and overall space complexity is O(1).
    """
    n = len(arr)

    # initialize a window size variable which will store the size of that hypothetical window
    # in which all the elements <= k.
    required_window_size = 0

    # loop in the array and get that window size in which all elements <= k can be stored. This
    # can be done in O(n) time and O(1) space.
    for i in arr:
        if i <= k:
            required_window_size += 1

    # in the first window starting from index 0 till required window size, get the count of all
    # the elements which are > k. Basically for now this is the minimum number of swaps required
    # to group all the <= k elements together because we will have to remove these "unfavourable"
    # elements with the "favorable" ones.
    greater_than_k_in_window = 0
    for i in range(required_window_size):
        if arr[i] > k:
            greater_than_k_in_window += 1

    # now, start from 1st index upto the last window. This will take another O(n) time.
    for i in range(1, n - required_window_size + 1):
        # create a local variable storing the current count of greater than k elements in the window
        local_greater_elements = greater_than_k_in_window

        # get inclusive window limits
        start = i
        end = i + required_window_size - 1

        # if the end element (which is just added) is > k, then it means that in our window one
        # unfavorable element has been added.
        if arr[end] > k:
            local_greater_elements += 1

        # if the last element which just got removed from the window was also unfavorable, then
        # decrease the count of unfavorable elements.
        if arr[start - 1] > k:
            local_greater_elements -= 1

        # finally, update the global `greater_than_k_in_window` which will act as our answer with
        # the minimum of current `greater_than_k_in_window` and `local_greater_elements` found in
        # the current window.
        greater_than_k_in_window = min(greater_than_k_in_window, local_greater_elements)

    # return the global minimum swaps required
    return greater_than_k_in_window


print(min_swaps_for_k_together([2, 1, 5, 6, 3], 3))
print(min_swaps_for_k_together([2, 7, 9, 5, 8, 7, 4], 6))
print(min_swaps_for_k_together([5, 4, 6, 10, 35, 30, 8], 9))
print(min_swaps_for_k_together([1, 15, 18, 3, 14, 18, 5], 9))
print(min_swaps_for_k_together([1, 12, 10, 3, 14, 10, 5], 8))
print(min_swaps_for_k_together([1, 1, 2, 3, 1], 1))
print(min_swaps_for_k_together([7, 3, 2, 5, 1, 6, 4], 4))