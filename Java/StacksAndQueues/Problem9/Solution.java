package StacksAndQueues.Problem9;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static List<Integer> getNextGreaterElements(List<Integer> arr) {
        int i = arr.size() - 1;
        Stack<Integer> stack = new Stack<>();
        List<Integer> result = new ArrayList<>();
        while (i >= 0) {
            while (stack.top() != null && stack.top() < arr.get(i)) {
                stack.pop();
            }
            if (stack.isEmpty()) {
                result.add(-1);
            } else {
                result.add(stack.top());
            }
            stack.push(arr.get(i));
            i -= 1;
        }
        return result.reversed();
    }

    public static void main(String[] args) {
        System.out.println(getNextGreaterElements(Arrays.asList(1, 3, 2, 4)));
        System.out.println(getNextGreaterElements(Arrays.asList(6, 8, 0, 1, 3)));
        System.out.println(getNextGreaterElements(Arrays.asList(1, 2, 3, 5)));
        System.out.println(getNextGreaterElements(Arrays.asList(5, 4, 3, 1)));
    }
}
