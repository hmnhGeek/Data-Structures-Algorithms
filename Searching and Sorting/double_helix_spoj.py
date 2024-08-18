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
    def traverse(arr, row, col):
        # The recursion stack will take O(path length) space, i.e., O(N + 2N) = O(N) (2N for arr). The time
        # complexity would be O({2^N} * log(N)) where in at each cell we have two options, either to continue on same
        # row, or switch and at each cell we also do a binary search to check if the same value exist in the other
        # row or not.

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
        # Time complexity is thus O(N log(N)) and space complexity is O(N).

        # The approach is to merge the two arrays into a matrix. arr1 will act as row 0 and arr2 will act as row 1.
        # The one with shorter length will have -inf appended in the matrix. The reason is simple, we want that path
        # which yields max sum, and traversing on -inf will avoid that path.
        n1, n2 = len(arr1), len(arr2)
        nmax = max(n1, n2)
        arr = [[float('-inf') for _ in range(nmax)], [float('-inf') for _ in range(nmax)]]

        # fill up the matrix's first row
        for i in range(len(arr1)):
            arr[0][i] = arr1[i]

        # fill up the matrix's second row
        for j in range(len(arr2)):
            arr[1][j] = arr2[j]

        # Now we have DP problem on matrix traversal with maximum sum starting from rightmost column to the leftmost
        # column.
        n = len(arr[0])
        return max(traverse(arr, 0, n - 1), traverse(arr, 1, n - 1))

    print(get_max_path_sum([0, 2, 6, 7, 8, 9], [0, 2, 4, 5, 7, 9]))
    print(
        get_max_path_sum([3, 5, 7, 9, 20, 25, 30, 40, 55, 56, 57, 60, 62], [1, 4, 7, 11, 14, 25, 44, 47, 55, 57, 100]))
    print(get_max_path_sum([-5, 100, 1000, 1005], [-12, 1000, 1001]))


def memoized():
    def traverse(arr, row, col, dp):
        # The recursion stack will take O(path length + space of dp array) space, i.e., O(N + 2N) = O(N)
        # (assuming same length of both the arrays in worst case). The time complexity would
        # be O(N * log(N)) where in at each cell we have two options, but because of overlapping sub-problems, we can
        # reduce this from 2^N to N.

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
        # read the logic of combining the arrays in recursive solution.
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
        # The time complexity still remains O(N * log(N)) but space complexity reduces to just O(2N) = O(N) with no
        # recursion calls.

        # We first combine the two arrays.
        n1, n2 = len(arr1), len(arr2)
        nmax = max(n1, n2)
        arr = [[float('-inf') for _ in range(nmax)], [float('-inf') for _ in range(nmax)]]
        dp = {0: {i: float('-inf') for i in range(nmax)}, 1: {i: float('-inf') for i in range(nmax)}}

        for i in range(len(arr1)):
            arr[0][i] = arr1[i]

        for j in range(len(arr2)):
            arr[1][j] = arr2[j]

        n = len(arr[0])

        # we set the base conditions.
        dp[0][0] = arr[0][0]
        dp[1][0] = arr[1][0]

        # This O(2N) loop will run for the case when we assume to start from row = 0 (first array).
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

        # This O(2N) loop will run for the case when we assume to start from row = 1 (second array).
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

        # once both cases have been checked, we will finally return the maximum value from the last column of dp matrix.
        return max(dp[0][n - 1], dp[1][n - 1])

    print(get_max_path_sum([0, 2, 6, 7, 8, 9], [0, 2, 4, 5, 7, 9]))
    print(
        get_max_path_sum([3, 5, 7, 9, 20, 25, 30, 40, 55, 56, 57, 60, 62], [1, 4, 7, 11, 14, 25, 44, 47, 55, 57, 100]))
    print(get_max_path_sum([-5, 100, 1000, 1005], [-12, 1000, 1001]))


print("Recursive Solution")
recursive()

print()
print("Memoized Solution")
memoized()

print()
print("Tabulation Solution")
tabulation()