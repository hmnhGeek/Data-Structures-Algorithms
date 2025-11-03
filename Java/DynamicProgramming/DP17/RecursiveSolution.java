package DynamicProgramming.DP17;

import java.util.List;

public class RecursiveSolution {
    /*
        Time complexity is exponential and space complexity is O(n).
     */
    public static Integer getCount(List<Integer> arr, Integer target) {
        int n = arr.size();
        return solve(arr, n - 1, target);
    }

    public static Integer solve(List<Integer> arr, int i, int j) {
        if (j == 0) return 1;
        if (i == 0) {
            if (arr.getFirst() == j) return 1;
            return 0;
        }
        Integer left = 0;
        if (j >= arr.get(i)) {
            left = solve(arr, i - 1, j - arr.get(i));
        }
        Integer right = solve(arr, i - 1, j);
        return left + right;
    }
}
