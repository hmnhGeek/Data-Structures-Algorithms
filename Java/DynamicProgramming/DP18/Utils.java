package DynamicProgramming.DP18;

import java.util.HashMap;
import java.util.Map;

public class Utils {
    public static Map<Integer, Map<Integer, Integer>> getDp(Integer n, Integer target, Integer defaultValue) {
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < n; i += 1) {
            dp.put(i, getPrev(target, defaultValue));
        }
        return dp;
    }

    public static Map<Integer, Integer> getPrev(Integer target, Integer defaultValue) {
        Map<Integer, Integer> subMap = new HashMap<>();
        for (int j = 0; j < target + 1; j += 1) {
            subMap.put(j, defaultValue);
        }
        return subMap;
    }
}
