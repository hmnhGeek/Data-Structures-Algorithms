package Strings.Problem13;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MemoizedSolution {
    public static Integer getMinCost(List<Integer> words, Integer k) {
        /*
            Time complexity is O(n*k) and space complexity is O(n + nk).
         */
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i < words.size(); i += 1) {
            Map<Integer, Integer> subMap = new HashMap<>();
            for (int j = 0; j <= k; j += 1) {
                subMap.put(j, null);
            }
            dp.put(i, subMap);
        }
        return getMinCost(1, words.getFirst(), words, k, dp);
    }

    private static Integer getMinCost(int i, int j, List<Integer> words, Integer k, Map<Integer, Map<Integer, Integer>> dp) {
        if (i == words.size()) return 0;
        if (dp.get(i).get(j) != null) return dp.get(i).get(j);
        int newSpacesCount = j + 1 + words.get(i);
        int costOnStayingOnSameLine = Integer.MAX_VALUE;
        if (newSpacesCount <= k) {
            costOnStayingOnSameLine = getMinCost(i + 1, newSpacesCount, words, k, dp);
        }
        int costOnGoingToNextLine = (k - j)*(k - j) + getMinCost(i + 1, words.get(i), words, k, dp);
        dp.get(i).put(j, Math.min(costOnStayingOnSameLine, costOnGoingToNextLine));
        return dp.get(i).get(j);
    }
}
