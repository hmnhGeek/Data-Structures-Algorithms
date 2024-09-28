def recursive():
    def evaluate_boolean_expression(expression, i, j, is_true_lookup):
        """
            Time complexity is exponential and space complexity is O(n).
        """

        # if there are no partitions left to do, return 0 number of ways
        if i > j:
            return 0

        if i == j:
            # if there is only one boolean value to evaluate
            if is_true_lookup:
                # if you're looking for True, return 1 way if this boolean value is "T", else return 0 ways.
                return expression[i] == "T"
            else:
                # if you're looking for False, return 1 way if this boolean value is "F", else return 0 ways.
                return expression[i] == "F"

        # store the number of ways to be returned later on.
        number_of_ways = 0

        # traverse on the logical operators with step count of 2. Note that logical operators start from `i + 1`th
        # index and at every 2nd step they are found till `j - 1`th index.
        for index in range(i + 1, j, 2):
            # count the number of ways the left partition from this operator would yield a True.
            left_true_ways = evaluate_boolean_expression(expression, i, index - 1, 1)

            # count the number of ways the left partition from this operator would yield a False.
            left_false_ways = evaluate_boolean_expression(expression, i, index - 1, 0)

            # count the number of ways the right partition from this operator would yield a True.
            right_true_ways = evaluate_boolean_expression(expression, index + 1, j, 1)

            # count the number of ways the right partition from this operator would yield a False.
            right_false_ways = evaluate_boolean_expression(expression, index + 1, j, 0)

            # store the boolean operator at this index.
            boolean_operator = expression[index]

            # if the boolean operator is an AND...
            if boolean_operator == "&":
                # and if you're looking for true evaluation
                if is_true_lookup:
                    # then the number of ways would be the product of left true ways and right true ways.
                    number_of_ways += (left_true_ways * right_true_ways)
                else:
                    # else if you're looking for false evaluation.
                    number_of_ways += (left_true_ways * right_false_ways) + (right_true_ways * left_false_ways) + (left_false_ways * right_false_ways)

            # else if the boolean expression is an OR...
            elif boolean_operator == "|":
                # and if you're looking for true evaluation
                if is_true_lookup:
                    # then the number of ways would be the sum of lf_t * rt_f and lf_f * rt_t and lf_t * rt_t
                    number_of_ways += (left_true_ways * right_false_ways) + (right_true_ways * left_false_ways) + (left_true_ways * right_true_ways)
                else:
                    # else if you're looking for false evaluation.
                    number_of_ways += (left_false_ways * right_false_ways)

            # else, if the boolean expression is a XOR...
            else:
                # and if you're looking for true evaluation
                if is_true_lookup:
                    # then the number of ways would be the sum of lf_t * rt_f and lf_f * rt_t
                    number_of_ways += (left_true_ways * right_false_ways) + (right_true_ways * left_false_ways)
                else:
                    # else if you're looking for false evaluation.
                    number_of_ways += (left_false_ways * right_false_ways) + (left_true_ways * right_true_ways)

        # finally return the number of ways
        return number_of_ways

    def evaluate(expression):
        # we are looking for true evaluation.
        return evaluate_boolean_expression(expression, 0, len(expression) - 1, 1)

    print(evaluate("T|T&F"))
    print(evaluate("T^T^F"))
    print(evaluate("F|T^F"))
    print(evaluate("T^F&T"))
    print(evaluate("T|T&F^T"))


def memoized():
    def evaluate_boolean_expression(expression, i, j, is_true_lookup, dp):
        """
            Time complexity is exponential and space complexity is O(n).
        """

        # if there are no partitions left to do, return 0 number of ways
        if i > j:
            return 0

        if i == j:
            # if there is only one boolean value to evaluate
            if is_true_lookup:
                # if you're looking for True, return 1 way if this boolean value is "T", else return 0 ways.
                return expression[i] == "T"
            else:
                # if you're looking for False, return 1 way if this boolean value is "F", else return 0 ways.
                return expression[i] == "F"

        if dp[i][j][is_true_lookup] is not None:
            return dp[i][j][is_true_lookup]

        # store the number of ways to be returned later on.
        number_of_ways = 0

        # traverse on the logical operators with step count of 2. Note that logical operators start from `i + 1`th
        # index and at every 2nd step they are found till `j - 1`th index.
        for index in range(i + 1, j, 2):
            # count the number of ways the left partition from this operator would yield a True.
            left_true_ways = evaluate_boolean_expression(expression, i, index - 1, 1, dp)

            # count the number of ways the left partition from this operator would yield a False.
            left_false_ways = evaluate_boolean_expression(expression, i, index - 1, 0, dp)

            # count the number of ways the right partition from this operator would yield a True.
            right_true_ways = evaluate_boolean_expression(expression, index + 1, j, 1, dp)

            # count the number of ways the right partition from this operator would yield a False.
            right_false_ways = evaluate_boolean_expression(expression, index + 1, j, 0, dp)

            # store the boolean operator at this index.
            boolean_operator = expression[index]

            # if the boolean operator is an AND...
            if boolean_operator == "&":
                # and if you're looking for true evaluation
                if is_true_lookup:
                    # then the number of ways would be the product of left true ways and right true ways.
                    number_of_ways += (left_true_ways * right_true_ways)
                else:
                    # else if you're looking for false evaluation.
                    number_of_ways += (left_true_ways * right_false_ways) + (right_true_ways * left_false_ways) + (left_false_ways * right_false_ways)

            # else if the boolean expression is an OR...
            elif boolean_operator == "|":
                # and if you're looking for true evaluation
                if is_true_lookup:
                    # then the number of ways would be the sum of lf_t * rt_f and lf_f * rt_t and lf_t * rt_t
                    number_of_ways += (left_true_ways * right_false_ways) + (right_true_ways * left_false_ways) + (left_true_ways * right_true_ways)
                else:
                    # else if you're looking for false evaluation.
                    number_of_ways += (left_false_ways * right_false_ways)

            # else, if the boolean expression is a XOR...
            else:
                # and if you're looking for true evaluation
                if is_true_lookup:
                    # then the number of ways would be the sum of lf_t * rt_f and lf_f * rt_t
                    number_of_ways += (left_true_ways * right_false_ways) + (right_true_ways * left_false_ways)
                else:
                    # else if you're looking for false evaluation.
                    number_of_ways += (left_false_ways * right_false_ways) + (left_true_ways * right_true_ways)

        # finally return the number of ways
        dp[i][j][is_true_lookup] = number_of_ways
        return number_of_ways

    def evaluate(expression):
        n = len(expression)
        dp = {i: {j: {1: None, 0: None} for j in range(n)} for i in range(n)}
        # we are looking for true evaluation.
        return evaluate_boolean_expression(expression, 0, len(expression) - 1, 1, dp)

    print(evaluate("T|T&F"))
    print(evaluate("T^T^F"))
    print(evaluate("F|T^F"))
    print(evaluate("T^F&T"))
    print(evaluate("T|T&F^T"))


recursive()
print()
memoized()