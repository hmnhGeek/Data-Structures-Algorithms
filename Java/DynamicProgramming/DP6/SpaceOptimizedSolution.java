package DynamicProgramming.DP6;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpaceOptimizedSolution {
    /*
        Time complexity is O(n) and space complexity is O(n).
     */
    private static Integer houseRobber(List<Integer> arr) {
        int prev2 = 0, prev = 0;
        for (int i = 0; i < arr.size(); i += 1) {
            Integer left = arr.get(i) + prev2;
            Integer right = prev;
            int curr = Math.max(left, right);
            prev2 = prev;
            prev = curr;
        }
        return prev;
    }

    public static Integer houseRobber2(List<Integer> arr) {
        Integer x = houseRobber(arr.subList(0, arr.size() - 1));
        Integer y = houseRobber(arr.subList(1, arr.size()));
        return Math.max(x, y);
    }
}
