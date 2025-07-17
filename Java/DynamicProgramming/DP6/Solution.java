// Problem link - https://neetcode.io/problems/house-robber-ii
// Solution - https://www.youtube.com/watch?v=3WaxQMELSkw&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=7

package DynamicProgramming.DP6;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        System.out.println(RecursiveSolution.houseRobber2(Arrays.asList(2, 3, 2)));
        System.out.println(RecursiveSolution.houseRobber2(Arrays.asList(1,2,3,1)));
        System.out.println(RecursiveSolution.houseRobber2(Arrays.asList(1, 2, 3)));
        System.out.println(RecursiveSolution.houseRobber2(Arrays.asList(2,9,8,3,6)));
        System.out.println();
        System.out.println(MemoizedSolution.houseRobber2(Arrays.asList(2, 3, 2)));
        System.out.println(MemoizedSolution.houseRobber2(Arrays.asList(1,2,3,1)));
        System.out.println(MemoizedSolution.houseRobber2(Arrays.asList(1, 2, 3)));
        System.out.println(MemoizedSolution.houseRobber2(Arrays.asList(2,9,8,3,6)));
        System.out.println();
        System.out.println(TabulationSolution.houseRobber2(Arrays.asList(2, 3, 2)));
        System.out.println(TabulationSolution.houseRobber2(Arrays.asList(1,2,3,1)));
        System.out.println(TabulationSolution.houseRobber2(Arrays.asList(1, 2, 3)));
        System.out.println(TabulationSolution.houseRobber2(Arrays.asList(2,9,8,3,6)));
        System.out.println();
        System.out.println(SpaceOptimizedSolution.houseRobber2(Arrays.asList(2, 3, 2)));
        System.out.println(SpaceOptimizedSolution.houseRobber2(Arrays.asList(1,2,3,1)));
        System.out.println(SpaceOptimizedSolution.houseRobber2(Arrays.asList(1, 2, 3)));
        System.out.println(SpaceOptimizedSolution.houseRobber2(Arrays.asList(2,9,8,3,6)));
    }
}
