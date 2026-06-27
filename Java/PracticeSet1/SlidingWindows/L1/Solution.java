package PracticeSet1.SlidingWindows.L1;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static Integer getMaxPointsFromCards(List<Integer> arr, Integer k) {
        int sum = 0;
        for (int i = 0; i < k; i += 1) {
            sum += arr.get(i);
        }
        int maxSum = sum;
        int j = arr.size() - 1, i = k - 1;
        while (i >= 0) {
            sum -= arr.get(i);
            i -= 1;
            sum += arr.get(j);
            j -= 1;
            maxSum = Math.max(maxSum, sum);
        }
        return maxSum;
    }

    public static void main(String[] args) {
        System.out.println(getMaxPointsFromCards(Arrays.asList(1,2,3,4,5,6,1), 3));
        System.out.println(getMaxPointsFromCards(Arrays.asList(2, 2, 2), 2));
        System.out.println(getMaxPointsFromCards(Arrays.asList(9,7,7,9,7,7,9), 7));
    }
}
