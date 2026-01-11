package StacksAndQueues.Problem11;

import java.util.Arrays;
import java.util.List;

public class Utils {
    private static final List<Character> operators = Arrays.asList('+', '-', '/', '*');

    public static String convertToPostfix(String expr) {
        Stack<Character> stack = new Stack<>();
        String postfix = "";
        for (int i = 0; i < expr.length(); i += 1) {
            Character character = expr.charAt(i);
            if (character == '(' || operators.contains(character)) {
                stack.push(character);
            } else if (character == ')') {
                while (stack.top() != '(') {
                    postfix += stack.pop();
                }
                stack.pop();
            } else {
                postfix += character;
            }
        }
        return postfix;
    }

    public static Integer evaluatePostfix(String postfix) {
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < postfix.length(); i += 1) {
            Character character = postfix.charAt(i);
            if (operators.contains(character)) {
                Integer a = stack.pop(), b = stack.pop();
                if (character == '+') {
                    stack.push(a + b);
                } else if (character == '-') {
                    stack.push(b - a);
                } else if (character == '/') {
                    stack.push(b / a);
                } else {
                    stack.push(a * b);
                }
            } else {
                stack.push(Integer.parseInt(character.toString()));
            }
        }
        return stack.top();
    }
}
