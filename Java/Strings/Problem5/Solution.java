// Problem link - https://leetcode.com/problems/count-and-say/description/


package Strings.Problem5;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    private static String getRle(String s) {
        StringBuilder stringBuilder = new StringBuilder();
        int n = s.length();
        int i = 0;
        Map<Character, Integer> d = new HashMap<>();
        while (i < n) {
            Character c = s.charAt(i);
            int count = 1;
            i += 1;
            while (i < n && s.charAt(i) == c) {
                count += 1;
                i += 1;
            }
            stringBuilder.append(String.format("%d%s", count, c));
        }
        return stringBuilder.toString();
    }

    public static String countAndSay(int n) {
        if (n == 1) return "1";
        String result = countAndSay(n - 1);
        return getRle(result);
    }

    public static void main(String[] args) {
        System.out.println("Run Length Encoding");
        System.out.println(getRle("11"));
        System.out.println(getRle("3322251"));
        System.out.println(getRle("AAAABBBCCDAA"));
        System.out.println(getRle("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"));

        System.out.println();

        System.out.println("Count and Say Problem");
        System.out.println(countAndSay(4));
        System.out.println(countAndSay(1));
        System.out.println(countAndSay(3));
        System.out.println(countAndSay(5));
    }
}
