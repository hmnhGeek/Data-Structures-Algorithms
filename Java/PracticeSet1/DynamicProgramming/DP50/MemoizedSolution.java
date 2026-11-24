package PracticeSet1.DynamicProgramming.DP50;

import java.util.*;

public class MemoizedSolution {
    /*
        Time complexity is O(n^3) and space complexity is O(n + n^2).
     */
    public static Integer getMinCostToCutSticks(List<Integer> cuts, Integer rodSize) {
        int n = cuts.size();
        List<Integer> modifiedCuts = new ArrayList<>(Arrays.asList(0));
        modifiedCuts.addAll(cuts);
        modifiedCuts.add(rodSize);
        Collections.sort(modifiedCuts);
        Map<Integer, Map<Integer, Integer>> dp = initDP(n, null);
        return solve(modifiedCuts, 1, n, dp);
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

    private static Integer solve(List<Integer> cuts, int i, int j, Map<Integer, Map<Integer, Integer>> dp) {
        if (i > j) return 0;
        if (dp.get(i).get(j) != null) {
            System.out.println("Found overlapping sub-problem.");
            return dp.get(i).get(j);
        }
        Integer minCost = Integer.MAX_VALUE;
        for (int k = i; k <= j; k += 1) {
            Integer cost = (cuts.get(j + 1) - cuts.get(i - 1)) + solve(cuts, i, k - 1, dp) + solve(cuts, k + 1, j, dp);
            minCost = Math.min(minCost, cost);
        }
        dp.get(i).put(j, minCost);
        return dp.get(i).get(j);
    }
}
