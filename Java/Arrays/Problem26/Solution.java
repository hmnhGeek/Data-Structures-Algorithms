package Arrays.Problem26;

import java.util.Arrays;

public class Solution {
    public static void recursive() {
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(10, 22, 5, 75, 65, 80)));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(100, 30, 15, 10, 8, 25, 80)));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(90, 80, 70, 60, 50)));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(3, 3, 5, 0, 0, 3, 1, 4)));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(1, 3, 1, 2, 4, 8)));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(5, 4, 3, 2, 1)));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(1, 2, 3, 4, 5)));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(7, 1, 5, 3, 6, 4)));
        System.out.println();
    }

    public static void memoized() {
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(10, 22, 5, 75, 65, 80)));
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(100, 30, 15, 10, 8, 25, 80)));
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(90, 80, 70, 60, 50)));
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(3, 3, 5, 0, 0, 3, 1, 4)));
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(1, 3, 1, 2, 4, 8)));
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(5, 4, 3, 2, 1)));
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(1, 2, 3, 4, 5)));
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(7, 1, 5, 3, 6, 4)));
        System.out.println();
    }

    public static void main(String[] args) {
        recursive();
        memoized();
    }
}
