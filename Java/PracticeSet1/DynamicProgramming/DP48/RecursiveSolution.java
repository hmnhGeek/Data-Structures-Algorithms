package PracticeSet1.DynamicProgramming.DP48;

import java.util.List;

public class RecursiveSolution {
    /*
        Time complexity is exponential and space complexity is O(n).
     */
    public static Integer getMinCostForMultiplication(List<Integer> arr) {
        int n = arr.size();
        return solve(arr, 1, n - 1);
    }

    private static Integer solve(List<Integer> arr, int i, int j) {
        if (i == j) {
            return 0;
        }
        Integer minOps = Integer.MAX_VALUE;
        for (int k = i; k < j; k += 1) {
            Integer operations = (arr.get(i - 1) * arr.get(k) * arr.get(j)) + solve(arr, i, k) + solve(arr, k + 1, j);
            minOps = Math.min(minOps, operations);
        }
        return minOps;
    }
}
