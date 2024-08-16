# Problem link - https://www.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x5651/1
# Solution - https://www.youtube.com/watch?v=UXValb-h70s

def recursive():
    def solve_smallest_subarray(arr, index, sum_to_form, recursion_depth, global_min, original_value):
        # if you've reached index 0
        if index == 0:
            # if at index 0, the sum to form is negative, this means you've got a sub array which is of more length
            # than the point from where the recursion started. Just check if it is even smaller than any previously
            # held subarray Please note that here we have not consumed index 0 into our subarray and that is why we
            # are straight away comparing the received recursion depth.
            if sum_to_form < 0:
                global_min = min(global_min, recursion_depth)

            # if the sum to form at index 0 is non-negative, check if by using arr[0] can we make it negative or not?
            # Basically, we are saying that if we used index 0 in the subarray, can we make sum greater than the sum
            # from which we started. If yes, i.e., if by consuming index 0, we can make such a sum, increase depth by
            # 1 more unit and update the global minimum length of the subarray.
            elif sum_to_form - arr[0] < 0:
                global_min = min(global_min, recursion_depth + 1)

            # otherwise, no need to do anything, simply return whatever global minimum length that we have till now.
            return global_min

        # if at any index, sum to form becomes negative, that means we have got a subarray whose sum is greater than the
        # sum from which we started. Update the global min and return it.
        if sum_to_form < 0:
            global_min = min(global_min, recursion_depth)
            return global_min

        # otherwise, go into the left recursion by consuming this index, and increase the recursion depth. Global
        # minimum length will be updated accordingly.
        global_min = solve_smallest_subarray(arr, index - 1, sum_to_form - arr[index], recursion_depth + 1, global_min, original_value)

        # now go into the right recursion, but since you're not consuming this index, reset the recursion depth back
        # to 0. Because from here, we will be finding a new subarray. Also, reset the sum to obtain to original sum,
        # because we have to find another subarray now. Please note that any updates done to global_min in left
        # recursion will have no implications on the right recursion because global_min is just for tracking purposes.
        global_min = solve_smallest_subarray(arr, index - 1, original_value, 0, global_min, original_value)

        # finally return the updated minimum length of the subarray.
        return global_min

    def find_smallest_subarray_with_sum_gt_k(arr, k):
        # Time complexity would be exponential (O(2^n)) and space complexity would be O(n)

        n = len(arr)

        # assume that the minimum length that we can obtain is infinite for the first time; we will continuously
        # reduce it.
        min_length = float('inf')

        # recursively solve this problem. we will basically count the recursion depth and reset it to 0 if we have a
        # discontinuity
        sub_array_length = solve_smallest_subarray(arr, n - 1, k, 0, min_length, k)

        # at the end, if the min_length is still infinite, then such a sub-array is not possible, return 0.
        if sub_array_length == float('inf'):
            return 0

        # else return subarray length.
        return sub_array_length

    print(find_smallest_subarray_with_sum_gt_k([1, 4, 45, 6, 0, 19], 51))
    print(find_smallest_subarray_with_sum_gt_k([1, 10, 5, 2, 7], 100))
    print(find_smallest_subarray_with_sum_gt_k([1, 10, 5, 2, 7], 9))
    print(find_smallest_subarray_with_sum_gt_k([1, 11, 100, 1, 0, 200, 3, 2, 1, 250], 280))
    print(find_smallest_subarray_with_sum_gt_k([1, 2, 4], 8))


def optimized():
    # The optimized code uses VARIABLE SLIDING WINDOW TECHNIQUE.
    # Time complexity is worst case would be O(2N) = O(N) and space would be O(1).
    # For understanding O(2N), use this example: [0, 0, 0, 99, 101] and k = 100.

    def find_smallest_subarray_with_sum_gt_k(arr, k):
        # we must keep a track of the sum obtained continuously.
        sum_tracker = 0

        # keep window limits. Initially the window size is 0.
        low, high, n = 0, 0, len(arr)

        # store the minimum length of the sub array as infinite.
        min_length = float('inf')

        # until the right boundary of the window is within the array.
        while high < n:
            # if the sum till now is less than or equal to k, we can expand more to the right.
            if sum_tracker <= k:
                sum_tracker += arr[high]
                high += 1

            # else we are just greater than k
            else:
                # update the minimum length of the subarray. Why not high - low - 1? Because in the previous iteration,
                # high = actual_high (that must be used here) + 1. Hence, this 1 cancels the -1.
                min_length = min(min_length, high - low)

                # let's start shrinking now from the left side of the window to reduce the subarray length.
                sum_tracker -= arr[low]
                low += 1

        # at last, return the minimum length obtained for the subarray.
        return min_length if min_length != float('inf') else 0

    print(find_smallest_subarray_with_sum_gt_k([1, 4, 45, 6, 0, 19], 51))
    print(find_smallest_subarray_with_sum_gt_k([1, 10, 5, 2, 7], 100))
    print(find_smallest_subarray_with_sum_gt_k([1, 10, 5, 2, 7], 9))
    print(find_smallest_subarray_with_sum_gt_k([1, 11, 100, 1, 0, 200, 3, 2, 1, 250], 280))
    print(find_smallest_subarray_with_sum_gt_k([1, 2, 4], 8))


print("Recursive solution")
recursive()
print()
print("Optimized solution using sliding window technique")
optimized()
