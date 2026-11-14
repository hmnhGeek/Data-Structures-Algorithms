package SearchingAndSorting.Problem37;

import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        optimalSolution();
        betterSolution();
    }

    private static void optimalSolution() {
        System.out.println("From optimal solution with O(n) time and O(1) space.");
        System.out.println(OptimalSolution.solve(Arrays.asList(10, 3, 5, 6, 2)));
        System.out.println(OptimalSolution.solve(Arrays.asList(12, 0)));
        System.out.println(OptimalSolution.solve(Arrays.asList(0)));
        System.out.println(OptimalSolution.solve(Arrays.asList(1, 2, 3, 4, 5)));
        System.out.println(OptimalSolution.solve(Arrays.asList(-1, 1, 0, -3, 3)));
        System.out.println(OptimalSolution.solve(Arrays.asList(1, 2, 3, 4)));
        System.out.println(OptimalSolution.solve(Arrays.asList(1, 3, 3, 10, 2)));
        System.out.println(OptimalSolution.solve(Arrays.asList(2, 4, 6, 3, 1, 1)));
        System.out.println(OptimalSolution.solve(Arrays.asList(1, 10, 1, 2, 2)));
        System.out.println(OptimalSolution.solve(Arrays.asList(2, 12, 1, 1, 20, 1)));
        System.out.println();
    }

    private static void betterSolution() {
        System.out.println("From better solution with O(n) time and O(1) space.");
        System.out.println(BetterSolution.solve(Arrays.asList(10, 3, 5, 6, 2)));
        System.out.println(BetterSolution.solve(Arrays.asList(12, 0)));
        System.out.println(BetterSolution.solve(Arrays.asList(0)));
        System.out.println(BetterSolution.solve(Arrays.asList(1, 2, 3, 4, 5)));
        System.out.println(BetterSolution.solve(Arrays.asList(-1, 1, 0, -3, 3)));
        System.out.println(BetterSolution.solve(Arrays.asList(1, 2, 3, 4)));
        System.out.println(BetterSolution.solve(Arrays.asList(1, 3, 3, 10, 2)));
        System.out.println(BetterSolution.solve(Arrays.asList(2, 4, 6, 3, 1, 1)));
        System.out.println(BetterSolution.solve(Arrays.asList(1, 10, 1, 2, 2)));
        System.out.println(BetterSolution.solve(Arrays.asList(2, 12, 1, 1, 20, 1)));
        System.out.println();
    }
}
