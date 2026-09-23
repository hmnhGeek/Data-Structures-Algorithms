package DynamicProgramming.DP44;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpaceOptimizedSolution {
    public static Integer getLDSLength(List<Integer> arr) {
        /*
            Time complexity is O(n^2) and space complexity is O(n).
         */
        int n = arr.size();
        Map<Integer, Integer> prev = new HashMap<>();
        for (int j = 0; j < n + 1; j += 1) {
            prev.put(j, 0);
        }
        for (int j = 0; j < n + 1; j += 1) {
            if (j == n) {
                prev.put(j, 1);
            } else if (arr.getFirst() % arr.get(j) == 0 || arr.get(j) % arr.getFirst() == 0) {
                prev.put(j, 1);
            }
        }

        for (int i = 1; i < n; i += 1) {
            Map<Integer, Integer> curr = new HashMap<>();
            for (int j = 0; j < n + 1; j += 1) {
                curr.put(j, 0);
            }
            for (int j = 1; j < n + 1; j += 1) {
                if (j == n) {
                    curr.put(j, Math.max(
                            1 + prev.get(i),
                            prev.get(j)
                    ));
                } else {
                    Integer left = Integer.MIN_VALUE;
                    if (arr.get(i) % arr.get(j) == 0 || arr.get(j) % arr.get(i) == 0) {
                        left = 1 + prev.get(i);
                    }
                    Integer right = prev.get(j);
                    curr.put(j, Math.max(left, right));
                }
            }
            prev = curr;
        }

        return prev.get(n);
    }
}
