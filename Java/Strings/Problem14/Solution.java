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

    public static void main(String[] args) {
        recursive();
    }
}
