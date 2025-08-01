// Problem link - https://www.programiz.com/java-programming/examples/check-valid-shuffle-of-strings
// Solution - https://www.youtube.com/watch?v=qN_vwYtvFUM


package Strings.Problem4;

public class Solution {
    public static boolean isValidShuffle(String s1, String s2, String s) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */
        int n1 = s1.length(), n2 = s2.length(), n = s.length();
        if (n1 + n2 != n) return false;
        int i = 0, j = 0, k = 0;
        while (k < n) {
            if (i < n1 && s1.charAt(i) == s.charAt(k)) {
                i += 1;
            } else if (j < n2 && s2.charAt(j) == s.charAt(k)) {
                j += 1;
            } else {
                return false;
            }
            k += 1;
        }
        if (i < n1 || j < n2) return false;
        return true;
    }

    public static void main(String[] args) {
        System.out.println(isValidShuffle("xy", "12", "1xy2"));
        System.out.println(isValidShuffle("XY", "12", "Y1X2"));
    }
}
