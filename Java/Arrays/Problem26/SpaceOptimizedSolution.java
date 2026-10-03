package Arrays.Problem26;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpaceOptimizedSolution {
    /*
        Time complexity is O(n) and space complexity is O(1).
     */
    public static Integer getMaxProfit(List<Integer> arr) {
        Map<Boolean, Map<Integer, Integer>> nxt = new HashMap<>();
        for (Boolean j : List.of(true, false)) {
            Map<Integer, Integer> subMap2 = new HashMap<>();
            subMap2.put(0, 0);
            subMap2.put(1, 0);
            subMap2.put(2, 0);
            nxt.put(j, subMap2);
        }
        for (int i = arr.size() - 1; i >= 0; i -= 1) {
            Map<Boolean, Map<Integer, Integer>> curr = new HashMap<>();
            for (Boolean j : List.of(true, false)) {
                Map<Integer, Integer> subMap2 = new HashMap<>();
                subMap2.put(0, 0);
                subMap2.put(1, 0);
                subMap2.put(2, 0);
                curr.put(j, subMap2);
            }
            for (boolean j : List.of(true, false)) {
                for (int k = 1; k <= 2; k += 1) {
                    if (j) {
                        curr.get(j).put(k, Math.max(
                                -arr.get(i) + nxt.get(!j).get(k),
                                nxt.get(j).get(k)
                        ));
                    } else {
                        curr.get(j).put(k, Math.max(
                                arr.get(i) + nxt.get(!j).get(k - 1),
                                nxt.get(j).get(k)
                        ));
                    }
                }
            }
            nxt = curr;
        }
        return nxt.get(true).get(2);
    }
}
