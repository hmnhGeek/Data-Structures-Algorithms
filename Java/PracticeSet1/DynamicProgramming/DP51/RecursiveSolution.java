package PracticeSet1.DynamicProgramming.DP51;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class RecursiveSolution {
    public static Integer getMaxCoins(List<Integer> balloons) {
        /*
            Time complexity is exponential and space complexity is O(n).
         */
        int n = balloons.size();
        List<Integer> allBalloons = new ArrayList<>(Arrays.asList(1));
        allBalloons.addAll(balloons);
        allBalloons.add(1);
        return solve(allBalloons, 1, n);
    }

    private static Integer solve(List<Integer> arr, int i, int j) {
        if (i > j) return 0;
        Integer maxCoins = Integer.MIN_VALUE;
        for (int k = i; k <= j; k += 1) {
            Integer coins = arr.get(i - 1) * arr.get(k) * arr.get(j + 1) + solve(arr, i, k - 1) + solve(arr, k + 1, j);
            maxCoins = Math.max(coins, maxCoins);
        }
        return maxCoins;
    }
}
