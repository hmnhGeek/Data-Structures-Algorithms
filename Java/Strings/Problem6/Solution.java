package Strings.Problem6;

public class Solution {
    public static void main(String[] args) {
        System.out.println(longestPalindromicSubstring("babad"));
        System.out.println(longestPalindromicSubstring("forgeeksskeegfor"));
        System.out.println(longestPalindromicSubstring("Geeks"));
        System.out.println(longestPalindromicSubstring("abc"));
    }

    public static String longestPalindromicSubstring(String string) {
        String result = "";
        Integer resultLength = 0;

        for (int i = 0; i < string.length(); i += 1) {
            int left = i, right = i;
            while (left >= 0 && right < string.length() && string.charAt(left) == string.charAt(right)) {
                if (right - left + 1 > resultLength) {
                    resultLength = right - left + 1;
                    result = string.substring(left, right + 1);
                }
                left -= 1;
                right += 1;
            }

            left = i;
            right = i + 1;
            while (left >= 0 && right < string.length() && string.charAt(left) == string.charAt(right)) {
                if (right - left + 1 > resultLength) {
                    resultLength = right - left + 1;
                    result = string.substring(left, right + 1);
                }
                left -= 1;
                right += 1;
            }
        }

        return result;
    }
}
