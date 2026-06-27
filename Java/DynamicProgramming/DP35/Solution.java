package DynamicProgramming.DP35;

import java.util.Arrays;

public class Solution {
    public static void recursive() {
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(7, 1, 5, 3, 6, 4)));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(2, 100, 150, 120)));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(1, 2, 3, 4)));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(2, 2, 2, 2)));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(17, 20, 11, 9, 12, 6)));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(98, 101, 66, 72)));
        System.out.println();
    }

    public static void memoized() {
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(7, 1, 5, 3, 6, 4)));
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(2, 100, 150, 120)));
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(1, 2, 3, 4)));
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(2, 2, 2, 2)));
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(17, 20, 11, 9, 12, 6)));
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(98, 101, 66, 72)));
        System.out.println();
    }

    public static void tabulation() {
        System.out.println(TabulationSolution.getMaxProfit(Arrays.asList(7, 1, 5, 3, 6, 4)));
        System.out.println(TabulationSolution.getMaxProfit(Arrays.asList(2, 100, 150, 120)));
        System.out.println(TabulationSolution.getMaxProfit(Arrays.asList(1, 2, 3, 4)));
        System.out.println(TabulationSolution.getMaxProfit(Arrays.asList(2, 2, 2, 2)));
        System.out.println(TabulationSolution.getMaxProfit(Arrays.asList(17, 20, 11, 9, 12, 6)));
        System.out.println(TabulationSolution.getMaxProfit(Arrays.asList(98, 101, 66, 72)));
        System.out.println();
    }

    public static void spaceOptimized() {
        System.out.println(SpaceOptimizedSolution.getMaxProfit(Arrays.asList(7, 1, 5, 3, 6, 4)));
        System.out.println(SpaceOptimizedSolution.getMaxProfit(Arrays.asList(2, 100, 150, 120)));
        System.out.println(SpaceOptimizedSolution.getMaxProfit(Arrays.asList(1, 2, 3, 4)));
        System.out.println(SpaceOptimizedSolution.getMaxProfit(Arrays.asList(2, 2, 2, 2)));
        System.out.println(SpaceOptimizedSolution.getMaxProfit(Arrays.asList(17, 20, 11, 9, 12, 6)));
        System.out.println(SpaceOptimizedSolution.getMaxProfit(Arrays.asList(98, 101, 66, 72)));
        System.out.println();
    }

    public static void main(String[] args) {
        recursive();
        memoized();
        tabulation();
        spaceOptimized();
    }
}
