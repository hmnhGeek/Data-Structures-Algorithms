package Heap.Problem12;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        System.out.println(test(5, 15, 1, 3, 2, 8));
        System.out.println(test(2, 2, 2, 2));
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
