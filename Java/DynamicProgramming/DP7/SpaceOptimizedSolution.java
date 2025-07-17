package DynamicProgramming.DP7;

import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpaceOptimizedSolution {
    /*
        Time complexity is O(3n) and space complexity is O(3).
     */
    public static Integer getMaxPoints(List<List<Integer>> matrix) {
        int n = matrix.size();
        Map<Integer, Integer> prev = new HashMap<>();
        for (int j = 0; j < 3; j += 1) {
            prev.put(j, matrix.getFirst().get(j));
        }
        for (int i = 1; i < n; i += 1) {
            Map<Integer, Integer> curr = new HashMap<>();
            for (int k = 0; k < 3; k += 1) {
                curr.put(k, Integer.MIN_VALUE);
            }
            for (int j = 0; j < 3; j += 1) {
                int result = Integer.MIN_VALUE;
                List<Integer> nextIndices = Utils.getNext(j);
                for (int index : nextIndices) {
                    result = Math.max(result, matrix.get(i).get(j) + prev.get(index));
                }
                curr.put(j, result);
            }
            prev = curr;
        }
        return Collections.max(prev.values());
    }
}
