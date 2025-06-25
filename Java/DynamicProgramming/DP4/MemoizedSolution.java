// Problem link - https://atcoder.jp/contests/dp/tasks/dp_b
// Solution - https://www.youtube.com/watch?v=Kmh3rhyEtB8&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=5

package DynamicProgramming.DP4;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    /*
        Time complexity is O(n * k) and space complexity is O(2n).
     */
    private static Integer frogJump(List<Integer> arr, Integer k) {
        Map<Integer, Integer> dp = new HashMap<>();
        for (int i = 0; i <= arr.size() - 1; i += 1) {
            dp.put(i, null);
        }
        return solve(arr, arr.size() - 1, k, dp);
    }

    private static Integer solve(List<Integer> arr, int i, Integer k, Map<Integer, Integer> dp) {
        if (i == 0) return 0;
        if (dp.get(i) != null) {
            return dp.get(i);
        }
        Integer energy = Integer.MAX_VALUE;
        for (int j = 1; j <= k; j += 1) {
            if (i - j >= 0) {
                energy = Math.min(energy, Math.abs(arr.get(i - j) - arr.get(i)) + solve(arr, i - j, k, dp));
            }
        }
        dp.put(i, energy);
        return dp.get(i);
    }

    public static void main(String[] args) {
        System.out.println(frogJump(List.of(10, 30, 50, 60, 20, 10), 3));
        System.out.println(frogJump(List.of(10, 30, 50, 60, 20, 10), 2));
        System.out.println(frogJump(List.of(10, 30, 50, 60, 20, 10), 4));
        System.out.println(frogJump(List.of(10, 30, 50, 60, 20, 10), 1));
        System.out.println(frogJump(List.of(10, 30, 40, 50, 20), 3));
        System.out.println(frogJump(List.of(10, 20, 10), 1));
        System.out.println(frogJump(List.of(40, 10, 20, 70, 80, 10, 20, 70, 80, 60), 4));
    }
}
