package DynamicProgramming.DP4;

import java.util.List;

public class RecursiveSolution {
    /*
        Time complexity is exponential and space complexity is O(n).
     */
    private static Integer frogJump(List<Integer> arr, Integer k) {
        return solve(arr, arr.size() - 1, k);
    }

    private static Integer solve(List<Integer> arr, int i, Integer k) {
        if (i == 0) return 0;
        Integer energy = Integer.MAX_VALUE;
        for (int j = 1; j <= k; j += 1) {
            if (i - j >= 0) {
                energy = Math.min(energy, Math.abs(arr.get(i - j) - arr.get(i)) + solve(arr, i - j, k));
            }
        }
        return energy;
    }

    public static void main(String[] args) {
        System.out.println(frogJump(List.of(10, 30, 50, 60, 20, 10), 3));
        System.out.println(frogJump(List.of(10, 30, 50, 60, 20, 10), 2));
        System.out.println(frogJump(List.of(10, 30, 50, 60, 20, 10), 4));
        System.out.println(frogJump(List.of(10, 30, 50, 60, 20, 10), 1));
        System.out.println(frogJump(List.of(10, 30, 40, 50, 20), 3));
        System.out.println(frogJump(List.of(10, 20, 10), 1));
        System.out.println(frogJump(List.of(40, 10, 20, 70, 80, 10, 20, 70, 80, 60), 4));
    }
}
