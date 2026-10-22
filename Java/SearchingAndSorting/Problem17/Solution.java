// Problem link - https://www.geeksforgeeks.org/problems/sort-by-set-bit-count1153/1
// Solution - https://www.youtube.com/watch?v=2owpaafBIgw


package SearchingAndSorting.Problem17;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void sortBySetBits(List<Integer> arr) {
        /*
            Time complexity is O(n * log(n)) and space complexity is O(1).
         */
        arr.sort((a, b) -> {
            int setBitsInA = Integer.bitCount(a);
            int setBitsInB = Integer.bitCount(b);

            // 1. If set bit counts are different, sort in descending order of set bits
            if (setBitsInA != setBitsInB) {
                return Integer.compare(setBitsInB, setBitsInA);
            }

            // 2. If set bit counts are the same, return 0 to preserve stable order
            return 0;
        });
        System.out.println(arr);
    }

    public static void main(String[] args) {
        sortBySetBits(Arrays.asList(5, 2, 3, 9, 4, 6, 7, 15, 32));
    }
}
