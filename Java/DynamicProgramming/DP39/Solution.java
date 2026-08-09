package DynamicProgramming.DP39;

import java.util.Arrays;

public class Solution {
    private static void recursive() {
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(4, 9, 0, 4, 10)));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(1, 2, 3, 4)));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(5, 4, 3)));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(1, 2, 3, 0, 2)));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(1)));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(3, 1, 6, 1, 2, 4)));
        System.out.println();
    }

    private static void memoized() {
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(4, 9, 0, 4, 10)));
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(1, 2, 3, 4)));
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(5, 4, 3)));
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(1, 2, 3, 0, 2)));
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(1)));
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(3, 1, 6, 1, 2, 4)));
        System.out.println();
    }

    private static void tabulation() {
        System.out.println(TabulationSolution.getMaxProfit(Arrays.asList(4, 9, 0, 4, 10)));
        System.out.println(TabulationSolution.getMaxProfit(Arrays.asList(1, 2, 3, 4)));
        System.out.println(TabulationSolution.getMaxProfit(Arrays.asList(5, 4, 3)));
        System.out.println(TabulationSolution.getMaxProfit(Arrays.asList(1, 2, 3, 0, 2)));
        System.out.println(TabulationSolution.getMaxProfit(Arrays.asList(1)));
        System.out.println(TabulationSolution.getMaxProfit(Arrays.asList(3, 1, 6, 1, 2, 4)));
        System.out.println();
    }

    private static void spaceOptimized() {
        System.out.println(SpaceOptimizedSolution.getMaxProfit(Arrays.asList(4, 9, 0, 4, 10)));
        System.out.println(SpaceOptimizedSolution.getMaxProfit(Arrays.asList(1, 2, 3, 4)));
        System.out.println(SpaceOptimizedSolution.getMaxProfit(Arrays.asList(5, 4, 3)));
        System.out.println(SpaceOptimizedSolution.getMaxProfit(Arrays.asList(1, 2, 3, 0, 2)));
        System.out.println(SpaceOptimizedSolution.getMaxProfit(Arrays.asList(1)));
        System.out.println(SpaceOptimizedSolution.getMaxProfit(Arrays.asList(3, 1, 6, 1, 2, 4)));
        System.out.println();
    }

    public static void main(String[] args) {
        recursive();
        memoized();
        tabulation();
        spaceOptimized();
    }
}
