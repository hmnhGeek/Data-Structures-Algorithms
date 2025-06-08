package Matrix.Problem6;

import java.util.List;

public class Utility {
    public static Integer getMaxAreaInHistogram(List<Integer> histogram) {
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
}
