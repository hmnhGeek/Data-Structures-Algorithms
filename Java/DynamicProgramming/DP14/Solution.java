// Problem link - https://www.naukri.com/code360/problems/subset-sum-equal-to-k_1550954?leftPanelTab=1%3Fsource%3Dyoutube&campaign=striver_dp_videos
// Solution - https://www.youtube.com/watch?v=fWX9xDmIzRI&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=15


package DynamicProgramming.DP14;

import java.util.List;

import static DynamicProgramming.DP14.RecursiveSolution.subsetSum;

public class Solution {
    public static void recursive() {
        System.out.println(RecursiveSolution.subsetSum(List.of(1, 2, 3, 4), 4));
        System.out.println(subsetSum(List.of(4, 3, 2, 1), 5));
        System.out.println(RecursiveSolution.subsetSum(List.of(2, 5, 1, 6, 7), 4));
        System.out.println(RecursiveSolution.subsetSum(List.of(6, 1, 2, 1), 4));
        System.out.println(RecursiveSolution.subsetSum(List.of(1, 7, 2, 9, 10), 6));
        System.out.println(RecursiveSolution.subsetSum(List.of(3, 34, 4, 12, 5, 2), 9));
        System.out.println(RecursiveSolution.subsetSum(List.of(3, 34, 4, 12, 5, 2), 30));
        System.out.println();
    }

    public static void memoized() {
        System.out.println(MemoizedSolution.subsetSum(List.of(1, 2, 3, 4), 4));
        System.out.println(MemoizedSolution.subsetSum(List.of(4, 3, 2, 1), 5));
        System.out.println(MemoizedSolution.subsetSum(List.of(2, 5, 1, 6, 7), 4));
        System.out.println(MemoizedSolution.subsetSum(List.of(6, 1, 2, 1), 4));
        System.out.println(MemoizedSolution.subsetSum(List.of(1, 7, 2, 9, 10), 6));
        System.out.println(MemoizedSolution.subsetSum(List.of(3, 34, 4, 12, 5, 2), 9));
        System.out.println(MemoizedSolution.subsetSum(List.of(3, 34, 4, 12, 5, 2), 30));
        System.out.println();
    }

    public static void tabulation() {
        System.out.println(TabulationSolution.subsetSum(List.of(1, 2, 3, 4), 4));
        System.out.println(TabulationSolution.subsetSum(List.of(4, 3, 2, 1), 5));
        System.out.println(TabulationSolution.subsetSum(List.of(2, 5, 1, 6, 7), 4));
        System.out.println(TabulationSolution.subsetSum(List.of(6, 1, 2, 1), 4));
        System.out.println(TabulationSolution.subsetSum(List.of(1, 7, 2, 9, 10), 6));
        System.out.println(TabulationSolution.subsetSum(List.of(3, 34, 4, 12, 5, 2), 9));
        System.out.println(TabulationSolution.subsetSum(List.of(3, 34, 4, 12, 5, 2), 30));
        System.out.println();
    }

    public static void spaceOptimized() {
        System.out.println(SpaceOptimizedSolution.subsetSum(List.of(1, 2, 3, 4), 4));
        System.out.println(SpaceOptimizedSolution.subsetSum(List.of(4, 3, 2, 1), 5));
        System.out.println(SpaceOptimizedSolution.subsetSum(List.of(2, 5, 1, 6, 7), 4));
        System.out.println(SpaceOptimizedSolution.subsetSum(List.of(6, 1, 2, 1), 4));
        System.out.println(SpaceOptimizedSolution.subsetSum(List.of(1, 7, 2, 9, 10), 6));
        System.out.println(SpaceOptimizedSolution.subsetSum(List.of(3, 34, 4, 12, 5, 2), 9));
        System.out.println(SpaceOptimizedSolution.subsetSum(List.of(3, 34, 4, 12, 5, 2), 30));
        System.out.println();
    }

    public static void main(String[] args) {
        recursive();
        memoized();
        tabulation();
        spaceOptimized();
    }
}
