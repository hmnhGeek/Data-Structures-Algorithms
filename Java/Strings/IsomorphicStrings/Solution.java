// Problem link - https://www.geeksforgeeks.org/problems/isomorphic-strings-1587115620/1
// Solution - https://www.youtube.com/watch?v=1UNjU3YMUCs


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
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
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
