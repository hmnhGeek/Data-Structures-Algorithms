// Problem link - https://www.naukri.com/code360/problems/maximum-sum-of-non-adjacent-elements_843261?source=youtube&campaign=striver_dp_videos
// Solution - https://www.youtube.com/watch?v=GrMBfJNk_NY&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=6

package DynamicProgramming.DP5;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    /*
        Time complexity is O(n) and space complexity is O(n).
     */
    public static Integer houseRobber(List<Integer> arr) {
        int n = arr.size();
        Map<Integer, Integer> dp = new HashMap<>();
        for (int i = -2; i < n; i += 1) {
            dp.put(i, Integer.MIN_VALUE);
        }
        dp.put(-2, 0);
        dp.put(-1, 0);
        dp.put(0, arr.getFirst());
        for (int i = 1; i < n; i += 1) {
            Integer left = arr.get(i) + dp.get(i - 2);
            Integer right = dp.get(i - 1);
            dp.put(i, Math.max(left, right));
        }
        return dp.get(n - 1);
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
