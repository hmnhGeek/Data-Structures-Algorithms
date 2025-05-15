package DynamicProgramming.DP55;

import java.util.List;

public class Utils {
    private static Integer getStackTop(Stack<Integer> stack) {
        Integer top = stack.top();
        if (top == null) return -1;
        return top;
    }

    public static Integer getMaxAreaInHistogram(List<Integer> arr) {
        Stack<Integer> stack = new Stack<>();
        int n = arr.size();
        int maxArea = Integer.MIN_VALUE;
        for (int i = 0; i < n; i += 1) {
            while (!stack.isEmpty() && arr.get(getStackTop(stack)) > arr.get(i)) {
                Integer bar = arr.get(stack.pop());
                Integer leftBoundaryIndex = getStackTop(stack);
                Integer rightBoundaryIndex = i;
                Integer area = bar * (rightBoundaryIndex - leftBoundaryIndex - 1);
                maxArea = Math.max(area, maxArea);
            }
            stack.push(i);
        }
        while (!stack.isEmpty()) {
            Integer bar = arr.get(stack.pop());
            Integer leftBoundaryIndex = getStackTop(stack);
            Integer area = bar * (n - leftBoundaryIndex - 1);
            maxArea = Math.max(area, maxArea);
        }
        return maxArea;
    }
}
