// Problem link - https://leetcode.com/problems/minimum-cost-to-cut-a-stick/
// Solution - https://www.youtube.com/watch?v=xwomavsC86c&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=51


package PracticeSet1.DynamicProgramming.DP50;


import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        System.out.println("Recursive Solution");
        System.out.println(RecursiveSolution.getMinCostToCutSticks(Arrays.asList(1, 3, 4, 5), 7));
        System.out.println(RecursiveSolution.getMinCostToCutSticks(Arrays.asList(1, 3), 4));
        System.out.println(RecursiveSolution.getMinCostToCutSticks(Arrays.asList(1, 3, 4), 5));
        System.out.println(RecursiveSolution.getMinCostToCutSticks(Arrays.asList(1, 3, 4, 7), 10));
        System.out.println(RecursiveSolution.getMinCostToCutSticks(Arrays.asList(1, 3), 10));
        System.out.println(RecursiveSolution.getMinCostToCutSticks(Arrays.asList(5, 6, 1, 4, 2), 9));
        System.out.println();
        System.out.println("Memoized Solution");
        System.out.println(MemoizedSolution.getMinCostToCutSticks(Arrays.asList(1, 3, 4, 5), 7));
        System.out.println(MemoizedSolution.getMinCostToCutSticks(Arrays.asList(1, 3), 4));
        System.out.println(MemoizedSolution.getMinCostToCutSticks(Arrays.asList(1, 3, 4), 5));
        System.out.println(MemoizedSolution.getMinCostToCutSticks(Arrays.asList(1, 3, 4, 7), 10));
        System.out.println(MemoizedSolution.getMinCostToCutSticks(Arrays.asList(1, 3), 10));
        System.out.println(MemoizedSolution.getMinCostToCutSticks(Arrays.asList(5, 6, 1, 4, 2), 9));
        System.out.println();
        System.out.println("Tabulation Solution");
        System.out.println(TabulationSolution.getMinCostToCutSticks(Arrays.asList(1, 3, 4, 5), 7));
        System.out.println(TabulationSolution.getMinCostToCutSticks(Arrays.asList(1, 3), 4));
        System.out.println(TabulationSolution.getMinCostToCutSticks(Arrays.asList(1, 3, 4), 5));
        System.out.println(TabulationSolution.getMinCostToCutSticks(Arrays.asList(1, 3, 4, 7), 10));
        System.out.println(TabulationSolution.getMinCostToCutSticks(Arrays.asList(1, 3), 10));
        System.out.println(TabulationSolution.getMinCostToCutSticks(Arrays.asList(5, 6, 1, 4, 2), 9));
        System.out.println();
    }
}
