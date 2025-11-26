package DynamicProgramming.DP19;

import java.util.Arrays;

public class Solution {
    public static void recursive() {
        System.out.println(RecursiveSolution.getKnapsack(
                Arrays.asList(1, 2, 4, 5),
                Arrays.asList(5, 4, 8, 6),
                5
        ));
        System.out.println(RecursiveSolution.getKnapsack(
                Arrays.asList(4, 5, 1),
                Arrays.asList(1, 2, 3),
                4
        ));
        System.out.println(RecursiveSolution.getKnapsack(
                Arrays.asList(4, 5, 6),
                Arrays.asList(1, 2, 3),
                3
        ));
        System.out.println(RecursiveSolution.getKnapsack(
                Arrays.asList(5, 4, 6, 3),
                Arrays.asList(10, 40, 30, 50),
                5
        ));
    }

    public static void main(String[] args) {
        recursive();
        System.out.println();
    }
}
