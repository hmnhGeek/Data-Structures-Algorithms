package SearchingAndSorting.Problem12;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    public static Integer houseRobber(List<Integer> arr) {
        /*
            Time complexity is O(n) and space complexity is O(2n).
         */
        Map<Integer, Map<Boolean, Integer>> dp = new HashMap<>();
        for (int i = 0; i < arr.size(); i += 1) {
            Map<Boolean, Integer> row = new HashMap<>();
            row.put(true, null);
            row.put(false, null);
            dp.put(i, row);
        }
        return Math.max(
                solve(arr, arr.size() - 1, true, dp),
                solve(arr, arr.size() - 1, false, dp)
        );
    }

    private static Integer solve(List<Integer> arr, int i, boolean j, Map<Integer, Map<Boolean, Integer>> dp) {
        if (i == -1 || i == -2) return 0;
        if (dp.get(i).get(j) != null) {
            return dp.get(i).get(j);
        }
        if (j) {
            dp.get(i).put(j, arr.get(i) + Math.max(
                    solve(arr, i - 2, true, dp),
                    solve(arr, i - 2, false, dp)
            ));
        } else {
            dp.get(i).put(j, Math.max(
                    solve(arr, i - 1, true, dp),
                    solve(arr, i - 1, false, dp)
            ));
        }
        return dp.get(i).get(j);
    }
}
