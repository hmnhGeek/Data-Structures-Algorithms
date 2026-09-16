package PracticeSet2.Matrix.Problem6;

import java.util.List;

public class Utils {
    public static Integer maxAreaInHistogram(List<Integer> histogram) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        Stack<Integer> stack = new Stack<>();
        int n = histogram.size();
        Integer maxArea = 0;
        for (int i = 0; i < histogram.size(); i += 1) {
            while (!stack.isEmpty() && histogram.get(stack.top()) > histogram.get(i)) {
                Integer bar = histogram.get(stack.pop());
                int lb = stack.top() != null ? stack.top() : -1;
                int area = bar * (i - lb - 1);
                maxArea = Math.max(maxArea, area);
            }
            stack.push(i);
        }
        while (!stack.isEmpty()) {
            Integer bar = histogram.get(stack.pop());
            int lb = stack.top() != null ? stack.top() : -1;
            int area = bar * (n - lb - 1);
            maxArea = Math.max(maxArea, area);
        }
        return maxArea;
    }
}
