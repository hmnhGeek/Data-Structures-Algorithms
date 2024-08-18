def get_idx_from(arr, elem):
    # Typical binary search to find the index of element `elem` in array `arr`, if any, else None.
    # This will take O(log(N)) time.
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = int(low + (high - low) / 2)

        if arr[mid] == elem:
            return mid

        if arr[mid] > elem:
            high = mid - 1
        else:
            low = mid + 1
    return None


def recursive():
    def traverse(arr1, arr2, row, col):
        # The recursion stack will take O(path length) space, i.e., O(max(len(arr1), len(arr2)) = O(N) (assuming same
        # length of both the arrays in worst case). The time complexity would be O({2^N} * log(N)) where in at each
        # cell we have two options, either to continue on same array, or switch and at each cell we also do a binary
        # search to check if the same value exist in the other array or not.

        # if at any point row becomes negative, return -inf so that in max() function, the other value is picked.
        if row < 0:
            return float('-inf')

        # if you managed to reach the 0th index of any of the array, return their value at 0th index.
        if row == 0:
            return arr1[row] if col == 0 else arr2[row]

        # again, one option is to continue on the same array; we will call it left recursion; just move to previous
        # index on the same array.
        left = traverse(arr1, arr2, row - 1, col)

        # the right recursion is little tricky. We first store the value of the current cell
        right = float('-inf')
        if col == 0:
            # you are on a cell of first array.
            curr_val = arr1[row]
            # get the index of the same cell value in the other array, if the value exists, otherwise we will get a
            # None.
            switch_idx = get_idx_from(arr2, curr_val)
        else:
            # you are on a cell of second array.
            curr_val = arr2[row]
            # get the index of the same cell value in the other array, if the value exists, otherwise we will get a
            # None.
            switch_idx = get_idx_from(arr1, curr_val)

        # if the same cell value is found in the other array as well, then we must have an intersection. The right
        # recursion would be row - 1 of the other array, i.e., switch_idx - 1 of the other array, because the common
        # value is already taken from this array (on which we are right now).
        if switch_idx is not None:
            # to switch the array, ensure that you change the col value.
            right = traverse(arr1, arr2, switch_idx - 1, 1 if col == 0 else 0)

        # finally, add the current cell's value to the max of left and right recursion and return it.
        return curr_val + max(left, right)

    def get_max_path_sum(arr1, arr2):
        n1 = len(arr1)
        n2 = len(arr2)

        # we have two options:
        # Option 1: Start the traversal from arr1, i.e., col = 0 and row = n1 - 1
        # Option 2: Start the traversal from arr2, i.e., col = 1 and row = n2 - 1
        # We return the max() path sum
        return max(traverse(arr1, arr2, n1 - 1, 0), traverse(arr1, arr2, n2 - 1, 1))

    print(get_max_path_sum([0, 2, 6, 7, 8, 9], [0, 2, 4, 5, 7, 9]))
    print(get_max_path_sum([3, 5, 7, 9, 20, 25, 30, 40, 55, 56, 57, 60, 62], [1, 4, 7, 11, 14, 25, 44, 47, 55, 57, 100]))
    print(get_max_path_sum([-5, 100, 1000, 1005], [-12, 1000, 1001]))


def memoized():
    def traverse(arr1, arr2, row, col, dp):
        # The recursion stack will take O(path length + space of dp array) space, i.e., O(max(len(arr1), len(arr2)) +
        # 2*N) = O(N + 2N) = O(N) (assuming same length of both the arrays in worst case). The time complexity would
        # be O(N * log(N)) where in at each cell we have two options, but because of overlapping sub-problems, we can
        # reduce this from 2^N to N.

        # if at any point row becomes negative, return -inf so that in max() function, the other value is picked.
        if row < 0:
            return float('-inf')

        # if you managed to reach the 0th index of any of the array, return their value at 0th index.
        if row == 0:
            return arr1[row] if col == 0 else arr2[row]

        if dp[row][col] is not None:
            return dp[row][col]

        # again, one option is to continue on the same array; we will call it left recursion; just move to previous
        # index on the same array.
        left = traverse(arr1, arr2, row - 1, col, dp)

        # the right recursion is little tricky. We first store the value of the current cell
        right = float('-inf')
        if col == 0:
            # you are on a cell of first array.
            curr_val = arr1[row]
            # get the index of the same cell value in the other array, if the value exists, otherwise we will get a
            # None.
            switch_idx = get_idx_from(arr2, curr_val)
        else:
            # you are on a cell of second array.
            curr_val = arr2[row]
            # get the index of the same cell value in the other array, if the value exists, otherwise we will get a
            # None.
            switch_idx = get_idx_from(arr1, curr_val)

        # if the same cell value is found in the other array as well, then we must have an intersection. The right
        # recursion would be row - 1 of the other array, i.e., switch_idx - 1 of the other array, because the common
        # value is already taken from this array (on which we are right now).
        if switch_idx is not None:
            # to switch the array, ensure that you change the col value.
            right = traverse(arr1, arr2, switch_idx - 1, 1 if col == 0 else 0, dp)

        # finally, add the current cell's value to the max of left and right recursion and return it.
        dp[row][col] = curr_val + max(left, right)
        return dp[row][col]

    def get_max_path_sum(arr1, arr2):
        n1 = len(arr1)
        n2 = len(arr2)

        # we have two options:
        # Option 1: Start the traversal from arr1, i.e., col = 0 and row = n1 - 1
        # Option 2: Start the traversal from arr2, i.e., col = 1 and row = n2 - 1
        # We return the max() path sum
        dp1 = {i: {0: None, 1: None} for i in range(n1)}
        dp2 = {i: {0: None, 1: None} for i in range(n2)}
        return max(traverse(arr1, arr2, n1 - 1, 0, dp1), traverse(arr1, arr2, n2 - 1, 1, dp2))

    print(get_max_path_sum([0, 2, 6, 7, 8, 9], [0, 2, 4, 5, 7, 9]))
    print(get_max_path_sum([3, 5, 7, 9, 20, 25, 30, 40, 55, 56, 57, 60, 62], [1, 4, 7, 11, 14, 25, 44, 47, 55, 57, 100]))
    print(get_max_path_sum([-5, 100, 1000, 1005], [-12, 1000, 1001]))


def recursive2():
    def traverse(arr, row, col):
        # The recursion stack will take O(path length) space, i.e., O(N). The time complexity would be
        # O({2^N} * log(N)) where in at each cell we have two options, either to continue on same row,
        # or switch and at each cell we also do a binary search to check if the same value exist in the
        # other row or not.

        # if at any point row becomes negative, return -inf so that in max() function, the other value is picked.
        if col < 0:
            return float('-inf')

        # if you managed to reach column 0, return the value of the cell you're on.
        if col == 0:
            return arr[row][col]

        # one option is to continue on the same row; we will call it left recursion; just move to previous column.
        left = traverse(arr, row, col - 1)

        # the right recursion is little tricky. We first store the value of the current cell. Also, for now we will
        # assume that right recursion is not possible, i.e., you cannot switch to the other row.
        right = float('-inf')
        cell_val = arr[row][col]

        # To check if we can switch or not, we will use binary search on the other row and check if the same value on
        # which we are standing right now is present in the other row or not.
        if row == 0:
            switch_idx = get_idx_from(arr[1], cell_val)
        else:
            switch_idx = get_idx_from(arr[0], cell_val)

        # if the same cell value is found in the other row as well, then we must have an intersection. The right
        # recursion would be col - 1 of the other row, i.e., switch_idx - 1 of the other row, because the common
        # value is already taken from this row (on which we are right now).
        if switch_idx is not None:
            # to switch the row, ensure that you change the row value.
            right = traverse(arr, 1 if row == 0 else 0, switch_idx - 1)

        # finally, add the current cell's value to the max of left and right recursion and return it.
        return cell_val + max(left, right)

    def get_max_path_sum(arr1, arr2):
        n1, n2 = len(arr1), len(arr2)
        nmax = max(n1, n2)
        arr = [[float('-inf') for _ in range(nmax)], [float('-inf') for _ in range(nmax)]]

        for i in range(len(arr1)):
            arr[0][i] = arr1[i]

        for j in range(len(arr2)):
            arr[1][j] = arr2[j]

        n = len(arr[0])
        return max(traverse(arr, 0, n - 1), traverse(arr, 1, n - 1))

    print(get_max_path_sum([0, 2, 6, 7, 8, 9], [0, 2, 4, 5, 7, 9]))
    print(
        get_max_path_sum([3, 5, 7, 9, 20, 25, 30, 40, 55, 56, 57, 60, 62], [1, 4, 7, 11, 14, 25, 44, 47, 55, 57, 100]))
    print(get_max_path_sum([-5, 100, 1000, 1005], [-12, 1000, 1001]))


def memoized2():
    def traverse(arr, row, col, dp):
        if col < 0:
            return float('-inf')

        if col == 0:
            return arr[row][col]

        if dp[row][col] is not None:
            return dp[row][col]

        left = traverse(arr, row, col - 1, dp)
        right = float('-inf')
        cell_val = arr[row][col]

        if row == 0:
            switch_idx = get_idx_from(arr[1], cell_val)
        else:
            switch_idx = get_idx_from(arr[0], cell_val)

        if switch_idx is not None:
            right = traverse(arr, 1 if row == 0 else 0, switch_idx - 1, dp)

        dp[row][col] = cell_val + max(left, right)
        return dp[row][col]

    def get_max_path_sum(arr1, arr2):
        n1, n2 = len(arr1), len(arr2)
        nmax = max(n1, n2)
        arr = [[float('-inf') for _ in range(nmax)], [float('-inf') for _ in range(nmax)]]
        dp = [[None for _ in range(nmax)], [None for _ in range(nmax)]]

        for i in range(len(arr1)):
            arr[0][i] = arr1[i]

        for j in range(len(arr2)):
            arr[1][j] = arr2[j]

        n = len(arr[0])
        return max(traverse(arr, 0, n - 1, dp), traverse(arr, 1, n - 1, dp))

    print(get_max_path_sum([0, 2, 6, 7, 8, 9], [0, 2, 4, 5, 7, 9]))
    print(
        get_max_path_sum([3, 5, 7, 9, 20, 25, 30, 40, 55, 56, 57, 60, 62], [1, 4, 7, 11, 14, 25, 44, 47, 55, 57, 100]))
    print(get_max_path_sum([-5, 100, 1000, 1005], [-12, 1000, 1001]))


def tabulation():
    def get_max_path_sum(arr1, arr2):
        n1, n2 = len(arr1), len(arr2)
        nmax = max(n1, n2)
        arr = [[float('-inf') for _ in range(nmax)], [float('-inf') for _ in range(nmax)]]
        dp = {0: {i: float('-inf') for i in range(nmax)}, 1: {i: float('-inf') for i in range(nmax)}}

        for i in range(len(arr1)):
            arr[0][i] = arr1[i]

        for j in range(len(arr2)):
            arr[1][j] = arr2[j]

        n = len(arr[0])
        dp[0][0] = arr[0][0]
        dp[1][0] = arr[1][0]

        for row in range(2):
            for col in range(1, n):
                left = dp[row][col - 1]
                right = float('-inf')
                cell_val = arr[row][col]

                if row == 0:
                    switch_idx = get_idx_from(arr[1], cell_val)
                else:
                    switch_idx = get_idx_from(arr[0], cell_val)

                if switch_idx is not None and switch_idx > 0:
                    right = dp[1 if row == 0 else 0][switch_idx - 1]

                dp[row][col] = cell_val + max(left, right)

        for row in range(1, -1, -1):
            for col in range(1, n):
                left = dp[row][col - 1]
                right = float('-inf')
                cell_val = arr[row][col]

                if row == 0:
                    switch_idx = get_idx_from(arr[1], cell_val)
                else:
                    switch_idx = get_idx_from(arr[0], cell_val)

                if switch_idx is not None and switch_idx > 0:
                    right = dp[1 if row == 0 else 0][switch_idx - 1]

                dp[row][col] = cell_val + max(left, right)

        return max(dp[0][n - 1], dp[1][n - 1])

    print(get_max_path_sum([0, 2, 6, 7, 8, 9], [0, 2, 4, 5, 7, 9]))
    print(
        get_max_path_sum([3, 5, 7, 9, 20, 25, 30, 40, 55, 56, 57, 60, 62], [1, 4, 7, 11, 14, 25, 44, 47, 55, 57, 100]))
    print(get_max_path_sum([-5, 100, 1000, 1005], [-12, 1000, 1001]))


tabulation()