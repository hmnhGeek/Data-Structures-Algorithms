package DynamicProgramming.DP41;

import java.util.List;

public class RecursiveSolution {
    public static Integer getLISLength(List<Integer> arr) {
        int n = arr.size();
        return solve(arr, n - 1, n, n);
    }

    private static Integer solve(List<Integer> arr, int i, int j, int n) {
        if (i == 0) {
            if (arr.get(i) < Utils.getValAtIdx(arr, j, n)) {
                return 1;
            }
            return 0;
        }
        Integer left = Integer.MIN_VALUE;
        if (arr.get(i) < Utils.getValAtIdx(arr, j, n)) {
            left = 1 + solve(arr, i - 1, i, n);
        }
        Integer right = solve(arr, i - 1, j, n);
        return Math.max(left, right);
    }
}
