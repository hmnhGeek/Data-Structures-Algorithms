// Problem link - https://www.naukri.com/code360/problems/mining-diamonds_4244494?source=youtube&campaign=striver_dp_videos
// Solution - https://www.youtube.com/watch?v=Yz4LlDSlkns&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=52


package PracticeSet1.DynamicProgramming.DP51;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        System.out.println("Recursive Solution");
        System.out.println(RecursiveSolution.getMaxCoins(Arrays.asList(3, 1, 5, 8)));
        System.out.println(RecursiveSolution.getMaxCoins(Arrays.asList(7, 1, 8)));
        System.out.println(RecursiveSolution.getMaxCoins(Arrays.asList(9, 1)));
        System.out.println(RecursiveSolution.getMaxCoins(Arrays.asList(1, 2, 3, 4, 5)));
        System.out.println(RecursiveSolution.getMaxCoins(Arrays.asList(1, 5, 2, 8)));
        System.out.println(RecursiveSolution.getMaxCoins(Arrays.asList(5, 10)));
        System.out.println(RecursiveSolution.getMaxCoins(Arrays.asList(1, 5)));
        System.out.println();

        System.out.println("Memoized Solution");
        System.out.println(MemoizedSolution.getMaxCoins(Arrays.asList(3, 1, 5, 8)));
        System.out.println(MemoizedSolution.getMaxCoins(Arrays.asList(7, 1, 8)));
        System.out.println(MemoizedSolution.getMaxCoins(Arrays.asList(9, 1)));
        System.out.println(MemoizedSolution.getMaxCoins(Arrays.asList(1, 2, 3, 4, 5)));
        System.out.println(MemoizedSolution.getMaxCoins(Arrays.asList(1, 5, 2, 8)));
        System.out.println(MemoizedSolution.getMaxCoins(Arrays.asList(5, 10)));
        System.out.println(MemoizedSolution.getMaxCoins(Arrays.asList(1, 5)));
        System.out.println();

        System.out.println("Tabulation Solution");
        System.out.println(TabulationSolution.getMaxCoins(Arrays.asList(3, 1, 5, 8)));
        System.out.println(TabulationSolution.getMaxCoins(Arrays.asList(7, 1, 8)));
        System.out.println(TabulationSolution.getMaxCoins(Arrays.asList(9, 1)));
        System.out.println(TabulationSolution.getMaxCoins(Arrays.asList(1, 2, 3, 4, 5)));
        System.out.println(TabulationSolution.getMaxCoins(Arrays.asList(1, 5, 2, 8)));
        System.out.println(TabulationSolution.getMaxCoins(Arrays.asList(5, 10)));
        System.out.println(TabulationSolution.getMaxCoins(Arrays.asList(1, 5)));
        System.out.println();
    }
}
