package PracticeSet1.DynamicProgramming.DP50;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class RecursiveSolution {
    public static Integer getMinCostToCutSticks(List<Integer> cuts, Integer rodSize) {
        int n = cuts.size();
        List<Integer> modifiedCuts = new ArrayList<>(Arrays.asList(0));
        modifiedCuts.addAll(cuts);
        modifiedCuts.add(rodSize);
        return solve(modifiedCuts, 1, n);
    }

    private static Integer solve(List<Integer> cuts, int i, int j) {
        if (i > j) return 0;
        Integer minCost = Integer.MAX_VALUE;
        for (int k = i; k <= j; k += 1) {
            Integer cost = (cuts.get(j + 1) - cuts.get(i - 1)) + solve(cuts, i, k - 1) + solve(cuts, k + 1, j);
            minCost = Math.min(minCost, cost);
        }
        return minCost;
    }
}
