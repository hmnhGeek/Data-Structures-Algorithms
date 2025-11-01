// Problem link - https://www.geeksforgeeks.org/problems/find-median-in-a-stream-1587115620/1
// Solution - https://www.youtube.com/watch?v=Yv2jzDzYlp8


package Heap.Problem12;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(test(5, 15, 1, 3, 2, 8));
        System.out.println(test(2, 2, 2, 2));
        System.out.println(test(2, 1, 8, 6, 3, 4));
    }

    public static List<Double> test(Integer...args) {
        MedianFinder<Integer> medianFinder = new MedianFinder<>();
        List<Double> result = new ArrayList<>();
        for (Integer i : args) {
            medianFinder.insert(i);
            result.add(medianFinder.getMedian());
        }
        return result;
    }
}
