// Problem link - https://www.geeksforgeeks.org/dsa/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/#expected-approach-using-deque-on-time-and-ok-space
// Solution - https://www.youtube.com/watch?v=29OnjVQ-fk4


package PracticeSet1.Heap.Problem3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static List<Integer> getSlidingWindowMaximum(List<Integer> arr, int k) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        int n = arr.size();
        List<Integer> result = new ArrayList<>();
        Deque<Integer> deque = new Deque<>();
        if (n == 0) return result;
        for (int i = 0; i < n; i += 1) {
            // if the frontal index is outside the left boundary of the window,
            // then pop from front.
            while (!deque.isEmpty() && deque.getFront() <= i - k) {
                deque.popFront();
            }

            // if current element is greater than queue's back, continuously pop
            // from the back so that monotonous decreasing order is maintained.
            while (!deque.isEmpty() && arr.get(i) > arr.get(deque.getBack())) {
                deque.popBack();
            }

            // push the current index.
            deque.pushBack(i);

            // while `i` is greater than the right boundary of the first window, update
            // maximums.
            if (i >= k - 1) {
                result.add(arr.get(deque.getFront()));
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(getSlidingWindowMaximum(Arrays.asList(1, 2, 3, 1, 4, 5, 2, 3, 6), 3));
        System.out.println(getSlidingWindowMaximum(Arrays.asList(5, 1, 3, 4, 2, 6), 1));
        System.out.println(getSlidingWindowMaximum(Arrays.asList(1, 3, 2, 1, 7, 3), 3));
        System.out.println(getSlidingWindowMaximum(Arrays.asList(1,3,-1,-3,5,3,6,7), 3));
        System.out.println(getSlidingWindowMaximum(Arrays.asList(4,0,-1,3,5,3,6,8), 3));
    }
}
