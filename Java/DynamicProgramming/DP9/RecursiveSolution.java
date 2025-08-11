package DynamicProgramming.DP9;

import java.util.List;

public class RecursiveSolution {
    public static Integer getPathCount(List<List<Integer>> mtx) {
        if (mtx.getFirst().getFirst().equals(-1) || mtx.getLast().getLast().equals(-1)) return 0;
        int n = mtx.size(), m = mtx.getFirst().size();
        return solve(mtx, n - 1, m - 1);
    }

    private static Integer solve(List<List<Integer>> mtx, int i, int j) {
        /*
            Time complexity is O(2^{mn}) and space complexity is O(m + n).
         */
        if (i < 0 || j < 0) return 0;
        if (i == 0 && j == 0) return 1;
        if (mtx.get(i).get(j).equals(-1)) return 0;
        Integer upDirection = solve(mtx, i - 1, j);
        Integer leftDirection = solve(mtx, i, j - 1);
        return upDirection + leftDirection;
    }
}
