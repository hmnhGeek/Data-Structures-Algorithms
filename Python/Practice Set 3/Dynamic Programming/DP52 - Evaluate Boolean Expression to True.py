def recursive():
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


recursive()
print()
