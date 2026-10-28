package PracticeSet1.DynamicProgramming.DP48;


import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        recursive();
        memoized();
        tabulation();
    }

    private static void recursive() {
        System.out.println(RecursiveSolution.getMinCostForMultiplication(Arrays.asList(10, 20, 30, 40, 50)));
        System.out.println(RecursiveSolution.getMinCostForMultiplication(Arrays.asList(10, 20, 30, 40)));
        System.out.println(RecursiveSolution.getMinCostForMultiplication(Arrays.asList(4, 5, 3, 2)));
        System.out.println(RecursiveSolution.getMinCostForMultiplication(Arrays.asList(10, 15, 20, 25)));
        System.out.println(RecursiveSolution.getMinCostForMultiplication(Arrays.asList(1, 4, 3, 2)));
        System.out.println(RecursiveSolution.getMinCostForMultiplication(Arrays.asList(2, 1, 3, 4)));
        System.out.println(RecursiveSolution.getMinCostForMultiplication(Arrays.asList(1, 2, 3, 4, 3)));
        System.out.println();
    }

    private static void memoized() {
        System.out.println(MemoizedSolution.getMinCostForMultiplication(Arrays.asList(10, 20, 30, 40, 50)));
        System.out.println(MemoizedSolution.getMinCostForMultiplication(Arrays.asList(10, 20, 30, 40)));
        System.out.println(MemoizedSolution.getMinCostForMultiplication(Arrays.asList(4, 5, 3, 2)));
        System.out.println(MemoizedSolution.getMinCostForMultiplication(Arrays.asList(10, 15, 20, 25)));
        System.out.println(MemoizedSolution.getMinCostForMultiplication(Arrays.asList(1, 4, 3, 2)));
        System.out.println(MemoizedSolution.getMinCostForMultiplication(Arrays.asList(2, 1, 3, 4)));
        System.out.println(MemoizedSolution.getMinCostForMultiplication(Arrays.asList(1, 2, 3, 4, 3)));
        System.out.println();
    }

    private static void tabulation() {
        System.out.println(TabulationSolution.getMinCostForMultiplication(Arrays.asList(10, 20, 30, 40, 50)));
        System.out.println(TabulationSolution.getMinCostForMultiplication(Arrays.asList(10, 20, 30, 40)));
        System.out.println(TabulationSolution.getMinCostForMultiplication(Arrays.asList(4, 5, 3, 2)));
        System.out.println(TabulationSolution.getMinCostForMultiplication(Arrays.asList(10, 15, 20, 25)));
        System.out.println(TabulationSolution.getMinCostForMultiplication(Arrays.asList(1, 4, 3, 2)));
        System.out.println(TabulationSolution.getMinCostForMultiplication(Arrays.asList(2, 1, 3, 4)));
        System.out.println(TabulationSolution.getMinCostForMultiplication(Arrays.asList(1, 2, 3, 4, 3)));
        System.out.println();
    }
}
