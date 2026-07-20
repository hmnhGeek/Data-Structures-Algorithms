package DynamicProgramming.DP37;

import java.util.Arrays;

public class Solution {
    public static void recursive() {
        System.out.println(RecursiveSolution.findMaxProfit(Arrays.asList(3, 3, 5, 0, 0, 3, 1, 4)));
        System.out.println(RecursiveSolution.findMaxProfit(Arrays.asList(1, 3, 1, 2, 4, 8)));
        System.out.println(RecursiveSolution.findMaxProfit(Arrays.asList(5, 4, 3, 2, 1)));
        System.out.println(RecursiveSolution.findMaxProfit(Arrays.asList(1, 2, 3, 4, 5)));
        System.out.println(RecursiveSolution.findMaxProfit(Arrays.asList(7, 1, 5, 3, 6, 4)));
        System.out.println();
    }

    public static void memoized() {
        System.out.println(MemoizedSolution.findMaxProfit(Arrays.asList(3, 3, 5, 0, 0, 3, 1, 4)));
        System.out.println(MemoizedSolution.findMaxProfit(Arrays.asList(1, 3, 1, 2, 4, 8)));
        System.out.println(MemoizedSolution.findMaxProfit(Arrays.asList(5, 4, 3, 2, 1)));
        System.out.println(MemoizedSolution.findMaxProfit(Arrays.asList(1, 2, 3, 4, 5)));
        System.out.println(MemoizedSolution.findMaxProfit(Arrays.asList(7, 1, 5, 3, 6, 4)));
        System.out.println();
    }

    public static void tabulation() {
        System.out.println(TabulationSolution.findMaxProfit(Arrays.asList(3, 3, 5, 0, 0, 3, 1, 4)));
        System.out.println(TabulationSolution.findMaxProfit(Arrays.asList(1, 3, 1, 2, 4, 8)));
        System.out.println(TabulationSolution.findMaxProfit(Arrays.asList(5, 4, 3, 2, 1)));
        System.out.println(TabulationSolution.findMaxProfit(Arrays.asList(1, 2, 3, 4, 5)));
        System.out.println(TabulationSolution.findMaxProfit(Arrays.asList(7, 1, 5, 3, 6, 4)));
        System.out.println();
    }

    public static void main(String[] args) {
        recursive();
        memoized();
        tabulation();
    }
}
