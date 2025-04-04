// Problem link - https://leetcode.com/problems/minimum-cost-to-cut-a-stick/
// Solution - https://www.youtube.com/watch?v=xwomavsC86c&list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY&index=51


package DynamicProgramming;

import java.util.*;
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

class DP50Memoized {
    /**
     * Time complexity is O(n^3) and space complexity is O(n + n^2).
     */

    private static Integer solve(List<Integer> arr, Integer i, Integer j, Map<Integer, Map<Integer, Integer>> dp) {
        if (i > j) {
            return 0;
        }
        if (dp.get(i).get(j) != null) {
            return dp.get(i).get(j);
        }
        int minCost = Integer.MAX_VALUE;
        for (int k = i; k <= j; k += 1) {
            int cost = arr.get(j + 1) - arr.get(i - 1) + solve(arr, i, k - 1, dp) + solve(arr, k + 1, j, dp);
            minCost = Math.min(cost, minCost);
        }
        Map<Integer, Integer> v = dp.get(i);
        v.put(j, minCost);
        dp.put(i, v);
        return dp.get(i).get(j);
    }

    public static Integer getMinCostToCutRod(List<Integer> arr, Integer length) {
        int n = arr.size();
        QuickSort.sort(arr);
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 1; i <= n; i += 1) {
            Map<Integer, Integer> v = new HashMap<>();
            for (int j = 1; j <= n; j += 1) {
                v.put(j, null);
            }
            dp.put(i, v);
        }
        List<Integer> rod = Stream.of(List.of(0), arr, List.of(length)).flatMap(List::stream).toList();
        return DP50Memoized.solve(rod, 1, n, dp);
    }
}

class DP50Tabulation {
    /**
     * Time complexity is O(n^3) and space complexity is O(n^2).
     */

    public static Integer getMinCostToCutRod(List<Integer> arr, Integer length) {
        int n = arr.size();
        QuickSort.sort(arr);

        // using n + 1 and 0 in range because we have added 0 and stick_size to the cuts array.
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        for (int i = 0; i <= n + 1; i += 1) {
            Map<Integer, Integer> v = new HashMap<>();
            for (int j = 0; j <= n; j += 1) {
                v.put(j, 0);
            }
            dp.put(i, v);
        }
        List<Integer> rod = Stream.of(List.of(0), arr, List.of(length)).flatMap(List::stream).toList();
        for (int i = n; i >= 1; i -= 1) {
            for (int j = 1; j <= n; j += 1) {
                if (i > j) {
                    continue;
                }
                int minCost = Integer.MAX_VALUE;
                for (int k = i; k <= j; k += 1) {
                    int cost = rod.get(j + 1) - rod.get(i - 1) + dp.get(i).get(k - 1) + dp.get(k + 1).get(j);
                    minCost = Math.min(cost, minCost);
                }
                Map<Integer, Integer> v = dp.get(i);
                v.put(j, minCost);
                dp.put(i, v);
            }
        }
        return dp.get(1).get(n);
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

        System.out.println("Memoized Solution");
        System.out.println(DP50Memoized.getMinCostToCutRod(Arrays.asList(1, 3, 4, 5), 7));
        System.out.println(DP50Memoized.getMinCostToCutRod(Arrays.asList(1, 3), 4));
        System.out.println(DP50Memoized.getMinCostToCutRod(Arrays.asList(1, 3, 4), 5));
        System.out.println(DP50Memoized.getMinCostToCutRod(Arrays.asList(1, 3, 4, 7), 10));
        System.out.println(DP50Memoized.getMinCostToCutRod(Arrays.asList(1, 3), 10));
        System.out.println(DP50Memoized.getMinCostToCutRod(Arrays.asList(5, 6, 1, 4, 2), 9));

        System.out.println("Tabulation Solution");
        System.out.println(DP50Tabulation.getMinCostToCutRod(Arrays.asList(1, 3, 4, 5), 7));
        System.out.println(DP50Tabulation.getMinCostToCutRod(Arrays.asList(1, 3), 4));
        System.out.println(DP50Tabulation.getMinCostToCutRod(Arrays.asList(1, 3, 4), 5));
        System.out.println(DP50Tabulation.getMinCostToCutRod(Arrays.asList(1, 3, 4, 7), 10));
        System.out.println(DP50Tabulation.getMinCostToCutRod(Arrays.asList(1, 3), 10));
        System.out.println(DP50Tabulation.getMinCostToCutRod(Arrays.asList(5, 6, 1, 4, 2), 9));
    }
}