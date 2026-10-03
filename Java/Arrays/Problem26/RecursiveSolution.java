package Arrays.Problem26;

import java.util.List;

public class RecursiveSolution {
    public static Integer getMaxProfit(List<Integer> arr) {
        int n = arr.size();
        return solve(arr, 0, true, 2);
    }

    private static Integer solve(List<Integer> arr, Integer i, Boolean j, Integer k) {
        if (k == 0) return 0;
        if (i == arr.size()) return 0;
        if (j) {
            return Math.max(
                    -arr.get(i) + solve(arr, i + 1, !j, k),
                    solve(arr, i + 1, j, k)
            );
        } else {
            return Math.max(
                    arr.get(i) + solve(arr, i + 1, !j, k - 1),
                    solve(arr, i + 1, j, k)
            );
        }
    }
}
