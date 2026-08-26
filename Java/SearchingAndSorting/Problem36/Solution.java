// Problem link - https://www.geeksforgeeks.org/problems/zero-sum-subarrays1825/1
// Solution - https://www.youtube.com/watch?v=xvNwoz-ufXA


package SearchingAndSorting.Problem36;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static Integer getZeroSumSubArraysCount(List<Integer> arr, Integer k) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, 1);
        int prefixSum = 0;
        int count = 0;
        for (int i = 0; i < arr.size(); i += 1) {
            prefixSum += arr.get(i);
            if (map.containsKey(prefixSum - k)) {
                count += map.get(prefixSum - k);
            }
            map.put(prefixSum, map.getOrDefault(prefixSum, 0) + 1);
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println(getZeroSumSubArraysCount(Arrays.asList(0, 0, 5, 5, 0, 0), 0));
        System.out.println(getZeroSumSubArraysCount(Arrays.asList(6, -1, -3, 4, -2, 2, 4, 6, -12, -7), 0));
        System.out.println(getZeroSumSubArraysCount(Arrays.asList(0), 0));
    }
}
