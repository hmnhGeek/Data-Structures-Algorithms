def recursive():
    """
        Time complexity is exponential and space complexity is O(n + m).
    """

    def solve(mtx, i, a, b, n, m):
        # if alice and bob have reached 0th row
        if i == 0:
            # if alice is at (0, 0)
            if a == 0:
                # then chocolates for sure will contain mtx[0][0]
                _sum = mtx[0][0]
                # if bob is also at its place, i.e., (0, m - 1), then add bob's chocolates also.
                if b == m - 1:
                    _sum += mtx[0][m - 1]
                # finally, return the chocolates
                return _sum
            else:
                # however, if alice is not at (0, 0)

                # and bob is at its place, then return only bob's chocolates
                if b == m - 1:
                    return mtx[0][m - 1]
                else:
                    # if both of them are at wrong places, return 0 chocolates.
                    return 0

        # initialize a cost variable to find the max chocolates collected from all the paths.
        cost = 0
        for da in [-1, 0, 1]:
            for db in [-1, 0, 1]:
                next_a, next_b = a + da, b + db
                if 0 <= next_a < m and 0 <= next_b < m and 0 <= i - 1 < n:
                    count = solve(mtx, i - 1, next_a, next_b, n, m)
                    # if both alice and bob are at same cell, add chocolate only once.
                    if a == b:
                        count += mtx[i][a]
                    else:
                        # else add chocolates of both
                        count += mtx[i][a] + mtx[i][b]
                    # update the max chocolates
                    cost = max(cost, count)
        # return the max chocolates obtained.
        return cost

    def cherry_pickup(mtx):
        n, m = len(mtx), len(mtx[0])
        max_chocos = 0
        # initialize starting points of alice and bob by looping m^2 times.
        for alice in range(m):
            for bob in range(m):
                # retrieve the max chocolates obtained
                cost = solve(mtx, n - 1, alice, bob, n, m)
                # update the max chocolates
                max_chocos = max(max_chocos, cost)
        # return the max chocolates obtained.
        return max_chocos

    print(
        cherry_pickup(
            [
                [2, 3, 1, 2],
                [3, 4, 2, 2],
                [5, 6, 3, 5]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [1, 1],
                [1, 2]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [3, 7],
                [7, 6]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [4, 5],
                [3, 7],
                [4, 2]
            ]
        )
    )

    print(cherry_pickup([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))
    print(
        cherry_pickup(
            [
                [4, 1, 2],
                [3, 6, 1],
                [1, 6, 6],
                [3, 1, 2]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [2, 0, 0, 0, 0, 0, 2],
                [2, 1, 0, 0, 0, 4, 0],
                [2, 0, 10, 0, 1, 0, 0],
                [0, 3, 0, 6, 5, 0, 0],
                [1, 0, 3, 4, 0, 0, 6]
            ]
        )
    )


def memoized():
    """
        Time complexity is O(m^2 * m^2 * n) and space complexity is O(n + m + nm^2).
    """

    def solve(mtx, i, a, b, n, m, dp):
        # if alice and bob have reached 0th row
        if i == 0:
            # if alice is at (0, 0)
            if a == 0:
                # then chocolates for sure will contain mtx[0][0]
                _sum = mtx[0][0]
                # if bob is also at its place, i.e., (0, m - 1), then add bob's chocolates also.
                if b == m - 1:
                    _sum += mtx[0][m - 1]
                # finally, return the chocolates
                return _sum
            else:
                # however, if alice is not at (0, 0)

                # and bob is at its place, then return only bob's chocolates
                if b == m - 1:
                    return mtx[0][m - 1]
                else:
                    # if both of them are at wrong places, return 0 chocolates.
                    return 0

        if dp[i][a][b] is not None:
            return dp[i][a][b]

        # initialize a cost variable to find the max chocolates collected from all the paths.
        cost = 0
        for da in [-1, 0, 1]:
            for db in [-1, 0, 1]:
                next_a, next_b = a + da, b + db
                if 0 <= next_a < m and 0 <= next_b < m and 0 <= i - 1 < n:
                    count = solve(mtx, i - 1, next_a, next_b, n, m, dp)
                    # if both alice and bob are at same cell, add chocolate only once.
                    if a == b:
                        count += mtx[i][a]
                    else:
                        # else add chocolates of both
                        count += mtx[i][a] + mtx[i][b]
                    # update the max chocolates
                    cost = max(cost, count)
        # return the max chocolates obtained.
        dp[i][a][b] = cost
        return dp[i][a][b]

    def cherry_pickup(mtx):
        n, m = len(mtx), len(mtx[0])
        max_chocos = 0
        dp = {i: {a: {b: None for b in range(m)} for a in range(m)} for i in range(n)}
        # initialize starting points of alice and bob by looping m^2 times.
        for alice in range(m):
            for bob in range(m):
                # retrieve the max chocolates obtained
                cost = solve(mtx, n - 1, alice, bob, n, m, dp)
                # update the max chocolates
                max_chocos = max(max_chocos, cost)
        # return the max chocolates obtained.
        return max_chocos

    print(
        cherry_pickup(
            [
                [2, 3, 1, 2],
                [3, 4, 2, 2],
                [5, 6, 3, 5]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [1, 1],
                [1, 2]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [3, 7],
                [7, 6]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [4, 5],
                [3, 7],
                [4, 2]
            ]
        )
    )

    print(cherry_pickup([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))
    print(
        cherry_pickup(
            [
                [4, 1, 2],
                [3, 6, 1],
                [1, 6, 6],
                [3, 1, 2]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [2, 0, 0, 0, 0, 0, 2],
                [2, 1, 0, 0, 0, 4, 0],
                [2, 0, 10, 0, 1, 0, 0],
                [0, 3, 0, 6, 5, 0, 0],
                [1, 0, 3, 4, 0, 0, 6]
            ]
        )
    )


def tabulation():
    """
        Time complexity is O(m^2 * m^2 * n) and space complexity is O(nm^2).
    """
    def cherry_pickup(mtx):
        n, m = len(mtx), len(mtx[0])
        max_chocos = 0
        dp = {i: {a: {b: 0 for b in range(m)} for a in range(m)} for i in range(n)}

        for a in dp[0]:
            for b in dp[0][a]:
                if a == 0:
                    # then chocolates for sure will contain mtx[0][0]
                    _sum = mtx[0][0]
                    # if bob is also at its place, i.e., (0, m - 1), then add bob's chocolates also.
                    if b == m - 1:
                        _sum += mtx[0][m - 1]
                    # finally, return the chocolates
                    dp[0][a][b] = _sum
                else:
                    # however, if alice is not at (0, 0)

                    # and bob is at its place, then return only bob's chocolates
                    if b == m - 1:
                        dp[0][a][b] = mtx[0][m - 1]
                    else:
                        # if both of them are at wrong places, return 0 chocolates.
                        dp[0][a][b] = 0

        # initialize starting points of alice and bob by looping m^2 times.
        for alice in range(m):
            for bob in range(m):
                for i in range(1, n):
                    for a in range(m):
                        for b in range(m):
                            # initialize a cost variable to find the max chocolates collected from all the paths.
                            cost = 0
                            for da in [-1, 0, 1]:
                                for db in [-1, 0, 1]:
                                    next_a, next_b = a + da, b + db
                                    if 0 <= next_a < m and 0 <= next_b < m and 0 <= i - 1 < n:
                                        count = dp[i - 1][next_a][next_b]
                                        # if both alice and bob are at same cell, add chocolate only once.
                                        if a == b:
                                            count += mtx[i][a]
                                        else:
                                            # else add chocolates of both
                                            count += mtx[i][a] + mtx[i][b]
                                        # update the max chocolates
                                        cost = max(cost, count)
                            # return the max chocolates obtained.
                            dp[i][a][b] = cost

                # retrieve the max chocolates obtained
                cost = dp[n - 1][alice][bob]
                # update the max chocolates
                max_chocos = max(max_chocos, cost)
        # return the max chocolates obtained.
        return max_chocos

    print(
        cherry_pickup(
            [
                [2, 3, 1, 2],
                [3, 4, 2, 2],
                [5, 6, 3, 5]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [1, 1],
                [1, 2]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [3, 7],
                [7, 6]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [4, 5],
                [3, 7],
                [4, 2]
            ]
        )
    )

    print(cherry_pickup([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))
    print(
        cherry_pickup(
            [
                [4, 1, 2],
                [3, 6, 1],
                [1, 6, 6],
                [3, 1, 2]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [2, 0, 0, 0, 0, 0, 2],
                [2, 1, 0, 0, 0, 4, 0],
                [2, 0, 10, 0, 1, 0, 0],
                [0, 3, 0, 6, 5, 0, 0],
                [1, 0, 3, 4, 0, 0, 6]
            ]
        )
    )


def space_optimized():
    """
        Time complexity is O(m^2 * m^2 * n) and space complexity is O(m^2).
    """
    def cherry_pickup(mtx):
        n, m = len(mtx), len(mtx[0])
        max_chocos = 0

        # initialize starting points of alice and bob by looping m^2 times.
        for alice in range(m):
            for bob in range(m):
                prev = {a: {b: 0 for b in range(m)} for a in range(m)}

                for a in prev:
                    for b in prev[a]:
                        if a == 0:
                            # then chocolates for sure will contain mtx[0][0]
                            _sum = mtx[0][0]
                            # if bob is also at its place, i.e., (0, m - 1), then add bob's chocolates also.
                            if b == m - 1:
                                _sum += mtx[0][m - 1]
                            # finally, return the chocolates
                            prev[a][b] = _sum
                        else:
                            # however, if alice is not at (0, 0)

                            # and bob is at its place, then return only bob's chocolates
                            if b == m - 1:
                                prev[a][b] = mtx[0][m - 1]
                            else:
                                # if both of them are at wrong places, return 0 chocolates.
                                prev[a][b] = 0
                for i in range(1, n):
                    curr = {a: {b: 0 for b in range(m)} for a in range(m)}
                    for a in range(m):
                        for b in range(m):
                            # initialize a cost variable to find the max chocolates collected from all the paths.
                            cost = 0
                            for da in [-1, 0, 1]:
                                for db in [-1, 0, 1]:
                                    next_a, next_b = a + da, b + db
                                    if 0 <= next_a < m and 0 <= next_b < m and 0 <= i - 1 < n:
                                        count = prev[next_a][next_b]
                                        # if both alice and bob are at same cell, add chocolate only once.
                                        if a == b:
                                            count += mtx[i][a]
                                        else:
                                            # else add chocolates of both
                                            count += mtx[i][a] + mtx[i][b]
                                        # update the max chocolates
                                        cost = max(cost, count)
                            # return the max chocolates obtained.
                            curr[a][b] = cost
                    prev = curr
                # retrieve the max chocolates obtained
                cost = prev[alice][bob]
                # update the max chocolates
                max_chocos = max(max_chocos, cost)
        # return the max chocolates obtained.
        return max_chocos

    print(
        cherry_pickup(
            [
                [2, 3, 1, 2],
                [3, 4, 2, 2],
                [5, 6, 3, 5]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [1, 1],
                [1, 2]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [3, 7],
                [7, 6]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [4, 5],
                [3, 7],
                [4, 2]
            ]
        )
    )

    print(cherry_pickup([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))
    print(
        cherry_pickup(
            [
                [4, 1, 2],
                [3, 6, 1],
                [1, 6, 6],
                [3, 1, 2]
            ]
        )
    )

    print(
        cherry_pickup(
            [
                [2, 0, 0, 0, 0, 0, 2],
                [2, 1, 0, 0, 0, 4, 0],
                [2, 0, 10, 0, 1, 0, 0],
                [0, 3, 0, 6, 5, 0, 0],
                [1, 0, 3, 4, 0, 0, 6]
            ]
        )
    )


recursive()
print()
memoized()
print()
tabulation()
print()
space_optimized()