def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """

    def solve(expr, i, j, to_true):
        if i > j:
            return 0
        if i == j:
            if to_true:
                return 1 if expr[i] == "T" else 0
            else:
                return 1 if expr[i] == "F" else 0

        num_ways = 0
        for k in range(i + 1, j, 2):
            operator = expr[k]

            left_to_true = solve(expr, i, k - 1, True)
            left_to_false = solve(expr, i, k - 1, False)
            right_to_true = solve(expr, k + 1, j, True)
            right_to_false = solve(expr, k + 1, j, False)

            if operator == "&":
                if to_true:
                    num_ways += (left_to_true * right_to_true)
                else:
                    num_ways += (left_to_true * right_to_false) + (left_to_false * right_to_true) + (left_to_false * right_to_false)
            elif operator == "|":
                if to_true:
                    num_ways += (left_to_true * right_to_false) + (left_to_false * right_to_true) + (left_to_true * right_to_true)
                else:
                    num_ways += (left_to_false * right_to_false)
            else:
                if to_true:
                    num_ways += (left_to_true * right_to_false) + (left_to_false * right_to_true)
                else:
                    num_ways += (left_to_true * right_to_true) + (left_to_false * right_to_false)
        return num_ways

    def evaluate(expr):
        n = len(expr)
        return solve(expr, 0, n - 1, True)

    print(evaluate("F|T^F"))
    print(evaluate("T|T&F"))
    print(evaluate("T^T^F"))
    print(evaluate("T|T&F^T"))
    print(evaluate("T^F|F"))


def memoized():
    """
        Time complexity is O(2 * n^3) and space complexity is O(n + 2n^2).
    """

    def solve(expr, i, j, to_true, dp):
        if i > j:
            return 0
        if i == j:
            if to_true:
                return 1 if expr[i] == "T" else 0
            else:
                return 1 if expr[i] == "F" else 0

        if dp[i][j][to_true] is not None:
            return dp[i][j][to_true]

        num_ways = 0
        for k in range(i + 1, j, 2):
            operator = expr[k]

            left_to_true = solve(expr, i, k - 1, True, dp)
            left_to_false = solve(expr, i, k - 1, False, dp)
            right_to_true = solve(expr, k + 1, j, True, dp)
            right_to_false = solve(expr, k + 1, j, False, dp)

            if operator == "&":
                if to_true:
                    num_ways += (left_to_true * right_to_true)
                else:
                    num_ways += (left_to_true * right_to_false) + (left_to_false * right_to_true) + (left_to_false * right_to_false)
            elif operator == "|":
                if to_true:
                    num_ways += (left_to_true * right_to_false) + (left_to_false * right_to_true) + (left_to_true * right_to_true)
                else:
                    num_ways += (left_to_false * right_to_false)
            else:
                if to_true:
                    num_ways += (left_to_true * right_to_false) + (left_to_false * right_to_true)
                else:
                    num_ways += (left_to_true * right_to_true) + (left_to_false * right_to_false)
        dp[i][j][to_true] = num_ways
        return dp[i][j][to_true]

    def evaluate(expr):
        n = len(expr)
        dp = {i: {j: {True: None, False: None} for j in range(n)} for i in range(n)}
        return solve(expr, 0, n - 1, True, dp)

    print(evaluate("F|T^F"))
    print(evaluate("T|T&F"))
    print(evaluate("T^T^F"))
    print(evaluate("T|T&F^T"))
    print(evaluate("T^F|F"))


def tabulation():
    """
        Time complexity is O(2 * n^3) and space complexity is O(2n^2).
    """
    def evaluate(expr):
        n = len(expr)
        dp = {i: {j: {True: 0, False: 0} for j in range(n + 1)} for i in range(n + 1)}
        for i in range(0, n, 2):
            dp[i][i][True] = 1 if expr[i] == "T" else 0
            dp[i][i][False] = 1 if expr[i] == "F" else 0
        for i in range(n - 1, -1, -1):
            for j in range(n):
                if i >= j:
                    continue
                for to_true in [True, False]:
                    num_ways = 0
                    for k in range(i + 1, j, 2):
                        operator = expr[k]

                        left_to_true = dp[i][k - 1][True]
                        left_to_false = dp[i][k - 1][False]
                        right_to_true = dp[k + 1][j][True]
                        right_to_false = dp[k + 1][j][False]

                        if operator == "&":
                            if to_true:
                                num_ways += (left_to_true * right_to_true)
                            else:
                                num_ways += (left_to_true * right_to_false) + (left_to_false * right_to_true) + (
                                            left_to_false * right_to_false)
                        elif operator == "|":
                            if to_true:
                                num_ways += (left_to_true * right_to_false) + (left_to_false * right_to_true) + (
                                            left_to_true * right_to_true)
                            else:
                                num_ways += (left_to_false * right_to_false)
                        else:
                            if to_true:
                                num_ways += (left_to_true * right_to_false) + (left_to_false * right_to_true)
                            else:
                                num_ways += (left_to_true * right_to_true) + (left_to_false * right_to_false)
                    dp[i][j][to_true] = num_ways

        return dp[0][n - 1][True]

    print(evaluate("F|T^F"))
    print(evaluate("T|T&F"))
    print(evaluate("T^T^F"))
    print(evaluate("T|T&F^T"))
    print(evaluate("T^F|F"))


recursive()
print()
memoized()
print()
tabulation()
