// Problem link - https://www.geeksforgeeks.org/problems/expression-contains-redundant-bracket-or-not/0
// Solution - https://www.youtube.com/watch?v=BmZnJehDzyU&t=3105s


package StacksAndQueues.Problem19;

import java.util.List;

public class Solution {
    private static final List<Character> operators = List.of('+', '-', '/', '*');

    public static boolean hasRedundantBrackets(String expr) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        Stack<Character> stack = new Stack<>();
        for (Character character : expr.toCharArray()) {
            if (operators.contains(character) || character == '(') {
                stack.push(character);
            } else if (character == ')') {
                if (stack.top() == '(') return true;
                while (stack.top() != '(') {
                    stack.pop();
                }
                stack.pop();
            }
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println(Solution.hasRedundantBrackets("((a+b))"));
        System.out.println(Solution.hasRedundantBrackets("(a+(b)/c)"));
        System.out.println(Solution.hasRedundantBrackets("(a+b+(c+d))"));
        System.out.println(Solution.hasRedundantBrackets("(a+b)"));
        System.out.println(Solution.hasRedundantBrackets("(a+c*b)+(c)"));
        System.out.println(Solution.hasRedundantBrackets("(a*b+(c/d))"));
        System.out.println(Solution.hasRedundantBrackets("((a/b))"));
    }
}
