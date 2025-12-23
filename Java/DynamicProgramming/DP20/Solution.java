// Problem link - https://www.naukri.com/code360/problems/minimum-elements_3843091?leftPanelTab=1%3Fsource%3Dyoutube&campaign=striver_dpseries
// Solution - https://www.youtube.com/watch?v=myPeWb3Y68A&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=21


package DynamicProgramming.DP20;

import java.util.Arrays;

public class Solution {
    private static void recursive() {
        System.out.println(RecursiveSolution.getMinCoins(Arrays.asList(1, 2, 3), 7));
        System.out.println(RecursiveSolution.getMinCoins(Arrays.asList(1), 0));
        System.out.println(RecursiveSolution.getMinCoins(Arrays.asList(12, 1, 3), 4));
        System.out.println(RecursiveSolution.getMinCoins(Arrays.asList(2, 1), 11));
        System.out.println(RecursiveSolution.getMinCoins(Arrays.asList(1, 2, 5), 11));
        System.out.println(RecursiveSolution.getMinCoins(Arrays.asList(2), 3));
        System.out.println(RecursiveSolution.getMinCoins(Arrays.asList(1), 0));
        System.out.println(RecursiveSolution.getMinCoins(Arrays.asList(25, 10, 5), 30));
        System.out.println(RecursiveSolution.getMinCoins(Arrays.asList(9, 6, 5, 1), 19));
        System.out.println(RecursiveSolution.getMinCoins(Arrays.asList(5, 1), 0));
        System.out.println(RecursiveSolution.getMinCoins(Arrays.asList(4, 6, 2), 5));
        System.out.println();
    }

    private static void memoized() {
        System.out.println(MemoizedSolution.getMinCoins(Arrays.asList(1, 2, 3), 7));
        System.out.println(MemoizedSolution.getMinCoins(Arrays.asList(1), 0));
        System.out.println(MemoizedSolution.getMinCoins(Arrays.asList(12, 1, 3), 4));
        System.out.println(MemoizedSolution.getMinCoins(Arrays.asList(2, 1), 11));
        System.out.println(MemoizedSolution.getMinCoins(Arrays.asList(1, 2, 5), 11));
        System.out.println(MemoizedSolution.getMinCoins(Arrays.asList(2), 3));
        System.out.println(MemoizedSolution.getMinCoins(Arrays.asList(1), 0));
        System.out.println(MemoizedSolution.getMinCoins(Arrays.asList(25, 10, 5), 30));
        System.out.println(MemoizedSolution.getMinCoins(Arrays.asList(9, 6, 5, 1), 19));
        System.out.println(MemoizedSolution.getMinCoins(Arrays.asList(5, 1), 0));
        System.out.println(MemoizedSolution.getMinCoins(Arrays.asList(4, 6, 2), 5));
        System.out.println();
    }

    private static void tabulation() {
        System.out.println(TabulationSolution.getMinCoins(Arrays.asList(1, 2, 3), 7));
        System.out.println(TabulationSolution.getMinCoins(Arrays.asList(1), 0));
        System.out.println(TabulationSolution.getMinCoins(Arrays.asList(12, 1, 3), 4));
        System.out.println(TabulationSolution.getMinCoins(Arrays.asList(2, 1), 11));
        System.out.println(TabulationSolution.getMinCoins(Arrays.asList(1, 2, 5), 11));
        System.out.println(TabulationSolution.getMinCoins(Arrays.asList(2), 3));
        System.out.println(TabulationSolution.getMinCoins(Arrays.asList(1), 0));
        System.out.println(TabulationSolution.getMinCoins(Arrays.asList(25, 10, 5), 30));
        System.out.println(TabulationSolution.getMinCoins(Arrays.asList(9, 6, 5, 1), 19));
        System.out.println(TabulationSolution.getMinCoins(Arrays.asList(5, 1), 0));
        System.out.println(TabulationSolution.getMinCoins(Arrays.asList(4, 6, 2), 5));
        System.out.println();
    }

    private static void spaceOptimized() {
        System.out.println(SpaceOptimizedSolution.getMinCoins(Arrays.asList(1, 2, 3), 7));
        System.out.println(SpaceOptimizedSolution.getMinCoins(Arrays.asList(1), 0));
        System.out.println(SpaceOptimizedSolution.getMinCoins(Arrays.asList(12, 1, 3), 4));
        System.out.println(SpaceOptimizedSolution.getMinCoins(Arrays.asList(2, 1), 11));
        System.out.println(SpaceOptimizedSolution.getMinCoins(Arrays.asList(1, 2, 5), 11));
        System.out.println(SpaceOptimizedSolution.getMinCoins(Arrays.asList(2), 3));
        System.out.println(SpaceOptimizedSolution.getMinCoins(Arrays.asList(1), 0));
        System.out.println(SpaceOptimizedSolution.getMinCoins(Arrays.asList(25, 10, 5), 30));
        System.out.println(SpaceOptimizedSolution.getMinCoins(Arrays.asList(9, 6, 5, 1), 19));
        System.out.println(SpaceOptimizedSolution.getMinCoins(Arrays.asList(5, 1), 0));
        System.out.println(SpaceOptimizedSolution.getMinCoins(Arrays.asList(4, 6, 2), 5));
        System.out.println();
    }

    public static void main(String[] args) {
        recursive();
        memoized();
        tabulation();
        spaceOptimized();
    }
}
