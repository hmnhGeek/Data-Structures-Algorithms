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
    }
}
