package DynamicProgramming.DP18;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    /*
        Time complexity is O(n*target) and space complexity is O(n + n*target).
     */
    public static int getCount(List<Integer> arr, Integer target) {
        int n = arr.size();
        Map<Integer, Map<Integer, Integer>> dp = Utils.getDp(n, target, null);
        return solve(arr, n - 1, target, dp);
    }

    public static int solve(List<Integer> arr, Integer i, Integer j, Map<Integer, Map<Integer, Integer>> dp) {
        if (j == 0) return 1;
        if (i == 0) {
            if (arr.getFirst().equals(j)) return 1;
            return 0;
        }
        if (dp.get(i).get(j) != null) return dp.get(i).get(j);
        Integer left = 0;
        if (j >= arr.get(i)) {
            left = solve(arr, i - 1, j - arr.get(i), dp);
        }
        Integer right = solve(arr, i - 1, j, dp);
        dp.get(i).put(j, left + right);
        return dp.get(i).get(j);
    }
}
