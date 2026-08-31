package DynamicProgramming.DP41;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpaceOptimizedSolution {
    /*
        Time complexity is O(n^2) and space complexity is O(n).
     */
    public static Integer getLISLength(List<Integer> arr) {
        int n = arr.size();
        Map<Integer, Integer> prev = new HashMap<>();
        for (int j = 0; j <= n + 1; j += 1) {
            prev.put(j, 0);
        }
        for (int j = 0; j <= n + 1; j += 1) {
            if (arr.getFirst() < Utils.getValAtIdx(arr, j, n)) {
                prev.put(j, 1);
            }
        }
        for (int i = 1; i < n; i += 1) {
            Map<Integer, Integer> curr = new HashMap<>();
            for (int j = 0; j <= n + 1; j += 1) {
                curr.put(j, 0);
            }
            for (int j = n; j >= 0; j -= 1) {
                Integer left = Integer.MIN_VALUE;
                if (arr.get(i) < Utils.getValAtIdx(arr, j, n)) {
                    left = 1 + prev.get(i);
                }
                Integer right = prev.get(j);
                curr.put(j, Math.max(left, right));
            }
            prev = curr;
        }
        return prev.get(n);
    }
}
