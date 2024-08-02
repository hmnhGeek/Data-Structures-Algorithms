# Problem Link - https://www.naukri.com/code360/problems/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum_842494?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=GS_OqZb2CWc&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=17

def get_min_diff(arr):
    # This is the exact same question as subset sum equals k. We could have done it using recursion,
    # memoization and tabulation as well. In recursive and memoized solution, we would have checked
    # for each target sum by making recursive calls for each sum. In tabulation, we could have achieved
    # the results in better space (by avoiding recursions), but tabulation holds useless space of O(n*k).
    # Space optimized solution directly does everything in O(k) space. Refer to that question for better
    # understanding. For now, we can say that the time complexity is O(n + k) and space complexity is O(k).
    # O(n + k) because at the end, we are also looping k times to check the minimum difference.

    sigma = sum(arr)
    target = sigma

    # create a prev row which represents the case if the slice of arr till 0th index is taken, i.e.,
    # when only the first element of the array is taken.
    prev = {tgt: False for tgt in range(target + 1)}

    # In that case, target = 0 will always be True.
    prev[0] = True
    # And target == arr[0] will also be always True.
    prev[arr[0]] = True

    # we have already defined prev for 0th index, so let's start from index = 1.
    for index in range(1, len(arr)):
        # define curr row for index = `index`
        curr = {tgt: False for tgt in range(target - max(arr), target + 1)}
        # and set target = 0 to True
        curr[0] = True

        # target = 0 is already set in prev and curr, start from 1 and check till the
        # total sum of the original array, i.e., when you are considering the full array
        # as a subset and there is no second array, i.e., s1 = sum(arr) and s2 = 0.
        for tgt in range(1, target + 1):
            left, right = False, False

            # if you've considered arr[index] in the formation of tgt and if it is present in
            # prev, then assign value from prev row for left sub-problem.
            if tgt - arr[index] in prev:
                left = prev[tgt - arr[index]]

            # if you've not considered arr[index] in the formation of tgt and if tgt is present
            # in prev, then assign value from prev row for right sub-problem.
            if tgt in prev:
                right = prev[tgt]

            # if either of the sub-problems can make target tgt, set curr[tgt] to True.
            curr[tgt] = left or right

        prev = curr

    # now the prev array has all the possible targets for all the subsets till last index of the array.
    # initialize a minimum difference as infinity.
    min_diff = float('inf')

    # Loop through all the possible sums that can be made from one subset of the array, i.e.,
    # loop from 0 till sum(arr). Check if target sum of each iteration of the loop is possible
    # or not considering till the last index of original array (prev holds these values). If
    # the sum = target is possible, update the minimum difference by taking the min of existing
    # minimum difference and abs(s1 - s2) = abs(s1 - sigma + s1) = abs(2*s1 - sigma).
    for tgt in range(sigma + 1):
        if prev[tgt]:
            min_diff = min(min_diff, abs(2 * tgt - sigma))

    # At last, you have the smallest difference in sums s1 and s2 from subsets 1 and 2 of the
    # original array.
    return min_diff


print(
    get_min_diff(
        [3, 1, 5, 2, 8]
    )
)

print(
    get_min_diff(
        [1, 2, 3, 4]
    )
)

print(
    get_min_diff(
        [8, 6, 5]
    )
)
