// Problem link - https://www.geeksforgeeks.org/problems/target-sum-1626326450/1
// Solution - https://www.youtube.com/watch?v=b3GD8263-PQ&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=22


package DynamicProgramming.DP21;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static Integer getTargetSum(List<Integer> arr, Integer target) {
        int sum = 0;
        for (Integer i : arr) {
            sum += i;
        }
        if ((target + sum) % 2 != 0) return -1;
        Integer targetForSubset = (target + sum)/2;
        return SpaceOptimizedSolution.countSubsets(arr, targetForSubset);
    }

    public static void main(String[] args) {
        System.out.println(getTargetSum(Arrays.asList(1, 1, 1, 1, 1), 3));
        System.out.println(getTargetSum(Arrays.asList(1, 2, 3, 1), 3));
        System.out.println(getTargetSum(Arrays.asList(1, 2, 3), 2));
        System.out.println(getTargetSum(Arrays.asList(1, 1), 0));
        System.out.println(getTargetSum(Arrays.asList(1), 1));
    }
}
