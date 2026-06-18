package SearchingAndSorting.Problem12;

import java.util.Arrays;

public class Solution {
    public static void recursive() {
        System.out.println(RecursiveSolution.houseRobber(Arrays.asList(2, 1, 4, 9)));
        System.out.println(RecursiveSolution.houseRobber(Arrays.asList(1, 2, 4)));
        System.out.println(RecursiveSolution.houseRobber(Arrays.asList(1, 2, 3, 5, 4)));
        System.out.println(RecursiveSolution.houseRobber(Arrays.asList(1, 2, 3, 1, 3, 5, 8, 1, 9)));
        System.out.println(RecursiveSolution.houseRobber(Arrays.asList(2, 7, 9, 3, 1)));
        System.out.println(RecursiveSolution.houseRobber(Arrays.asList(1, 2, 3, 1)));
        System.out.println(RecursiveSolution.houseRobber(Arrays.asList(1, 5, 2, 1, 6)));
        System.out.println();
    }

    public static void memoized() {
        System.out.println(MemoizedSolution.houseRobber(Arrays.asList(2, 1, 4, 9)));
        System.out.println(MemoizedSolution.houseRobber(Arrays.asList(1, 2, 4)));
        System.out.println(MemoizedSolution.houseRobber(Arrays.asList(1, 2, 3, 5, 4)));
        System.out.println(MemoizedSolution.houseRobber(Arrays.asList(1, 2, 3, 1, 3, 5, 8, 1, 9)));
        System.out.println(MemoizedSolution.houseRobber(Arrays.asList(2, 7, 9, 3, 1)));
        System.out.println(MemoizedSolution.houseRobber(Arrays.asList(1, 2, 3, 1)));
        System.out.println(MemoizedSolution.houseRobber(Arrays.asList(1, 5, 2, 1, 6)));
        System.out.println();
    }

    public static void main(String[] args) {
        recursive();
        memoized();
    }
}
