// Problem link - https://www.naukri.com/code360/problems/count-ways-to-reach-nth-stairs_798650?source=youtube&campaign=striver_dp_videos
// Solution - https://www.youtube.com/watch?v=mLfjzJsN8us&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=3


package DynamicProgramming.DP2;

public class SpaceOptimizedSolution {
    public static int climbingStairs(Integer n) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */
        int prev2 = 0, prev1 = 1;
        for (int i = 1; i <= n; i += 1) {
            int left = prev1;
            int right = prev2;
            int curr = left + right;
            prev2 = prev1;
            prev1 = curr;
        }
        return prev1;
    }

    public static void main(String[] args) {
        System.out.println(climbingStairs(3));
        System.out.println(climbingStairs(4));
        System.out.println(climbingStairs(5));
        System.out.println(climbingStairs(1));
        System.out.println(climbingStairs(2));
    }
}
