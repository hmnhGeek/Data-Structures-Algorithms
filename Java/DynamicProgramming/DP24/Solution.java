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

    public static void main(String[] args) {
        recursive();
        memoized();
        tabulation();
    }
}
