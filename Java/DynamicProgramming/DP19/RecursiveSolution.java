package DynamicProgramming.DP19;

import java.util.List;

public class RecursiveSolution {
    /*
        Time complexity is exponential and space complexity is O(n).
     */
    public static Integer getKnapsack(List<Integer> weights, List<Integer> values, Integer capacity) {
        int n = weights.size();
        return solve(weights, values, n - 1, capacity);
    }

    private static Integer solve(List<Integer> weights, List<Integer> values, int i, Integer capacity) {
        if (capacity == 0) {
            return 0;
        }
        if (i == 0) {
            if (capacity >= weights.getFirst()) return values.getFirst();
            return 0;
        }
        Integer left = 0;
        if (capacity >= weights.get(i)) {
            left = values.get(i) + solve(weights, values, i - 1, capacity - weights.get(i));
        }
        Integer right = solve(weights, values, i - 1, capacity);
        return Math.max(left, right);
    }
}
