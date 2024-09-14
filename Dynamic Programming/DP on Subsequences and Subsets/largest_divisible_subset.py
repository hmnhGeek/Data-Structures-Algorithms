# Problem link - https://www.naukri.com/code360/problems/divisible-set_3754960?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=gDuZwBW9VvM&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=46


def divisible_nums(x, y):
    if x is None or y is None:
        return True
    return x % y == 0 or y % x == 0


def self_solution():
    def solve_for_largest_divisible_subset(arr, index, largest_divisible_subset, prev_value):
        # The time complexity of this solution is O(2^n) and space would be O(n + n) {one extra `n` for largest
        # subset arr}.

        # if you've reached index 0
        if index == 0:
            # check if 0th index element and previous value are divisible or not.
            if divisible_nums(arr[0], prev_value):
                # if yes, then add the 0th element to the largest subset
                largest_divisible_subset += [arr[0]]
            # finally, return the largest subset
            return largest_divisible_subset

        # assuming left recursion is not possible
        left = []
        # however, if array element at this index and previous value are divisible, then do a left recursion
        if divisible_nums(arr[index], prev_value):
            # do a left recursion by going to one lower index, adding the current element into the largest subset and
            # updating the prev_value to current element.
            left = solve_for_largest_divisible_subset(arr, index - 1, largest_divisible_subset + [arr[index]],
                                                      arr[index])

        # do a right recursion by simply avoiding the current index element into the largest subset and keep the same
        # prev_value
        right = solve_for_largest_divisible_subset(arr, index - 1, largest_divisible_subset, prev_value)

        # finally, update the largest subset with the max list obtained from the left or right recursion and return it.
        largest_divisible_subset = max(left, right, key=len)
        return largest_divisible_subset

    def get_largest_divisible_subset(arr):
        n = len(arr)
        # create a copy of the original array to avoid changing the input array
        copy = [i for i in arr]
        # sort the copied array
        copy.sort()

        # solve the problem starting from last index using recursion
        return solve_for_largest_divisible_subset(copy, n - 1, [], None)

    print(get_largest_divisible_subset([1, 16, 7, 8, 4]))
    print(get_largest_divisible_subset([1, 2, 5]))
    print(get_largest_divisible_subset([3, 3, 3]))
    print(get_largest_divisible_subset([2, 4, 3, 8]))


def get_largest_divisible_subset(arr):
    # Overall time complexity is O(n^2) and space complexity is O(n).

    n = len(arr)

    # sort the array which will take O(nlog(n))
    arr.sort()

    # assuming that each index has only one subset initially (ending at itself).
    dp = {i: 1 for i in range(n)}

    # assuming that each element is the self-parent
    parents = {i: i for i in range(n)}

    # loop on all the indices which will take O(n^2)
    for i in range(n):
        # start another loop from ith index till end.
        for prev in range(i):
            # if the element at index i and at index `prev` are divisible and if adding this ith index to the subset
            # of prev will increase the subset length of current ith index, then include this ith element in the subset
            if divisible_nums(arr[i], arr[prev]) and 1 + dp[prev] > dp[i]:
                dp[i] = 1 + dp[prev]
                parents[i] = prev

    largest_subset_length_index = max(dp, key=dp.get)
    largest_divisible_subset = []

    # start iterating from the last index and obtain the sequence by following the parents.
    start = largest_subset_length_index
    while parents[start] != start:
        largest_divisible_subset.append(arr[start])
        start = parents[start]

    # once at the ultimate parent, include that as well
    largest_divisible_subset.append(arr[start])
    return largest_divisible_subset


print("My Solution")
self_solution()

print()
print("Video Solution")
print(get_largest_divisible_subset([1, 16, 7, 8, 4]))
print(get_largest_divisible_subset([1, 2, 5]))
print(get_largest_divisible_subset([3, 3, 3]))
print(get_largest_divisible_subset([2, 4, 3, 8]))