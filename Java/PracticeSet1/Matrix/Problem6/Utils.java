package PracticeSet1.Matrix.Problem6;

import java.util.List;

public class Utils {
    public static Integer getMaxAreaHistogram(List<Integer> arr) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        Stack<Integer> stack = new Stack<>();
        Integer maxArea = 0;
        for (int i = 0; i < arr.size(); i += 1) {
            while (!stack.isEmpty() && arr.get(i) < arr.get(stack.top())) {
                Integer bar = arr.get(stack.pop());
                Integer top = stack.top() != null ? stack.top() : -1;
                Integer area = bar * (i - top - 1);
                maxArea = Math.max(area, maxArea);
            }
            stack.push(i);
        }
        while (!stack.isEmpty()) {
            Integer bar = arr.get(stack.pop());
            Integer top = stack.top() != null ? stack.top() : -1;
            Integer area = bar * (arr.size() - top - 1);
            maxArea = Math.max(area, maxArea);
        }
        return maxArea;
    }
}
