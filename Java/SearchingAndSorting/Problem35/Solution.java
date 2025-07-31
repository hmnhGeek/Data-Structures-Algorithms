// Problem link - https://www.geeksforgeeks.org/dsa/in-place-merge-sort/


package SearchingAndSorting.Problem35;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        /*
            Time complexity is O(n * log(n)) and space complexity is O(n).
         */
        List<Integer> l1 = Arrays.asList(1,2,9,6,4,6,2);
        Utils.sort(l1);
        System.out.println(l1);

        List<Integer> l2 = Arrays.asList(68,65,89,34,5);
        Utils.sort(l2);
        System.out.println(l2);
    }
}
