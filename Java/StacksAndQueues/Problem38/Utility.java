// Problem link - https://www.geeksforgeeks.org/next-smaller-element/

package StacksAndQueues.Problem38;

import java.util.ArrayList;
import java.util.List;

public class Utility {
    public static <T extends Comparable<T>> List<T> getNextSmaller(List<T> arr) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        int n = arr.size();
        int i = n - 1;
        Stack<T> stack = new Stack<>();
        List<T> result = new ArrayList<>();
        while (i >= 0) {
            while (!stack.isEmpty() && stack.top().compareTo(arr.get(i)) >= 0) {
                stack.pop();
            }
            result.add(stack.top());
            stack.push(arr.get(i));
            i -= 1;
        }
        return result.reversed();
    }
}
