package SearchingAndSorting.Problem12;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpaceOptimizedSolution {
    public static Integer houseRobber(List<Integer> arr) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */
        Map<Boolean, Integer> prev2 = new HashMap<>();
        prev2.put(true, 0);
        prev2.put(false, 0);

        Map<Boolean, Integer> prev = new HashMap<>();
        prev.put(true, 0);
        prev.put(false, 0);

        for (int i = 0; i < arr.size(); i += 1) {
            Map<Boolean, Integer> curr = new HashMap<>();
            curr.put(true, 0);
            curr.put(false, 0);
            for (boolean j : List.of(true, false)) {
                if (j) {
                    curr.put(j, arr.get(i) + Math.max(
                            prev2.get(true),
                            prev2.get(false)
                    ));
                } else {
                    curr.put(j, Math.max(
                            prev.get(true),
                            prev.get(false)
                    ));
                }
            }
            prev2 = prev;
            prev = curr;
        }

        return Math.max(
                prev.get(true),
                prev.get(false)
        );
    }
}
