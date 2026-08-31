package DynamicProgramming.DP41;

import java.util.List;

public class Solution {
    public static void recursive() {
        System.out.println(RecursiveSolution.getLISLength(List.of(10, 9, 2, 5, 3, 7, 101, 18)));
        System.out.println(RecursiveSolution.getLISLength(List.of(5, 4, 11, 1, 16, 8)));
        System.out.println(RecursiveSolution.getLISLength(List.of(1, 2, 2)));
        System.out.println(RecursiveSolution.getLISLength(List.of(3, 10, 2, 1, 20)));
        System.out.println(RecursiveSolution.getLISLength(List.of(30, 20, 10)));
        System.out.println(RecursiveSolution.getLISLength(List.of(2, 2, 2)));
        System.out.println(RecursiveSolution.getLISLength(List.of(10, 20, 35, 80)));
        System.out.println();
    }

    public static void main(String[] args) {
        recursive();
    }
}
