package DynamicProgramming.DP54;

import java.util.List;

public class RecursiveSolution {
    private static Integer solve(List<Integer> arr, Integer i, Integer k, Integer n) {
        if (i.equals(n)) return 0;
        Integer maxCost = Integer.MIN_VALUE;
        Integer maxValue = Integer.MIN_VALUE;
        for (int j = i; j < Math.min(i + k, n); j += 1) {
            maxValue = Math.max(arr.get(j), maxValue);
            Integer cost = (maxValue * (j - i + 1)) + solve(arr, j + 1, k, n);
            maxCost = Math.max(maxCost, cost);
        }
        return maxCost;
    }

    public static Integer maxSumPartition(List<Integer> arr, Integer k) {
        /*
            Time complexity is exponential and space complexity is O(n).
         */
        int n = arr.size();
        return solve(arr, 0, k, n);
    }
}
