package DynamicProgramming;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Stream;

class QuickSort {
    public static <T extends Comparable<T>> void sort(List<T> arr) {
        QuickSort.sort(arr, 0, arr.size() - 1);
    }

    private static <T extends Comparable<T>> void sort(List<T> arr, int low, int high) {
        if (low >= high) {
            return;
        }
        int partitionIndex = QuickSort.getPartitionIndex(arr, low, high);
        QuickSort.sort(arr, low, partitionIndex - 1);
        QuickSort.sort(arr, partitionIndex + 1, high);
    }

    private static <T extends Comparable<T>> Integer getPartitionIndex(List<T> arr, int low, int high) {
        T pivot = arr.get(low);
        int i = low, j = high;
        while (i < j) {
            while (arr.get(i).compareTo(pivot) <= 0 && i <= high - 1) {
                i += 1;
            }
            while (arr.get(j).compareTo(pivot) > 0 && j >= low + 1) {
                j -= 1;
            }
            if (i < j) {
                Collections.swap(arr, i, j);
            }
        }
        Collections.swap(arr, low, j);
        return j;
    }
}

class DP50Recursive {
    /**
     * Time complexity is exponential and space complexity is O(n).
     */

    private static Integer solve(List<Integer> arr, Integer i, Integer j) {
        if (i > j) {
            return 0;
        }
        int minCost = Integer.MAX_VALUE;
        for (int k = i; k <= j; k += 1) {
            int cost = arr.get(j + 1) - arr.get(i - 1) + solve(arr, i, k - 1) + solve(arr, k + 1, j);
            minCost = Math.min(cost, minCost);
        }
        return minCost;
    }

    public static Integer getMinCostToCutRod(List<Integer> arr, Integer length) {
        int n = arr.size();
        QuickSort.sort(arr);
        List<Integer> rod = Stream.of(List.of(0), arr, List.of(length)).flatMap(List::stream).toList();
        return DP50Recursive.solve(rod, 1, n);
    }
}

class Solution {
    public static void main(String[] args) {
        System.out.println("Recursive Solution");
        System.out.println(DP50Recursive.getMinCostToCutRod(Arrays.asList(1, 3, 4, 5), 7));
        System.out.println(DP50Recursive.getMinCostToCutRod(Arrays.asList(1, 3), 4));
        System.out.println(DP50Recursive.getMinCostToCutRod(Arrays.asList(1, 3, 4), 5));
        System.out.println(DP50Recursive.getMinCostToCutRod(Arrays.asList(1, 3, 4, 7), 10));
        System.out.println(DP50Recursive.getMinCostToCutRod(Arrays.asList(1, 3), 10));
        System.out.println(DP50Recursive.getMinCostToCutRod(Arrays.asList(5, 6, 1, 4, 2), 9));
    }
}