package Arrays.Problem13;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static Integer kadane(List<Integer> arr) {
        int currSum = 0, maxSum = 0;
        int i = 0, n = arr.size();
        while (i < n) {
            currSum += arr.get(i);
            if (maxSum < currSum) {
                maxSum = currSum;
            }
            if (currSum < 0) {
                currSum = 0;
            }
            i += 1;
        }
        return maxSum;
    }

    public static void main(String[] args) {
        System.out.println(kadane(Arrays.asList(2, 3, -8, 7, -1, 2, 3)));
        System.out.println(kadane(Arrays.asList(-2, -4)));
        System.out.println(kadane(Arrays.asList(5, 4, 1, 7, 8)));
        System.out.println(kadane(Arrays.asList(-2,1,-3,4,-1,2,1,-5,4)));
        System.out.println(kadane(List.of(1)));
        System.out.println(kadane(Arrays.asList(5,4,-1,7,8)));
    }
}
