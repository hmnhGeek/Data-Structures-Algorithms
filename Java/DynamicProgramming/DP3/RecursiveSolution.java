// Problem link - https://www.naukri.com/code360/problems/frog-jump_3621012
// Solution - https://www.youtube.com/watch?v=EgG3jsGoPvQ&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=4


package DynamicProgramming.DP3;

import java.util.Arrays;
import java.util.List;

public class RecursiveSolution {
    public static Integer frogJump(List<Integer> arr) {
        /*
            Time complexity is exponential and space complexity is O(n).
         */
        int n = arr.size();
        return solve(arr, n - 1);
    }

    private static Integer solve(List<Integer> arr, Integer i) {
        if (i == 0) return 0;
        int left = Integer.MAX_VALUE;
        if (i - 1 >= 0) {
            left = solve(arr, i - 1) + Math.abs(arr.get(i) - arr.get(i - 1));
        }
        int right = Integer.MAX_VALUE;
        if (i - 2 >= 0) {
            right = solve(arr, i - 2) + Math.abs(arr.get(i) - arr.get(i - 2));
        }
        return Math.min(left, right);
    }

    public static void main(String[] args) {
        System.out.println(frogJump(Arrays.asList(10, 20, 30, 10)));
        System.out.println(frogJump(Arrays.asList(10, 50, 10)));
        System.out.println(frogJump(Arrays.asList(7, 4, 4, 2, 6, 6, 3, 4)));
        System.out.println(frogJump(Arrays.asList(4, 8, 3, 10, 4, 4)));
        System.out.println(frogJump(Arrays.asList(30, 20, 50, 10, 40)));
    }
}
