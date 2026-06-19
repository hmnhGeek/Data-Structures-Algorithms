// Problem link - https://www.geeksforgeeks.org/problems/longest-prefix-suffix2527/1
// Solution - https://www.youtube.com/watch?v=qases-9gOpk
// Problem link - https://www.geeksforgeeks.org/dsa/kmp-algorithm-for-pattern-searching/


package Strings.Problem19;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println("LPS Code Run");
        System.out.println(Utils.getLPS("abab"));
        System.out.println(Utils.getLPS("aabcdaabc"));
        System.out.println(Utils.getLPS("aaaa"));
        System.out.println();
        System.out.println("KMP Run");
        System.out.println(getKMPMatch("abcab", "ab"));
        System.out.println(getKMPMatch("aabaacaadaabaaba", "aaba"));
        System.out.println(getKMPMatch("abracadabra", "abra"));
        System.out.println(getKMPMatch("abcabcabc", "abc"));
    }

    public static List<Integer> getKMPMatch(String text, String pattern) {
        List<Integer> lps = Utils.getLPS(pattern);
        List<Integer> result = new ArrayList<>();
        int i = 0, j = 0;
        int n = text.length();
        int m = pattern.length();
        while (i < n) {
            if (text.charAt(i) == pattern.charAt(j)) {
                i += 1;
                j += 1;
            }
            if (j == m) {
                result.add(i - j);
                j = lps.get(j - 1);
            } else if (pattern.charAt(j) != text.charAt(i)) {
                if (j >= 1) {
                    j = lps.get(j - 1);
                } else {
                    i += 1;
                }
            }
        }
        return result;
    }
}
