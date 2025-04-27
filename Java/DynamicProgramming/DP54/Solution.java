// Problem link - https://leetcode.com/problems/partition-array-for-maximum-sum/description/
// Solution - https://www.youtube.com/watch?v=PhWWJmaKfMc&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=55

package DynamicProgramming.DP54;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        System.out.println(RecursiveSolution.maxSumPartition(Arrays.asList(1, 15, 7, 9, 2, 5, 10), 3));
        System.out.println(RecursiveSolution.maxSumPartition(Arrays.asList(1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3), 4));
        System.out.println(RecursiveSolution.maxSumPartition(Arrays.asList(1), 1));
        System.out.println();

        System.out.println(MemoizedSolution.maxSumPartition(Arrays.asList(1, 15, 7, 9, 2, 5, 10), 3));
        System.out.println(MemoizedSolution.maxSumPartition(Arrays.asList(1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3), 4));
        System.out.println(MemoizedSolution.maxSumPartition(Arrays.asList(1), 1));
        System.out.println();

        System.out.println(TabulationSolution.maxSumPartition(Arrays.asList(1, 15, 7, 9, 2, 5, 10), 3));
        System.out.println(TabulationSolution.maxSumPartition(Arrays.asList(1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3), 4));
        System.out.println(TabulationSolution.maxSumPartition(Arrays.asList(1), 1));
        System.out.println();
    }
}
