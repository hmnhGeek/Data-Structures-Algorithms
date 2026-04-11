// Problem link - https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1


package Strings.Problem16;

import java.util.Map;

public class Solution {
    private static final Map<Character, Character> bracketMap = Map.of(
            ']', '[',
            '}', '{',
            ')', '('
    );

    public static boolean isBalanced(String string) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        Stack<Character> stack = new Stack<>();
        for (Character bracket : string.toCharArray()) {
            if (bracket == '(' || bracket == '[' || bracket == '{') {
                stack.push(bracket);
            } else {
                // got a closing bracket but stack is empty.
                if (stack.isEmpty()) return false;
                if (stack.top() != bracketMap.get(bracket)) return false;
                stack.pop();
            }
        }
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        System.out.println(Solution.isBalanced("{([])}"));          // true
        System.out.println(Solution.isBalanced("([]"));             // false
        System.out.println(Solution.isBalanced("()"));              // true
        System.out.println(Solution.isBalanced("[()]{}{[()()]()}"));// true
        System.out.println(Solution.isBalanced("[(])"));            // false
        System.out.println(Solution.isBalanced("()[]{}"));          // true
        System.out.println(Solution.isBalanced("(]"));              // false
        System.out.println(Solution.isBalanced("{[(])}"));          // false
    }
}
