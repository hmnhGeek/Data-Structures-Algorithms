// Problem link - https://www.naukri.com/code360/problems/rod-cutting-problem_800284?source=youtube&campaign=striver_dp_videos
// Solution - https://www.youtube.com/watch?v=mO8XpGoJwuo&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=25


package DynamicProgramming.DP24;

import java.util.Arrays;

public class Solution {
    private static void recursive() {
        System.out.println(RecursiveSolution.getMaxCost(Arrays.asList(2, 5, 7, 8, 10)));
        System.out.println(RecursiveSolution.getMaxCost(Arrays.asList(3, 5, 8, 9, 10, 17, 17, 20)));
        System.out.println(RecursiveSolution.getMaxCost(Arrays.asList(3, 5, 6, 7, 10, 12)));
        System.out.println(RecursiveSolution.getMaxCost(Arrays.asList(1, 10, 3, 1, 3, 1, 5, 9)));
        System.out.println(RecursiveSolution.getMaxCost(Arrays.asList(1, 5, 8, 9, 10, 17, 17, 20)));
        System.out.println(RecursiveSolution.getMaxCost(Arrays.asList(3)));
        System.out.println();
    }

    private static void memoized() {
        System.out.println(MemoizedSolution.getMaxCost(Arrays.asList(2, 5, 7, 8, 10)));
        System.out.println(MemoizedSolution.getMaxCost(Arrays.asList(3, 5, 8, 9, 10, 17, 17, 20)));
        System.out.println(MemoizedSolution.getMaxCost(Arrays.asList(3, 5, 6, 7, 10, 12)));
        System.out.println(MemoizedSolution.getMaxCost(Arrays.asList(1, 10, 3, 1, 3, 1, 5, 9)));
        System.out.println(MemoizedSolution.getMaxCost(Arrays.asList(1, 5, 8, 9, 10, 17, 17, 20)));
        System.out.println(MemoizedSolution.getMaxCost(Arrays.asList(3)));
        System.out.println();
    }

    private static void tabulation() {
        System.out.println(TabulationSolution.getMaxCost(Arrays.asList(2, 5, 7, 8, 10)));
        System.out.println(TabulationSolution.getMaxCost(Arrays.asList(3, 5, 8, 9, 10, 17, 17, 20)));
        System.out.println(TabulationSolution.getMaxCost(Arrays.asList(3, 5, 6, 7, 10, 12)));
        System.out.println(TabulationSolution.getMaxCost(Arrays.asList(1, 10, 3, 1, 3, 1, 5, 9)));
        System.out.println(TabulationSolution.getMaxCost(Arrays.asList(1, 5, 8, 9, 10, 17, 17, 20)));
        System.out.println(TabulationSolution.getMaxCost(Arrays.asList(3)));
        System.out.println();
    }

    private static void spaceOptimized() {
        System.out.println(SpaceOptimizedSolution.getMaxCost(Arrays.asList(2, 5, 7, 8, 10)));
        System.out.println(SpaceOptimizedSolution.getMaxCost(Arrays.asList(3, 5, 8, 9, 10, 17, 17, 20)));
        System.out.println(SpaceOptimizedSolution.getMaxCost(Arrays.asList(3, 5, 6, 7, 10, 12)));
        System.out.println(SpaceOptimizedSolution.getMaxCost(Arrays.asList(1, 10, 3, 1, 3, 1, 5, 9)));
        System.out.println(SpaceOptimizedSolution.getMaxCost(Arrays.asList(1, 5, 8, 9, 10, 17, 17, 20)));
        System.out.println(SpaceOptimizedSolution.getMaxCost(Arrays.asList(3)));
        System.out.println();
    }

    public static void main(String[] args) {
        recursive();
        memoized();
        tabulation();
        spaceOptimized();
    }
}
