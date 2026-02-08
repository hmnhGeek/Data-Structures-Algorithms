package Strings.Problem14;

public class Solution {
    private static void recursive() {
        System.out.println(RecursiveSolution.getMinOps("abc", "dc"));
        System.out.println(RecursiveSolution.getMinOps("whgtdwhgtdg", "aswcfg"));
        System.out.println(RecursiveSolution.getMinOps("geek", "gesek"));
        System.out.println(RecursiveSolution.getMinOps("cat", "cut"));
        System.out.println(RecursiveSolution.getMinOps("sunday", "saturday"));
        System.out.println();
    }

    private static void memoized() {
        System.out.println(MemoizedSolution.getMinOps("abc", "dc"));
        System.out.println(MemoizedSolution.getMinOps("whgtdwhgtdg", "aswcfg"));
        System.out.println(MemoizedSolution.getMinOps("geek", "gesek"));
        System.out.println(MemoizedSolution.getMinOps("cat", "cut"));
        System.out.println(MemoizedSolution.getMinOps("sunday", "saturday"));
        System.out.println();
    }

    private static void tabulation() {
        System.out.println(TabulationSolution.getMinOps("abc", "dc"));
        System.out.println(TabulationSolution.getMinOps("whgtdwhgtdg", "aswcfg"));
        System.out.println(TabulationSolution.getMinOps("geek", "gesek"));
        System.out.println(TabulationSolution.getMinOps("cat", "cut"));
        System.out.println(TabulationSolution.getMinOps("sunday", "saturday"));
        System.out.println();
    }

    public static void main(String[] args) {
        recursive();
        memoized();
        tabulation();
    }
}
