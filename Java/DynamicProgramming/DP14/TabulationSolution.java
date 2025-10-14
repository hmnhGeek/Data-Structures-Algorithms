package DynamicProgramming.DP14;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    /*
        Time complexity is O(nk) and space complexity is O(nk).
     */
    public static boolean subsetSum(List<Integer> arr, Integer k) {
        int n = arr.size();
        Map<Integer, Map<Integer, Boolean>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Boolean> sub = new HashMap<>();
            for (int j = 0; j <= k; j += 1) {
                sub.put(j, false);
            }
            dp.put(i, sub);
        }

        for (int i = 0; i < n; i += 1) {
            dp.get(i).put(0, true);
        }
        dp.get(0).put(arr.getFirst(), true);

        for (int i = 1; i < n; i += 1) {
            for (int j = 0; j <= k; j += 1) {
                boolean left = false;
                if (arr.get(i) <= j) {
                    left = dp.get(i - 1).get(j - arr.get(i));
                }
                boolean right = dp.get(i - 1).get(j);
                dp.get(i).put(j, left || right);
            }
        }

        return dp.get(n - 1).get(k);
    }
}
