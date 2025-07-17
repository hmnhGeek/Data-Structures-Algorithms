package DynamicProgramming.DP7;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    /*
        Time complexity is O(3n) and space complexity is O(3n).
     */
    public static Integer getMaxPoints(List<List<Integer>> matrix) {
        int n = matrix.size();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Integer> row = new HashMap<>();
            for (int j = 0; j < 3; j += 1) {
                row.put(j, Integer.MIN_VALUE);
            }
            dp.put(i, row);
        }
        for (int j = 0; j < 3; j += 1) {
            dp.get(0).put(j, matrix.getFirst().get(j));
        }
        int result = Integer.MIN_VALUE;
        for (int j = 0; j < 3; j += 1) {
            for (int i = 1; i < n; i += 1) {
                List<Integer> nextIndices = Utils.getNext(j);
                for (int index : nextIndices) {
                    result = Math.max(result, matrix.get(i).get(j) + dp.get(i - 1).get(index));
                }
                dp.get(i).put(j, result);
            }
        }

        return result;
    }
}
