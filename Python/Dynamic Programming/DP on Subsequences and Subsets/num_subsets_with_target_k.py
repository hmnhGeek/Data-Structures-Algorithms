# Problem link - https://www.naukri.com/code360/problems/number-of-subsets_3952532?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=ZHyb-A2Mte4&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=18

def recursive():
    def f(arr, index, target):
        # if index is negative, return 0, target can't be formed.
        if index < 0:
            return 0

        # if target is negative, return 0, target can't be formed.
        if target < 0:
            return 0

        # if target got 0, it can be formed, return 1 as count.
        if target == 0:
            return 1

        # if on index == 0, check if 0th element is target itself or not. If yes, return count 1, else count 0.
        if index == 0:
            return 1 if target == arr[0] else 0

        # return the total count obtained by summing the cases when index from array is considered and when it
        # is not considered.
        return f(arr, index - 1, target - arr[index]) + f(arr, index - 1, target)

    def count_subsets(arr, target):
        # Overall time complexity is O(2^n) and overall space complexity is O(n).

        # if array is empty or has only one element, handle those edge cases.
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return 1 if target == arr[0] else 0

        # otherwise return the count obtained by calling the recursive function f().
        return f(arr, len(arr) - 1, target)


    print(
        count_subsets(
            [1, 2, 2, 3],
            3
        )
    )

    print(
        count_subsets(
            [1, 1, 4, 5],
            5
        )
    )

    print(
        count_subsets(
            [2, 34, 5],
            40
        )
    )

    print(
        count_subsets(
            [1, 7, 2, 9, 10],
            6
        )
    )

    print(
        count_subsets(
            [1, 2, 3, 4],
            4
        )
    )

    print(
        count_subsets(
            [6, 1, 2, 1],
            4
        )
    )


def memoized():
    def f(arr, index, target, dp):
        # if index is negative, return 0, target can't be formed.
        if index < 0:
            return 0

        # if target is negative, return 0, target can't be formed.
        if target < 0:
            return 0

        # if target got 0, it can be formed, return 1 as count.
        if target == 0:
            return 1

        # if on index == 0, check if 0th element is target itself or not. If yes, return count 1, else count 0.
        if index == 0:
            return 1 if target == arr[0] else 0

        if target in dp[index] and dp[index][target] is not None:
            return dp[index][target]

        # return the total count obtained by summing the cases when index from array is considered and when it
        # is not considered.
        dp[index][target] = f(arr, index - 1, target - arr[index], dp) + f(arr, index - 1, target, dp)
        return dp[index][target]

    def count_subsets(arr, target):
        # Overall time complexity is O(n*k) and overall space complexity is O(n*k + n).

        # if array is empty or has only one element, handle those edge cases.
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return 1 if target == arr[0] else 0

        dp = {i: {tgt: None for tgt in range(target + 1)} for i in range(len(arr))}

        # otherwise return the count obtained by calling the recursive function f().
        return f(arr, len(arr) - 1, target, dp)


    print(
        count_subsets(
            [1, 2, 2, 3],
            3
        )
    )

    print(
        count_subsets(
            [1, 1, 4, 5],
            5
        )
    )

    print(
        count_subsets(
            [2, 34, 5],
            40
        )
    )

    print(
        count_subsets(
            [1, 7, 2, 9, 10],
            6
        )
    )

    print(
        count_subsets(
            [1, 2, 3, 4],
            4
        )
    )

    print(
        count_subsets(
            [6, 1, 2, 1],
            4
        )
    )


def tabulation():
    def count_subsets(arr, target):
        # Overall time complexity is O(n*k) and overall space complexity is O(n*k), because recursion is eliminated.

        # if array is empty or has only one element, handle those edge cases.
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return 1 if target == arr[0] else 0

        # initialize a n*k dp array with count of subsets with target sums = tgt as 0 for all indices in the array.
        dp = {i: {tgt: 0 for tgt in range(target + 1)} for i in range(len(arr))}

        # for each index in the dp array, at target = 0, set count as 1, because target = 0 is a valid response.
        for index in dp:
            dp[index][0] = 1

        # for index 0, at target == arr[0], set count as 1.
        dp[0][arr[0]] = 1

        # we have completed the cases of index = 0, start from index = 1 till end (reverse of memoization).
        for index in range(1, len(arr)):
            # we have completed the case of target = 0, start from target = 1 till required target.
            for tgt in range(1, target + 1):
                # initialize left and right as 0, 0.
                left, right = 0, 0

                # if the tgt was considered in the previous index, get its value in left.
                if tgt - arr[index] in dp[index - 1]:
                    left = dp[index - 1][tgt - arr[index]]

                # if the tgt was not considered in the previous index, get its value in right.
                if tgt in dp[index - 1]:
                    right = dp[index - 1][tgt]

                # update the tgt value for current index as the sum of counts received from both the
                # cases in previous indices.
                dp[index][tgt] = left + right

        # at the end, answer lies in the last row of the dp array with target as last row's index.
        return dp[len(arr) - 1][target]

    print(
        count_subsets(
            [1, 2, 2, 3],
            3
        )
    )

    print(
        count_subsets(
            [1, 1, 4, 5],
            5
        )
    )

    print(
        count_subsets(
            [2, 34, 5],
            40
        )
    )

    print(
        count_subsets(
            [1, 7, 2, 9, 10],
            6
        )
    )

    print(
        count_subsets(
            [1, 2, 3, 4],
            4
        )
    )

    print(
        count_subsets(
            [6, 1, 2, 1],
            4
        )
    )


def space_optimized():
    def count_subsets(arr, target):
        # Overall time complexity is O(n*k) and overall space complexity is O(k), because only a single row for the
        # prev will be used.

        # if array is empty or has only one element, handle those edge cases.
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return 1 if target == arr[0] else 0

        # initialize a k-length dp array with count of subsets with target sums = tgt as 0 for all 0th index of array.
        prev = {tgt: 0 for tgt in range(target + 1)}

        # set the count of target = 0 for index = 0 as 1.
        prev[0] = 1

        # for index 0, at target == arr[0], set count as 1.
        prev[arr[0]] = 1

        # we have completed the cases of index = 0, start from index = 1 till end (reverse of memoization).
        for index in range(1, len(arr)):
            # initialize curr row.
            curr = {tgt: 0 for tgt in range(target + 1)}
            # even in the curr row (representing index = `index`), at target = 0, count will be 1.
            curr[0] = 1

            # we have completed the case of target = 0, start from target = 1 till required target.
            for tgt in range(1, target + 1):
                # initialize left and right as 0, 0.
                left, right = 0, 0

                # if the tgt was considered in the previous index, get its value in left.
                if tgt - arr[index] in prev:
                    left = prev[tgt - arr[index]]

                # if the tgt was not considered in the previous index, get its value in right.
                if tgt in prev:
                    right = prev[tgt]

                # update the tgt value for current index as the sum of counts received from both the
                # cases in previous indices.
                curr[tgt] = left + right
            prev = curr

        # at the end, answer lies in the last row of the dp array with target as last row's index.
        return prev[target]

    print(
        count_subsets(
            [1, 2, 2, 3],
            3
        )
    )

    print(
        count_subsets(
            [1, 1, 4, 5],
            5
        )
    )

    print(
        count_subsets(
            [2, 34, 5],
            40
        )
    )

    print(
        count_subsets(
            [1, 7, 2, 9, 10],
            6
        )
    )

    print(
        count_subsets(
            [1, 2, 3, 4],
            4
        )
    )

    print(
        count_subsets(
            [6, 1, 2, 1],
            4
        )
    )


print("Recursive Solution")
recursive()

print()
print("Memoized Solution")
memoized()

print()
print("Tabulation Solution")
tabulation()

print()
print("Space Optimized Solution")
space_optimized()