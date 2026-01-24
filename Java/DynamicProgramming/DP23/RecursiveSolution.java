package DynamicProgramming.DP23;

import java.util.List;

public class RecursiveSolution {
    /*
        Time complexity is exponential and space complexity is O(n).
     */
    public static Integer getUnboundedKnapsack(List<Integer> weights, List<Integer> values, Integer capacity) {
        if (capacity < 0 || weights.size() != values.size()) return null;
        int n = weights.size();
        return solve(weights, values, n - 1, capacity);
    }

    private static Integer solve(List<Integer> weights, List<Integer> values, int i, Integer j) {
        if (j == 0) return 0;
        if (i == 0) {
            if (j % weights.getFirst() == 0) {
                return (j / weights.getFirst()) * values.getFirst();
            }
            return 0;
        }
        Integer left = Integer.MIN_VALUE;
        if (j >= weights.get(i)) {
            left = values.get(i) + solve(weights, values, i, j - weights.get(i));
        }
        Integer right = solve(weights, values, i - 1, j);
        return Math.max(left, right);
    }
}
