package DynamicProgramming.DP12;

import java.util.List;

public class RecursiveSolution {
    public static Integer getMaxFallingSum(List<List<Integer>> mtx) {
        /*
            Time complexity is O(2^{m + n}) and space complexity is O(m + n).
         */
        int n = mtx.size(), m = mtx.getFirst().size();
        Integer result = Integer.MIN_VALUE;
        for (int endColIndex = 0; endColIndex < m; endColIndex += 1) {
            Integer pathSum = solve(mtx, n - 1, endColIndex, m);
            result = Math.max(pathSum, result);
        }
        return result;
    }

    private static Integer solve(List<List<Integer>> mtx, int i, int j, int m) {
        if (i == 0) {
            return mtx.getFirst().get(j);
        }
        Integer upperLeft = Integer.MIN_VALUE;
        if (0 <= i - 1 && 0 <= j - 1 && j - 1 < m) {
            upperLeft = solve(mtx, i - 1, j - 1, m);
        }
        Integer up = Integer.MIN_VALUE;
        if (0 <= i - 1) {
            up = solve(mtx, i - 1, j, m);
        }
        Integer upperRight = Integer.MIN_VALUE;
        if (0 <= i - 1 && 0 <= j + 1 && j + 1 < m) {
            upperRight = solve(mtx, i - 1, j + 1, m);
        }
        return mtx.get(i).get(j) + Math.max(upperLeft, Math.max(up, upperRight));
    }
}
