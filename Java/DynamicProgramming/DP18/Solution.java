package DynamicProgramming.DP18;


import java.util.List;

public class Solution {
    public static void recursive() {
        System.out.println(RecursiveSolution.getCount(List.of(1, 2, 2, 3), 3));
        System.out.println(RecursiveSolution.getCount(List.of(1, 1, 4, 5), 5));
        System.out.println(RecursiveSolution.getCount(List.of(1, 1, 1), 2));
        System.out.println(RecursiveSolution.getCount(List.of(2, 34, 5), 40));
        System.out.println(RecursiveSolution.getCount(List.of(1, 2, 3, 3), 6));
        System.out.println(RecursiveSolution.getCount(List.of(1, 1, 1, 1), 1));
        System.out.println(RecursiveSolution.getCount(List.of(5, 2, 3, 10, 6, 8), 10));
        System.out.println(RecursiveSolution.getCount(List.of(2, 5, 1, 4, 3), 10));
        System.out.println(RecursiveSolution.getCount(List.of(5, 7, 8), 3));
        System.out.println(RecursiveSolution.getCount(List.of(35, 2, 8, 22), 0));
    }

    public static void memoized() {
        System.out.println(MemoizedSolution.getCount(List.of(1, 2, 2, 3), 3));
        System.out.println(MemoizedSolution.getCount(List.of(1, 1, 4, 5), 5));
        System.out.println(MemoizedSolution.getCount(List.of(1, 1, 1), 2));
        System.out.println(MemoizedSolution.getCount(List.of(2, 34, 5), 40));
        System.out.println(MemoizedSolution.getCount(List.of(1, 2, 3, 3), 6));
        System.out.println(MemoizedSolution.getCount(List.of(1, 1, 1, 1), 1));
        System.out.println(MemoizedSolution.getCount(List.of(5, 2, 3, 10, 6, 8), 10));
        System.out.println(MemoizedSolution.getCount(List.of(2, 5, 1, 4, 3), 10));
        System.out.println(MemoizedSolution.getCount(List.of(5, 7, 8), 3));
        System.out.println(MemoizedSolution.getCount(List.of(35, 2, 8, 22), 0));
    }

    public static void main(String[] args) {
        recursive();
        System.out.println();
        memoized();
        System.out.println();
    }
}
