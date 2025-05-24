// Problem link - https://www.naukri.com/code360/problems/count-ways-to-reach-nth-stairs_798650?source=youtube&campaign=striver_dp_videos
// Solution - https://www.youtube.com/watch?v=mLfjzJsN8us&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=3


package DynamicProgramming.DP2;

import java.util.ArrayList;
import java.util.List;

public class MemoizedSolution {
    public static int climbingStairs(Integer n) {
        /*
            Time complexity is O(n) and space complexity is O(n + n).
         */
        List<Integer> dp = new ArrayList<>();
        for (int i = 0; i <= n; i += 1) {
            dp.add(null);
        }
        return solve(n, dp);
    }

    private static int solve(Integer n, List<Integer> dp) {
        if (n == 0) return 1;
        if (n < 0) return 0;
        if (dp.get(n) != null) {
            return dp.get(n);
        }
        int left = solve(n - 1, dp);
        int right = solve(n - 2, dp);
        dp.set(n, left + right);
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
