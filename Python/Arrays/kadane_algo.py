# Explanation - https://www.youtube.com/watch?v=HCL4_bOd3-4

def kadane(arr):
    # This algorithm can give the maximum sum in a subarray in O(n) time and O(1) space.

    # initialize current sum to track the accumulated sum at each iteration.
    curr_sum = 0

    # initialize the max_sum as -inf, because then it will cater for all negative elements
    # in the array as well. In the video explanation, they've initialized with 0.
    max_sum = float('-inf')

    # loop in the array
    for i in range(len(arr)):
        # accumulate the sum by adding arr[i]
        curr_sum += arr[i]

        # update the maximum sum
        max_sum = max(max_sum, curr_sum)

        # at any point, if curr_sum got negative, reset it to zero.
        # This ensures that we do not take any decreasing sum into
        # our answer
        if curr_sum < 0:
            curr_sum = 0

    # finally return the maximum sum obtained.
    return max_sum


print(kadane([1, 2, -1, 6, 8, -7, 3, 1]))
print(kadane([5, -4, -2, 6, -1]))
print(kadane([-5, -4, -2, -6, -1]))