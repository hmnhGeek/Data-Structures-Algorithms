package PracticeSet2.SlidingWindows.L7;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    public static void main(String[] args) {
        System.out.println(getSubString("bbacba"));
    }

    public static Integer getSubString(String string) {
        return getCountLessThan(string, 3) - getCountLessThan(string, 2);
    }

    private static Integer getCountLessThan(String string, int k) {
        if (k < 0) return 0;
        int left = 0, right = 0, count = 0;
        int n = string.length();
        Map<Character, Integer> d = new HashMap<>();
        d.put('a', 0);
        d.put('b', 0);
        d.put('c', 0);

        while (right < n) {
            d.put(string.charAt(right), d.get(string.charAt(right)) + 1);
            while (uniqueCount(d) > k) {
                d.put(string.charAt(left), d.get(string.charAt(left)) - 1);
                left += 1;
            }
            count += (right - left + 1);
            right += 1;
        }

        return count;
    }

    private static int uniqueCount(Map<Character, Integer> d) {
        int count = 0;
        for (Character c : d.keySet()) {
            if (d.get(c) > 0) count += 1;
        }
        return count;
    }
}
