# Problem link - https://leetcode.com/problems/3sum/description/

def using_sets():
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


def no_extra_space():
    def get_triplet_sum(arr):
        # overall time complexity is O(n * log(n) + n^2) and space is O(1).

        # handle the base cases
        if len(arr) < 3:
            return []
        if len(arr) == 3 and sum(arr):
            return [arr]

        # sort the array in O(n * log(n)) time.
        arr.sort()
        result = set()

        # this will take O(n^2) time to run both the loops.
        for i in range(len(arr)):
            # if i != 0 go till that `i` which is not equal to its previous
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            # initialize j and k.
            j = i + 1
            k = len(arr) - 1

            while j < k:
                s = arr[i] + arr[j] + arr[k]

                if s > 0:
                    # if sum is greater than 0, we need to reduce k to reduce sum
                    k -= 1
                elif s < 0:
                    # if sum is less than 0, we need to increase j to increase sum
                    j += 1
                else:
                    # if sum is 0, then add it to result, decrease k and increase j.
                    result.add((arr[i], arr[j], arr[k]))
                    j += 1
                    k -= 1

                    # move j and k until they are different from their previous values
                    # and also ensure that they do not go out of bounds
                    if j < k and arr[j] == arr[j - 1]:
                        j += 1
                    if j < k and arr[k] == arr[k + 1]:
                        k -= 1

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

print("Without extra space")
no_extra_space()
print()
print("With extra space but no sorting")
using_sets()