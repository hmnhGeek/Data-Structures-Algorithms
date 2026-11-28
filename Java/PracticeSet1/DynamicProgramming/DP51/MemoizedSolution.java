package PracticeSet1.DynamicProgramming.DP51;

import java.util.*;

public class MemoizedSolution {
    public static Integer getMaxCoins(List<Integer> balloons) {
        /*
            Time complexity is O(n^3) and space complexity is O(n + n^2).
         */
        int n = balloons.size();
        List<Integer> allBalloons = getAllBalloons(balloons);
        Map<Integer, Map<Integer, Integer>> dp = getBlankDP(n);
        return solve(allBalloons, 1, n, dp);
    }

    private static Map<Integer, Map<Integer, Integer>> getBlankDP(int n) {
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < n + 2; i += 1) {
            Map<Integer, Integer> subMap = new HashMap<>();
            for (int j = 0; j < n + 2; j += 1) {
                subMap.put(j, null);
            }
            dp.put(i, subMap);
        }
        return dp;
    }

    private static List<Integer> getAllBalloons(List<Integer> balloons) {
        List<Integer> allBalloons = new ArrayList<>(Arrays.asList(1));
        allBalloons.addAll(balloons);
        allBalloons.add(1);
        return allBalloons;
    }

    private static Integer solve(List<Integer> arr, int i, int j, Map<Integer, Map<Integer, Integer>> dp) {
        if (i > j) return 0;
        if (dp.get(i).get(j) != null) {
            System.out.println("Overlapping sub-problem...");
            return dp.get(i).get(j);
        }
        Integer maxCoins = Integer.MIN_VALUE;
        for (int k = i; k <= j; k += 1) {
            Integer coins = arr.get(i - 1) * arr.get(k) * arr.get(j + 1) + solve(arr, i, k - 1, dp) + solve(arr, k + 1, j, dp);
            maxCoins = Math.max(coins, maxCoins);
        }
        dp.get(i).put(j, maxCoins);
        return dp.get(i).get(j);
    }
}
