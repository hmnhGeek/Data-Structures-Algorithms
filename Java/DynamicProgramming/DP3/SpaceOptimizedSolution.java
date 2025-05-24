// Problem link - https://www.naukri.com/code360/problems/frog-jump_3621012
// Solution - https://www.youtube.com/watch?v=EgG3jsGoPvQ&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=4


package DynamicProgramming.DP3;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpaceOptimizedSolution {
    public static Integer frogJump(List<Integer> arr) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */
        int n = arr.size();
        int prev1 = 0, prev2 = 0;
        for (int i = 1; i < n; i += 1) {
            int left = prev1 + Math.abs(arr.get(i) - arr.get(i - 1));
            int right = Integer.MAX_VALUE;
            if (i - 2 >= 0) {
                right = prev2 + Math.abs(arr.get(i) - arr.get(i - 2));
            }
            int curr = Math.min(left, right);
            prev2 = prev1;
            prev1 = curr;
        }
        return prev1;
    }

    public static void main(String[] args) {
        System.out.println(frogJump(Arrays.asList(10, 20, 30, 10)));
        System.out.println(frogJump(Arrays.asList(10, 50, 10)));
        System.out.println(frogJump(Arrays.asList(7, 4, 4, 2, 6, 6, 3, 4)));
        System.out.println(frogJump(Arrays.asList(4, 8, 3, 10, 4, 4)));
        System.out.println(frogJump(Arrays.asList(30, 20, 50, 10, 40)));
    }
}
