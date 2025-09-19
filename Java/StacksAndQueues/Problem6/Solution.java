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

            // if it's an opening bracket, simply push it to the stack.
            if (openingBrackets.contains(character)) {
                stack.push(character);
            } else {
                // if it is a closing bracket, check if stack is empty. If stack is empty, this closing bracket
                // is unwanted, return false.
                if (stack.isEmpty()) return false;

                // find the opening bracket for this closing bracket.
                Character openingBracket = bracketsMapping.get(character);

                // if the opening bracket is on top of stack, pop it.
                if (stack.head.data.equals(openingBracket)) {
                    stack.pop();
                } else {
                    // else if some other opening bracket is on top, return false as this combination
                    // is not balanced.
                    return false;
                }
            }
            i += 1;
        }

        // if at the end, stack is empty, then its balanced else not.
        if (stack.isEmpty()) return true;
        return false;
    }
}
