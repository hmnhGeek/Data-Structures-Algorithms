// Problem link - https://www.geeksforgeeks.org/word-wrap-problem-dp-19/
// Solution - https://www.youtube.com/watch?v=1oKMVPryX18&t=655s


package Strings.Problem13;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        recursive();
        memoized();
        tabulation();
        spaceOptimized();
    }

    private static void recursive() {
        System.out.println(RecursiveSolution.getMinCost(Arrays.asList(3, 2, 2, 5), 6));
        System.out.println(RecursiveSolution.getMinCost(Arrays.asList(3, 2, 2), 4));
        System.out.println();
    }

    private static void memoized() {
        System.out.println(MemoizedSolution.getMinCost(Arrays.asList(3, 2, 2, 5), 6));
        System.out.println(MemoizedSolution.getMinCost(Arrays.asList(3, 2, 2), 4));
        System.out.println();
    }

    private static void tabulation() {
        System.out.println(TabulationSolution.getMinCost(Arrays.asList(3, 2, 2, 5), 6));
        System.out.println(TabulationSolution.getMinCost(Arrays.asList(3, 2, 2), 4));
        System.out.println();
    }

    private static void spaceOptimized() {
        System.out.println(SpaceOptimizedSolution.getMinCost(Arrays.asList(3, 2, 2, 5), 6));
        System.out.println(SpaceOptimizedSolution.getMinCost(Arrays.asList(3, 2, 2), 4));
        System.out.println();
    }
}
