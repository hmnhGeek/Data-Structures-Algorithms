// Problem link - https://www.naukri.com/code360/problems/maximum-path-sum-in-the-matrix_797998?source=youtube&campaign=striver_dp_videos
// Solution - https://www.youtube.com/watch?v=N_aJ5qQbYA0&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=13


package DynamicProgramming.DP12;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    public static Integer getMaxFallingSum(List<List<Integer>> mtx) {
        /*
            Time complexity is O(2^{m + n}) and space complexity is O(m + n).
         */
        int n = mtx.size(), m = mtx.getFirst().size();
        Integer result = Integer.MIN_VALUE;

        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Integer> row = new HashMap<>();
            for (int j = 0; j < m; j += 1) {
                row.putIfAbsent(j, null);
            }
            dp.putIfAbsent(i, row);
        }

        for (int endColIndex = 0; endColIndex < m; endColIndex += 1) {
            Integer pathSum = solve(mtx, n - 1, endColIndex, m, dp);
            result = Math.max(pathSum, result);
        }
        return result;
    }

    private static Integer solve(List<List<Integer>> mtx, int i, int j, int m, Map<Integer, Map<Integer, Integer>> dp) {
        if (i == 0) {
            return mtx.getFirst().get(j);
        }
        if (dp.get(i).get(j) != null) {
            return dp.get(i).get(j);
        }
        Integer upperLeft = Integer.MIN_VALUE;
        if (0 <= i - 1 && 0 <= j - 1 && j - 1 < m) {
            upperLeft = solve(mtx, i - 1, j - 1, m, dp);
        }
        Integer up = Integer.MIN_VALUE;
        if (0 <= i - 1) {
            up = solve(mtx, i - 1, j, m, dp);
        }
        Integer upperRight = Integer.MIN_VALUE;
        if (0 <= i - 1 && 0 <= j + 1 && j + 1 < m) {
            upperRight = solve(mtx, i - 1, j + 1, m, dp);
        }
        dp.get(i).put(j, mtx.get(i).get(j) + Math.max(upperLeft, Math.max(up, upperRight)));
        return dp.get(i).get(j);
    }
}
