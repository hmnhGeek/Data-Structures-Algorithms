package DynamicProgramming.DP40;

import java.util.Arrays;

public class Solution {
    public static void recursive() {
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(1,3,2,8,4,9),2));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(1,2,3),1));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(1,3,5,6),2));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(1,3,7,5,10,3),3));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(6,1,7,2,8,4),2));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(7,1,5,3,6,4),1));
        System.out.println();
    }

    public static void memoized() {
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(1,3,2,8,4,9),2));
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(1,2,3),1));
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(1,3,5,6),2));
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(1,3,7,5,10,3),3));
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(6,1,7,2,8,4),2));
        System.out.println(MemoizedSolution.getMaxProfit(Arrays.asList(7,1,5,3,6,4),1));
        System.out.println();
    }

    public static void tabulation() {
        System.out.println(TabulationSolution.getMaxProfit(Arrays.asList(1,3,2,8,4,9),2));
        System.out.println(TabulationSolution.getMaxProfit(Arrays.asList(1,2,3),1));
        System.out.println(TabulationSolution.getMaxProfit(Arrays.asList(1,3,5,6),2));
        System.out.println(TabulationSolution.getMaxProfit(Arrays.asList(1,3,7,5,10,3),3));
        System.out.println(TabulationSolution.getMaxProfit(Arrays.asList(6,1,7,2,8,4),2));
        System.out.println(TabulationSolution.getMaxProfit(Arrays.asList(7,1,5,3,6,4),1));
        System.out.println();
    }

    public static void spaceOptimized() {
        System.out.println(SpaceOptimizedSolution.getMaxProfit(Arrays.asList(1,3,2,8,4,9),2));
        System.out.println(SpaceOptimizedSolution.getMaxProfit(Arrays.asList(1,2,3),1));
        System.out.println(SpaceOptimizedSolution.getMaxProfit(Arrays.asList(1,3,5,6),2));
        System.out.println(SpaceOptimizedSolution.getMaxProfit(Arrays.asList(1,3,7,5,10,3),3));
        System.out.println(SpaceOptimizedSolution.getMaxProfit(Arrays.asList(6,1,7,2,8,4),2));
        System.out.println(SpaceOptimizedSolution.getMaxProfit(Arrays.asList(7,1,5,3,6,4),1));
        System.out.println();
    }


    public static void main(String[] args) {
        recursive();
        memoized();
        tabulation();
        spaceOptimized();
    }
}
