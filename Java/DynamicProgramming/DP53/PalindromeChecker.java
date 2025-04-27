package DynamicProgramming.DP53;

public class PalindromeChecker {
    public static boolean isPalindrome(String string) {
        int i = 0, j = string.length() - 1;
        while (i <= j) {
            if (string.charAt(i) == string.charAt(j)) {
                i += 1;
                j -= 1;
            } else {
                return false;
            }
        }
        return true;
    }
}
