package DynamicProgramming.DP16;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    /*
       Time complexity is O(n * target) and space complexity is O(n * target).
    */
    public static boolean subsetSum(List<Integer> arr, Integer target) {
        int n = arr.size();
        Map<Integer, Map<Integer, Boolean>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Boolean> subDp = new HashMap<>();
            for (int j = 0; j <= target; j += 1) {
                subDp.put(j, false);
            }
            dp.put(i, subDp);
        }
        for (int i = 0; i < n; i += 1) {
            dp.get(i).put(0, true);
        }
        dp.get(0).put(arr.getFirst(), true);
        for (int i = 1; i < n; i += 1) {
            for (int j = 0; j <= target; j += 1) {
                boolean left = false;
                if (arr.get(i) <= j) {
                    left = dp.get(i - 1).get(j - arr.get(i));
                }
                boolean right = dp.get(i - 1).get(j);
                dp.get(i).put(j, left || right);
            }
        }
        return dp.get(n - 1).get(target);
    }

    public static boolean solve(List<Integer> arr, int i, int j, Map<Integer, Map<Integer, Boolean>> dp) {
        if (j == 0) return true;
        if (i == 0) {
            return arr.getFirst() == j;
        }
        if (dp.get(i).get(j) != null) {
            return dp.get(i).get(j);
        }

        return dp.get(i).get(j);
    }
}
