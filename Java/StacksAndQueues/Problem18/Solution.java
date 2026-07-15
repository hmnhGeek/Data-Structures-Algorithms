package StacksAndQueues.Problem18;

public class Solution {
    public static Integer getValidSubstringLength(String brackets) {
        Stack<Character> stack = new Stack<>();
        int count = 0;
        int longestSubstring = 0;
        for (int i = 0; i < brackets.length(); i += 1) {
            Character bracket = brackets.charAt(i);
            if (bracket == '(') {
                stack.push(bracket);
            } else {
                if (!stack.isEmpty() && stack.top() == '(') {
                    stack.pop();
                    count += 2;
                } else {
                    longestSubstring = Math.max(longestSubstring, count);
                    count = 0;
                }
            }
        }
        longestSubstring = Math.max(longestSubstring, count);
        return longestSubstring;
    }

    public static void main(String[] args) {
        System.out.println(getValidSubstringLength("(()("));
        System.out.println(getValidSubstringLength("()(())("));
        System.out.println(getValidSubstringLength("(()())"));
        System.out.println(getValidSubstringLength(")())"));
        System.out.println(getValidSubstringLength("(()"));
        System.out.println(getValidSubstringLength(")()())"));
        System.out.println(getValidSubstringLength(""));
        System.out.println(getValidSubstringLength("()))((())"));
        System.out.println(getValidSubstringLength("))(("));
        System.out.println(getValidSubstringLength("()))((((())))))"));
        System.out.println(getValidSubstringLength(")(()"));
    }
}
