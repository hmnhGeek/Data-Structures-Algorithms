package DynamicProgramming;


class RecursiveSolutionDP52 {
    /**
     * Time complexity is exponential and space complexity is O(n).
     */

    private static Integer solve(String expression, Integer i, Integer j, Boolean evaluateTo) {
        if (i > j) {
            return 0;
        }
        if (i.equals(j)) {
            if (evaluateTo.equals(true)) {
                return expression.charAt(i) == 'T' ? 1 : 0;
            } else {
                return expression.charAt(i) == 'F' ? 1 : 0;
            }
        }
        int numWays = 0;
        for (int index = i + 1; index <= j - 1; index += 1) {
            Integer leftTrue = solve(expression, i, index - 1, true);
            Integer leftFalse = solve(expression, i, index - 1, false);
            Integer rightTrue = solve(expression, index + 1, j, true);
            Integer rightFalse = solve(expression, index + 1, j, false);
            char operator = expression.charAt(index);
            if (operator == '&') {
                if (evaluateTo.equals(true)) {
                    numWays += (leftTrue * rightTrue);
                } else {
                    numWays += (leftTrue * rightFalse + rightTrue * leftFalse + leftFalse * rightFalse);
                }
            } else if (operator == '|') {
                if (evaluateTo.equals(true)) {
                    numWays += (leftTrue * rightFalse + rightTrue * leftFalse + leftTrue * rightTrue);
                } else {
                    numWays += (leftFalse * rightFalse);
                }
            } else {
                if (evaluateTo.equals(true)) {
                    numWays += (leftTrue * rightFalse + rightTrue * leftFalse);
                } else {
                    numWays += (leftTrue * rightTrue + leftFalse * rightFalse);
                }
            }
        }
        return numWays;
    }

    public static Integer getNumWaysToEvaluateTo(String expression) {
        int n = expression.length();
        return solve(expression, 0, n - 1, true);
    }

    public static void main(String[] args) {
        System.out.println(getNumWaysToEvaluateTo("F|T^F"));
        System.out.println(getNumWaysToEvaluateTo("T|T&F"));
        System.out.println(getNumWaysToEvaluateTo("T^T^F"));
        System.out.println(getNumWaysToEvaluateTo("T|T&F^T"));
        System.out.println(getNumWaysToEvaluateTo("T^F|F"));
    }
}