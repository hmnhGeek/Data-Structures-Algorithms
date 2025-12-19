// Problem link - https://www.geeksforgeeks.org/split-the-binary-string-into-substrings-with-equal-number-of-0s-and-1s/
// Use first solution from problem link. Don't refer to any video.


package Strings.Problem12;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static List<String> getBalancedStrings(String string) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */
        int count = 0;
        StringBuilder temp = new StringBuilder();
        List<String> result = new ArrayList<>();

        for (int i = 0; i < string.length(); i += 1) {
            Character c = string.charAt(i);
            if (c == '0') {
                count += 1;
            } else {
                count -= 1;
            }
            temp.append(c);
            if (count == 0) {
                result.add(temp.toString());
                temp = new StringBuilder();
            }
        }

        return result;
    }

    public static void main(String[] args) {
        System.out.println(getBalancedStrings("0100110101"));
        System.out.println(getBalancedStrings("0111100010"));
        System.out.println(getBalancedStrings("0000000000"));
        System.out.println(getBalancedStrings("0010110010"));
        System.out.println(getBalancedStrings("00110011"));
    }
}
