package StacksAndQueues.Problem11;

public class Solution {
    public static void main(String[] args) {
        System.out.println(Utils.convertToPostfix("((A-B)*((C/(D+E))+F))"));
        System.out.println(Utils.convertToPostfix("((2+4)*(4+6))"));
        System.out.println(evaluate("((2+4)*(4+6))"));
        System.out.println(evaluate("((7*(5+5)/(2*5))-3)"));
    }

    public static Integer evaluate(String expr) {
        return Utils.evaluatePostfix(Utils.convertToPostfix(expr));
    }
}
