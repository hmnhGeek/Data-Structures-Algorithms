package PracticeSet1.DynamicProgramming.DP50;

import java.util.*;

public class TabulationSolution {
    /*
        Time complexity is O(n^3) and space complexity is O(n^2).
     */
    public static Integer getMinCostToCutSticks(List<Integer> cuts, Integer rodSize) {
        int n = cuts.size();
        List<Integer> modifiedCuts = new ArrayList<>(Arrays.asList(0));
        modifiedCuts.addAll(cuts);
        modifiedCuts.add(rodSize);
        Map<Integer, Map<Integer, Integer>> dp = initDP(n, Integer.MAX_VALUE);
        putBaseCaseInTabulationDP(n, dp);
        for (int i = n; i >= 1; i -= 1) {
            for (int j = 1; j <= n; j += 1) {
                if (i > j) continue;
                Integer minCost = Integer.MAX_VALUE;
                for (int k = i; k <= j; k += 1) {
                    Integer cost = (modifiedCuts.get(j + 1) - modifiedCuts.get(i - 1)) + dp.get(i).get(k - 1) + dp.get(k + 1).get(j);
                    minCost = Math.min(minCost, cost);
                }
                dp.get(i).put(j, minCost);
            }
        }
        return dp.get(1).get(n);
    }

    private static void putBaseCaseInTabulationDP(int n, Map<Integer, Map<Integer, Integer>> dp) {
        for (int i = 1; i <= n; i += 1) {
            for (int j = n; j >= 1; j -= 1) {
                if (i > j) dp.get(i).put(j, 0);
            }
        }
    }

    private static Map<Integer, Map<Integer, Integer>> initDP(int n, Integer v) {
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 1; i <= n; i += 1) {
            Map<Integer, Integer> subMap = new HashMap<>();
            for (int j = n; j >= 1; j -= 1) {
                subMap.put(j, v);
            }
            dp.put(i, subMap);
        }
        return dp;
    }
}
