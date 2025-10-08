// Problem link - https://www.geeksforgeeks.org/problems/value-equal-to-index-value1330/1


package SearchingAndSorting.Problem2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(getFixedPoints(Arrays.asList(15, 2, 45, 4, 7)));
        System.out.println(getFixedPoints(Arrays.asList(1)));
    }

    public static List<Integer> getFixedPoints(List<Integer> arr) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < arr.size(); i += 1) {
            if (i + 1 == arr.get(i)) {
                result.add(i + 1);
            }
        }
        return result;
    }
}
