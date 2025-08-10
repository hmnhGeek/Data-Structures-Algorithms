// Problem link - https://www.geeksforgeeks.org/dsa/count-possible-paths-top-left-bottom-right-nxm-matrix/
// Solution - https://www.youtube.com/watch?v=sdE0A2Oxofw&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=9


package DynamicProgramming.DP8;

public class Solution {
    public static void main(String[] args) {
        System.out.println(RecursiveSolution.getUniquePathsCount(3, 7));
        System.out.println(RecursiveSolution.getUniquePathsCount(3, 2));
        System.out.println(RecursiveSolution.getUniquePathsCount(2, 2));
        System.out.println(RecursiveSolution.getUniquePathsCount(2, 3));
        System.out.println();
        System.out.println(MemoizedSolution.getUniquePathsCount(3, 7));
        System.out.println(MemoizedSolution.getUniquePathsCount(3, 2));
        System.out.println(MemoizedSolution.getUniquePathsCount(2, 2));
        System.out.println(MemoizedSolution.getUniquePathsCount(2, 3));
        System.out.println();
        System.out.println(TabulationSolution.getUniquePathsCount(3, 7));
        System.out.println(TabulationSolution.getUniquePathsCount(3, 2));
        System.out.println(TabulationSolution.getUniquePathsCount(2, 2));
        System.out.println(TabulationSolution.getUniquePathsCount(2, 3));
        System.out.println();
        System.out.println(SpaceOptimizedSolution.getUniquePathsCount(3, 7));
        System.out.println(SpaceOptimizedSolution.getUniquePathsCount(3, 2));
        System.out.println(SpaceOptimizedSolution.getUniquePathsCount(2, 2));
        System.out.println(SpaceOptimizedSolution.getUniquePathsCount(2, 3));
    }
}
