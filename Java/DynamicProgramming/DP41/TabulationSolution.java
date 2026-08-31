package DynamicProgramming.DP41;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    /*
        Time complexity is O(n^2) and space complexity is O(n^2).
     */
    public static Integer getLISLength(List<Integer> arr) {
        int n = arr.size();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i <= n; i += 1) {
            Map<Integer, Integer> prev = new HashMap<>();
            for (int j = 0; j <= n + 1; j += 1) {
                prev.put(j, 0);
            }
            dp.put(i, prev);
        }
        for (int j = 0; j <= n + 1; j += 1) {
            if (arr.getFirst() < Utils.getValAtIdx(arr, j, n)) {
                dp.get(0).put(j, 1);
            }
        }
        for (int i = 1; i < n; i += 1) {
            for (int j = n; j >= 0; j -= 1) {
                Integer left = Integer.MIN_VALUE;
                if (arr.get(i) < Utils.getValAtIdx(arr, j, n)) {
                    left = 1 + dp.get(i - 1).get(i);
                }
                Integer right = dp.get(i - 1).get(j);
                dp.get(i).put(j, Math.max(left, right));
            }
        }
        return dp.get(n - 1).get(n);
    }
}
