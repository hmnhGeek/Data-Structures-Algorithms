package DynamicProgramming.DP54;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        System.out.println(RecursiveSolution.maxSumPartition(Arrays.asList(1, 15, 7, 9, 2, 5, 10), 3));
        System.out.println(RecursiveSolution.maxSumPartition(Arrays.asList(1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3), 4));
        System.out.println(RecursiveSolution.maxSumPartition(Arrays.asList(1), 1));
    }
}
