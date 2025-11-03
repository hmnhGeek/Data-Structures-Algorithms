package DynamicProgramming.DP17;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpaceOptimizedSolution {
    /*
        Time complexity is O(n*target) and space complexity is O(target).
     */
    public static Integer getCount(List<Integer> arr, Integer target) {
        int n = arr.size();
        Map<Integer, Integer> prev = getPrev(0, target);
        prev.put(0, 1);
        prev.put(arr.getFirst(), 1);
        for (int i = 1; i < n; i += 1) {
            Map<Integer, Integer> curr = getPrev(0, target);
            curr.put(0, 1);
            for (int j = 0; j <= target; j += 1) {
                Integer left = 0;
                if (j >= arr.get(i)) {
                    left = prev.get(j - arr.get(i));
                }
                Integer right = prev.get(j);
                curr.put(j, left + right);
            }
            prev = curr;
        }
        return prev.get(target);
    }

    private static Map<Integer, Integer> getPrev(Integer defaultValue, int target) {
        Map<Integer, Integer> prev = new HashMap<>();
        for (int j = 0; j <= target; j += 1) {
            prev.put(j, defaultValue);
        }
        return prev;
    }
}
