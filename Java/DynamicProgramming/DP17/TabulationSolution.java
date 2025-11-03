package DynamicProgramming.DP17;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    /*
        Time complexity is O(n*target) and space complexity is O(n*target).
     */
    public static Integer getCount(List<Integer> arr, Integer target) {
        int n = arr.size();
        Map<Integer, Map<Integer, Integer>> dp = getDp(0, n, target);
        for (int i = 0; i < n; i += 1) {
            dp.get(i).put(0, 1);
        }
        dp.get(0).put(arr.getFirst(), 1);
        for (int i = 1; i < n; i += 1) {
            for (int j = 0; j <= target; j += 1) {
                Integer left = 0;
                if (j >= arr.get(i)) {
                    left = dp.get(i - 1).get(j - arr.get(i));
                }
                Integer right = dp.get(i - 1).get(j);
                dp.get(i).put(j, left + right);
            }
        }
        return dp.get(n - 1).get(target);
    }

    private static Map<Integer, Map<Integer, Integer>> getDp(Integer defaultValue, int n, int target) {
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Integer> subMap = new HashMap<>();
            for (int j = 0; j <= target; j += 1) {
                subMap.put(j, defaultValue);
            }
            dp.put(i, subMap);
        }
        return dp;
    }
}
