// Problem link - https://www.geeksforgeeks.org/dsa/stack-permutations-check-if-an-array-is-stack-permutation-of-other/#expected-approach-simulating-push-and-pop-on-time-and-o1-space


package StacksAndQueues.Problem22;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static <T> Boolean stackPermutation(List<T> a, List<T> b) {
        /*
            Time complexity is O(n) time and O(n) space.
         */
        Stack<T> stack = new Stack<>();
        int j = 0;
        for (int i = 0; i < a.size(); i += 1) {
            stack.push(a.get(i));
            while (!stack.isEmpty() && stack.top() == b.get(j)) {
                stack.pop();
                j += 1;
            }
        }
        return j == b.size();
    }

    public static void main(String[] args) {
        System.out.println(stackPermutation(Arrays.asList(1, 2, 3), Arrays.asList(2, 1, 3)));
        System.out.println(stackPermutation(Arrays.asList(1, 2, 3), Arrays.asList(3, 1, 2)));
    }
}
