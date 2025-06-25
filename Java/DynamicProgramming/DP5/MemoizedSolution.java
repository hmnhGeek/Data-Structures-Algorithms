package DynamicProgramming.DP5;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    /*
        Time complexity is O(n) and space complexity is O(2n).
     */
    public static Integer houseRobber(List<Integer> arr) {
        int n = arr.size();
        Map<Integer, Integer> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            dp.put(i, null);
        }
        return solve(arr, n - 1, dp);
    }

    private static Integer solve(List<Integer> arr, int i, Map<Integer, Integer> dp) {
        if (i < 0) return 0;
        if (i == 0) return arr.getFirst();
        if (dp.get(i) != null) {
            return dp.get(i);
        }
        Integer left = arr.get(i) + solve(arr, i - 2, dp);
        Integer right = solve(arr, i - 1, dp);
        dp.put(i, Math.max(left, right));
        return dp.get(i);
    }

    public static void main(String[] args) {
        System.out.println(houseRobber(List.of(2, 1, 4, 9)));
        System.out.println(houseRobber(List.of(1, 2, 4)));
        System.out.println(houseRobber(List.of(1, 2, 3, 5, 4)));
        System.out.println(houseRobber(List.of(1, 2, 3, 1, 3, 5, 8, 1, 9)));
        System.out.println(houseRobber(List.of(2, 7, 9, 3, 1)));
        System.out.println(houseRobber(List.of(1, 2, 3, 1)));
        System.out.println(houseRobber(List.of(1, 5, 2, 1, 6)));
    }
}
