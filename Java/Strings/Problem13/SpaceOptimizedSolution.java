package Strings.Problem13;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpaceOptimizedSolution {
    public static Integer getMinCost(List<Integer> words, Integer k) {
        /*
            Time complexity is O(n*k) and space complexity is O(k).
         */
        Map<Integer, Integer> nxt = new HashMap<>();
        for (int j = 0; j <= k; j += 1) {
            nxt.put(j, 0);
        }
        int n = words.size();
        for (int i = n - 1; i > 0; i -= 1) {
            Map<Integer, Integer> curr = new HashMap<>();
            for (int j = 0; j <= k; j += 1) {
                curr.put(j, Integer.MAX_VALUE);
            }
            for (int j = 0; j <= k; j += 1) {
                int newSpacesCount = j + 1 + words.get(i);
                int costOnStayingOnSameLine = Integer.MAX_VALUE;
                if (newSpacesCount <= k) {
                    costOnStayingOnSameLine = nxt.get(newSpacesCount);
                }
                int costOnGoingToNextLine = (k - j)*(k - j) + nxt.get(words.get(i));
                curr.put(j, Math.min(costOnStayingOnSameLine, costOnGoingToNextLine));
            }
            nxt = curr;
        }

        return nxt.get(words.getFirst());
    }
}
