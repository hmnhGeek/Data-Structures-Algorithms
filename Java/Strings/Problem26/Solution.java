package Strings.Problem26;

import java.util.Map;

public class Solution {
    public static Integer getIntVal(String roman) {
        Map<Character, Integer> map = Map.of(
                'I', 1,
                'V', 5,
                'X', 10,
                'L', 50,
                'C', 100,
                'D', 500,
                'M', 1000
        );

        int n = roman.length();
        int result = 0;
        for (int i = 0; i < n; i += 1) {
            if (i + 1 < n && map.get(roman.charAt(i)) < map.get(roman.charAt(i + 1))) {
                result -= map.get(roman.charAt(i));
            } else {
                result += map.get(roman.charAt(i));
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(getIntVal("IX"));
        System.out.println(getIntVal("XL"));
        System.out.println(getIntVal("MCMIV"));
    }
}
