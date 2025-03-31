package BinarySearch;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

class Utility {
    public static <T> List<T> getList(Integer size, T defaultValue) {
        List<T> list = new ArrayList<>();
        for (int i = 0; i < size; i += 1) {
            list.add(defaultValue);
        }
        return list;
    }
}

class LinearSolution {
    public static Double getMinimizedMaxDistance(List<Integer> arr, Integer k) {
        int n = arr.size();
        List<Integer> slots = Utility.getList(n - 1, 0);
        for (int i = 0; i < k; i += 1) {
            int maxSlotIndex = -1;
            double maxSlotLength = 0.0;
            for (int j = 0; j < n - 1; j += 1) {
                int left = arr.get(j);
                int right = arr.get(j + 1);
                double slotLength = (right - left)/((double) slots.get(j) + 1.0);
                if (maxSlotLength < slotLength) {
                    maxSlotLength = slotLength;
                    maxSlotIndex = j;
                }
            }
            slots.set(maxSlotIndex, slots.get(maxSlotIndex) + 1);
        }
        double maxSlotLength = 0;
        for (int j = 0; j < n - 1; j += 1) {
            int left = arr.get(j);
            int right = arr.get(j + 1);
            double slotLength = (right - left)/((double) slots.get(j) + 1.0);
            if (maxSlotLength < slotLength) {
                maxSlotLength = slotLength;
            }
        }
        return maxSlotLength;
    }
}

class Solution {
    public static void main(String[] args) {
        System.out.println(LinearSolution.getMinimizedMaxDistance(Arrays.asList(1, 13, 17, 23), 5));
        System.out.println(LinearSolution.getMinimizedMaxDistance(Arrays.asList(1,2,3,4,5,6,7), 6));
        System.out.println(LinearSolution.getMinimizedMaxDistance(Arrays.asList(1, 2, 3, 4, 5), 4));
        System.out.println(LinearSolution.getMinimizedMaxDistance(IntStream.range(1, 11).boxed().toList(), 1));
        System.out.println(LinearSolution.getMinimizedMaxDistance(Arrays.asList(3, 6, 12, 19, 33, 44, 67, 72, 89, 95), 2));
        System.out.println(LinearSolution.getMinimizedMaxDistance(Arrays.asList(1, 13, 17, 23), 5));
    }
}