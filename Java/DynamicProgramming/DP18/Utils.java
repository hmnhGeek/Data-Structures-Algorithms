package DynamicProgramming.DP18;

import java.util.HashMap;
import java.util.Map;

public class Utils {
    public static Map<Integer, Map<Integer, Integer>> getDp(Integer n, Integer target, Integer defaultValue) {
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            Map<Integer, Integer> subMap = new HashMap<>();
            for (int j = 0; j < target; j += 1) {
                subMap.put(j, defaultValue);
            }
            dp.put(i, subMap);
        }
        return dp;
    }
}
