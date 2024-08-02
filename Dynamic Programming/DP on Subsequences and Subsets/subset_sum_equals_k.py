# Problem link - https://www.naukri.com/code360/problems/subset-sum-equal-to-k_1550954?leftPanelTab=1%3Fsource%3Dyoutube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=fWX9xDmIzRI&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=15

def recursive():
    def f(arr, index, target):
        # if at any point you were able to reach a negative index,
        # that means you still have a target (because target == 0 check
        # is placed below). In this case, irrespective of what target is
        # return False.
        if index < 0:
            return False

        # if index is non-negative, but target became negative, that means
        # the numbers in the array cannot form the target, return False.
        if target < 0:
            return False

        # if index is non-negative and target became 0, that means a subset
        # is possible which can form the target from the array.
        if target == 0:
            return True

        # if index is 0 and target is equal to element at index 0, return True
        # as the final leftover can be made using arr[0]
        if index == 0:
            return arr[0] == target

        # in the recursive call, simply take the OR of the cases when you take the
        # index value and when you not.
        return f(arr, index - 1, target - arr[index]) or f(arr, index - 1, target)

    def is_sum_possible(arr, target):
        # At each index we have 2 choices. Thus, we say, time complexity is O(2^n)
        # and space complexity is O(n) for the recursion stack.

        # avoid recursion if possible.
        if len(arr) == 0:
            return False
        if len(arr) == 1:
            return arr[0] == target

        # we will make a call from the end of the array. Let us make a call to f()
        # and check if last index can make a target or not. Internally, this function
        # will handle the cases when `n-1` is picked and when it is not picked.
        n = len(arr)
        return f(arr, n - 1, target)

    print(
        is_sum_possible(
            [6, 1, 2, 1],
            4
        )
    )

    print(
        is_sum_possible(
            [1, 7, 2, 9, 10],
            6
        )
    )

    print(
        is_sum_possible(
            [1, 2, 3, 4],
            4
        )
    )

    print(
        is_sum_possible(
            [3, 34, 4, 12, 5, 2],
            9
        )
    )

    print(
        is_sum_possible(
            [3, 34, 4, 12, 5, 2],
            30
        )
    )


def memoized():
    def f(arr, index, target, dp):
        # if at any point you were able to reach a negative index,
        # that means you still have a target (because target == 0 check
        # is placed below). In this case, irrespective of what target is
        # return False.
        if index < 0:
            return False

        # if index is non-negative, but target became negative, that means
        # the numbers in the array cannot form the target, return False.
        if target < 0:
            return False

        # if index is non-negative and target became 0, that means a subset
        # is possible which can form the target from the array.
        if target == 0:
            return True

        # if index is 0 and target is equal to element at index 0, return True
        # as the final leftover can be made using arr[0]
        if index == 0:
            return arr[0] == target

        if target in dp[index] and dp[index][target] is not None:
            return dp[index][target]

        # in the recursive call, simply take the OR of the cases when you take the
        # index value and when you not.
        dp[index][target] = f(arr, index - 1, target - arr[index], dp) or f(arr, index - 1, target, dp)
        return dp[index][target]

    def is_sum_possible(arr, target):
        # Because of memoization, we have reduced calls to recursive f() for overlapping
        # sub-problems, and thus, time complexity is now O(n). Space complexity is O(n + n*target)
        # for the recursion stack and the dp array.

        # avoid recursion if possible.
        if len(arr) == 0:
            return False
        if len(arr) == 1:
            return arr[0] == target

        # it's a very complicated search space to think of. For indices, it's simple, simply go from 0
        # till n - 1. However, for target, we need to think a little. Consider this example [1, 7, 2, 9, 10]
        # with target = 6. At the least, what can target range go to? Shouldn't it go till target - max(arr), i.e.,
        # 6 - 10 = -4. Check by drawing recursion tree, and you will see that this statement is true. At max,
        # target range can go till target, i.e., 6. Hence, the target search space is from -4 to 6.
        dp = {i: {tgt: None for tgt in range(target - max(arr), target + 1)} for i in range(len(arr))}

        # we will make a call from the end of the array. Let us make a call to f()
        # and check if last index can make a target or not. Internally, this function
        # will handle the cases when `n-1` is picked and when it is not picked.
        n = len(arr)
        return f(arr, n - 1, target, dp)

    print(
        is_sum_possible(
            [6, 1, 2, 1],
            4
        )
    )

    print(
        is_sum_possible(
            [1, 7, 2, 9, 10],
            6
        )
    )

    print(
        is_sum_possible(
            [1, 2, 3, 4],
            4
        )
    )

    print(
        is_sum_possible(
            [3, 34, 4, 12, 5, 2],
            9
        )
    )

    print(
        is_sum_possible(
            [3, 34, 4, 12, 5, 2],
            30
        )
    )


def tabulation():
    def is_sum_possible(arr, target):
        # Time complexity is now O(n). Space complexity is O(n*target) for the dp array.

        # avoid recursion if possible.
        if len(arr) == 0:
            return False
        if len(arr) == 1:
            return arr[0] == target

        # it's a very complicated search space to think of. For indices, it's simple, simply go from 0
        # till n - 1. However, for target, we need to think a little. Consider this example [1, 7, 2, 9, 10]
        # with target = 6. At the least, what can target range go to? Shouldn't it go till target - max(arr), i.e.,
        # 6 - 10 = -4. Check by drawing recursion tree, and you will see that this statement is true. At max,
        # target range can go till target, i.e., 6. Hence, the target search space is from -4 to 6.
        dp = {i: {tgt: False for tgt in range(target - max(arr), target + 1)} for i in range(len(arr))}

        # for all the indices, set the value of target = 0 to True, because at any index, if we find target = 0,
        # we can say that target can be achieved in this array.
        for index in dp:
            dp[index][0] = True

        # for the index = 0, target is achievable if target == arr[0]. In our target search space,
        # we can manually set dp[0]'s that index where target and arr[0] are same to True, right?
        # That's what I have done here.
        dp[0][arr[0]] = True

        n = len(arr)

        # we have already set values for target = 0 and index = 0, let us start looping both of them
        # from values 1.
        for index in range(1, n):
            for tgt in range(1, target + 1):
                # additional checks for left and right, assume initially for them to be false only.
                # consider this case: in array [1, 7, 2, 9, 10] when in this loop tgt = 1 and index = 1,
                # in that case, tgt - arr[index] = -6 which is not present in our dp target space which
                # is from -4 to 6. Hence, we will by default mark left and right as False. Technically,
                # what this means is that when you come to index 1 in the array, you can never have target
                # as 1, that's why ou search space is also reduced.
                left, right = False, False

                if tgt - arr[index] in dp[index - 1]:
                    left = dp[index - 1][tgt - arr[index]]
                if tgt in dp[index - 1]:
                    right = dp[index - 1][tgt]

                dp[index][tgt] = left or right

        # final answer always lie at the last index.
        return dp[n - 1][target]



    print(
        is_sum_possible(
            [6, 1, 2, 1],
            4
        )
    )

    print(
        is_sum_possible(
            [1, 7, 2, 9, 10],
            6
        )
    )

    print(
        is_sum_possible(
            [1, 2, 3, 4],
            4
        )
    )

    print(
        is_sum_possible(
            [3, 34, 4, 12, 5, 2],
            9
        )
    )

    print(
        is_sum_possible(
            [3, 34, 4, 12, 5, 2],
            30
        )
    )


def space_optimized():
    def is_sum_possible(arr, target):
        # Time complexity is now O(n). Space complexity is O(target) for the dp array.

        # avoid recursion if possible.
        if len(arr) == 0:
            return False
        if len(arr) == 1:
            return arr[0] == target

        # it's a very complicated search space to think of. For indices, it's simple, simply go from 0
        # till n - 1. However, for target, we need to think a little. Consider this example [1, 7, 2, 9, 10]
        # with target = 6. At the least, what can target range go to? Shouldn't it go till target - max(arr), i.e.,
        # 6 - 10 = -4. Check by drawing recursion tree, and you will see that this statement is true. At max,
        # target range can go till target, i.e., 6. Hence, the target search space is from -4 to 6.

        # Currently, prev denotes target space for index = 0, and so, we will start from index = 1.
        prev = {tgt: False for tgt in range(target - max(arr), target + 1)}

        # set the value of target = 0 to True for index = 0.
        prev[0] = True

        # for the index = 0, target is achievable if target == arr[0].
        prev[arr[0]] = True

        n = len(arr)

        # we have already set values for target = 0 and index = 0, let us start looping both of them
        # from values 1.
        for index in range(1, n):
            curr = {tgt: False for tgt in range(target - max(arr), target + 1)}

            # always mark target = 0 in curr as True.
            curr[0] = True

            for tgt in range(1, target + 1):
                # additional checks for left and right, assume initially for them to be false only.
                # consider this case: in array [1, 7, 2, 9, 10] when in this loop tgt = 1 and index = 1,
                # in that case, tgt - arr[index] = -6 which is not present in our dp target space which
                # is from -4 to 6. Hence, we will by default mark left and right as False. Technically,
                # what this means is that when you come to index 1 in the array, you can never have target
                # as 1, that's why ou search space is also reduced.
                left, right = False, False

                if tgt - arr[index] in prev:
                    left = prev[tgt - arr[index]]
                if tgt in prev:
                    right = prev[tgt]

                curr[tgt] = left or right
            prev = curr

        # final answer always lie at the last index.
        return prev[target]



    print(
        is_sum_possible(
            [6, 1, 2, 1],
            4
        )
    )

    print(
        is_sum_possible(
            [1, 7, 2, 9, 10],
            6
        )
    )

    print(
        is_sum_possible(
            [1, 2, 3, 4],
            4
        )
    )

    print(
        is_sum_possible(
            [3, 34, 4, 12, 5, 2],
            9
        )
    )

    print(
        is_sum_possible(
            [3, 34, 4, 12, 5, 2],
            30
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