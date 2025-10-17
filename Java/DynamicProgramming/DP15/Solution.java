package DynamicProgramming.DP15;

import java.util.Arrays;

public class Solution {
    public static void recursive() {
        System.out.println(RecursiveSolution.subsetSum(Arrays.asList(2, 3, 3, 3, 4, 5)));
        System.out.println(RecursiveSolution.subsetSum(Arrays.asList(3, 1, 1, 2, 2, 1)));
        System.out.println(RecursiveSolution.subsetSum(Arrays.asList(5, 6, 5, 11, 6)));
        System.out.println(RecursiveSolution.subsetSum(Arrays.asList(2, 2, 1, 1, 1, 1, 1, 3, 3)));
        System.out.println(RecursiveSolution.subsetSum(Arrays.asList(8, 7, 6, 12, 4, 5)));
        System.out.println(RecursiveSolution.subsetSum(Arrays.asList(1, 5, 11, 5)));
        System.out.println(RecursiveSolution.subsetSum(Arrays.asList(1, 3, 5)));
        System.out.println(RecursiveSolution.subsetSum(Arrays.asList(1, 2, 3, 5)));
    }

    public static void memoized() {
        System.out.println(MemoizedSolution.subsetSum(Arrays.asList(2, 3, 3, 3, 4, 5)));
        System.out.println(MemoizedSolution.subsetSum(Arrays.asList(3, 1, 1, 2, 2, 1)));
        System.out.println(MemoizedSolution.subsetSum(Arrays.asList(5, 6, 5, 11, 6)));
        System.out.println(MemoizedSolution.subsetSum(Arrays.asList(2, 2, 1, 1, 1, 1, 1, 3, 3)));
        System.out.println(MemoizedSolution.subsetSum(Arrays.asList(8, 7, 6, 12, 4, 5)));
        System.out.println(MemoizedSolution.subsetSum(Arrays.asList(1, 5, 11, 5)));
        System.out.println(MemoizedSolution.subsetSum(Arrays.asList(1, 3, 5)));
        System.out.println(MemoizedSolution.subsetSum(Arrays.asList(1, 2, 3, 5)));
    }

    public static void tabulation() {
        System.out.println(TabulationSolution.subsetSum(Arrays.asList(2, 3, 3, 3, 4, 5)));
        System.out.println(TabulationSolution.subsetSum(Arrays.asList(3, 1, 1, 2, 2, 1)));
        System.out.println(TabulationSolution.subsetSum(Arrays.asList(5, 6, 5, 11, 6)));
        System.out.println(TabulationSolution.subsetSum(Arrays.asList(2, 2, 1, 1, 1, 1, 1, 3, 3)));
        System.out.println(TabulationSolution.subsetSum(Arrays.asList(8, 7, 6, 12, 4, 5)));
        System.out.println(TabulationSolution.subsetSum(Arrays.asList(1, 5, 11, 5)));
        System.out.println(TabulationSolution.subsetSum(Arrays.asList(1, 3, 5)));
        System.out.println(TabulationSolution.subsetSum(Arrays.asList(1, 2, 3, 5)));
    }

    public static void spaceOptimizedSolution() {
        System.out.println(SpaceOptimizedSolution.subsetSum(Arrays.asList(2, 3, 3, 3, 4, 5)));
        System.out.println(SpaceOptimizedSolution.subsetSum(Arrays.asList(3, 1, 1, 2, 2, 1)));
        System.out.println(SpaceOptimizedSolution.subsetSum(Arrays.asList(5, 6, 5, 11, 6)));
        System.out.println(SpaceOptimizedSolution.subsetSum(Arrays.asList(2, 2, 1, 1, 1, 1, 1, 3, 3)));
        System.out.println(SpaceOptimizedSolution.subsetSum(Arrays.asList(8, 7, 6, 12, 4, 5)));
        System.out.println(SpaceOptimizedSolution.subsetSum(Arrays.asList(1, 5, 11, 5)));
        System.out.println(SpaceOptimizedSolution.subsetSum(Arrays.asList(1, 3, 5)));
        System.out.println(SpaceOptimizedSolution.subsetSum(Arrays.asList(1, 2, 3, 5)));
    }

    public static void main(String[] args) {
        recursive();
        System.out.println();
        memoized();
        System.out.println();
        tabulation();
        System.out.println();
        spaceOptimizedSolution();
    }
}
