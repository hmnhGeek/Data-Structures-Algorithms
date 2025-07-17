package DynamicProgramming.DP6;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    /*
        Time complexity is O(n) and space complexity is O(2n).
     */
    private static Integer houseRobber(List<Integer> arr) {
        Map<Integer, Integer> dp = new HashMap<>();
        for (int i = 0; i < arr.size(); i += 1) {
            dp.put(i, null);
        }
        dp.put(-2, null);
        dp.put(-1, null);
        return solve(arr, arr.size() - 1, dp);
    }

    private static Integer solve(List<Integer> arr, int i, Map<Integer, Integer> dp) {
        if (i < 0) return 0;
        if (dp.get(i) != null) return dp.get(i);
        Integer left = arr.get(i) + solve(arr, i - 2, dp);
        Integer right = solve(arr, i - 1, dp);
        dp.put(i, Math.max(left, right));
        return dp.get(i);
    }

    public static Integer houseRobber2(List<Integer> arr) {
        Integer x = houseRobber(arr.subList(0, arr.size() - 1));
        Integer y = houseRobber(arr.subList(1, arr.size()));
        return Math.max(x, y);
    }
}
