package DynamicProgramming.DP10;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpaceOptimizedSolution {
    /*
        Time complexity is O(m * n) and space complexity is O(m).
     */
    public static Integer minPathSum(List<List<Integer>> mtx) {
        int n = mtx.size(), m = mtx.getFirst().size();

        Map<Integer, Integer> prev = new HashMap<>();
        prev.put(0, mtx.getFirst().getFirst());
        for (int j = 1; j < m; j += 1) {
            prev.put(j, mtx.getFirst().get(j) + prev.get(j - 1));
        }

        for (int i = 1; i < n; i += 1) {
            Map<Integer, Integer> curr = new HashMap<>();
            for (int j = 0; j < m; j += 1) {
                curr.put(j, Integer.MAX_VALUE);
            }
            curr.put(0, mtx.get(i).getFirst() + prev.get(0));
            for (int j = 1; j < m; j += 1) {
                Integer left = Integer.MAX_VALUE;
                if (0 <= i - 1 && i - 1 < n) {
                    left = mtx.get(i).get(j) + prev.get(j);
                }
                Integer right = Integer.MAX_VALUE;
                if (0 <= j - 1 && j - 1 < m) {
                    right = mtx.get(i).get(j) + curr.get(j - 1);
                }
                curr.put(j, Math.min(left, right));
            }
            prev = curr;
        }
        return prev.get(m - 1);
    }
}
