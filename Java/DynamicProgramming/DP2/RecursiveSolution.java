// Problem link - https://www.naukri.com/code360/problems/count-ways-to-reach-nth-stairs_798650?source=youtube&campaign=striver_dp_videos
// Solution - https://www.youtube.com/watch?v=mLfjzJsN8us&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=3


package DynamicProgramming.DP2;

public class RecursiveSolution {
    public static int climbingStairs(int n) {
        /*
            Time complexity is O(2^n) and space complexity is O(n).
         */
        return solve(n);
    }

    private static int solve(int n) {
        if (n == 0) return 1;
        if (n < 0) return 0;
        int left = solve(n - 1);
        int right = solve(n - 2);
        return left + right;
    }

    public static void main(String[] args) {
        System.out.println(climbingStairs(3));
        System.out.println(climbingStairs(4));
        System.out.println(climbingStairs(5));
        System.out.println(climbingStairs(1));
        System.out.println(climbingStairs(2));
    }
}
