package DynamicProgramming.DP6;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    /*
        Time complexity is O(n) and space complexity is O(n).
     */
    private static Integer houseRobber(List<Integer> arr) {
        Map<Integer, Integer> dp = new HashMap<>();
        for (int i = 0; i < arr.size(); i += 1) {
            dp.put(i, null);
        }
        dp.put(-2, 0);
        dp.put(-1, 0);
        for (int i = 0; i < arr.size(); i += 1) {
            Integer left = arr.get(i) + dp.get(i - 2);
            Integer right = dp.get(i - 1);
            dp.put(i, Math.max(left, right));
        }
        return dp.get(arr.size() - 1);
    }

    public static Integer houseRobber2(List<Integer> arr) {
        Integer x = houseRobber(arr.subList(0, arr.size() - 1));
        Integer y = houseRobber(arr.subList(1, arr.size()));
        return Math.max(x, y);
    }
}
