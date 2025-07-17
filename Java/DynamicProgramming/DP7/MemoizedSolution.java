package DynamicProgramming.DP7;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    /*
        Time complexity is O(3n) and space complexity is O(4n).
     */
    public static Integer getMaxPoints(List<List<Integer>> matrix) {
        int n = matrix.size();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Integer> row = new HashMap<>();
            for (int j = 0; j < 3; j += 1) {
                row.put(j, null);
            }
            dp.put(i, row);
        }
        return Math.max(
                solve(matrix, n - 1, 2, dp),
                Math.max(
                        solve(matrix, n - 1, 0, dp),
                        solve(matrix, n - 1, 1, dp)
                )
        );
    }

    private static Integer solve(List<List<Integer>> matrix, int i, int j, Map<Integer, Map<Integer, Integer>> dp) {
        if (i == 0) return matrix.getFirst().get(j);
        if (dp.get(i).get(j) != null) {
            return dp.get(i).get(j);
        }
        List<Integer> nextIndices = Utils.getNext(j);
        Integer result = Integer.MIN_VALUE;
        for (int index : nextIndices) {
            result = Math.max(result, matrix.get(i).get(j) + solve(matrix, i - 1, index, dp));
        }
        dp.get(i).put(j, result);
        return dp.get(i).get(j);
    }
}
