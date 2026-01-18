package Strings.Problem13;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        recursive();
        memoized();
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
}
