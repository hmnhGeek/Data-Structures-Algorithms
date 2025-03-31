# Problem link - https://www.naukri.com/code360/problems/problem-name-boolean-evaluation_1214650?source=youtube&campaign=striver_dp_videos
# Solution - https://www.youtube.com/watch?v=MM7fXopgyjw&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=53


def recursive():
    """
        Time complexity is exponential and space is O(n).
    """

    def solve(expression, i, j, need_true):
        if i > j:
            return 0
        if i == j:
            if need_true:
                return 1 if expression[i] == "T" else 0
            else:
                return 1 if expression[i] == "F" else 0

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


def memoized():
    """
        Time complexity is O(n^3) and space is O(n + n^2).
    """

    def solve(expression, i, j, need_true, dp):
        if i > j:
            return 0
        if i == j:
            if need_true:
                return 1 if expression[i] == "T" else 0
            else:
                return 1 if expression[i] == "F" else 0

        if dp[i][j][need_true] is not None:
            return dp[i][j][need_true]

        num_ways = 0
        for k in range(i + 1, j, 2):
            lt = solve(expression, i, k - 1, True, dp)
            lf = solve(expression, i, k - 1, False, dp)
            rt = solve(expression, k + 1, j, True, dp)
            rf = solve(expression, k + 1, j, False, dp)

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
        dp[i][j][need_true] = num_ways
        return num_ways

    def evaluate(expression: str):
        n = len(expression)
        dp = {i: {j: {True: None, False: None} for j in range(n)} for i in range(n)}
        return solve(expression, 0, n - 1, True, dp)

    print(evaluate("T|T&F"))
    print(evaluate("T^T^F"))
    print(evaluate("F|T^F"))
    print(evaluate("T|T&F^T"))


def tabulation():
    """
        Time complexity is O(n^3) and space is O(n^2).
    """
    def evaluate(expression: str):
        n = len(expression)
        dp = {i: {j: {True: 0, False: 0} for j in range(n)} for i in range(n)}
        for i in dp:
            dp[i][i][True] = 1 if expression[i] == "T" else 0
            dp[i][i][False] = 1 if expression[i] == "F" else 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    continue
                for need_true in [True, False]:
                    num_ways = 0
                    for k in range(i + 1, j, 2):
                        lt = dp[i][k - 1][True]
                        lf = dp[i][k - 1][False]
                        rt = dp[k + 1][j][True]
                        rf = dp[k + 1][j][False]

                        operator = expression[k]
                        if operator == "&":
                            if need_true:
                                num_ways += lt * rt
                            else:
                                num_ways += (lt * rf) + (lf * rt) + (lf * rf)
                        elif operator == "|":
                            if need_true:
                                num_ways += (lt * rt) + (lf * rt) + (lt * rf)
                            else:
                                num_ways += (lf * rf)
                        else:
                            if need_true:
                                num_ways += (lt * rf) + (lf * rt)
                            else:
                                num_ways += (lt * rt) + (lf * rf)
                    dp[i][j][need_true] = num_ways

        return dp[0][n - 1][True]

    print(evaluate("T|T&F"))
    print(evaluate("T^T^F"))
    print(evaluate("F|T^F"))
    print(evaluate("T|T&F^T"))


recursive()
print()
memoized()
print()
tabulation()