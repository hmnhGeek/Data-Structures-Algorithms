package Strings.Problem13;

import java.util.List;

public class RecursiveSolution {
    public static Integer getMinCost(List<Integer> words, Integer k) {
        /*
            Time complexity is exponential and space complexity is O(n).
         */
        return getMinCost(1, words.getFirst(), words, k);
    }

    private static Integer getMinCost(int curr, int consumedSpaces, List<Integer> words, Integer k) {
        if (curr == words.size()) return 0;

        int newSpacesCount = consumedSpaces + 1 + words.get(curr);
        int costOnStayingOnSameLine = Integer.MAX_VALUE;
        if (newSpacesCount <= k) {
            costOnStayingOnSameLine = getMinCost(curr + 1, newSpacesCount, words, k);
        }
        int costOnGoingToNextLine = (k - consumedSpaces)*(k - consumedSpaces) + getMinCost(curr + 1, words.get(curr), words, k);
        return Math.min(costOnStayingOnSameLine, costOnGoingToNextLine);
    }
}
