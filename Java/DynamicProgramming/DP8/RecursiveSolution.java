package DynamicProgramming.DP8;

public class RecursiveSolution {
    public static Integer getUniquePathsCount(Integer n, Integer m) {
        /*
            Time complexity is O(2^{m + n}) and space complexity is O(n + m).
         */
        return solve(n - 1, m - 1);
    }

    private static Integer solve(Integer i, Integer j) {
        if (i < 0 || j < 0) return 0;
        if (i.equals(0) && j.equals(0)) return 1;
        Integer upDirection = solve(i - 1, j);
        Integer leftDirection = solve(i, j - 1);
        return upDirection + leftDirection;
    }
}
