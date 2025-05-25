// Problem link - https://www.geeksforgeeks.org/problems/palindrome-string0817/1

package Strings.Problem2;

public class Solution {
    public static boolean isPalindrome(String string) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */
        int n = string.length();
        int low = 0, high = n - 1;
        while (low <= high) {
            if (string.charAt(low) == string.charAt(high)) {
                low += 1;
                high -= 1;
            } else {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(isPalindrome("abba"));
        System.out.println(isPalindrome("abc"));
        System.out.println(isPalindrome("a"));
        System.out.println(isPalindrome("acbca"));
    }
}
