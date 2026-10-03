package Arrays.Problem26;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    /*
        Time complexity is O(n) and space complexity is O(n + n).
     */
    public static Integer getMaxProfit(List<Integer> arr) {
        Map<Integer, Map<Boolean, Map<Integer, Integer>>> dp = new HashMap<>();
        for (int i = 0; i <= arr.size(); i += 1) {
            Map<Boolean, Map<Integer, Integer>> subMap = new HashMap<>();
            for (Boolean j : List.of(true, false)) {
                Map<Integer, Integer> subMap2 = new HashMap<>();
                subMap2.put(0, null);
                subMap2.put(1, null);
                subMap2.put(2, null);
                subMap.put(j, subMap2);
            }
            dp.put(i, subMap);
        }
        return solve(arr, 0, true, 2, dp);
    }

    private static Integer solve(List<Integer> arr, Integer i, Boolean j, Integer k, Map<Integer, Map<Boolean, Map<Integer, Integer>>> dp) {
        if (k == 0) return 0;
        if (i == arr.size()) return 0;
        if (dp.get(i).get(j).get(k) != null) {
            return dp.get(i).get(j).get(k);
        }
        if (j) {
            dp.get(i).get(j).put(k, Math.max(
                    -arr.get(i) + solve(arr, i + 1, !j, k, dp),
                    solve(arr, i + 1, j, k, dp)
            ));
        } else {
            dp.get(i).get(j).put(k, Math.max(
                    arr.get(i) + solve(arr, i + 1, !j, k - 1, dp),
                    solve(arr, i + 1, j, k, dp)
            ));
        }
        return dp.get(i).get(j).get(k);
    }
}
