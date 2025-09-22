package DynamicProgramming.DP12;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
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
                row.putIfAbsent(j, Integer.MIN_VALUE);
            }
            dp.putIfAbsent(i, row);
        }

        for (int j = 0; j < m; j += 1) {
            dp.get(0).put(j, mtx.getFirst().get(j));
        }

        for (int endColIndex = 0; endColIndex < m; endColIndex += 1) {

            for (int i = 1; i < n; i += 1) {
                for (int j = 0; j < m; j += 1) {
                    Integer upperLeft = Integer.MIN_VALUE;
                    if (0 <= i - 1 && 0 <= j - 1 && j - 1 < m) {
                        upperLeft = dp.get(i - 1).get(j - 1);
                    }
                    Integer up = Integer.MIN_VALUE;
                    if (0 <= i - 1) {
                        up = dp.get(i - 1).get(j);
                    }
                    Integer upperRight = Integer.MIN_VALUE;
                    if (0 <= i - 1 && 0 <= j + 1 && j + 1 < m) {
                        upperRight = dp.get(i - 1).get(j + 1);
                    }
                    dp.get(i).put(j, mtx.get(i).get(j) + Math.max(upperLeft, Math.max(up, upperRight)));
                }
            }

            Integer pathSum = dp.get(n - 1).get(endColIndex);
            result = Math.max(pathSum, result);
        }
        return result;
    }
}
