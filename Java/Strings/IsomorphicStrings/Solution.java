package Strings.IsomorphicStrings;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    public static void main(String[] args) {
        System.out.println(areIsomorphic("aab", "xxy"));
        System.out.println(areIsomorphic("aab", "xyz"));
        System.out.println(areIsomorphic("aac", "xyz"));
    }

    public static Boolean areIsomorphic(String s1, String s2) {
        if (s1.length() != s2.length()) return false;
        Map<Character, Character> map = new HashMap<>();
        for (int i = 0; i < s1.length(); i += 1) {
            char ss = s1.charAt(i);
            char tt = s2.charAt(i);
            if ((map.containsKey(ss) && map.get(ss) != tt) || (!map.containsKey(ss) && map.values().contains(tt))) return false;
            map.put(ss, tt);
        }
        return true;
    }
}
