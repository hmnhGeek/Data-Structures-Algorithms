// Problem link - https://www.geeksforgeeks.org/problems/count-the-reversals0401/1
// Solution - https://www.youtube.com/watch?v=-n_CsIL3Ts4


package Strings.Problem21;

public class Solution {
    public static Integer minSwapsForBalancing(String brackets) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */
        int n = brackets.length();
        Stack<Character> stack = new Stack<>();
        if (n % 2 == 1) return -1;
        int openCount = 0, closeCount = 0;
        for (int i = 0; i < n; i += 1) {
            Character bracket = brackets.charAt(i);
            if (bracket == '{') {
                stack.push(bracket);
                openCount += 1;
            } else if (!stack.isEmpty()) {
                stack.pop();
                openCount -= 1;
            } else {
                closeCount += 1;
            }
        }
        if (openCount % 2 == 0) {
            openCount = openCount / 2;
        } else {
            openCount = (openCount / 2) + 1;
        }
        if (closeCount % 2 == 0) {
            closeCount = closeCount / 2;
        } else {
            closeCount = (closeCount / 2) + 1;
        }
        return openCount + closeCount;
    }

    public static void main(String[] args) {
        System.out.println(minSwapsForBalancing("}{{}}{{{"));
        System.out.println(minSwapsForBalancing("{{}{{{}{{}}{{"));
        System.out.println(minSwapsForBalancing("{{"));
        System.out.println(minSwapsForBalancing("}{}{"));
    }
}
