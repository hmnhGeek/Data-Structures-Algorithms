package DynamicProgramming;


import java.util.HashMap;
import java.util.Map;

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


class MemoizedSolutionDP52 {
    /**
     * Time complexity is O(n^3) and space complexity is O(n + n^2).
     */

    private static Integer solve(String expression, Integer i, Integer j, Boolean evaluateTo, Map<Integer, Map<Integer, Map<Boolean, Integer>>> dp) {
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
        if (dp.get(i).get(j).get(evaluateTo) != null) {
            return dp.get(i).get(j).get(evaluateTo);
        }
        int numWays = 0;
        for (int index = i + 1; index <= j - 1; index += 1) {
            Integer leftTrue = solve(expression, i, index - 1, true, dp);
            Integer leftFalse = solve(expression, i, index - 1, false, dp);
            Integer rightTrue = solve(expression, index + 1, j, true, dp);
            Integer rightFalse = solve(expression, index + 1, j, false, dp);
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
        Map<Integer, Map<Boolean, Integer>> submap = dp.get(i);
        Map<Boolean, Integer> submap2 = submap.get(j);
        submap2.put(evaluateTo, numWays);
        submap.put(j, submap2);
        dp.put(i, submap);
        return dp.get(i).get(j).get(evaluateTo);
    }

    public static Integer getNumWaysToEvaluateTo(String expression) {
        int n = expression.length();
        Map<Integer, Map<Integer, Map<Boolean, Integer>>> dp = new HashMap<>();
        for (int i = 0; i <= n - 1; i += 1) {
            Map<Integer, Map<Boolean, Integer>> submap = new HashMap<>();
            for (int j = 0; j <= n - 1; j += 1) {
                Map<Boolean, Integer> submap2 = new HashMap<>();
                submap2.put(true, null);
                submap2.put(false, null);
                submap.put(j, submap2);
            }
            dp.put(i, submap);
        }
        return solve(expression, 0, n - 1, true, dp);
    }

    public static void main(String[] args) {
        System.out.println(getNumWaysToEvaluateTo("F|T^F"));
        System.out.println(getNumWaysToEvaluateTo("T|T&F"));
        System.out.println(getNumWaysToEvaluateTo("T^T^F"));
        System.out.println(getNumWaysToEvaluateTo("T|T&F^T"));
        System.out.println(getNumWaysToEvaluateTo("T^F|F"));
    }
}