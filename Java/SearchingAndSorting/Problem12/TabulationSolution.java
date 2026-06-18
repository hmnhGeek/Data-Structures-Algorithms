package SearchingAndSorting.Problem12;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    public static Integer houseRobber(List<Integer> arr) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        Map<Integer, Map<Boolean, Integer>> dp = new HashMap<>();
        for (int i = -2; i < arr.size(); i += 1) {
            Map<Boolean, Integer> row = new HashMap<>();
            row.put(true, 0);
            row.put(false, 0);
            dp.put(i, row);
        }

        for (int i = 0; i < arr.size(); i += 1) {
            for (boolean j : List.of(true, false)) {
                if (j) {
                    dp.get(i).put(j, arr.get(i) + Math.max(
                            dp.get(i - 2).get(true),
                            dp.get(i - 2).get(false)
                    ));
                } else {
                    dp.get(i).put(j, Math.max(
                            dp.get(i - 1).get(true),
                            dp.get(i - 1).get(false)
                    ));
                }
            }
        }

        return Math.max(
                dp.get(arr.size() - 1).get(true),
                dp.get(arr.size() - 1).get(false)
        );
    }
}
