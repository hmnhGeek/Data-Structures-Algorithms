package DynamicProgramming.DP18;

import java.util.List;
import java.util.Map;

public class SpaceOptimizedSolution {
    /*
        Time complexity is O(n*target) and space complexity is O(target).
     */
    public static int getCount(List<Integer> arr, Integer target) {
        int n = arr.size();
        Map<Integer, Integer> prev = Utils.getPrev(target, 0);
        prev.put(0, 1);
        prev.put(arr.getFirst(), 1);
        for (int i = 1; i < n; i += 1) {
            Map<Integer, Integer> curr = Utils.getPrev(target, 0);
            curr.put(0, 1);
            for (int j = 0; j < target + 1; j += 1) {
                Integer left = 0;
                if (j >= arr.get(i)) {
                    left = prev.get(j - arr.get(i));
                }
                Integer right = prev.get(j);
                curr.put(j, left + right);
            }
            prev = curr;
        }
        return prev.get(target);
    }
}
