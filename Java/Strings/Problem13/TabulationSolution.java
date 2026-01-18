package Strings.Problem13;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TabulationSolution {
    public static Integer getMinCost(List<Integer> words, Integer k) {
        /*
            Time complexity is O(n*k) and space complexity is O(nk).
         */
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i <= words.size(); i += 1) {
            Map<Integer, Integer> subMap = new HashMap<>();
            for (int j = 0; j <= k; j += 1) {
                subMap.put(j, Integer.MAX_VALUE);
            }
            dp.put(i, subMap);
        }
        for (int j = 0; j <= k; j += 1) {
            dp.get(words.size()).put(j, 0);
        }
        int n = words.size();
        for (int i = n - 1; i >= 0; i -= 1) {
            for (int j = 0; j <= k; j += 1) {
                int newSpacesCount = j + 1 + words.get(i);
                int costOnStayingOnSameLine = Integer.MAX_VALUE;
                if (newSpacesCount <= k) {
                    costOnStayingOnSameLine = dp.get(i + 1).get(newSpacesCount);
                }
                int costOnGoingToNextLine = (k - j)*(k - j) + dp.get(i + 1).get(words.get(i));
                dp.get(i).put(j, Math.min(costOnStayingOnSameLine, costOnGoingToNextLine));
            }
        }

        return dp.get(1).get(words.getFirst());
    }
}
