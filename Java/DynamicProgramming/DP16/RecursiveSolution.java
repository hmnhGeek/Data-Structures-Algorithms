package DynamicProgramming.DP16;

import java.util.List;

public class RecursiveSolution {
    public static boolean subsetSum(List<Integer> arr, Integer target) {
        int n = arr.size();
        return solve(arr, n - 1, target);
    }

    public static boolean solve(List<Integer> arr, int i, int j) {
        if (j == 0) return true;
        if (i == 0) {
            return arr.getFirst() == j;
        }
        boolean left = false;
        if (arr.get(i) <= j) {
            left = solve(arr, i - 1, j - arr.get(i));
        }
        boolean right = solve(arr, i - 1, j);
        return left || right;
    }
}
