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
}
