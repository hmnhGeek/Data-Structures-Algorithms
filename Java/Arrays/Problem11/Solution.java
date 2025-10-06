// Problem link - https://leetcode.com/problems/find-the-duplicate-number/description/
// Solution - https://www.youtube.com/watch?v=49HrEGt6D2s


package Arrays.Problem11;

import java.util.Arrays;
import java.util.List;

public class Solution {
    public static Integer getDuplicate(List<Integer> arr) {
        /*
            Time complexity is O(n) and space complexity is O(1).
         */
        int n = arr.size();
        if (n == 0) return -1;
        int slow = arr.get(0);
        int fast = arr.get(0);

        // detect cycle
        while (true) {
            slow = arr.get(slow);
            fast = arr.get(arr.get(fast));
            if (slow == fast) break;
        }

        // get the cycle starting point
        slow = arr.get(0);
        while (slow != fast) {
            slow = arr.get(slow);
            fast = arr.get(fast);
        }

        return slow; // or fast, since they are same.
    }

    public static void main(String[] args) {
        System.out.println(getDuplicate(Arrays.asList(3, 1, 3, 4, 2)));
        System.out.println(getDuplicate(Arrays.asList(3, 3, 3, 3, 3)));
        System.out.println(getDuplicate(Arrays.asList(1, 3, 4, 2, 2)));
    }
}
