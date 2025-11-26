package DynamicProgramming.DP18;

import java.util.List;
import java.util.Map;

public class TabulationSolution {
    /*
        Time complexity is O(n*target) and space complexity is O(n*target).
     */
    public static int getCount(List<Integer> arr, Integer target) {
        int n = arr.size();
        Map<Integer, Map<Integer, Integer>> dp = Utils.getDp(n, target, 0);
        for (int i = 0; i < n; i += 1) {
            dp.get(i).put(0, 1);
        }
        dp.get(0).put(arr.getFirst(), 1);
        for (int i = 1; i < n; i += 1) {
            for (int j = 0; j < target + 1; j += 1) {
                Integer left = 0;
                if (j >= arr.get(i)) {
                    left = dp.get(i - 1).get(j - arr.get(i));
                }
                Integer right = dp.get(i - 1).get(j);
                dp.get(i).put(j, left + right);
            }
        }
        return dp.get(n - 1).get(target);
    }
}
