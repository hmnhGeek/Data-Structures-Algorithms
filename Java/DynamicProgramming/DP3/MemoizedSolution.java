package DynamicProgramming.DP3;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    public static Integer frogJump(List<Integer> arr) {
        /*
            Time complexity is O(n) and space complexity is O(2n).
         */
        int n = arr.size();
        Map<Integer, Integer> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            dp.put(i, null);
        }
        return solve(arr, n - 1, dp);
    }

    private static Integer solve(List<Integer> arr, Integer i, Map<Integer, Integer> dp) {
        if (i == 0) return 0;
        if (dp.get(i) != null) {
            return dp.get(i);
        }
        int left = Integer.MAX_VALUE;
        if (i - 1 >= 0) {
            left = solve(arr, i - 1, dp) + Math.abs(arr.get(i) - arr.get(i - 1));
        }
        int right = Integer.MAX_VALUE;
        if (i - 2 >= 0) {
            right = solve(arr, i - 2, dp) + Math.abs(arr.get(i) - arr.get(i - 2));
        }
        dp.put(i, Math.min(left, right));
        return dp.get(i);
    }

    public static void main(String[] args) {
        System.out.println(frogJump(Arrays.asList(10, 20, 30, 10)));
        System.out.println(frogJump(Arrays.asList(10, 50, 10)));
        System.out.println(frogJump(Arrays.asList(7, 4, 4, 2, 6, 6, 3, 4)));
        System.out.println(frogJump(Arrays.asList(4, 8, 3, 10, 4, 4)));
        System.out.println(frogJump(Arrays.asList(30, 20, 50, 10, 40)));
    }
}
