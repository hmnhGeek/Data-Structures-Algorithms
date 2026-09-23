package DynamicProgramming.DP44;

import java.util.List;

public class RecursiveSolution {
    public static Integer getLDSLength(List<Integer> arr) {
        /*
            Time complexity is exponential and space complexity is O(n).
         */
        int n = arr.size();
        return solve(arr, n - 1, n, n);
    }

    private static Integer solve(List<Integer> arr, int i, Integer j, int n) {
        if (i == 0) {
            if (j == n) return 1;
            if (arr.get(i) % arr.get(j) == 0 || arr.get(j) % arr.get(i) == 0) {
                return 1;
            }
            return 0;
        }

        if (j == n) {
            return Math.max(
                    1 + solve(arr, i - 1, i, n),
                    solve(arr, i - 1, j, n)
            );
        }
        Integer left = Integer.MIN_VALUE;
        if (arr.get(i) % arr.get(j) == 0 || arr.get(j) % arr.get(i) == 0) {
            left = 1 + solve(arr, i - 1, i, n);
        }
        Integer right = solve(arr, i - 1, j, n);
        return Math.max(left, right);
    }
}
