def recursive():
    """
        Time complexity is exponential and space is O(n).
    """

    def solve(expression, i, j, need_true):
        if i > j:
            return 0
        if i == j:
            if need_true:
                return expression[i] == "T"
            else:
                return expression[i] == "F"

        num_ways = 0
        for k in range(i + 1, j, 2):
            lt = solve(expression, i, k - 1, True)
            lf = solve(expression, i, k - 1, False)
            rt = solve(expression, k + 1, j, True)
            rf = solve(expression, k + 1, j, False)

            operator = expression[k]
            if operator == "&":
                if need_true:
                    num_ways += lt * rt
                else:
                    num_ways += (lt*rf) + (lf*rt) + (lf*rf)
            elif operator == "|":
                if need_true:
                    num_ways += (lt*rt) + (lf*rt) + (lt*rf)
                else:
                    num_ways += (lf*rf)
            else:
                if need_true:
                    num_ways += (lt*rf) + (lf*rt)
                else:
                    num_ways += (lt*rt) + (lf*rf)
        return num_ways

    def evaluate(expression: str):
        n = len(expression)
        return solve(expression, 0, n - 1, True)

    print(evaluate("T|T&F"))
    print(evaluate("T^T^F"))
    print(evaluate("F|T^F"))
    print(evaluate("T|T&F^T"))


recursive()