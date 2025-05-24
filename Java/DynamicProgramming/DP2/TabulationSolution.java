// Problem link - https://www.naukri.com/code360/problems/count-ways-to-reach-nth-stairs_798650?source=youtube&campaign=striver_dp_videos
// Solution - https://www.youtube.com/watch?v=mLfjzJsN8us&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=3


package DynamicProgramming.DP2;

import java.util.HashMap;
import java.util.Map;

public class TabulationSolution {
    public static int climbingStairs(Integer n) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        Map<Integer, Integer> dp = new HashMap<>();
        for (int i = -2; i <= n; i += 1) {
            dp.put(i, 0);
        }
        dp.put(0, 1);

        for (int i = 1; i <= n; i += 1) {
            int left = dp.get(i - 1);
            int right = dp.get(i - 2);
            dp.put(i, left + right);
        }
        return dp.get(n);
    }

    public static void main(String[] args) {
        System.out.println(climbingStairs(3));
        System.out.println(climbingStairs(4));
        System.out.println(climbingStairs(5));
        System.out.println(climbingStairs(1));
        System.out.println(climbingStairs(2));
    }
}
