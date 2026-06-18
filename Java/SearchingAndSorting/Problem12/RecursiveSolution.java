package SearchingAndSorting.Problem12;

import java.util.List;

public class RecursiveSolution {
    public static Integer houseRobber(List<Integer> arr) {
        return Math.max(
                solve(arr, arr.size() - 1, true),
                solve(arr, arr.size() - 1, false)
        );
    }

    private static Integer solve(List<Integer> arr, int i, boolean canPick) {
        if (i == -1 || i == -2) return 0;
        if (canPick) {
            return arr.get(i) + Math.max(
                    solve(arr, i - 2, true),
                    solve(arr, i - 2, false)
            );
        } else {
            return Math.max(
                    solve(arr, i - 1, true),
                    solve(arr, i - 1, false)
            );
        }
    }
}
