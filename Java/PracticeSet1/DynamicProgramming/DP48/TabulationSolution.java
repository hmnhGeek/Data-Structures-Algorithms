package PracticeSet1.DynamicProgramming.DP48;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    /*
        Time complexity is O(n^3) and space complexity is O(n^2).
     */
    public static Integer getMinCostForMultiplication(List<Integer> arr) {
        int n = arr.size();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Integer> subMap = new HashMap<>();
            for (int j = 0; j < n; j += 1) {
                subMap.put(j, 0);
            }
            dp.put(i, subMap);
        }
        for (int i = n - 1; i >= 1; i -= 1) {
            for (int j = i; j < n; j += 1) {
                if (i >= j) continue;
                Integer minOps = Integer.MAX_VALUE;
                for (int k = i; k < j; k += 1) {
                    Integer operations = (arr.get(i - 1) * arr.get(k) * arr.get(j)) + dp.get(i).get(k) + dp.get(k + 1).get(j);
                    minOps = Math.min(minOps, operations);
                }
                dp.get(i).put(j, minOps);
            }
        }
        return dp.get(1).get(n - 1);
    }
}
