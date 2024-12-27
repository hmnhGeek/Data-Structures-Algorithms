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


recursive()