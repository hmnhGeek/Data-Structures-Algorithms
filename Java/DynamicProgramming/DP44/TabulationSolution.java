package DynamicProgramming.DP44;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    public static Integer getLDSLength(List<Integer> arr) {
        /*
            Time complexity is O(n^2) and space complexity is O(n^2).
         */
        int n = arr.size();
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Integer> prev = new HashMap<>();
            for (int j = 0; j < n + 1; j += 1) {
                prev.put(j, 0);
            }
            dp.put(i, prev);
        }
        for (int j = 0; j < n + 1; j += 1) {
            if (j == n) {
                dp.get(0).put(j, 1);
            } else if (arr.getFirst() % arr.get(j) == 0 || arr.get(j) % arr.getFirst() == 0) {
                dp.get(0).put(j, 1);
            }
        }

        for (int i = 1; i < n; i += 1) {
            for (int j = 1; j < n + 1; j += 1) {
                if (j == n) {
                    dp.get(i).put(j, Math.max(
                            1 + dp.get(i - 1).get(i),
                            dp.get(i - 1).get(j)
                    ));
                } else {
                    Integer left = Integer.MIN_VALUE;
                    if (arr.get(i) % arr.get(j) == 0 || arr.get(j) % arr.get(i) == 0) {
                        left = 1 + dp.get(i - 1).get(i);
                    }
                    Integer right = dp.get(i - 1).get(j);
                    dp.get(i).put(j, Math.max(left, right));
                }
            }
        }

        return dp.get(n - 1).get(n);
    }
}
