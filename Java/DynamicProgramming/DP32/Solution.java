// Problem link - https://www.naukri.com/code360/problems/subsequence-counting_3755256?source=youtube&campaign=striver_dp_videos
// Solution - https://www.youtube.com/watch?v=nVG7eTiD2bY&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=33


package DynamicProgramming.DP32;

public class Solution {
    public static void main(String[] args) {
        recursive();
        memoized();
        tabulation();
        spaceOptimized();
    }

    private static void recursive() {
        System.out.println(RecursiveSolution.getDistinctSubsequencesCount("babgbag", "bag"));
        System.out.println(RecursiveSolution.getDistinctSubsequencesCount("brootgroot", "brt"));
        System.out.println(RecursiveSolution.getDistinctSubsequencesCount("dingdingdingding", "ing"));
        System.out.println(RecursiveSolution.getDistinctSubsequencesCount("aaaaa", "a"));
        System.out.println(RecursiveSolution.getDistinctSubsequencesCount("rabbbit", "rabbit"));
        System.out.println(RecursiveSolution.getDistinctSubsequencesCount("banana", "ban"));
        System.out.println(RecursiveSolution.getDistinctSubsequencesCount("geeksforgeeks", "ge"));
        System.out.println();
    }

    private static void memoized() {
        System.out.println(MemoizedSolution.getDistinctSubsequencesCount("babgbag", "bag"));
        System.out.println(MemoizedSolution.getDistinctSubsequencesCount("brootgroot", "brt"));
        System.out.println(MemoizedSolution.getDistinctSubsequencesCount("dingdingdingding", "ing"));
        System.out.println(MemoizedSolution.getDistinctSubsequencesCount("aaaaa", "a"));
        System.out.println(MemoizedSolution.getDistinctSubsequencesCount("rabbbit", "rabbit"));
        System.out.println(MemoizedSolution.getDistinctSubsequencesCount("banana", "ban"));
        System.out.println(MemoizedSolution.getDistinctSubsequencesCount("geeksforgeeks", "ge"));
        System.out.println();
    }

    private static void tabulation() {
        System.out.println(TabulationSolution.getDistinctSubsequencesCount("babgbag", "bag"));
        System.out.println(TabulationSolution.getDistinctSubsequencesCount("brootgroot", "brt"));
        System.out.println(TabulationSolution.getDistinctSubsequencesCount("dingdingdingding", "ing"));
        System.out.println(TabulationSolution.getDistinctSubsequencesCount("aaaaa", "a"));
        System.out.println(TabulationSolution.getDistinctSubsequencesCount("rabbbit", "rabbit"));
        System.out.println(TabulationSolution.getDistinctSubsequencesCount("banana", "ban"));
        System.out.println(TabulationSolution.getDistinctSubsequencesCount("geeksforgeeks", "ge"));
        System.out.println();
    }

    private static void spaceOptimized() {
        System.out.println(SpaceOptimizedSolution.getDistinctSubsequencesCount("babgbag", "bag"));
        System.out.println(SpaceOptimizedSolution.getDistinctSubsequencesCount("brootgroot", "brt"));
        System.out.println(SpaceOptimizedSolution.getDistinctSubsequencesCount("dingdingdingding", "ing"));
        System.out.println(SpaceOptimizedSolution.getDistinctSubsequencesCount("aaaaa", "a"));
        System.out.println(SpaceOptimizedSolution.getDistinctSubsequencesCount("rabbbit", "rabbit"));
        System.out.println(SpaceOptimizedSolution.getDistinctSubsequencesCount("banana", "ban"));
        System.out.println(SpaceOptimizedSolution.getDistinctSubsequencesCount("geeksforgeeks", "ge"));
        System.out.println();
    }
}
