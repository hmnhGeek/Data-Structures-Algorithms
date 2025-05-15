// Problem link - https://www.geeksforgeeks.org/maximum-size-rectangle-binary-sub-matrix-1s/
// Solution - https://www.youtube.com/watch?v=tOylVCugy9k&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=56

package DynamicProgramming.DP55;

import java.util.List;

public class Utils {
    private static Integer getStackTop(Stack<Integer> stack) {
        Integer top = stack.top();
        if (top == null) return -1;
        return top;
    }

    public static Integer getMaxAreaInHistogram(List<Integer> arr) {
        /*
            Time complexity is O(n) and space complexity is O(n) for the stack.
         */

        // create required variables.
        Stack<Integer> stack = new Stack<>();
        int n = arr.size();
        int maxArea = Integer.MIN_VALUE;

        for (int i = 0; i < n; i += 1) {
            // while the stack has some elements and top element is greater than ith element, we must pop, because we
            // want to maintain linearly increasing order in the stack.
            while (!stack.isEmpty() && arr.get(getStackTop(stack)) > arr.get(i)) {
                // get the bar, which is the top element on the stack.
                Integer bar = arr.get(stack.pop());

                // element just before the top (new top now), will be the left boundary of the bar.
                Integer leftBoundaryIndex = getStackTop(stack);

                // for the top element, ith bar will be the right boundary.
                Integer rightBoundaryIndex = i;

                // get the area formed by this bar and update max area.
                Integer area = bar * (rightBoundaryIndex - leftBoundaryIndex - 1);
                maxArea = Math.max(area, maxArea);
            }

            // finally, once there is no greater element on top of the stack, push `i`.
            stack.push(i);
        }

        // once the iteration is over, stack will contain all those elements whose right boundary is `n`.
        while (!stack.isEmpty()) {
            Integer bar = arr.get(stack.pop());
            Integer leftBoundaryIndex = getStackTop(stack);
            Integer area = bar * (n - leftBoundaryIndex - 1);
            maxArea = Math.max(area, maxArea);
        }

        // return the max area.
        return maxArea;
    }
}
