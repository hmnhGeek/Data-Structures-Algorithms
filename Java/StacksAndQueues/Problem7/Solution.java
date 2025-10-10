// Problem link - https://www.geeksforgeeks.org/problems/reverse-a-string-using-stack/1


package StacksAndQueues.Problem7;

public class Solution {
    public static void main(String[] args) {
        test('g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's');
    }

    public static <T> void test(T...args) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */
        Stack<T> stack = new Stack<>();
        for (T x : args) {
            stack.push(x);
        }
        System.out.println(stack);
        stack.reverse();
        System.out.println(stack);
        System.out.println();
    }
}
