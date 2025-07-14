// Problem link - https://www.geeksforgeeks.org/dsa/a-program-to-check-if-strings-are-rotations-of-each-other/
// Solution - https://www.youtube.com/watch?v=8ZKA6VA0J9I

package Strings.CheckStringRotation;

public class Solution {
    public static void main(String[] args) {
        System.out.println(isRotation("abcd", "cdab"));
        System.out.println(isRotation("aab", "aba"));
        System.out.println(isRotation("abcd", "acbd"));
    }

    public static boolean isRotation(String s1, String s2) {
        /*
            Time complexity is O(2n) and space complexity is O(2n).
         */
        String temp = s1 + s1;
        return temp.contains(s2);
    }
}
