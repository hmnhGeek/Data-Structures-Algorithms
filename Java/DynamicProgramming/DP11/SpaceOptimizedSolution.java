package DynamicProgramming.DP11;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpaceOptimizedSolution {
    /*
        Time complexity is O(n*n*n) and space complexity is O(n).
     */
    public static Integer getMinPathSum(List<List<Integer>> triangle) {
        int n = triangle.size();
        Integer result = Integer.MAX_VALUE;
        for (int k = 0; k < n; k += 1) {
            Map<Integer, Integer> prev = getRow(triangle, n);
            for (int i = 1; i < n; i += 1) {
                Map<Integer, Integer> curr = getRow(triangle, n);
                for (int j = 0; j < i + 1; j += 1) {
                    Integer up = Integer.MAX_VALUE;
                    if (0 <= i - 1 && j < i) {
                        up = prev.get(j);
                    }
                    Integer diagonal = Integer.MAX_VALUE;
                    if (0 <= i - 1 && 0 <= j - 1) {
                        diagonal = prev.get(j - 1);
                    }
                    curr.put(j, triangle.get(i).get(j) + Math.min(up, diagonal));
                }
                prev = curr;
            }

            result = Math.min(result, prev.get(k));
        }
        return result;
    }

    private static Map<Integer, Integer> getRow(List<List<Integer>> triangle, int n) {
        Map<Integer, Integer> prev = new HashMap<>();
        for (int j = 0; j < n; j += 1) {
            prev.put(j, Integer.MAX_VALUE);
        }
        prev.put(0, triangle.getFirst().getFirst());
        return prev;
    }
}
