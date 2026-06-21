package PracticeSet1.Heap.Problem3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static List<Integer> getSlidingWindowMaximum(List<Integer> arr, int k) {
        int n = arr.size();
        List<Integer> result = new ArrayList<>();
        Deque<Integer> deque = new Deque<>();
        if (n == 0) return result;
        for (int i = 0; i < n; i += 1) {
            while (!deque.isEmpty() && deque.getFront() <= i - k) {
                deque.popFront();
            }
            while (!deque.isEmpty() && arr.get(i) > arr.get(deque.getBack())) {
                deque.popBack();
            }
            deque.pushBack(i);
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
