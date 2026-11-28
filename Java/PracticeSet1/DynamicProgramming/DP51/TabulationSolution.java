package PracticeSet1.DynamicProgramming.DP51;

import java.util.*;

public class TabulationSolution {
    public static Integer getMaxCoins(List<Integer> balloons) {
        /*
            Time complexity is O(n^3) and space complexity is O(n^2).
         */
        int n = balloons.size();
        List<Integer> allBalloons = getAllBalloons(balloons);
        Map<Integer, Map<Integer, Integer>> dp = getBlankDP(n);
        for (int i = n; i >= 1; i -= 1) {
            for (int j = 1; j <= n ; j += 1) {
                if (i > j) continue;
                Integer maxCoins = Integer.MIN_VALUE;
                for (int k = i; k <= j; k += 1) {
                    Integer coins = allBalloons.get(i - 1) * allBalloons.get(k) * allBalloons.get(j + 1) + dp.get(i).get(k - 1) + dp.get(k + 1).get(j);
                    maxCoins = Math.max(coins, maxCoins);
                }
                dp.get(i).put(j, maxCoins);
            }
        }
        return dp.get(1).get(n);
    }

    private static Map<Integer, Map<Integer, Integer>> getBlankDP(int n) {
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < n + 2; i += 1) {
            Map<Integer, Integer> subMap = new HashMap<>();
            for (int j = 0; j < n + 2; j += 1) {
                subMap.put(j, 0);
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
}
