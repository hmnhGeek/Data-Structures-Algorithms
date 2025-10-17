package DynamicProgramming.DP15;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpaceOptimizedSolution {
    /*
        Time complexity is O(nk) and space complexity is O(k).
     */
    public static boolean subsetSum(List<Integer> arr) {
        int n = arr.size();
        int k = arr.stream().mapToInt(Integer::intValue).sum();
        if (k % 2 != 0) return false;

        Map<Integer, Boolean> prev = new HashMap<>();
        for (int j = 0; j < k; j += 1) {
            prev.put(j, false);
        }

        prev.put(0, true);
        prev.put(arr.getFirst(), true);

        int target = k / 2;
        for (int i = 1; i < n; i += 1) {
            Map<Integer, Boolean> curr = new HashMap<>();
            for (int j = 0; j < k; j += 1) {
                curr.put(j, false);
            }
            for (int j = 0; j <= target; j += 1) {
                boolean left = false;
                if (arr.get(i) <= j) {
                    left = prev.get(j - arr.get(i));
                }
                boolean right = prev.get(j);
                curr.put(j, left || right);
            }
            prev = curr;
        }
        return prev.get(target);
    }
}
