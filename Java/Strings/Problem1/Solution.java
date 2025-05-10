// Problem link - https://leetcode.com/problems/reverse-string/description/

package Strings.Problem1;

public class Solution {
    public static String reverseString(String string) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        StringBuilder stringBuilder = new StringBuilder();
        int n = string.length();
        for (int i = n - 1; i >= 0; i -= 1) {
            stringBuilder.append(string.charAt(i));
        }
        return stringBuilder.toString();
    }

    public static void main(String[] args) {
        System.out.println(reverseString("hello"));
        System.out.println(reverseString("Hannah"));
    }
}
