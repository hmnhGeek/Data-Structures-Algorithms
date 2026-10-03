package Arrays.Problem26;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    /*
        Time complexity is O(n) and space complexity is O(n).
     */
    public static Integer getMaxProfit(List<Integer> arr) {
        Map<Integer, Map<Boolean, Map<Integer, Integer>>> dp = new HashMap<>();
        for (int i = 0; i <= arr.size(); i += 1) {
            Map<Boolean, Map<Integer, Integer>> subMap = new HashMap<>();
            for (Boolean j : List.of(true, false)) {
                Map<Integer, Integer> subMap2 = new HashMap<>();
                subMap2.put(0, 0);
                subMap2.put(1, 0);
                subMap2.put(2, 0);
                subMap.put(j, subMap2);
            }
            dp.put(i, subMap);
        }
        for (int i = arr.size() - 1; i >= 0; i -= 1) {
            for (boolean j : List.of(true, false)) {
                for (int k = 1; k <= 2; k += 1) {
                    if (j) {
                        dp.get(i).get(j).put(k, Math.max(
                                -arr.get(i) + dp.get(i + 1).get(!j).get(k),
                                dp.get(i + 1).get(j).get(k)
                        ));
                    } else {
                        dp.get(i).get(j).put(k, Math.max(
                                arr.get(i) + dp.get(i + 1).get(!j).get(k - 1),
                                dp.get(i + 1).get(j).get(k)
                        ));
                    }
                }
            }
        }
        return dp.get(0).get(true).get(2);
    }
}
