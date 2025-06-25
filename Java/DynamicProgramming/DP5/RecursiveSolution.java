package DynamicProgramming.DP5;

import java.util.List;

public class RecursiveSolution {
    /*
        Time complexity is O(2^n) and space complexity is O(n).
     */
    public static Integer houseRobber(List<Integer> arr) {
        int n = arr.size();
        return solve(arr, n - 1);
    }

    private static Integer solve(List<Integer> arr, int i) {
        if (i < 0) return 0;
        if (i == 0) return arr.getFirst();
        Integer left = arr.get(i) + solve(arr, i - 2);
        Integer right = solve(arr, i - 1);
        return Math.max(left, right);
    }

    public static void main(String[] args) {
        System.out.println(houseRobber(List.of(2, 1, 4, 9)));
        System.out.println(houseRobber(List.of(1, 2, 4)));
        System.out.println(houseRobber(List.of(1, 2, 3, 5, 4)));
        System.out.println(houseRobber(List.of(1, 2, 3, 1, 3, 5, 8, 1, 9)));
        System.out.println(houseRobber(List.of(2, 7, 9, 3, 1)));
        System.out.println(houseRobber(List.of(1, 2, 3, 1)));
        System.out.println(houseRobber(List.of(1, 5, 2, 1, 6)));
    }
}
