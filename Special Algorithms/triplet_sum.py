# Problem link - https://leetcode.com/problems/3sum/description/

def get_triplet_sum(arr):
    # Overall time is O(n^2) and and space is O(n) in worst case for mp set.

    # handle edge cases
    if len(arr) < 3:
        return []
    if len(arr) == 3 and sum(arr) == 0:
        return [arr]

    # initialize a set map which will store elements between `i` and `j`.
    mp = set()

    # result is initialized as set so that only unique elements are found inside it.
    result = set()

    # start looping on i from 0.
    for i in range(len(arr)):
        # start looping from i + 1 on j.
        for j in range(i + 1, len(arr)):
            # for sum equal to 0, we need req sum to be present in the slice between `i` and `j`.
            req = -(arr[i] + arr[j])

            # if req is in mp, we have found a triplet, sort it, and convert to tuple and add to
            # result set. In python only tuples can be stored in a set.
            if req in mp:
                x = [arr[i], arr[j], req]

                # as elements are only 3, it will take O(9) = O(1) time.
                x.sort()

                # O(1)
                result.add(tuple(x))

            # also ensure that you add jth element in mp so that for next iteration, it lies
            # in the slice. It takes O(1) time.
            mp.add(arr[j])

        # clear the mp once all the subsets starting with `i` are computed, takes O(1) time.
        mp.clear()

    # return the unique results.
    return result


print(
    get_triplet_sum([-1, -1, 2, 0, 1])
)

print(
    get_triplet_sum([0, 0, 0, 0])
)

print(
    get_triplet_sum([-3, 0, 1, 2, -1, 1, -2])
)

print(
    get_triplet_sum([-5, 2, -1, -2, 3])
)