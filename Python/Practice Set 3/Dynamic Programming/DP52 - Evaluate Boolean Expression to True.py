def recursive():
    """
        Time complexity is exponential and space complexity is O(n).
    """

    def solve(expression, i, j, evaluate_to):
        if i > j:
            return 0
        if i == j:
            if evaluate_to:
                return 1 if expression[i] == 'T' else 0
            return 1 if expression[i] == 'F' else 0
        num_ways = 0
        for index in range(i + 1, j, 2):
            operator = expression[index]
            left_true = solve(expression, i, index - 1, True)
            left_false = solve(expression, i, index - 1, False)
            right_true = solve(expression, index + 1, j, True)
            right_false = solve(expression, index + 1, j, False)
            if operator == "&":
                if evaluate_to:
                    num_ways += (left_true * right_true)
                else:
                    num_ways += (left_true * right_false + right_true * left_false + left_false * right_false)
            elif operator == "|":
                if evaluate_to:
                    num_ways += (left_true * right_true + left_true * right_false + left_false * right_true)
                else:
                    num_ways += (left_false * right_false)
            else:
                if evaluate_to:
                    num_ways += (left_true * right_false + right_true * left_false)
                else:
                    num_ways += (left_true * right_true + left_false * right_false)
        return num_ways

    def evaluate(expression):
        n = len(expression)
        return solve(expression, 0, n - 1, True)

    print(evaluate("F|T^F"))
    print(evaluate("T|T&F"))
    print(evaluate("T^T^F"))
    print(evaluate("T|T&F^T"))
    print(evaluate("T^F|F"))


def memoized():
    """
        Time complexity is O(n^3) and space complexity is O(n + n^2).
    """

    def solve(expression, i, j, evaluate_to, dp):
        if i > j:
            return 0
        if i == j:
            if evaluate_to:
                return 1 if expression[i] == 'T' else 0
            return 1 if expression[i] == 'F' else 0
        if dp[i][j][evaluate_to] is not None:
            return dp[i][j][evaluate_to]
        num_ways = 0
        for index in range(i + 1, j, 2):
            operator = expression[index]
            left_true = solve(expression, i, index - 1, True, dp)
            left_false = solve(expression, i, index - 1, False, dp)
            right_true = solve(expression, index + 1, j, True, dp)
            right_false = solve(expression, index + 1, j, False, dp)
            if operator == "&":
                if evaluate_to:
                    num_ways += (left_true * right_true)
                else:
                    num_ways += (left_true * right_false + right_true * left_false + left_false * right_false)
            elif operator == "|":
                if evaluate_to:
                    num_ways += (left_true * right_true + left_true * right_false + left_false * right_true)
                else:
                    num_ways += (left_false * right_false)
            else:
                if evaluate_to:
                    num_ways += (left_true * right_false + right_true * left_false)
                else:
                    num_ways += (left_true * right_true + left_false * right_false)
        dp[i][j][evaluate_to] = num_ways
        return dp[i][j][evaluate_to]

    def evaluate(expression):
        n = len(expression)
        dp = {i: {j: {True: None, False: None} for j in range(n)} for i in range(n)}
        return solve(expression, 0, n - 1, True, dp)

    print(evaluate("F|T^F"))
    print(evaluate("T|T&F"))
    print(evaluate("T^T^F"))
    print(evaluate("T|T&F^T"))
    print(evaluate("T^F|F"))


def tabulation():
    """
        Time complexity is O(n^3) and space complexity is O(n^2).
    """
    def evaluate(expression):
        n = len(expression)
        dp = {i: {j: {True: 0, False: 0} for j in range(n)} for i in range(n)}
        for i in dp:
            dp[i][i][True] = 1 if expression[i] == 'T' else 0
            dp[i][i][False] = 1 if expression[i] == 'F' else 0
        for i in range(n - 1, -1, -1):
            for j in range(n):
                if i >= j:
                    continue
                for evaluate_to in [True, False]:
                    num_ways = 0
                    for index in range(i + 1, j, 2):
                        operator = expression[index]
                        left_true = dp[i][index - 1][True]
                        left_false = dp[i][index - 1][False]
                        right_true = dp[index + 1][j][True]
                        right_false = dp[index + 1][j][False]
                        if operator == "&":
                            if evaluate_to:
                                num_ways += (left_true * right_true)
                            else:
                                num_ways += (left_true * right_false + right_true * left_false + left_false * right_false)
                        elif operator == "|":
                            if evaluate_to:
                                num_ways += (left_true * right_true + left_true * right_false + left_false * right_true)
                            else:
                                num_ways += (left_false * right_false)
                        else:
                            if evaluate_to:
                                num_ways += (left_true * right_false + right_true * left_false)
                            else:
                                num_ways += (left_true * right_true + left_false * right_false)
                    dp[i][j][evaluate_to] = num_ways
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
