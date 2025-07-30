// Problem link - https://www.geeksforgeeks.org/problems/binary-subarray-with-sum/0
// Solution - https://www.youtube.com/watch?v=XnMdNUkX6VM&list=PLgUwDviBIf0q7vrFA_HEWcqRqMpCXzYAL&index=9


package SlidingWindows.L9;

import java.util.Arrays;
import java.util.List;

public class Solution {
    private static Integer sumLessThanEqualTo(List<Integer> arr, Integer sum) {
        if (sum < 0) {
            return 0;
        }
        int sumTracker = 0;
        int count = 0;
        int left = 0, right = 0;
        int n = arr.size();
        while (right < n) {
            sumTracker += arr.get(right);
            while (sumTracker > sum) {
                sumTracker -= arr.get(left);
                left += 1;
            }
            count += (right - left + 1);
            right += 1;
        }
        return count;
    }

    public static Integer binarySubarraysCount(List<Integer> arr, Integer sum) {
        /*
            The idea is that in a binary array, the sum == k can be found out using the formula:
                f(sum = k) = f(sum <= k) - f(sum <= k-1)

            Overall time complexity is O(2n) and space complexity is O(1).
         */
        return sumLessThanEqualTo(arr, sum) - sumLessThanEqualTo(arr, sum - 1);
    }

    public static void main(String[] args) {
        System.out.println(Solution.binarySubarraysCount(Arrays.asList(1, 0, 1, 0, 1), 2));
        System.out.println(Solution.binarySubarraysCount(Arrays.asList(0, 0, 0, 0, 0), 0));
        System.out.println(Solution.binarySubarraysCount(Arrays.asList(1, 0, 1, 1, 0, 1), 2));
        System.out.println(Solution.binarySubarraysCount(Arrays.asList(1, 0, 1, 1, 1, 0, 1), 3));
        System.out.println(Solution.binarySubarraysCount(Arrays.asList(1, 1, 0, 1, 1), 5));
    }
}
