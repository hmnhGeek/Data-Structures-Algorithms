package DynamicProgramming.DP11;

import java.util.List;

public class RecursiveSolution {
    /*
        Time complexity is O(2^{m + n}) and space complexity is O(n + m).
     */
    public static Integer getMinPathSum(List<List<Integer>> triangle) {
        int n = triangle.size();
        Integer result = Integer.MAX_VALUE;
        for (int j = 0; j < n; j += 1) {
            result = Math.min(result, solve(triangle, n - 1, j, n));
        }
        return result;
    }

    private static Integer solve(List<List<Integer>> triangle, int i, int j, int n) {
        if (i == 0 && j == 0) {
            return triangle.getFirst().getFirst();
        }
        Integer up = Integer.MAX_VALUE;
        if (0 <= i - 1 && j < i) {
            up = solve(triangle, i - 1, j, n);
        }
        Integer diagonal = Integer.MAX_VALUE;
        if (0 <= i - 1 && 0 <= j - 1) {
            diagonal = solve(triangle, i - 1, j - 1, n);
        }
        return triangle.get(i).get(j) + Math.min(up, diagonal);
    }
}
