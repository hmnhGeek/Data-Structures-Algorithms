package DynamicProgramming.DP15;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    /*
        Time complexity is O(nk) and space complexity is O(nk).
     */
    public static boolean subsetSum(List<Integer> arr) {
        int n = arr.size();
        int k = arr.stream().mapToInt(Integer::intValue).sum();
        if (k % 2 != 0) return false;
        Map<Integer, Map<Integer, Boolean>> dp = new HashMap<>();
        updateDpArray(dp, n, k);
        for (int i = 0; i < n; i += 1) {
            dp.get(i).put(0, true);
        }
        dp.get(0).put(arr.getFirst(), true);

        int target = k / 2;
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

    private static void updateDpArray(Map<Integer, Map<Integer, Boolean>> dp, int n, int k) {
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Boolean> subMap = new HashMap<>();
            for (int j = 0; j < k; j += 1) {
                subMap.put(j, false);
            }
            dp.put(i, subMap);
        }
    }
}
