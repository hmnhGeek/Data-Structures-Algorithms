package DynamicProgramming.DP21;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpaceOptimizedSolution {
    /*
        Time complexity is O(n*target) and space complexity is O(target).
     */
    public static Integer countSubsets(List<Integer> arr, Integer target) {
        int n = arr.size();
        Map<Integer, Integer> prev = new HashMap<>();
        for (int j = 0; j <= target; j += 1) {
            prev.put(j, 0);
        }
        prev.put(0, 1);
        prev.put(arr.getFirst(), 1);
        for (int i = 1; i < n; i += 1) {
            Map<Integer, Integer> curr = new HashMap<>();
            for (int j = 0; j <= target; j += 1) {
                curr.put(j, 0);
            }
            curr.put(0, 1);
            for (int j = 0; j <= target; j += 1) {
                Integer left = 0;
                if (arr.get(i) <= j) {
                    left = prev.get(j - arr.get(i));
                }
                Integer right = prev.get(j);
                curr.put(j, left + right);
            }
            prev = curr;
        }
        return prev.get(target);
    }
}
