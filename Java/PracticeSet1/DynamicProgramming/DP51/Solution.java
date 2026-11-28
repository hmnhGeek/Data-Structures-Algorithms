package PracticeSet1.DynamicProgramming.DP51;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        System.out.println(RecursiveSolution.getMaxCoins(Arrays.asList(3, 1, 5, 8)));
        System.out.println(RecursiveSolution.getMaxCoins(Arrays.asList(7, 1, 8)));
        System.out.println(RecursiveSolution.getMaxCoins(Arrays.asList(9, 1)));
        System.out.println(RecursiveSolution.getMaxCoins(Arrays.asList(1, 2, 3, 4, 5)));
        System.out.println(RecursiveSolution.getMaxCoins(Arrays.asList(1, 5, 2, 8)));
        System.out.println(RecursiveSolution.getMaxCoins(Arrays.asList(5, 10)));
        System.out.println(RecursiveSolution.getMaxCoins(Arrays.asList(1, 5)));
        System.out.println();
    }
}
