package StacksAndQueues.Problem6;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static void main(String[] args) {

        System.out.println(isValidParenthesis("())"));
        System.out.println(isValidParenthesis("[()]{}{[()()]()}"));
        System.out.println(isValidParenthesis("{([])}"));
        System.out.println(isValidParenthesis("()"));
        System.out.println(isValidParenthesis("([]"));
        System.out.println(isValidParenthesis("[(])"));
        System.out.println(isValidParenthesis("()[]{}"));
        System.out.println(isValidParenthesis("(]"));

    }

    private static Map<Character, Character> getBracketsMapping() {
        Map<Character, Character> mapping = new HashMap<>();
        mapping.put(')', '(');
        mapping.put('}', '{');
        mapping.put(']', '[');
        return mapping;
    }

    public static boolean isValidParenthesis(String brackets) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> bracketsMapping = getBracketsMapping();
        List<Character> openingBrackets = Arrays.asList('(', '[', '{');
        int i = 0, n = brackets.length();
        while (i < n) {
            Character character = brackets.charAt(i);
            if (openingBrackets.contains(character)) {
                stack.push(character);
            } else {
                if (stack.isEmpty()) return false;
                Character openingBracket = bracketsMapping.get(character);
                if (stack.head.data.equals(openingBracket)) {
                    stack.pop();
                } else {
                    return false;
                }
            }
            i += 1;
        }
        if (stack.isEmpty()) return true;
        return false;
    }
}
