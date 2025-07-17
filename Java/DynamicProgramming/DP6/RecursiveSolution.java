package DynamicProgramming.DP6;

import java.util.List;

public class RecursiveSolution {
    /*
        Time complexity is O(2^n) and space complexity is O(n).
     */
    private static Integer houseRobber(List<Integer> arr) {
        return solve(arr, arr.size() - 1);
    }

    private static Integer solve(List<Integer> arr, int i) {
        if (i < 0) return 0;
        Integer left = arr.get(i) + solve(arr, i - 2);
        Integer right = solve(arr, i - 1);
        return Math.max(left, right);
    }

    public static Integer houseRobber2(List<Integer> arr) {
        Integer x = houseRobber(arr.subList(0, arr.size() - 1));
        Integer y = houseRobber(arr.subList(1, arr.size()));
        return Math.max(x, y);
    }
}
