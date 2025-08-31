package DynamicProgramming.DP10;

import java.util.List;

public class RecursiveSolution {
    /*
        Time complexity is O(2^{m + n}) and space complexity is O(m + n).
     */
    public static Integer minPathSum(List<List<Integer>> mtx) {
        int n = mtx.size(), m = mtx.getFirst().size();
        return solve(mtx, n - 1, m - 1, n, m);
    }

    private static Integer solve(List<List<Integer>> mtx, int i, int j, int n, int m) {
        if (i == 0 && j == 0) {
            return mtx.getFirst().getFirst();
        }
        Integer left = Integer.MAX_VALUE;
        if (0 <= i - 1 && i - 1 < n) {
            left = mtx.get(i).get(j) + solve(mtx, i - 1, j, n, m);
        }
        Integer right = Integer.MAX_VALUE;
        if (0 <= j - 1 && j - 1 < m) {
            right = mtx.get(i).get(j) + solve(mtx, i, j - 1, n, m);
        }
        return Math.min(left, right);
    }
}
