// Problem link - https://www.geeksforgeeks.org/problems/maximum-rectangular-area-in-a-histogram-1587115620/1


package StacksAndQueues.Problem17;

import java.util.List;

public class Solution {
    public static Integer maxAreaInHistogram(List<Integer> histogram) {
        /*
            Time complexity is O(n) and space complexity is O(n).
         */
        Stack<Integer> stack = new Stack<>();
        int maxArea = 0;
        for (int i = 0; i < histogram.size(); i += 1) {
            while (!stack.isEmpty() && histogram.get(i) < histogram.get(stack.top())) {
                Integer bar = histogram.get(stack.pop());
                int lb = stack.isEmpty() ? -1 : stack.top();
                int area = bar * (i - lb - 1);
                maxArea = Math.max(area, maxArea);
            }
            stack.push(i);
        }
        while (!stack.isEmpty()) {
            Integer bar = histogram.get(stack.pop());
            int lb = stack.isEmpty() ? -1 : stack.top();
            int area = bar * (histogram.size() - lb - 1);
            maxArea = Math.max(area, maxArea);
        }
        return maxArea;
    }

    public static void main(String[] args) {
        System.out.println(maxAreaInHistogram(List.of(60, 20, 50, 40, 10, 50, 60)));
        System.out.println(maxAreaInHistogram(List.of(7, 2, 8, 9, 1, 3, 6, 5)));
        System.out.println(maxAreaInHistogram(List.of(3)));
        System.out.println(maxAreaInHistogram(List.of(2, 1, 5, 6, 2, 3)));
        System.out.println(maxAreaInHistogram(List.of(2, 4)));
        System.out.println(maxAreaInHistogram(List.of(1, 0, 1, 2, 2, 2, 2, 1, 0, 2)));
        System.out.println(maxAreaInHistogram(List.of(1, 2, 1, 0, 1, 1, 0, 0, 2, 2)));
        System.out.println(maxAreaInHistogram(List.of(8, 6, 3, 5, 0, 0, 4, 10, 2, 5)));
        System.out.println(maxAreaInHistogram(List.of(6, 1, 8, 10, 5, 7, 0, 4, 5, 8)));
    }
}
