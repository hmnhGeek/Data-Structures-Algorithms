// Problem link - https://www.geeksforgeeks.org/problems/majority-element-1587115620/1
// Solution - https://www.youtube.com/watch?v=nP_ns3uSh80


package SearchingAndSorting.Problem8;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static Integer getMajorityElement(List<Integer> arr) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */
        Integer count = 0, element = null;
        int mainCount = 0;
        for (int i = 0; i < arr.size(); i += 1) {
            if (count == 0) {
                element = arr.get(i);
            } else if (element == arr.get(i)) {
                count += 1;
            } else {
                count -= 1;
            }
        }
        for (Integer i : arr) {
            if (i == element) {
                mainCount += 1;
            }
        }
        if (mainCount > arr.size()/2) {
            return element;
        }
        return null;
    }

    public static void main(String[] args) {
        System.out.println(getMajorityElement(Arrays.asList(1, 1, 2, 1, 3, 5, 1)));
        System.out.println(getMajorityElement(Arrays.asList(7)));
        System.out.println(getMajorityElement(Arrays.asList(2, 13)));
    }
}
