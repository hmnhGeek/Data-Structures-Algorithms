package DynamicProgramming.DP36;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        recursive();
        memoized();
        tabulation();
    }

    private static void recursive() {
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(7, 1, 5, 3, 6, 4)));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(1, 2, 3, 4, 5, 6, 7)));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(7, 6, 5, 4, 3, 2, 1)));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(1, 2, 3, 4, 5)));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(100, 180, 260, 310, 40, 535, 695)));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(4, 2, 2, 2, 4)));
        System.out.println();
    }

    private static void memoized() {
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(7, 1, 5, 3, 6, 4)));
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(1, 2, 3, 4, 5, 6, 7)));
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(7, 6, 5, 4, 3, 2, 1)));
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(1, 2, 3, 4, 5)));
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(100, 180, 260, 310, 40, 535, 695)));
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(4, 2, 2, 2, 4)));
        System.out.println();
    }

    private static void tabulation() {
        System.out.println(TabulationSolution.getMaxProfit(Arrays.asList(7, 1, 5, 3, 6, 4)));
        System.out.println(TabulationSolution.getMaxProfit(Arrays.asList(1, 2, 3, 4, 5, 6, 7)));
        System.out.println(TabulationSolution.getMaxProfit(Arrays.asList(7, 6, 5, 4, 3, 2, 1)));
        System.out.println(TabulationSolution.getMaxProfit(Arrays.asList(1, 2, 3, 4, 5)));
        System.out.println(TabulationSolution.getMaxProfit(Arrays.asList(100, 180, 260, 310, 40, 535, 695)));
        System.out.println(TabulationSolution.getMaxProfit(Arrays.asList(4, 2, 2, 2, 4)));
        System.out.println();
    }
}
