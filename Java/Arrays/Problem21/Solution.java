// Problem link - https://www.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1
// Solution - https://www.youtube.com/watch?v=xvNwoz-ufXA


package Arrays.Problem21;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Solution {
    public static Boolean hasZeroSumSubArray(List<Integer> arr) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        return hasSumSubArray(arr, 0);
    }

    private static Boolean hasSumSubArray(List<Integer> arr, int target) {
        Map<Integer, Integer> prefixSums = new HashMap<>();
        prefixSums.put(0, 1);
        int prefixSum = 0;
        int count = 0;
        for (int i = 0; i < arr.size(); i += 1) {
            prefixSum += arr.get(i);
            count += prefixSums.getOrDefault(prefixSum - target, 0);
            prefixSums.put(
                    prefixSum,
                    prefixSums.getOrDefault(prefixSum, 0) + 1
            );
        }
        return count > 0;
    }

    public static void main(String[] args) {
        System.out.println(Solution.hasZeroSumSubArray(Arrays.asList(4, 2, -3, 1, 6)));
        System.out.println(Solution.hasZeroSumSubArray(Arrays.asList(9, -3, 3, -1, 6, -5)));
        System.out.println(Solution.hasZeroSumSubArray(Arrays.asList(4, 2, 0, 1, 6)));
        System.out.println(Solution.hasZeroSumSubArray(Arrays.asList(1, 4, -5)));
        System.out.println(Solution.hasZeroSumSubArray(Arrays.asList(1, 3, -1, 4, -4)));
        System.out.println(Solution.hasZeroSumSubArray(Arrays.asList(1, -1, 2, -2)));
        System.out.println(Solution.hasZeroSumSubArray(Arrays.asList(1, 2, 1, -2)));
    }
}
