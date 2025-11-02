package DynamicProgramming.DP16;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpaceOptimizedSolution {
    /*
       Time complexity is O(n * target) and space complexity is O(target).
    */
    public static boolean subsetSum(List<Integer> arr, Integer target) {
        int n = arr.size();
        Map<Integer, Boolean> prev = new HashMap<>();
        for (int j = 0; j <= target; j += 1) {
            prev.put(j, false);
        }
        prev.put(0, true);
        prev.put(arr.getFirst(), true);
        for (int i = 1; i < n; i += 1) {
            Map<Integer, Boolean> curr = new HashMap<>();
            for (int j = 0; j <= target; j += 1) {
                curr.put(j, false);
            }
            curr.put(0, true);
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
