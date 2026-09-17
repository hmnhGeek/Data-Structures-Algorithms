// Problem link - https://www.geeksforgeeks.org/problems/zero-sum-subarrays1825/1
// Solution - https://www.youtube.com/watch?v=xvNwoz-ufXA


package SearchingAndSorting.Problem15;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    private static Integer countSumSubArrays(List<Integer> arr, int k) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);
        int sum = 0, count = 0;
        for (int i = 0; i < arr.size(); i += 1) {
            sum += arr.get(i);
            if (map.containsKey(sum - k)) {
                count += map.get(sum - k);
            }
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }
        return count;
    }

    public static Integer getZeroSumSubArrays(List<Integer> arr) {
        return countSumSubArrays(arr, 0);
    }

    public static void main(String[] args) {
        System.out.println("Zero sum sub-arrays");
        System.out.println(getZeroSumSubArrays(Arrays.asList(0, 0, 5, 5, 0, 0)));
        System.out.println(getZeroSumSubArrays(Arrays.asList(6, -1, -3, 4, -2, 2, 4, 6, -12, -7)));
        System.out.println(getZeroSumSubArrays(Arrays.asList(0)));
        System.out.println(getZeroSumSubArrays(Arrays.asList(1, 4, -5)));
        System.out.println(getZeroSumSubArrays(Arrays.asList(-1, 1, 0, 1)));
        System.out.println(getZeroSumSubArrays(Arrays.asList(-1, 0, 1, -1)));
        System.out.println(getZeroSumSubArrays(Arrays.asList(-2, 0, 2)));
        System.out.println();
        System.out.println("General Solution");
        System.out.println(countSumSubArrays(Arrays.asList(1, 2, 3, -3, 1, 1, 1, 4, 2, -3), 3));
    }
}
