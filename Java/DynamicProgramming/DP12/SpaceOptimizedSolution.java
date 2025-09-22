package DynamicProgramming.DP12;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpaceOptimizedSolution {
    public static Integer getMaxFallingSum(List<List<Integer>> mtx) {
        /*
            Time complexity is O(m^2 * n) and space complexity is O(m).
         */
        int n = mtx.size(), m = mtx.getFirst().size();
        Integer result = Integer.MIN_VALUE;

        for (int endColIndex = 0; endColIndex < m; endColIndex += 1) {

            Map<Integer, Integer> prev = new HashMap<>();
            for (int j = 0; j < m; j += 1) {
                prev.put(j, mtx.getFirst().get(j));
            }

            for (int i = 1; i < n; i += 1) {
                Map<Integer, Integer> curr = new HashMap<>();
                for (int j = 0; j < m; j += 1) {
                    Integer upperLeft = Integer.MIN_VALUE;
                    if (0 <= i - 1 && 0 <= j - 1 && j - 1 < m) {
                        upperLeft = prev.get(j - 1);
                    }
                    Integer up = Integer.MIN_VALUE;
                    if (0 <= i - 1) {
                        up = prev.get(j);
                    }
                    Integer upperRight = Integer.MIN_VALUE;
                    if (0 <= i - 1 && 0 <= j + 1 && j + 1 < m) {
                        upperRight = prev.get(j + 1);
                    }
                    curr.put(j, mtx.get(i).get(j) + Math.max(upperLeft, Math.max(up, upperRight)));
                }
                prev = curr;
            }

            Integer pathSum = prev.get(endColIndex);
            result = Math.max(pathSum, result);
        }
        return result;
    }
}
