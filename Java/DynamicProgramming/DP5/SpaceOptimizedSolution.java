package DynamicProgramming.DP5;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpaceOptimizedSolution {
    /*
        Time complexity is O(n) and space complexity is O(1).
     */
    public static Integer houseRobber(List<Integer> arr) {
        int n = arr.size();
        Map<Integer, Integer> dp = new HashMap<>();
        for (int i = -2; i < n; i += 1) {
            dp.put(i, Integer.MIN_VALUE);
        }
        int prev2 = 0;
        int prev = arr.getFirst();
        for (int i = 1; i < n; i += 1) {
            int curr = Integer.MIN_VALUE;
            Integer left = arr.get(i) + prev2;
            Integer right = prev;
            curr = Math.max(left, right);
            prev2 = prev;
            prev = curr;
        }
        return prev;
    }

    public static void main(String[] args) {
        System.out.println(houseRobber(List.of(2, 1, 4, 9)));
        System.out.println(houseRobber(List.of(1, 2, 4)));
        System.out.println(houseRobber(List.of(1, 2, 3, 5, 4)));
        System.out.println(houseRobber(List.of(1, 2, 3, 1, 3, 5, 8, 1, 9)));
        System.out.println(houseRobber(List.of(2, 7, 9, 3, 1)));
        System.out.println(houseRobber(List.of(1, 2, 3, 1)));
        System.out.println(houseRobber(List.of(1, 5, 2, 1, 6)));
    }
}
