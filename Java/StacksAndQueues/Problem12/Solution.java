package StacksAndQueues.Problem12;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Solution {
    public static void main(String[] args) {
        System.out.println(evaluate(Arrays.asList("2", "3", "1", "*", "+", "9", "-")));
        System.out.println(evaluate(Arrays.asList("2", "3", "^", "1", "+")));
        System.out.println(evaluate(Arrays.asList("2", "3", "1", "*", "+", "9", "-")));
        System.out.println(evaluate(Arrays.asList("1", "2", "3", "+", "*", "8", "-")));
        System.out.println(evaluate(Arrays.asList("100", "200", "+", "2", "/", "5", "*", "7", "+")));
    }

    public static String evaluate(List<String> postfix) {
        Stack<String> stack = new Stack<>();
        Set<String> operators = new HashSet<>(Arrays.asList("+", "-", "/", "^", "*"));
        for (String string : postfix) {
            if (operators.contains(string)) {
                String a = stack.pop(), b = stack.pop();
                Double x = Double.parseDouble(a), y = Double.parseDouble(b);
                if (string == "+") {
                    stack.push(String.valueOf(x + y));
                } else if (string == "-") {
                    stack.push(String.valueOf(y - x));
                } else if (string == "/") {
                    stack.push(String.valueOf(y / x));
                } else if (string == "^") {
                    stack.push(String.valueOf(Math.pow(y, x)));
                } else {
                    stack.push(String.valueOf(x * y));
                }
            } else {
                stack.push(string);
            }
        }
        return stack.top();
    }
}
