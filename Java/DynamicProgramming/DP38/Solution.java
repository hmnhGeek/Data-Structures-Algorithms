package DynamicProgramming.DP38;

import java.util.Arrays;

public class Solution {
    public static void recursive() {
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(3, 3, 5, 0, 0, 3, 1, 4), 2));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(1, 3, 1, 2, 4, 8), 2));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(5, 4, 3, 2, 1), 2));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(1, 2, 3, 4, 5), 2));
        System.out.println(RecursiveSolution.getMaxProfit(Arrays.asList(7, 1, 5, 3, 6, 4), 2));
        System.out.println();
    }

    public static void main(String[] args) {
        recursive();
    }
}
