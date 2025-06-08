package Matrix.Problem6;

import java.util.ArrayList;
import java.util.List;

public class Utility {
    public static Integer getMaxAreaInHistogram(List<Integer> histogram) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        Stack<Integer> stack = new Stack<>();
        int n = histogram.size();
        Integer maxArea = 0;
        for (int i = 0; i < n; i += 1) {
            while (!stack.isEmpty() && histogram.get(i) < histogram.get(stack.top())) {
                Integer bar = histogram.get(stack.pop());
                Integer rightBoundary = i;
                Integer leftBoundary = stack.top() == null ? -1 : stack.top();
                Integer area = bar * (rightBoundary - leftBoundary - 1);
                maxArea = Math.max(area, maxArea);
            }
            stack.push(i);
        }
        while (!stack.isEmpty()) {
            Integer bar = histogram.get(stack.pop());
            Integer leftBoundary = stack.top() == null ? -1 : stack.top();
            Integer area = bar * (n - leftBoundary - 1);
            maxArea = Math.max(area, maxArea);
        }
        return maxArea;
    }

    public static Integer maxRectangle(List<List<Integer>> matrix) {
        /*
            Time complexity is O(nm) and space complexity is O(m).
         */
        int n = matrix.size(), m = matrix.getFirst().size();
        Integer maxArea = 0;
        List<Integer> prevRow = new ArrayList<>();
        for (int j = 0; j < m; j += 1) {
            prevRow.add(0);
        }
        for (int i = 0; i < n; i += 1) {
            List<Integer> histogram = matrix.get(i);
            List<Integer> rectifiedHistogram = rectifyHistogram(histogram, prevRow);
            Integer area = getMaxAreaInHistogram(rectifiedHistogram);
            maxArea = Math.max(maxArea, area);
            prevRow = rectifiedHistogram;
        }
        return maxArea;
    }

    private static List<Integer> rectifyHistogram(List<Integer> histogram, List<Integer> prevRow) {
        int m = histogram.size();
        List<Integer> rectifiedHistogram = new ArrayList<>();
        for (int j = 0; j < m; j += 1) {
            if (histogram.get(j).equals(0)) {
                rectifiedHistogram.add(0);
            } else {
                rectifiedHistogram.add(prevRow.get(j) + histogram.get(j));
            }
        }
        return rectifiedHistogram;
    }
}
