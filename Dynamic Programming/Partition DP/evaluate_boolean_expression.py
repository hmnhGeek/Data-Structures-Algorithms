def recursive():
    def evaluate_boolean_expression(expression, i, j, is_true_lookup):
        if i > j:
            return 0
        if i == j:
            if is_true_lookup:
                return expression[i] == "T"
            else:
                return expression[i] == "F"

        number_of_ways = 0

        # traverse on the partitions
        for index in range(i + 1, j, 2):
            left_true_ways = evaluate_boolean_expression(expression, i, index - 1, 1)
            left_false_ways = evaluate_boolean_expression(expression, i, index - 1, 0)
            right_true_ways = evaluate_boolean_expression(expression, index + 1, j, 1)
            right_false_ways = evaluate_boolean_expression(expression, index + 1, j, 0)
            boolean_operator = expression[index]

            if boolean_operator == "&":
                if is_true_lookup:
                    number_of_ways += (left_true_ways * right_true_ways)
                else:
                    number_of_ways += (left_true_ways * right_false_ways) + (right_true_ways * left_false_ways) + (left_false_ways * right_false_ways)

            elif boolean_operator == "|":
                if is_true_lookup:
                    number_of_ways += (left_true_ways * right_false_ways) + (right_true_ways * left_false_ways) + (left_true_ways * right_true_ways)
                else:
                    number_of_ways += (left_false_ways * right_false_ways)

            else:
                if is_true_lookup:
                    number_of_ways += (left_true_ways * right_false_ways) + (right_true_ways * left_false_ways)
                else:
                    number_of_ways += (left_false_ways * right_false_ways) + (left_true_ways * right_true_ways)

        return number_of_ways

    def evaluate(expression):
        return evaluate_boolean_expression(expression, 0, len(expression) - 1, 1)

    print(evaluate("T|T&F"))
    print(evaluate("T^T^F"))
    print(evaluate("F|T^F"))
    print(evaluate("T^F&T"))

recursive()