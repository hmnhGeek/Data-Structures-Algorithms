// Problem link - https://www.geeksforgeeks.org/dsa/convert-sentence-equivalent-mobile-numeric-keypad-sequence/


package Strings.Problem20;

import java.util.HashMap;

public class Solution {
    public static void main(String[] args) {
        System.out.println(getNumericRepresentation("GEEKSFORGEEKS"));
        System.out.println(getNumericRepresentation("HELLO WORLD"));
    }

    public static String getNumericRepresentation(String string) {
        /*
            Time complexity is O(n) and space complexity is O(27).
         */
        HashMap<Character, String> map = new HashMap<>();
        populateMap(map);
        StringBuilder sb = new StringBuilder();
        for (Character c : string.toCharArray()) {
            sb.append(map.get(c));
        }
        return sb.toString();
    }

    private static void populateMap(HashMap<Character, String> map) {
        map.put('A', "2");
        map.put('B', "22");
        map.put('C', "222");
        map.put('D', "3");
        map.put('E', "33");
        map.put('F', "333");
        map.put('G', "4");
        map.put('H', "44");
        map.put('I', "444");
        map.put('J', "5");
        map.put('K', "55");
        map.put('L', "555");
        map.put('M', "6");
        map.put('N', "66");
        map.put('O', "666");
        map.put('P', "7");
        map.put('Q', "77");
        map.put('R', "777");
        map.put('S', "7777");
        map.put('T', "8");
        map.put('U', "88");
        map.put('V', "888");
        map.put('W', "9");
        map.put('X', "99");
        map.put('Y', "999");
        map.put('Z', "9999");
        map.put(' ', "0");
    }
}
