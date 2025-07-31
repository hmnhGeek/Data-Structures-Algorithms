// Problem link - https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1
// Solution - https://www.youtube.com/watch?v=HCL4_bOd3-4


package Arrays.Problem8;

import java.util.Arrays;
import java.util.List;

public class Solution {
    private static Integer kadaneAlgorithm(List<Integer> arr) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */
        int n = arr.size();
        Integer maxSum = Integer.MIN_VALUE;
        int i = 0;
        int currSum = 0;
        while (i < n) {
            currSum += arr.get(i);
            maxSum = Math.max(maxSum, currSum);
            if (currSum < 0) {
                currSum = 0;
            }
            i += 1;
        }
        return maxSum;
    }

    public static void main(String[] args) {
        System.out.println(kadaneAlgorithm(Arrays.asList(2, 3, -8, 7, -1, 2, 3)));
        System.out.println(kadaneAlgorithm(Arrays.asList(-2, -4)));
        System.out.println(kadaneAlgorithm(Arrays.asList(5, 4, 1, 7, 8)));
    }
}
