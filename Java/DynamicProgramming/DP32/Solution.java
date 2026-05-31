package DynamicProgramming.DP32;

public class Solution {
    public static void main(String[] args) {
        recursive();
        memoized();
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
}
