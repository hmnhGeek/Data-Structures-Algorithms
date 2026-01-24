// Problem link - https://www.geeksforgeeks.org/coin-change-dp-7/
// Solution - https://www.youtube.com/watch?v=HgyouUi11zk&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=23


package DynamicProgramming.DP22;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        recursive();
        memoized();
        tabulation();
    }

    private static void recursive() {
        System.out.println(RecursiveSolution.getNumWays(Arrays.asList(1, 2, 3), 4));
        System.out.println(RecursiveSolution.getNumWays(Arrays.asList(5, 3, 2), 1));
        System.out.println(RecursiveSolution.getNumWays(Arrays.asList(1, 2, 5), 5));
        System.out.println(RecursiveSolution.getNumWays(Arrays.asList(2), 3));
        System.out.println(RecursiveSolution.getNumWays(Arrays.asList(10), 10));
        System.out.println(RecursiveSolution.getNumWays(Arrays.asList(2, 5, 3, 6), 10));
        System.out.println();
    }

    private static void memoized() {
        System.out.println(MemoizedSolution.getNumWays(Arrays.asList(1, 2, 3), 4));
        System.out.println(MemoizedSolution.getNumWays(Arrays.asList(5, 3, 2), 1));
        System.out.println(MemoizedSolution.getNumWays(Arrays.asList(1, 2, 5), 5));
        System.out.println(MemoizedSolution.getNumWays(Arrays.asList(2), 3));
        System.out.println(MemoizedSolution.getNumWays(Arrays.asList(10), 10));
        System.out.println(MemoizedSolution.getNumWays(Arrays.asList(2, 5, 3, 6), 10));
        System.out.println();
    }

    private static void tabulation() {
        System.out.println(TabulationSolution.getNumWays(Arrays.asList(1, 2, 3), 4));
        System.out.println(TabulationSolution.getNumWays(Arrays.asList(5, 3, 2), 1));
        System.out.println(TabulationSolution.getNumWays(Arrays.asList(1, 2, 5), 5));
        System.out.println(TabulationSolution.getNumWays(Arrays.asList(2), 3));
        System.out.println(TabulationSolution.getNumWays(Arrays.asList(10), 10));
        System.out.println(TabulationSolution.getNumWays(Arrays.asList(2, 5, 3, 6), 10));
        System.out.println();
    }

    private static void spaceOptimized() {
        System.out.println(SpaceOptimizedSolution.getNumWays(Arrays.asList(1, 2, 3), 4));
        System.out.println(SpaceOptimizedSolution.getNumWays(Arrays.asList(5, 3, 2), 1));
        System.out.println(SpaceOptimizedSolution.getNumWays(Arrays.asList(1, 2, 5), 5));
        System.out.println(SpaceOptimizedSolution.getNumWays(Arrays.asList(2), 3));
        System.out.println(SpaceOptimizedSolution.getNumWays(Arrays.asList(10), 10));
        System.out.println(SpaceOptimizedSolution.getNumWays(Arrays.asList(2, 5, 3, 6), 10));
        System.out.println();
    }
}
